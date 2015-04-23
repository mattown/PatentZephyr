#
#  Use this class to talk with the postgres database, insert, schema updates, etc
#
import FileSystemSetup as FS
import postgres.SchemaGenerator as SG
import postgres.PostgresFunctionGenerator as FG
import etl.parser.schema.taCurrent as trademarks
import CFPAPIconfig as config
import subprocess

# psql runner
def run_psql_command(command):
    cmd = 'psql -c "%s"' % command
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

# simple method to clear all files in the sql generator template
def clear_template_files():
    FS.forceCreateRefreshDirectory(config.template_insert_path)
    FS.forceCreateRefreshDirectory(config.template_intake_schema_path)
    FS.forceCreateRefreshDirectory(config.template_schema_path)



def generate_template_examples():
    clear_template_files()
    SG.write_all(trademarks)

def generate_intake_schema(schema):
    data = SG.generate_intake_schema(schema)
    for item in data.keys():
        run_psql_command(data[item])

def delete_everything():
    run_psql_command("drop schema public cascade;create schema public;")


# hand this method a schema module and it'll attempt to load the parsed data into that modules corresponding intake schema
def load_intake(schema):
    parsed_files = FS.getParsedFiles()
    schema_name = schema.__name__.split('.')[-1]
    # generate a list with a 2 item list as elements, first element is target sql table, second element is the tab file location
    process_list = []
    for table_name in schema.data.keys():
        for file in parsed_files:
            if table_name in file and schema_name in file:
                process_list.append(['in_'+schema_name+"_"+table_name.lower(), file])
    # load each one individually now
    for item in process_list:
        cmd = SG.create_copy_statement(item[0],item[1])
        print cmd
        run_psql_command(cmd)

def load_trademarks():
    generate_intake_schema(trademarks)
    load_intake(trademarks)


# method for generating the main schema sql, we run this manually so we don't delete the data!

def generate_main_schema():
    FS.forceCreateRefreshDirectory('postgres/sql/main_schema')
    generate_main_schema_helper(trademarks)

def generate_main_schema_helper(schema):
    output = open( ('postgres/sql/main_schema/%s.sql' % schema.__name__.split('.')[-1])  ,'w')
    data = SG.generate_schema(schema)
    for item in data.keys():
        #run_psql_command(data[item])
        output.write(data[item]+'\n')


# method for generating the main postgres upsert for all schemas

def generate_main_delta_functions():
    FS.forceCreateRefreshDirectory('postgres/sql/db_functions')
    generate_delta_functions(trademarks)

def generate_delta_functions(schema):
    output = open( ('postgres/sql/db_functions/%s_delta_helpers.sql' % schema.__name__.split('.')[-1])  ,'w')
    data = FG.generate_upsert_helpers(schema)
    for item in data.keys():
        #run_psql_command(data[item])
        output.write(data[item])
    output.close()
    output = open( ('postgres/sql/db_functions/%s_delta_main.sql' % schema.__name__.split('.')[-1])  ,'w')
    data = FG.generate_upsert(schema)
    output.write(data)
    output.close()




generate_main_schema()
generate_main_delta_functions()

#delete_everything()
#load_trademarks()