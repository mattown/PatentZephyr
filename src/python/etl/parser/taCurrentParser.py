import codecs
import xml.etree.ElementTree as ET
import os

import PatentZephyr.src.python.CFPAPIconfig as config
import PatentZephyr.src.python.etl.parser.schema.taCurrent as schema
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
        self.tradenum = None
        self.tradeheader = {
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
        d = schema.data

        for k in self.headers[filename]:
            output.append(self.getData(ddict,k))
        try:
            data = config.file_delimiter.join(output)+config.file_newline
            assert len(d[filename]) == len(data.split(config.file_delimiter))
            self.filewriters[filename].write(data)
        except:
            print len(d[filename]), len(data.split(config.file_delimiter)), data,d[filename], output, ddict,self.headers[filename]


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



    def getTrademark(self, r):
        d = dict()

        d['version_no'] = self.tradeheader['version_no']
        d['version_date'] = self.tradeheader['version_date']
        d['creation_datetime'] = self.tradeheader['creation_datetime']
        d['data_available_code'] = self.tradeheader['data_available_code']
        d['file_segments'] = self.tradeheader['file_segments']
        d['action_keys'] = self.tradeheader['action_keys']

        d['serial_number'] = self.getXMLPathData(r,'serial-number')
        d['registration_number'] = self.getXMLPathData(r,'registration-number')
        d['transaction_date'] = self.getXMLPathData(r,'transaction-date')
        self.tradenum = '%s-%s-%s' % (d['serial_number'],d['registration_number'],d['transaction_date'] )
        d['tradenum'] = self.tradenum

        assert self.tradenum != None
        assert self.tradenum != ''

        d['case'] = self.getXMLPathData(r,'case-file-header/')
        d['filing_date'] = self.getXMLPathData(r,'case-file-header/filing-date')
        d['registration_date'] = self.getXMLPathData(r,'case-file-header/registration-date')
        d['status_code'] = self.getXMLPathData(r,'case-file-header/status-code')
        d['status_date'] = self.getXMLPathData(r,'case-file-header/status-date')
        d['mark_identification'] = self.getXMLPathData(r,'case-file-header/mark-identification')
        d['mark_drawing_code'] = self.getXMLPathData(r,'case-file-header/mark-drawing-code')
        d['published_for_opposition_date'] = self.getXMLPathData(r,'case-file-header/published-for-opposition-date')
        d['amend_to_register_date'] = self.getXMLPathData(r,'case-file-header/amend-to-register-date')
        d['abandonment_date'] = self.getXMLPathData(r,'case-file-header/abandonment-date')
        d['cancellation_code'] = self.getXMLPathData(r,'case-file-header/cancellation-code')
        d['cancellation_date'] = self.getXMLPathData(r,'case-file-header/cancellation-date')
        d['republished_12c_date'] = self.getXMLPathData(r,'case-file-header/republished-12c-date')
        d['domestic_representative_name'] = self.getXMLPathData(r,'case-file-header/domestic-representative-name')
        d['attorney_docket_number'] = self.getXMLPathData(r,'case-file-header/attorney-docket-number')
        d['attorney_name'] = self.getXMLPathData(r,'case-file-header/attorney-name')
        d['principal_register_amended_in'] = self.getXMLPathData(r,'case-file-header/principal-register-amended-in')
        d['supplemental_register_amended_in'] = self.getXMLPathData(r,'case-file-header/supplemental-register-amended-in')
        d['trademark_in'] = self.getXMLPathData(r,'case-file-header/trademark-in')
        d['collective_trademark_in'] = self.getXMLPathData(r,'case-file-header/collective-trademark-in')
        d['service_mark_in'] = self.getXMLPathData(r,'case-file-header/service-mark-in')
        d['collective_service_mark_in'] = self.getXMLPathData(r,'case-file-header/collective-service-mark-in')
        d['collective_membership_mark_in'] = self.getXMLPathData(r,'case-file-header/collective-membership-mark-in')
        d['certification_mark_in'] = self.getXMLPathData(r,'case-file-header/certification-mark-in')
        d['cancellation_pending_in'] = self.getXMLPathData(r,'case-file-header/cancellation-pending-in')
        d['published_concurrent_in'] = self.getXMLPathData(r,'case-file-header/published-concurrent-in')
        d['concurrent_use_in'] = self.getXMLPathData(r,'case-file-header/concurrent-use-in')
        d['concurrent_use_proceeding_in'] = self.getXMLPathData(r,'case-file-header/concurrent-use-proceeding-in')
        d['interference_pending_in'] = self.getXMLPathData(r,'case-file-header/interference-pending-in')
        d['opposition_pending_in'] = self.getXMLPathData(r,'case-file-header/opposition-pending-in')
        d['section_12c_in'] = self.getXMLPathData(r,'case-file-header/section-12c-in')
        d['section_2f_in'] = self.getXMLPathData(r,'case-file-header/section-2f-in')
        d['section_2f_in_part_in'] = self.getXMLPathData(r,'case-file-header/section-2f-in-part-in')
        d['renewal_filed_in'] = self.getXMLPathData(r,'case-file-header/renewal-filed-in')
        d['section_8_filed_in'] = self.getXMLPathData(r,'case-file-header/section-8-filed-in')
        d['section_8_partial_accept_in'] = self.getXMLPathData(r,'case-file-header/section-8-partial-accept-in')
        d['section_8_accepted_in'] = self.getXMLPathData(r,'case-file-header/section-8-accepted-in')
        d['section_15_acknowledged_in'] = self.getXMLPathData(r,'case-file-header/section-15-acknowledged-in')
        d['section_15_filed_in'] = self.getXMLPathData(r,'case-file-header/section-15-filed-in')
        d['supplemental_register_in'] = self.getXMLPathData(r,'case-file-header/supplemental-register-in')
        d['foreign_priority_in'] = self.getXMLPathData(r,'case-file-header/foreign-priority-in')
        d['change_registration_in'] = self.getXMLPathData(r,'case-file-header/change-registration-in')
        d['intent_to_use_in'] = self.getXMLPathData(r,'case-file-header/intent-to-use-in')
        d['intent_to_use_current_in'] = self.getXMLPathData(r,'case-file-header/intent-to-use-current-in')
        d['filed_as_use_application_in'] = self.getXMLPathData(r,'case-file-header/filed-as-use-application-in')
        d['amended_to_use_application_in'] = self.getXMLPathData(r,'case-file-header/amended-to-use-application-in')
        d['use_application_currently_in'] = self.getXMLPathData(r,'case-file-header/use-application-currently-in')
        d['amended_to_itu_application_in'] = self.getXMLPathData(r,'case-file-header/amended-to-itu-application-in')
        d['filing_basis_filed_as_44d_in'] = self.getXMLPathData(r,'case-file-header/filing-basis-filed-as-44d-in')
        d['amended_to_44d_application_in'] = self.getXMLPathData(r,'case-file-header/amended-to-44d-application-in')
        d['filing_basis_current_44d_in'] = self.getXMLPathData(r,'case-file-header/filing-basis-current-44d-in')
        d['filing_basis_filed_as_44e_in'] = self.getXMLPathData(r,'case-file-header/filing-basis-filed-as-44e-in')
        d['amended_to_44e_application_in'] = self.getXMLPathData(r,'case-file-header/amended-to-44e-application-in')
        d['filing_basis_current_44e_in'] = self.getXMLPathData(r,'case-file-header/filing-basis-current-44e-in')
        d['without_basis_currently_in'] = self.getXMLPathData(r,'case-file-header/without-basis-currently-in')
        d['filing_current_no_basis_in'] = self.getXMLPathData(r,'case-file-header/filing-current-no-basis-in')
        d['color_drawing_filed_in'] = self.getXMLPathData(r,'case-file-header/color-drawing-filed-in')
        d['color_drawing_current_in'] = self.getXMLPathData(r,'case-file-header/color-drawing-current-in')
        d['drawing_3d_filed_in'] = self.getXMLPathData(r,'case-file-header/drawing-3d-filed-in')
        d['drawing_3d_current_in'] = self.getXMLPathData(r,'case-file-header/drawing-3d-current-in')
        d['standard_characters_claimed_in'] = self.getXMLPathData(r,'case-file-header/standard-characters-claimed-in')
        d['filing_basis_filed_as_66a_in'] = self.getXMLPathData(r,'case-file-header/filing-basis-filed-as-66a-in')
        d['filing_basis_current_66a_in'] = self.getXMLPathData(r,'case-file-header/filing-basis-current-66a-in')
        d['renewal_date'] = self.getXMLPathData(r,'case-file-header/renewal-date')
        d['law_office_assigned_location_code'] = self.getXMLPathData(r,'case-file-header/law-office-assigned-location-code')
        d['current_location'] = self.getXMLPathData(r,'case-file-header/current-location')
        d['location_date'] = self.getXMLPathData(r,'case-file-header/location-date')
        d['employee_name'] = self.getXMLPathData(r,'case-file-header/employee-name')
        d['corr_add_1'] = self.getXMLPathData(r,'correspondent/address-1')
        d['corr_add_2'] = self.getXMLPathData(r,'correspondent/address-2')
        d['corr_add_3'] = self.getXMLPathData(r,'correspondent/address-3')
        d['corr_add_4'] = self.getXMLPathData(r,'correspondent/address-4')
        d['corr_add_6'] = self.getXMLPathData(r,'correspondent/address-5')
        d['international_registration_number'] = self.getXMLPathData(r,'international-registration/international-registration-number')
        d['international_registration_date'] = self.getXMLPathData(r,'international-registration/international-registration-date')
        d['international_publication_date'] = self.getXMLPathData(r,'international-registration/international-publication-date')
        d['international_renewal_date'] = self.getXMLPathData(r,'international-registration/international-renewal-date')
        d['auto_protection_date'] = self.getXMLPathData(r,'international-registration/auto-protection-date')
        d['international_death_date'] = self.getXMLPathData(r,'international-registration/international-death-date')
        d['international_status_code'] = self.getXMLPathData(r,'international-registration/international-status-code')
        d['international_status_date'] = self.getXMLPathData(r,'international-registration/international-status-date')
        d['priority_claimed_in'] = self.getXMLPathData(r,'international-registration/priority-claimed-in')
        d['priority_claimed_date'] = self.getXMLPathData(r,'international-registration/priority-claimed-date')
        d['first_refusal_in'] = self.getXMLPathData(r,'international-registration/first-refusal-in')


        return [d]


    def getCaseFileStatements(self, r):

        output = []

        for item in r.findall( 'case-file-statements/case-file-statement'):
            subdict = {}

            subdict['tradenum'] = self.tradenum
            subdict['type_code'] = self.getXMLPathData(item, 'type-code')
            subdict['text'] = self.getXMLPathData(item, 'text')
            output.append(subdict)
        return output

    def getCaseFileEventStatements(self, r):
        output = []
        for item in r.findall( 'case-file-event-statements/case-file-event-statement'):
            subdict = {}
            subdict['tradenum'] = self.tradenum
            subdict['code'] = self.getXMLPathData(item, 'code')
            subdict['type'] = self.getXMLPathData(item, 'type')
            subdict['description_text'] = self.getXMLPathData(item, 'description-text')
            subdict['date'] = self.getXMLPathData(item, 'date')
            subdict['number'] = self.getXMLPathData(item, 'number')
            output.append(subdict)
        return output


    def getPriorRegistrationApplications(self, r):
        output = []
        other = self.getXMLPathData(r, 'prior-registration-applications/other-related-in')
        for item in r.findall( 'prior-registration-applications/prior-registration-application'):
            subdict = {}
            subdict['tradenum'] = self.tradenum
            subdict['other_related_in'] = other
            subdict['relationship_type'] = self.getXMLPathData(item, 'relationship-type')
            subdict['number'] = self.getXMLPathData(item, 'number')
            output.append(subdict)
        return output

    def getForeignApplications(self, r):
        output = []
        for item in r.findall( 'foreign-applications/foreign-application'):
            subdict = {}
            subdict['tradenum'] = self.tradenum
            subdict['filing_date'] = self.getXMLPathData(item, 'filing-date')
            subdict['registration_date'] = self.getXMLPathData(item, 'registration-date')
            subdict['registration_expiration_date'] = self.getXMLPathData(item, 'registration-expiration-date')
            subdict['registration_renewal_date'] = self.getXMLPathData(item, 'registration-renewal-date')
            subdict['registration_renewal_expiration_date'] = self.getXMLPathData(item, 'registration-renewal-expiration-date')
            subdict['entry_number'] = self.getXMLPathData(item, 'entry-number')
            subdict['application_number'] = self.getXMLPathData(item, 'application-number')
            subdict['country'] = self.getXMLPathData(item, 'country')
            subdict['relationship_type'] = self.getXMLPathData(item, 'other')
            subdict['other'] = self.getXMLPathData(item, 'registration-number')
            subdict['registration_number'] = self.getXMLPathData(item, 'renewal-number')
            subdict['renewal_number'] = self.getXMLPathData(item, 'foreign-priority-claim-in')
            output.append(subdict)
        return output

    def getClassifications(self, r):
        output = []
        for item in r.findall( 'classifications/classification'):
            subdict = {}
            subdict['tradenum'] = self.tradenum
            subdict['international_code_total_no'] = self.getXMLPathData(item, 'international-code-total-no')
            subdict['us_code_total_no'] = self.getXMLPathData(item, 'us-code-total-no')
            subdict['international_code_concat'] = self.getXMLPathData(item, 'international-code')  # NEED CONCAT
            subdict['us_code_concat'] = self.getXMLPathData(item, 'us-code')   # NEED CONCAT
            subdict['status_code'] = self.getXMLPathData(item, 'status-code')
            subdict['status_date'] = self.getXMLPathData(item, 'status-date')
            subdict['first_use_anywhere_date'] = self.getXMLPathData(item, 'first-use-anywhere-date')
            subdict['first_use_in_commerce_date'] = self.getXMLPathData(item, 'first-use-in-commerce-date')
            subdict['primary_code'] = self.getXMLPathData(item, 'primary-code')
            output.append(subdict)
        return output

    def getCaseFileOwners(self, r):
        output = []
        for item in r.findall( 'case-file-owners/case-file-owner'):
            subdict = {}
            subdict['tradenum'] = self.tradenum
            subdict['entry_number'] = self.getXMLPathData(item, 'entry-number')
            subdict['party_type'] = self.getXMLPathData(item, 'party-type')
            subdict['nationality'] = self.getXMLPathData(item, 'nationality')
            subdict['legal_entity_type_code'] = self.getXMLPathData(item, 'legal-entity-type-code')
            subdict['relationship_type'] = self.getXMLPathData(item, 'entity-statement')
            subdict['entity_statement'] = self.getXMLPathData(item, 'number')
            subdict['relationship_type'] = self.getXMLPathData(item, 'relationship-type')
            subdict['party_name'] = self.getXMLPathData(item, 'party-name')
            subdict['address_1'] = self.getXMLPathData(item, 'address-1')
            subdict['address_2'] = self.getXMLPathData(item, 'address-2')
            subdict['city'] = self.getXMLPathData(item, 'city')
            subdict['state'] = self.getXMLPathData(item, 'state')
            subdict['country'] = self.getXMLPathData(item, 'country')
            subdict['other'] = self.getXMLPathData(item, 'other')
            subdict['postcode'] = self.getXMLPathData(item, 'postcode')
            subdict['dba_aka_text'] = self.getXMLPathData(item, 'dba-aka-text')
            subdict['composed_of_statement'] = self.getXMLPathData(item, 'composed-of-statement')
            subdict['name_change_explanation_concat'] = self.getXMLPathData(item, 'name-change-explanation')    # NEED CONCAT
            output.append(subdict)
        return output


    def getDesignSearch(self, r):
        output = []
        for item in r.findall( 'design-searches/design-search'):
            subdict = {}
            subdict['tradenum'] = self.tradenum
            subdict['code'] = self.getXMLPathData(item, 'code')
            output.append(subdict)
        return output



    def getMadrid(self, r):
        file_output = []
        history_output = []
        h = 0
        for item in r.findall( 'madrid-international-filing-requests/madrid-international-filing-record'):
            subdict = {}
            subdict['tradenum'] = self.tradenum
            subdict['entry_number'] = self.getXMLPathData(item, 'entry-number')
            subdict['reference_number'] = self.getXMLPathData(item, 'reference-number')
            subdict['original_filing_date_uspto'] = self.getXMLPathData(item, 'original-filing-date-uspto')
            subdict['international_registration_number'] = self.getXMLPathData(item, 'international-registration-number')
            subdict['international_registration_date'] = self.getXMLPathData(item, 'international-registration-date')
            subdict['international_status_code'] = self.getXMLPathData(item, 'international-status-code')
            subdict['international_status_date'] = self.getXMLPathData(item, 'international-status-date')
            subdict['international_renewal_date'] = self.getXMLPathData(item, 'international-renewal-date')
            f_id = '%s-%s' % (self.tradenum, str(h))
            h+=1
            subdict['history_id'] = f_id
            for subitem in item.findall('madrid-history-events/madrid-history-event'):
                ssdict = {}
                ssdict['tradenum'] = self.tradenum
                ssdict['history_id'] = f_id
                ssdict['code'] = self.getXMLPathData(subitem,'code')
                ssdict['date'] = self.getXMLPathData(subitem,'date' )
                ssdict['description_text'] = self.getXMLPathData(subitem,'description-text' )
                ssdict['entry_number'] = self.getXMLPathData(subitem,'entry-number' )
                history_output.append(ssdict)


            subdict['madrid_history_events'] = self.getXMLPathData(item, 'madrid-history-events')

            file_output.append(subdict)

        return [file_output, history_output]

    def updateHeaders(self, r):

        self.tradeheader['version_no'] =  self.getXMLPathData(r, 'version/version-no')
        self.tradeheader['version_date'] =  self.getXMLPathData(r, 'version/version-date')
        self.tradeheader['creation_datetime'] =  self.getXMLPathData(r, 'creation-datetime')
        self.tradeheader['data_available_code'] =  self.getXMLPathData(r, 'application-information/data-available-code')
        self.tradeheader['file_segments'] =  self.getXMLPathData(r, 'application-information/file-segments/file-segment')
        self.tradeheader['action_keys'] =  self.getXMLPathData(r, 'application-information/file-segments/action-keys/action-key')
    def parse(self, path):

        tree = ET.parse(path)
        root = tree.getroot()
        #root = ET.fromstring(data)

        #setup global headers
        self.updateHeaders(root)
        print self.headers
        for item in root.findall('application-information/file-segments/action-keys/case-file'):
            writedata = dict()
            self.tradenum = None

            writedata['trademark'] = self.getTrademark(item)

            writedata['case_file_statements'] = self.getCaseFileStatements(item)
            writedata['case_file_event_statement'] = self.getCaseFileEventStatements(item)
            writedata['prior_registration_applications'] = self.getPriorRegistrationApplications(item)

            writedata['foreign_applications'] = self.getForeignApplications(item)
            writedata['classifications'] = self.getClassifications(item)
            writedata['case_file_owners'] = self.getCaseFileOwners(item)

            writedata['design_search'] = self.getDesignSearch(item)
            madridData = self.getMadrid(item)
            writedata['madrid_filing_requests'] = madridData[0]
            writedata['madrid_history_events'] = madridData[1]

            for key in writedata.keys():
                for subitem in writedata[key]:
                    self.writeData(key, subitem)
        self.close()


if __name__ == '__main__':
    f = codecs.open('/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/apc150327.xml','r', encoding='UTF' )
    path = '/Users/matthewharrison/PycharmProjects/cuddlenuggets/PatentZephyr/PatentDisplayBuild'
    data = f.read().encode('utf-8')
    #root = ET.fromstring(data)


    p =parser(path,'taCurrent')
    p.parse('/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/apc150327.xml')
