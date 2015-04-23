import os

template_path = 'postgres/templates'
output_path = 'postgres/templates/gen_examples'



def create_upserts(schema):
    data = schema.data
    prefix = schema.__name__.split('.')[-1]
    output = {}
    source_table_header = 'in_'+prefix+"_"
    target_table_header = prefix+"_"
    data_desc = schema.desc
    for table in data.keys():

        target_table = target_table_header+table
        source_table = source_table_header+table
        target_fields = []
        source_fields = []
        conditions = []
        print table
        for field_list in data[table]:
            # 0 = field name, 1 = field type,
            # 2 = pk, 3 = special function
            target_fields.append(field_list[0])

            if field_list[3] != '':
                source_fields.append(field_list[3] % field_list[0])
            elif field_list[1] =='int':
                source_fields.append("CAST(nullif(%s, '') AS integer)" % field_list[0])
            else:
                source_fields.append(field_list[0])
            if 'pk' in field_list[2] or 'i' in field_list[2]:
                remove_header_condition = "%s != '%s' " % (field_list[0], field_list[0] )
                not_exists_condition = " NOT EXISTS (SELECT 1 FROM %s b WHERE b.%s = a.%s) " % (target_table,field_list[0], field_list[0] )
                conditions.append(remove_header_condition)
                conditions.append(not_exists_condition)

        f = open(os.path.join(template_path,'upsert_template.sql'),'r')
        upsert_template = str(f.read())
        f.close()
        upsert_template= upsert_template.replace("$TARGET_TABLE", target_table)
        upsert_template= upsert_template.replace("$TARGET_FIELDS", ',\n'.join(target_fields))
        upsert_template= upsert_template.replace("$SOURCE_SELECT", ',\n'.join(source_fields))
        upsert_template= upsert_template.replace("$SOURCE_TABLE", source_table)

        condition = "WHERE\n"+('and\n'.join(conditions))
        upsert_template= upsert_template.replace("$CONDITIONS", condition)

        f = open(os.path.join(template_path,'upsert_app_template.sql'),'r')
        upsert_app_template = str(f.read())
        f.close()
        upsert_app_template= upsert_app_template.replace("$FUNCITON", "upsert_%s_%s" % (data_desc, target_table))
        upsert_app_template= upsert_app_template.replace("$FUNCTION_STATEMENTS", upsert_template)

        output[table] = upsert_app_template

    return output

def generate_upsert_helpers(schema):
    data = create_upserts(schema)
    return data

def generate_upsert(schema):
    data = schema.data
    data_desc = schema.desc
    prefix = schema.__name__.split('.')[-1]
    target_table_header = prefix+"_"
    functions = []
    for table in data.keys():
        target_table = target_table_header+table
        functions.append('SELECT %s()' % ("upsert_%s_%s" % (data_desc, target_table)))
    f = open(os.path.join(template_path,'upsert_app_template.sql'),'r')
    app_template = str(f.read())
    f.close()
    app_template = app_template.replace("$FUNCITON",data_desc)
    app_template = app_template.replace("$FUNCTION_STATEMENTS",';\n'.join(functions))
    return app_template

