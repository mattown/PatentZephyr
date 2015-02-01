import codecs
import xml.etree.ElementTree as ET
import os

import PatentZephyr.src.python.CFPAPIconfig as config
import PatentZephyr.src.python.etl.parser.schema.tasCurrent as schema
import ParserUtils as util



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
        self.assignheader = {
            'version_no' : '',
            'version_date' : '',
            'action_key_code' : '',
            'transaction_date' : '',
            'data_available_code' : ''
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

        o['version_no'] = self.assignheader['version_no']
        o['version_date'] = self.assignheader['version_date']
        o['action_key_code'] = self.assignheader['action_key_code']
        o['transaction_date'] = self.assignheader['transaction_date']
        o['data_available_code'] = self.assignheader['data_available_code']

        o['reel_no'] = self.getXMLPathData(r, 'assignment/reel-no')
        o['frame_no'] = self.getXMLPathData(r, 'assignment/frame-no')

        self.assignnum = ('%s-%s') % (o['reel_no'], o['frame_no'])

        o['assign_id'] = self.assignnum

        o['last_update_date'] = self.getXMLPathData(r, 'assignment/last-update-date')
        o['purge_indicator'] = self.getXMLPathData(r, 'assignment/purge-indicator')
        o['date_recorded'] = self.getXMLPathData(r, 'assignment/date-recorded')
        o['page_count'] = self.getXMLPathData(r, 'assignment/page-count')
        o['cor_name'] = self.getXMLPathData(r, 'assignment/correspondent/person-or-organization-name')
        o['cor_add1'] = self.getXMLPathData(r, 'assignment/correspondent/address-1')
        o['cor_add2'] = self.getXMLPathData(r, 'assignment/correspondent/address-2')
        o['cor_add3'] = self.getXMLPathData(r, 'assignment/correspondent/address-3')
        o['cor_add4'] = self.getXMLPathData(r, 'assignment/correspondent/address-4')
        o['conveyance_text'] = self.getXMLPathData(r, 'assignment/conveyance-text')

        return [o]



    def getAssignors(self, r):

        assignor_output = []
        assignor_composed_output = []
        c = 0
        t = 'R'

        for item in r.findall('assignors/assignor'):
            c +=1
            sd1 = {}



            assignor_id = '%s-%s-%s' % (self.assignnum, str(c), t)

            sd1['assign_id'] = self.assignnum
            sd1['assignor_id'] = assignor_id
            sd1['name'] = self.getXMLPathData(item, 'person-or-organization-name')
            sd1['formerly_statement'] = self.getXMLPathData(item ,'formerly-statement')
            sd1['dba_aka_ta_statement'] = self.getXMLPathData(item ,'dba-aka-ta-statement')
            sd1['address_1'] = self.getXMLPathData(item ,'address-1')
            sd1['address_2'] = self.getXMLPathData(item ,'address-2')
            sd1['city'] = self.getXMLPathData(item ,'city')
            sd1['state'] = self.getXMLPathData(item ,'state')
            sd1['country_name'] = self.getXMLPathData(item ,'country-name')
            sd1['postcode'] = self.getXMLPathData(item ,'postcode')
            sd1['execution_date'] = self.getXMLPathData(item ,'execution-date')
            sd1['date_acknowledged'] = self.getXMLPathData(item ,'date-acknowledged')
            sd1['legal_entity_text'] = self.getXMLPathData(item ,'legal-entity-text')
            sd1['nationality'] = self.getXMLPathData(item ,'nationality')
            assignor_output.append(sd1)

            for subitem in item.findall('composed-of-statement/sub-party'):

                sd2 = {}
                sd2['assign_id'] = self.assignnum
                sd2['assignor_id'] = assignor_id
                sd2['name'] = self.getXMLPathData(subitem,'name')
                sd2['entity'] = self.getXMLPathData(subitem,'entity')
                sd2['stctry'] = self.getXMLPathData(subitem,'stctry')
                sd2['composed_of'] = self.getXMLPathData(subitem,'composed_of')

                assignor_composed_output.append(sd2)

        return [assignor_output, assignor_composed_output]


    def getAssignees(self, r):

        assignee_output = []
        assignee_composed_output = []
        c = 0
        t = 'E'

        for item in r.findall('assignees/assignee'):
            c +=1
            sd1 = {}
            assignor_id = '%s-%s-%s' % (self.assignnum, str(c), t)

            sd1['assign_id'] = self.assignnum
            sd1['assignor_id'] = assignor_id
            sd1['name'] = self.getXMLPathData(item, 'person-or-organization-name')
            sd1['formerly_statement'] = self.getXMLPathData(item ,'formerly-statement')
            sd1['dba_aka_ta_statement'] = self.getXMLPathData(item ,'dba-aka-ta-statement')
            sd1['address_1'] = self.getXMLPathData(item ,'address-1')
            sd1['address_2'] = self.getXMLPathData(item ,'address-2')
            sd1['city'] = self.getXMLPathData(item ,'city')
            sd1['state'] = self.getXMLPathData(item ,'state')
            sd1['country_name'] = self.getXMLPathData(item ,'country-name')
            sd1['postcode'] = self.getXMLPathData(item ,'postcode')
            sd1['legal_entity_text'] = self.getXMLPathData(item ,'legal-entity-text')
            sd1['nationality'] = self.getXMLPathData(item ,'nationality')
            assignee_output.append(sd1)

            for subitem in item.findall('composed-of-statement/sub-party'):

                sd2 = {}
                sd2['assign_id'] = self.assignnum
                sd2['assignor_id'] = assignor_id
                sd2['name'] = self.getXMLPathData(subitem,'name')
                sd2['entity'] = self.getXMLPathData(subitem,'entity')
                sd2['stctry'] = self.getXMLPathData(subitem,'stctry')
                sd2['composed_of'] = self.getXMLPathData(subitem,'composed_of')

                assignee_composed_output.append(sd2)

        return [assignee_output, assignee_composed_output]


    def getProperty(self, r):
        output = []
        for item in r.findall('properties/property'):

            o = {}
            o['assign_id'] = self.assignnum
            o['serial_no'] = self.getXMLPathData(item, 'serial-no')
            o['registration_no'] = self.getXMLPathData(item, 'registration-no')
            o['law_treaty_tlt_mark_name'] = self.getXMLPathData(item, 'trademark-law-treaty-property/tlt-mark-name')
            o['law_treaty_tlt_mark_description'] = self.getXMLPathData(item, 'trademark-law-treaty-property/tlt-mark-description')
            o['intl_reg_no'] = self.getXMLPathData(item, 'intl-reg-no')
            output.append(o)
        return output


    def updateHeaders(self, r):

        self.assignheader['version_no'] =  self.getXMLPathData(r, 'version/version-no')
        self.assignheader['version_date'] =  self.getXMLPathData(r, 'version/version-date')
        self.assignheader['action_key_code'] =  self.getXMLPathData(r, 'action-key-code')
        self.assignheader['transaction_date'] =  self.getXMLPathData(r, 'transaction-date')
        self.assignheader['data_available_code'] =  self.getXMLPathData(r, 'assignment-information/data-available-code')


    def parse(self, path):


        tree = ET.parse(path)
        root = tree.getroot()

        #setup global headers
        self.updateHeaders(root)

        for item in root.findall('assignment-information/assignment-entry'):
            writedata = dict()
            self.assignnum = None

            writedata['trademarkassignment'] = self.getAssignment(item)

            # get assignors
            assignorData = self.getAssignors(item)
            writedata['trademarkassignment_assignors'] = assignorData[0]
            writedata['trademarkassignment_assignor_composed_of'] = assignorData[1]

            # get assignees
            assigneeData = self.getAssignees(item)
            writedata['trademarkassignment_assignees'] = assigneeData[0]
            writedata['trademarkassignment_assignee_composed_of'] = assigneeData[1]



            writedata['trademarkassignment_properties'] = self.getProperty(item)


            for key in writedata.keys():
                for subitem in writedata[key]:
                    self.writeData(key, subitem)

        self.close()


if __name__ == '__main__':
    f = codecs.open('/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/asb150106.xml','r', encoding='UTF' )
    path = '/Users/matthewharrison/PycharmProjects/cuddlenuggets/PatentZephyr/PatentDisplayBuild'
    data = f.read().encode('utf-8')
    #root = ET.fromstring(data)


    p =parser(path)
    p.parse(data)
