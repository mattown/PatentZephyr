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
    'parsed_dir' : 'parsed_tmp',
    'postgres_schema_dir' : 'postgres_schema'
}

file_delimiter = '\t'
file_newline = '\n'
escaped_chars = ['\t','\n','\r']
null_value = ''

parser_to_year_map ={

            '2014' : '2014parser'

        }
