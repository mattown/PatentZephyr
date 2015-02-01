import codecs
import xml.etree.ElementTree as ET
import os

import PatentZephyr.src.python.CFPAPIconfig as config
import ParserUtils as util
import PatentZephyr.src.python.etl.parser.schema.paCurrent as schema

#
#
#  includes Revisions
#           2013-05-16
#           2012-12-04
#



class parser:
#
#   This should be static
#
#
#
    def __init__(self, path, filePrefix):
        self.outputpath = os.path.join(os.path.expanduser(config.target_dir), config.subdirs['parsed_dir'])
        self.filePrefix = filePrefix
        self.filewriters = self.getfilewriters(path)
        self.headers = self.getHeaders()
        self.writeHeaders()
        self.assignnum = None
        self.assignHeader = {
            'version_no' : '',
            'version_date' : '',
            'creation_datetime' : '',
            'data_available_code' : '',
            'file_segments' : '',
            'action_keys' : ''
        }


    def getHeaders(self):
        d = schema.data
        o = dict()
        for k in d.keys():
            o[k] = list()
            for p in d[k]:
                o[k].append(p[0])
        return o

    def getfilewriters(self, path):
        d = schema.data
        filewriter_out = dict()
        suffix = path.split('/')[-1].split('.')[0]
        version = self.filePrefix
        for k in d.keys():
            filename = ('%s_%s_%s.txt' % (k,suffix,version ))
            filepath = os.path.join(self.outputpath, filename)
            filewriter_out[k] = codecs.open(filepath,'w',encoding='utf-8')
        return filewriter_out


    def getData(self, subdict, key):
        if subdict.has_key(key):
            if subdict[key] == None:
                return config.null_value
            return subdict[key]
        else:
            return config.null_value

    def writeData(self, filename, ddict):
        output = []

        for k in self.headers[filename]:
            output.append(self.getData(ddict,k))
        try:
            self.filewriters[filename].write(config.file_delimiter.join(output)+config.file_newline)
        except:
            print output, ddict,self.headers[filename]
    def writeHeaders(self):
        d = schema.data
        for k in d.keys():
            headerpairs = d[k]
            data = []
            for pair in headerpairs:
                data.append(pair[0])
            delimiter = config.file_delimiter
            self.filewriters[k].write(delimiter.join(data)+config.file_newline)

    def close(self):
        for k in self.filewriters.keys():
            self.filewriters[k].close()

    def getXMLPathData(self, r, path):
        if r.find(path) != None:
            node = r.find(path)
            if node ==None:
                return config.null_value
            else:
                o = util.traverse(node)
                return util.clean(o)
        else:
            return config.null_value


