
import os
import python.etl.parser.schema.taCurrent as trademarks
target_dir = 'mamp'
template_dir = 'mamp/templates'



def normalize_string(s):
    s = s.replace("_", ' ').capitalize()
    return s

def create_map(s):
    if s =='string':
        return "text_data"
    if s =='date':
        return "date_data"
    return "numeric_data"

def generate_form_selects(schema):
    d = schema.data

    f = open(os.path.join(template_dir,'select_div_main_type.html'),'r')
    main_template = str(f.read())
    f.close()
    f = open(os.path.join(template_dir,'select_div_sub_type.html'),'r')
    subtype_template = str(f.read())
    f.close()
    #
    main_select = ['    <option value="0">Select Option</option>']
    i =0
    sub_selects = []

    #java script stuff
    map_list = []
    reset_subtype_list = []
    show_form_list = []


    # iterate through the schema, add items to the lists above which we'll later poke into the template files
    for key in d.keys():
        i = i+1
        select_template = '    <option value="%s">%s</option>' % (str(i),normalize_string(key))
        main_select.append(select_template)
        j = 0
        subselect = ['    <option value="0">Select Option</option>']
        for field in d[key]:
            j = j+1
            select_template = '    <option value="%s">%s</option>' % (str(j),normalize_string(field[0]))
            subselect.append(select_template)
            map_list.append('map[\'%s_%s\'] = "%s";' % (str(i), str(j),create_map(field[1])))
        reset_subtype_list.append('\t\tdocument.getElementById("%s").style.display = "none";' % ('f'+str(i)))

        show_form_list.append('\t\tif (selopt == %s) {\n\t\t\tdocument.getElementById("f%s").style.display = "block";\n\t\t}' % (str(i),str(i)))

        s_template = str(subtype_template)
        s_template = s_template.replace('$NUM', str(i))
        s_template = s_template.replace('$OPTION_DATA','\n'.join(subselect))
        sub_selects.append(s_template)

        #if (selopt == 1) {
        #    document.getElementById("f1").style.display = "block";
        #    document.getElementById("f2").style.display = "none";
        #}

    main_template = main_template.replace('$OPTION_DATA','\n'.join(main_select))

    schema_name = '%s-selects.html' % schema.__name__.split('.')[-1]
    output_file = open(os.path.join(target_dir,schema_name),'w')

    f = open(os.path.join(template_dir,'select_div_filter.html'),'r')
    filter_template = f.read()
    f.close()

    div_data = [main_template]+ sub_selects + [filter_template]

    for string_data in div_data:

        output_file.write(string_data+'\n\n')

    # linking
    output_file.close()

    #write to javascript file
    js_name = '%s-selects.js' % schema.__name__.split('.')[-1]
    output_file = open(os.path.join(target_dir,js_name),'w')

    f = open(os.path.join(template_dir,'select_filters.js'),'r')
    js_template = f.read()
    f.close()

    js_template = js_template.replace("$MAP_GEN", '\n'.join(map_list))
    js_template = js_template.replace("$RESET_ALL_LIST", '\n'.join(reset_subtype_list))
    js_template = js_template.replace("$SHOWFORM_LIST", '\n'.join(show_form_list))

    output_file.write(js_template)
    output_file.close()

    # write to master file

    f = open(os.path.join(template_dir,'test_select.html'),'r')
    final_output_template = f.read()
    f.close()
    final_output_template = final_output_template.replace("$DIV_DATA", '\n'.join(div_data))
    final_output_template = final_output_template.replace("$JAVASCRIPT_DATA", js_template)

    final_name = '%s-example.html' % schema.__name__.split('.')[-1]
    final_out_file = open(os.path.join(target_dir,final_name),'w')
    final_out_file.write(final_output_template)
    final_out_file.close()


def create_query_forms():
    generate_form_selects(trademarks)


create_query_forms()

