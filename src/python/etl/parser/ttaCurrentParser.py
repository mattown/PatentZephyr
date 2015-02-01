import codecs
import xml.etree.ElementTree as ET
import os

import PatentZephyr.src.python.CFPAPIconfig as config
import PatentZephyr.src.python.etl.parser.schema.ttaCurrent as schema
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
        self.ttanum = None
        self.ttaheader = {
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

    def getTtab(self, r):
        o = {}


        o['version_no'] = self.ttaheader['version_no']
        o['version_date'] = self.ttaheader['version_date']
        o['action_key_code'] = self.ttaheader['action_key_code']
        o['transaction_date'] = self.ttaheader['transaction_date']
        o['data_available_code'] = self.ttaheader['data_available_code']

        o['number'] = self.getXMLPathData(r, 'number')
        o['type_code'] = self.getXMLPathData(r, 'type-code')

        self.ttanum = '%s-%s' % (o['number'],o['type_code'])
        o['ttab_id'] = self.ttanum


        o['filing_date'] = self.getXMLPathData(r, 'filing-date')
        o['employee_number'] = self.getXMLPathData(r, 'mployee-number')
        o['interlocutory_attorney_name'] = self.getXMLPathData(r, 'interlocutory-attorney-name')
        o['location_code'] = self.getXMLPathData(r, 'location-code')
        o['day_in_location'] = self.getXMLPathData(r, 'day-in-location')
        o['charge_to_location_code'] = self.getXMLPathData(r, 'charge-to-location-code')
        o['charge_to_employee_name'] = self.getXMLPathData(r, 'charge-to-employee-name')
        o['status_update_date'] = self.getXMLPathData(r, 'status-update-date')
        o['status_code'] = self.getXMLPathData(r, 'status-code')

        return [o]

    def getProsecutionHistory(self, r):


        output = []

        for item in r.findall('prosecution-history/prosecution-entry'):
            o = {}

            o['ttab_id']= self.ttanum
            o['identifier'] = self.getXMLPathData(item, 'identifier')
            o['code'] = self.getXMLPathData(item, 'code')
            o['type_code'] = self.getXMLPathData(item, 'type-code')
            o['due_date'] = self.getXMLPathData(item, 'due-date')
            o['date'] = self.getXMLPathData(item, 'date')
            o['history_text'] = self.getXMLPathData(item, 'history-text')
            output.append(o)
        return output


    def getPartyData(self, r):


        output_party = []
        output_property = []
        output_address = []
        c = 0
        for item in r.findall('party-information/party'):
            sd1 ={}
            c +=1
            sd1['ttab_id'] = self.ttanum
            sd1['identifier'] = self.getXMLPathData(item, 'identifier')
            party_id = '%s-%s-%s' %(str(c), self.ttanum, sd1['identifier'])

            sd1['party_id'] = party_id
            sd1['role_code'] = self.getXMLPathData(item, 'role-code')
            sd1['name'] = self.getXMLPathData(item, 'name')
            sd1['orgname'] = self.getXMLPathData(item, 'orgname')
            output_party.append(sd1)

            for subitem in item.findall('property-information/property'):
                sd2 = {}
                sd2['ttab_id'] = self.ttanum
                sd2['party_id'] = party_id
                sd2['identifier'] = self.getXMLPathData(subitem, 'identifier')
                sd2['serial_number'] = self.getXMLPathData(subitem, 'serial-number')
                sd2['registration_number'] = self.getXMLPathData(subitem, 'registration-number')
                sd2['mark_text'] = self.getXMLPathData(subitem, 'mark-text')
                output_property.append(sd2)
            for subitem in item.findall('address-information/proceeding-address'):
                sd3 = {}
                sd3['ttab_id'] = self.ttanum
                sd3['party_id'] = party_id
                sd3['identifier'] = self.getXMLPathData(subitem, 'identifier')
                sd3['type_code'] = self.getXMLPathData(subitem, 'serial-number')
                sd3['name'] = self.getXMLPathData(subitem, 'name')
                sd3['orgname'] = self.getXMLPathData(subitem, 'orgname')
                sd3['address_1'] = self.getXMLPathData(subitem, 'address-1')
                sd3['city'] = self.getXMLPathData(subitem, 'city')
                sd3['state'] = self.getXMLPathData(subitem, 'state')
                sd3['country'] = self.getXMLPathData(subitem, 'country')
                sd3['postcode'] = self.getXMLPathData(subitem, 'postcode')
                output_address.append(sd3)
        return[output_party, output_property, output_address]









    def updateHeaders(self, r):

        self.ttaheader['version_no'] =  self.getXMLPathData(r, 'version/version-no')
        self.ttaheader['version_date'] =  self.getXMLPathData(r, 'version/version-date')
        self.ttaheader['action_key_code'] =  self.getXMLPathData(r, 'action-key-code')
        self.ttaheader['transaction_date'] =  self.getXMLPathData(r, 'transaction-date')
        self.ttaheader['data_available_code'] =  self.getXMLPathData(r, 'proceeding-information/data-available-code')


    def parse(self, path):

        print 'loading data into element tree'
        tree = ET.parse(path)
        root = tree.getroot()
        #root = ET.fromstring(data)
        print 'updating headers'
        #setup global headers
        self.updateHeaders(root)
        print 'cycling through proceeding-entry'
        c = 0
        for item in root.findall('proceeding-information/proceeding-entry'):
            c += 1
            #if c % 50000 == 0:
                #print c
            writedata = dict()
            self.ttanum = None

            writedata['ttab'] = self.getTtab(item)

            # get assignors
            assignorData = self.getPartyData(item)
            writedata['ttab_party'] = assignorData[0]
            writedata['ttab_party_property'] = assignorData[1]
            writedata['ttab_party_proceeding_address'] = assignorData[2]

            writedata['ttab_prosecution_history'] = self.getProsecutionHistory(item)


            for key in writedata.keys():
                for subitem in writedata[key]:
                    self.writeData(key, subitem)

        self.close()


#if __name__ == '__main__':
#f = codecs.open('/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/tt131231-01.xml','r', encoding='UTF' )
#path = '/Users/matthewharrison/PycharmProjects/cuddlenuggets/PatentZephyr/PatentDisplayBuild'

#print 'reading data....'
#data = f.read().encode('utf-8')
#print 'loading data into cache....'
#root = ET.fromstring(data)

#print 'setting up parser....'
#p =parser(path)
#print 'parsing data'
#p.parse('')
