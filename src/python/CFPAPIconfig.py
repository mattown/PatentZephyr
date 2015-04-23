import os
#
#  config file for patent ETL program
#
#   edit the hard path here
#
target_dir = '~/PatentDisplayBuild'

schema_dir = 'schemas'


# number of concurrent zip file downlaods
download_thread_pool_number = 10

# number of concurrent ETL processes [ a process reads a file then loaded to Memory then parsed in place ]
read_to_memory_to_parse_pool_number = 1


subdirs = {
    'download_dir' : 'download_tmp',
    'unziped_dir' : 'unzip_tmp',
    'parsed_dir' : 'parsed_tmp'
}

file_delimiter = '\t'
file_newline = '\n'
escaped_chars = ['\t','\n','\r']
null_value = ''


template_schema_path = 'postgres/templates/gen_examples/schema'
template_intake_schema_path = 'postgres/templates/gen_examples/intake_schema'
template_insert_path = 'postgres/templates/gen_examples/insert'