

import os

template_path = 'postgres/templates'
output_path = 'postgres/templates/gen_examples'



def create_copy_statement(table, filepath):
    f = open(os.path.join(template_path,'insert_template.sql'),'r')
    create_template = str(f.read())
    f.close()
    create_template = create_template.replace("$TABLE_NAME", table)
    create_template = create_template.replace('$TAB_FILE_LOCATION', filepath)
    return create_template

def create_table(table_name, columns, is_intake='f'):

    c = []
    table_index = table_name+'_k_idx'
    index_fields = []

    for item in columns:
        type = 'text'
        suffix = ''
        if is_intake =='f':
            if item[1] == 'int':
                type = 'integer'
            elif item[1] =='date':
                type = 'date'
        if 'pk' in item[2]:
            suffix = suffix+' PRIMARY KEY '
        if 'i' in item[2]:
            index_fields.append(item[0])
        c.append(' '.join([item[0],type+suffix+','] ) )
    #trim last comma
    c[-1] = c[-1][:-1]
    f = open(os.path.join(template_path,'create_template.sql'),'r')
    create_template = str(f.read())

    f.close()
    create_template = create_template.replace("$TABLE_NAME", table_name)
    create_template = create_template.replace('$TABLE_COLUMN_DATA', '\n'.join(c))
    create_template = create_template.replace('$TABLE_INDEX', table_index)
    create_template = create_template.replace('$INDEX_FIELDS', ',\n'.join(index_fields))
    return create_template

# d equals a schema objcet in src.python.etl.parser.schema
def create_tables(d, intake='f'):
    data = d.data
    prefix = d.__name__.split('.')[-1]
    output = {}
    table_header = ''
    if intake =='t':
        table_header ='in_'
    prefix = table_header+prefix
    for key in data.keys():
        tablename = key.lower()
        tablename = prefix+"_"+tablename
        outputdata = create_table(tablename, data[key], intake)
        output[tablename] = outputdata
    return output

def write_examples(dict, intake='f'):
    prefix = ''
    print os.getcwd()
    if intake =='t':
        prefix = 'intake_'
    outputpath = os.path.join(output_path,prefix+'schema')
    for item in dict.keys():
        f = open(os.path.join(outputpath,item+'.sql'),'w')
        f.write(dict[item])
        f.close()

def generate_intake_schema(schema):
    data = create_tables(schema, intake='t')
    return data

def generate_schema(schema):
    data = create_tables(schema, intake='f')
    return data

def write_all(schema):
    intake = generate_intake_schema(schema)
    final = generate_schema(schema)
    write_examples(final, intake='f')
    write_examples(intake, intake='t')


















