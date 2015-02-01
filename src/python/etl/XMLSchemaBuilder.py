
import xml.etree.ElementTree as ET


#
# get all allowable xpath
#

def remove_bad_paths(data):
    output = set()
    for item in data:
        if is_valid(item):
            output.add(item)
    return output

def is_valid(path):
    o = True
    bad_list = ['description/p/',
                '/maths/',
                'abstract/p/',
                'description-of-drawings/p/',
                'claim-text/',
                '/p/'
                ]
    for item in bad_list:
        if item in path:
            o = False
    return o



def get_et_xpath(path, element):
    output = set()
    newpath = '%s/%s' % (path, element.tag)

    output.add(newpath)
    for attrib in  get_attrib_xpath(element):
        n = '%s/%s' % (path, attrib)
        output.add(n)

    for c in element.getchildren():
        n = '%s/%s' % (path, element.tag)
        output = set(list(output) + list(get_et_xpath(n, c)))
    return output

def get_attrib_xpath(element):
    output = set()
    a = element.attrib
    for k in a.keys():
        str = ('%s@%s') % (element.tag,k)
        output.add(str)
    return output





class tree_builder:

    def __init__(self):
        self.output = set()


    def combine(self, data):


        self.output = set(list(self.output) + list(data))


    def parser(self, data, prefix):
        tree = ET.fromstring(data)
        s = get_et_xpath(prefix,tree)
        self.combine(s)
    def finish(self):
        o = list(self.output)
        o.sort()
        for i in o:
            print i
    def getset(self):
        return remove_bad_paths(self.output)


if __name__ == '__main__':
     test_file = open('/Users/matthewharrison/test.xml','r').read()
     t = tree_builder()
     t.parser(test_file)
     t.finish()
#     root = tree.getroot()
#
#
#     items = get_et_xpath(root.tag, root)
#     for item in items:
#         print item