#
#  Parser
#



    def getAssignment(self, r):

        o = {}
        o['dtd_version'] = self.assignHeader['dtd_version']
        o['date_produced'] = self.assignHeader['date_produced']
        o['action_key_code'] = self.assignHeader['action_key_code']
        o['transaction_date'] = self.assignHeader['transaction_date']

        o['reel_no'] = self.getXMLPathData(r, 'assignment-record/reel-no')
        o['frame_no'] = self.getXMLPathData(r, 'assignment-record/frame-no')
        self.assignnum = '%s-%s' % (o['frame_no'], o['reel_no'])
        o['assign_id'] = self.assignnum

        o['last_update_date'] = self.getXMLPathData(r, 'assignment-record/last-update-date/date')
        o['purge_indicator'] = self.getXMLPathData(r, 'assignment-record/purge-indicator')
        o['recorded_date'] = self.getXMLPathData(r, 'assignment-record/recorded-date/date')
        o['page_count'] = self.getXMLPathData(r, 'assignment-record/page-count')
        o['corr_name'] = self.getXMLPathData(r, 'assignment-record/correspondent/name')
        o['corr_add1'] = self.getXMLPathData(r, 'assignment-record/correspondent/address-1')
        o['corr_add2'] = self.getXMLPathData(r, 'assignment-record/correspondent/address-2')
        o['corr_add3'] = self.getXMLPathData(r,'assignment-record/correspondent/address-3' )
        o['corr_add4'] = self.getXMLPathData(r,'assignment-record/correspondent/address-4' )
        o['conveyance_text'] = self.getXMLPathData(r, 'assignment-record/conveyance-text' )

        name = r.find('assignment-record/correspondent/name')
        o['name_type'] = ''
        if name != None:
            if 'name-type' in name.keys():
                o['name_type'] = name['name-type']

        return [o]

    def getAssignor(self, r):

        output = []

        for item in r.findall('patent-assignors/patent-assignor'):
            o = {}
            o['assign_id'] = self.assignnum

            o['name'] = self.getXMLPathData(item, 'name')
            o['execution_date'] = self.getXMLPathData(item, 'execution-date/date')
            o['date_acknowledged'] = self.getXMLPathData(item, 'date-acknowledged/date')
            name = r.find('name')
            o['name_type'] = ''
            if name != None:
                if 'name-type' in name.keys():
                    o['name_type'] = name['name-type']
            output.append(o)

        return output

    def getAssignee(self, r):

        output = []

        for item in r.findall('patent-assignees/patent-assignee'):
            o = {}
            o['assign_id'] = self.assignnum

            o['name'] = self.getXMLPathData(item, 'name')
            o['address_1'] = self.getXMLPathData(item, 'address-1')
            o['address_2'] = self.getXMLPathData(item, 'address-2')
            o['city'] = self.getXMLPathData(item, 'city')
            o['state'] = self.getXMLPathData(item, 'state')
            o['country_name'] = self.getXMLPathData(item, 'country-name')
            o['postcode'] = self.getXMLPathData(item, 'postcode')
            name = r.find('name')
            o['name_type'] = ''
            if name != None:
                if 'name-type' in name.keys():
                    o['name_type'] = name['name-type']
            output.append(o)

        return output


    def getProperty(self,r):
        output = []
        for item in r.findall('patent-properties/patent-property'):
            invention_title = self.getXMLPathData(item, 'invention-title')
            for subitem in item.findall('document-id'):
                o = {}
                o['assign_id'] = self.assignnum
                o['invention_title'] = invention_title
                o['country'] = self.getXMLPathData(subitem, 'country')
                o['doc_number'] = self.getXMLPathData(subitem, 'doc-number')
                o['kind'] = self.getXMLPathData(subitem, 'kind')
                o['name'] = self.getXMLPathData(subitem, 'name')
                o['date'] = self.getXMLPathData(subitem, 'date')
                name = subitem.find('name')
                o['name_type'] = ''
                if name != None:
                    if 'name-type' in name.keys():
                        o['name_type'] = name['name-type']
                output.append(o)
        return output





    def updateHeaders(self, r):

        if 'dtd-version' in r.keys():
            self.assignHeader['dtd_version'] = r.attrib['dtd-version']
        else:
            self.assignHeader['dtd_version'] = ''
        if 'date-produced' in r.keys():
            self.assignHeader['date_produced'] = r.attrib['date-produced']
        else:
            self.assignHeader['dtd_version'] = ''

        self.assignHeader['action_key_code'] =  self.getXMLPathData(r, 'action-key-code')
        self.assignHeader['transaction_date'] =  self.getXMLPathData(r, 'transaction-date/date')








    def parse(self, path):

        tree = ET.parse(path)
        root = tree.getroot()
        #root = ET.fromstring(data)

        #setup global headers
        self.updateHeaders(root)

        for item in root.findall('patent-assignments/patent-assignment'):
            writedata = dict()
            self.assignnum = None

            writedata['patent_assignment'] = self.getAssignment(item)

            writedata['patent_assignment_assignor'] = self.getAssignor(item)

            writedata['patent_assignment_assignee'] = self.getAssignee(item)
            writedata['patent_assignment_property'] = self.getProperty(item)


            for key in writedata.keys():
                for subitem in writedata[key]:
                    self.writeData(key, subitem)
        self.close()


if __name__ == '__main__':
    path = '/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/ad20141231.xml'



    p =parser(path, 'paCurrent')
    p.parse(path)
