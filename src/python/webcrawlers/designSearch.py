#
#   Quick and dirty uspto design Search Parser
#
#   Main class returns json object with name value maps to the


# USPTO adds 2 mapping values to the codes, sometimes if the code is equal to the Alphebetic index it'll add that value
#
# Found here
#
# http://tess2.uspto.gov/tmdb/dscm/dsc_ai.htm
#
# in addition to the high level categories (first 2 digits)
# found here
# http://tess2.uspto.gov/tmdb/dscm/index.htm


import urllib
import pickle
import xml.etree.ElementTree as ET
import re
import time
import json
# time in seconds between page access
interval_time = 1

#
url1 = 'http://tess2.uspto.gov/tmdb/dscm/dsc_ai%s.htm'
url2 = 'http://tess2.uspto.gov/tmdb/dscm/index.htm'

xml_convert = [
    ['&','&amp;'],
    [' < ', ' ||lessthan|| ']

]


def to_xml(str):
    for item in xml_convert:
        str = str.replace(item[0],item[1])
    return str

def from_xml(str):
    for item in xml_convert:
        str = str.replace(item[1],item[0])
    return str


def get_url1_data():
    raw_json = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        time.sleep(interval_time)
        sub = ''
        if letter !='a':
            sub = letter
        print url1 % sub
        html_data = urllib.urlopen(url1 % sub).read().decode('cp1252').encode('utf-8')
        regex = "<tr><td><a href=.*>.*<\/a><\/td>\\n<td><a href=.*>.*<\/a><\/td><\/tr>"
        items = re.findall(regex,html_data)
        for item in items:
            st = to_xml(item)

            e = ET.fromstring(st)
            s = e.findall('td/a')
            assert len(s) ==2

            key, value = from_xml(s[1].text), from_xml(s[0].text)
            #assert output.has_key(key) ==False
            if raw_json.has_key(key):
                raw_json[key].append(value)
            else:
                raw_json[key] = [value]

    # clean up the raw json, get rid of the periods in the value and concat dups
    output = {}
    for key in raw_json.keys():
        k, v = key.replace('.',''), '; '.join(raw_json[key])
        output[k] = v
    return output

def get_url2_data():
    raw_json = {}
    html_data = urllib.urlopen(url2).read().decode('cp1252').encode('utf-8')



def get_mapping_as_json():
    return get_url1_data()


j = get_mapping_as_json()
print json.dumps(j, indent=4)





