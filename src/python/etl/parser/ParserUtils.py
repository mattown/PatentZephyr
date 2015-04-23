import xml.etree.ElementTree as ET
import PatentZephyr.src.python.CFPAPIconfig as config



def clean(data):
    if data == None:
        return config.null_value
    o = data.strip()
    for item in config.escaped_chars:
        #o = o.replace(item, "GG_FAGGOT")
        o = o.replace('\\','\\\\')
        o = o.replace(item, "\\"+item)
    return o

def traverse(node):
    text = ''
    if node.text != None:
        text += node.text
    children = node.getchildren()
    if len(children) > 0:
        for c in children:
            stag ="<%s>" % c.tag
            data = traverse(c)
            etag ="</%s>" % c.tag
            tail = ''
            if c.tail != None:
                tail = c.tail
            text += stag + data + etag + tail
    return text


if __name__ == '__main__':
    path = '/Users/matthewharrison/PycharmProjects/cuddlenuggets/PatentZephyr/src/python/etl/templates/DTD/test_xml_walk.xml'
    root = ET.ElementTree(file=path)
    c = root.find('othercit')




