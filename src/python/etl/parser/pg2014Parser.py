import codecs
import xml.etree.ElementTree as ET
import os

import PatentZephyr.src.python.CFPAPIconfig as config
import PatentZephyr.src.python.etl.parser.schema.pg2014 as schema
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
        self.patnum = None
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
#  Patent table
#
#
#

    def getPatent(self,root):
        o = dict()


        if 'lang' in root.keys():
            o['lang'] = root.attrib['lang']
        if 'dtd-version' in root.keys():
            o['dtd-version'] = root.attrib['dtd-version']
        if 'file' in root.keys():
            o['file'] = root.attrib['file']
        if 'status' in root.keys():
            o['status'] = root.attrib['status']
        if 'country' in root.keys():
            o['country'] = root.attrib['country']
        #['file_reference_id'] = self.getEval("base.find('publication-reference/document-id/country').text")
        o['pub_country'] = self.getXMLPathData(root,'us-bibliographic-data-grant/publication-reference/document-id/country')
        o['pub_doc_number'] = self.getXMLPathData(root,'us-bibliographic-data-grant/publication-reference/document-id/doc-number')
        o['pub_kind'] = self.getXMLPathData(root,'us-bibliographic-data-grant/publication-reference/document-id/kind')
        o['pub_name'] = self.getXMLPathData(root,'us-bibliographic-data-grant/publication-reference/document-id/name')
        o['pub_date'] = self.getXMLPathData(root,'us-bibliographic-data-grant/publication-reference/document-id/date')

        o['app_country'] = self.getXMLPathData(root,'us-bibliographic-data-grant/application-reference/document-id/country')
        o['app_doc_number'] = self.getXMLPathData(root,'us-bibliographic-data-grant/application-reference/document-id/doc-number')
        o['app_kind'] = self.getXMLPathData(root,'us-bibliographic-data-grant/application-reference/document-id/kind')
        o['app_name'] = self.getXMLPathData(root,'us-bibliographic-data-grant/application-reference/document-id/name')
        o['app_date'] = self.getXMLPathData(root,'us-bibliographic-data-grant/application-reference/document-id/date')


        if root.find('us-bibliographic-data-grant/us-sir-flag'):
            o['us_sir_flag'] = 'T'

        o['us_app_series_code'] = self.getXMLPathData(root,'us-bibliographic-data-grant/us-application-series-code')

        if root.find('us-bibliographic-data-grant/us-issued-on-continued-prosecution-application'):
            o['us_issue_ocpa'] = 'T'
        if root.find('us-bibliographic-data-grant/rule-47-flag'):
            o['rule_47_flag'] = 'T'


        o['invention_title'] = self.getXMLPathData(root,'us-bibliographic-data-grant/invention-title')
        o['patnum'] = o['pub_country']+o['pub_doc_number']+o['pub_kind']
        self.patnum = o['patnum']
        o['us_claim_statement'] = self.getXMLPathData(root,'us-claim-statement')

        return [o]
#
#  party table
#
#
#
    def getPeople(self,apps,type):
        output = []
        for person in apps:
            persond =dict()

            if 'app-type' in person.keys():
                persond['app_type'] = person.attrib['app-type']
            if 'rep-type' in person.keys():
                persond['rep_type'] = person.attrib['rep-type']
            if 'designation' in person.keys():
                persond['designation'] = person.attrib['designation']
            if 'assignee-type' in person.keys():
                persond['assignee_type'] = person.attrib['assignee-type']
            if 'applicant-authority-category' in person.keys():
                persond['applicant_authority_category'] = person.attrib['applicant-authority-category']

            subitems = person.findall('addressbook')
            for subitems in subitems:
                adddict = dict()
                adddict['patnum'] = self.patnum
                adddict['party_type'] = type
                adddict['us_rights'] = self.getXMLPathData(person, 'us-rights')

                output.append(dict(persond.items() +adddict.items()+self.parsePerson(subitems).items() +self.parseAddress(subitems).items() ))


        return output

    def parsePerson(self, lelements):
        o = dict()

        if 'sequence' in lelements.keys():
            o['sequence'] = lelements.attrib['sequence']
        o['first_name'] = self.getXMLPathData(lelements,'first-name')
        o['middle_name'] = self.getXMLPathData(lelements,'middle-name')
        o['last_name'] = self.getXMLPathData(lelements,'last-name')
        o['name'] = self.getXMLPathData(lelements,'name')
        o['orgname'] = self.getXMLPathData(lelements,'orgname')
        o['fax'] = self.getXMLPathData(lelements,'fax')
        o['email'] = self.getXMLPathData(lelements,'email')
        o['url'] = self.getXMLPathData(lelements,'url')
        o['ead'] = self.getXMLPathData(lelements,'ead')
        o['dtext'] = self.getXMLPathData(lelements,'dtext')
        o['prefix'] = self.getXMLPathData(lelements,'prefix')
        return o

    def parseAddress(self, aelement):
        o = dict()
        o['address_1'] = self.getXMLPathData(aelement, 'address/address-1')
        o['address_2'] = self.getXMLPathData(aelement, 'address/address-2')
        o['address_3'] = self.getXMLPathData(aelement, 'address/address-3')
        o['country'] = self.getXMLPathData(aelement, 'address/country')
        o['city'] = self.getXMLPathData(aelement, 'address/city')
        o['state'] = self.getXMLPathData(aelement, 'address/state')
        return o

    def getParties(self,bib):
        output = list()
        us_applicants = bib.findall('us-parties/us-applicants/us-applicant')
        agents = bib.findall('us-parties/agents/agent')
        inventors = bib.findall('us-parties/inventors/inventor')
        dead_inventors = bib.findall('us-parties/inventors/inventor')
        #add dead inventors
        for d in dead_inventors:
            o = dict()
            o['patnum'] = self.patnum
            o['party_type'] = 'deceased-inventor'
            o['deceased_inventor_raw'] = util.clean(util.traverse(d))
            output.append(o)
        dead_inventors_old = bib.findall('us-deceased-inventor')
        output += self.getPeople(us_applicants,'us-applicants')
        output += self.getPeople(agents,'agent')
        output += self.getPeople(inventors,'inventor')
        output += self.getPeople(dead_inventors_old,'deceased-inventor')
        return output
#
#  Abstract table
#
#
#

    def getAbstract(self,r):
        output = []
        abstracts = r.findall('abstract')
        for ab in abstracts:
            for p in ab.findall('p'):
                pdict = dict()
                if 'id' in p.keys():
                    pdict['id'] = p.attrib['id']
                if 'num' in p.keys():
                    pdict['num'] = p.attrib['num']
                pdict['adata'] = p.text
                pdict['patnum'] = self.patnum
                output.append(pdict)
        return output
#
#  priority claims table
#
#
#

    def getPriClaims(self,b):
        output = []
        claims = b.findall('priority-claims/priority-claim')
        for c in claims:
            o = dict()
            if 'sequence' in c.keys():
                o['sequence'] = c.attrib['sequence']
            if 'kind' in c.keys():
                o['kind'] = c.attrib['kind']
            o['document_number'] = self.getXMLPathData(c,'doc-number')
            o['country'] = self.getXMLPathData(c,'country')
            o['priority_date'] = self.getXMLPathData(c,'date')
            o['office_of_filing_region'] = self.getXMLPathData(c,'office-of-filing/region/country')
            o['office_of_filing_country'] = self.getXMLPathData(c,'office-of-filing/country')
            o['patnum'] = self.patnum
            output.append(o)
        return output

#
#  patent terms
#
#
#

    def getPTerms(self,b):
        output = []

        for i in b.findall('us-term-of-grant'):
            o = dict()
            o['patnum'] = self.patnum
            o['text'] = self.getXMLPathData(i,'text')
            o['length_of_grant'] = self.getXMLPathData(i,'length-of-grant')
            o['us_term_extension'] = self.getXMLPathData(i,'us-term-extension')
            o['disclaimer'] = self.getXMLPathData(i,'disclaimer/text')
            o['lapse_of_patent_doc_id'] = self.getXMLPathData(i,'lapse-of-patent/document-id')
            o['lapse_of_patent_text'] = self.getXMLPathData(i,'lapse-of-patent/text')
            output.append(o)
        return output
#
#  patent citations
#
#
#

    def getCitations(self,b):
        output = []

        for c in b.findall('us-references-cited/us-citation'):

            for pc in c.findall('patcit'):
                o = dict()
                if 'num' in pc.keys():
                    o['num'] = pc.attrib['num']
                o['type'] = 'patcit'
                o['nplcit_text'] = self.getXMLPathData(pc, 'text')
                o['country'] = self.getXMLPathData(pc, 'document-id/country')
                o['doc_number'] = self.getXMLPathData(pc, 'document-id/doc-number')
                o['kind'] = self.getXMLPathData(pc, 'document-id/kind')
                o['name'] = self.getXMLPathData(pc, 'document-id/country')
                o['date'] = self.getXMLPathData(pc, 'document-id/date')
                o['patnum'] = self.patnum
                output.append(o)

            for npl in c.findall('nplcit'):
                o = dict()
                if 'num' in npl.keys():
                    o['num'] = npl.attrib['num']
                o['type'] = 'patcit'
                o['nplcit_text'] = self.getXMLPathData(npl, 'text')
                o['country'] = self.getXMLPathData(npl, 'country')
                o['other_cit'] = self.getXMLPathData(npl, 'othercit')
                o['patnum'] = self.patnum
                output.append(o)
        return output

#
#  patent citations
#
#
#

# IPCR
    def getIPCR(self,b):
        output = []

        for c in b.findall('classifications-ipcr/classification-ipcr'):
            o = dict()
            o['patnum'] =self.patnum
            o['version'] =self.getXMLPathData(c,'ipc-version-indicator/date')
            o['classification_level'] =self.getXMLPathData(c,'classification-level')
            o['section'] =self.getXMLPathData(c,'section')
            o['class'] =self.getXMLPathData(c,'class')
            o['subclass'] =self.getXMLPathData(c,'subclass')
            o['main_group'] =self.getXMLPathData(c,'main-group')
            o['subgroup'] =self.getXMLPathData(c,'subgroup')
            o['symbol-position'] =self.getXMLPathData(c,'symbol-position')
            o['action_date'] =self.getXMLPathData(c,'action-date/date')
            o['classification_value'] =self.getXMLPathData(c,'classification-value')
            o['generating_office'] =self.getXMLPathData(c,'generating-office/country')
            o['classification_status'] =self.getXMLPathData(c,'classification-status')
            o['classification_data_source'] =self.getXMLPathData(c,'classification-data-source')
            output.append(o)
        return output
# CPC
    def getCPC(self,b):
        output = []

        for c in b.findall('classifications-cpc/main-cpc/classification-cpc'):

            o = dict()
            o['patnum'] =self.patnum
            o['type'] = 'main'
            o['version'] =self.getXMLPathData(c,'cpc-version-indicator/date')
            o['classification_level'] =self.getXMLPathData(c,'classification-level')
            o['section'] =self.getXMLPathData(c,'section')
            o['class'] =self.getXMLPathData(c,'class')
            o['subclass'] =self.getXMLPathData(c,'subclass')
            o['main_group'] =self.getXMLPathData(c,'main-group')
            o['subgroup'] =self.getXMLPathData(c,'subgroup')
            o['symbol-position'] =self.getXMLPathData(c,'symbol-position')
            o['action_date'] =self.getXMLPathData(c,'action-date/date')
            o['classification_value'] =self.getXMLPathData(c,'classification-value')
            o['generating_office'] =self.getXMLPathData(c,'generating-office/country')
            o['classification_status'] =self.getXMLPathData(c,'classification-status')
            o['classification_data_source'] =self.getXMLPathData(c,'classification-data-source')
            o['scheme_origination'] = self.getXMLPathData(c,'scheme-origination-code')
            output.append(o)
        for c in b.findall('classifications-cpc/further-cpc/classification-cpc'):
            o = dict()
            o['patnum'] =self.patnum
            o['type'] = 'further-cpc'
            o['version'] =self.getXMLPathData(c,'cpc-version-indicator/date')
            o['classification_level'] =self.getXMLPathData(c,'classification-level')
            o['section'] =self.getXMLPathData(c,'section')
            o['class'] =self.getXMLPathData(c,'class')
            o['subclass'] =self.getXMLPathData(c,'subclass')
            o['main_group'] =self.getXMLPathData(c,'main-group')
            o['subgroup'] =self.getXMLPathData(c,'subgroup')
            o['symbol-position'] =self.getXMLPathData(c,'symbol-position')
            o['action_date'] =self.getXMLPathData(c,'action-date/date')
            o['classification_value'] =self.getXMLPathData(c,'classification-value')
            o['generating_office'] =self.getXMLPathData(c,'generating-office/country')
            o['classification_status'] =self.getXMLPathData(c,'classification-status')
            o['classification_data_source'] =self.getXMLPathData(c,'classification-data-source')
            o['scheme_origination'] = self.getXMLPathData(c,'scheme-origination-code')
            output.append(o)
        for c in b.findall('classifications-cpc/further-cpc/combination-set'):
            o = dict()
            o['patnum'] =self.patnum
            o['type'] = 'combination-set'
            o['combination_group_number'] = self.getXMLPathData(c,'group-number')
            for sc in c.findall('combination-rank'):
                sub =dict()
                sub['combination_rank_number'] = self.getXMLPathData(sc,'rank_number')

                sub['version'] =self.getXMLPathData(sc,'classification-cpc/cpc-version-indicator/date')
                sub['classification_level'] =self.getXMLPathData(sc,'classification-cpc/classification-level')
                sub['section'] =self.getXMLPathData(sc,'classification-cpc/section')
                sub['class'] =self.getXMLPathData(sc,'classification-cpc/class')
                sub['subclass'] =self.getXMLPathData(sc,'classification-cpc/subclass')
                sub['main_group'] =self.getXMLPathData(sc,'classification-cpc/main-group')
                sub['subgroup'] =self.getXMLPathData(sc,'classification-cpc/subgroup')
                sub['symbol-position'] =self.getXMLPathData(sc,'classification-cpc/symbol-position')
                sub['action_date'] =self.getXMLPathData(sc,'classification-cpc/action-date/date')
                sub['classification_value'] =self.getXMLPathData(sc,'classification-cpc/classification-value')
                sub['generating_office'] =self.getXMLPathData(sc,'classification-cpc/generating-office/country')
                sub['classification_status'] =self.getXMLPathData(sc,'classification-cpc/classification-status')
                sub['classification_data_source'] =self.getXMLPathData(sc,'classification-cpc/classification-data-source')
                sub['scheme_origination'] = self.getXMLPathData(sc,'classification-cpc/scheme-origination-code')
                output.append(dict(o.items() + sub.items()))
        return output
# locarno
    def getLocarno(self, bib):
        output = []
        edition = ''
        for i in bib.findall('classification-locarno'):
            o = dict()

            o['edition'] = self.getXMLPathData(i, 'edition')
            o['locarno'] = self.getXMLPathData(i, 'main-classification')
            o['text'] = self.getXMLPathData(i, 'text')
            o['type'] = 'main'
            edition = o['edition']
            o['patnum'] =self.patnum
            output.append(o)
        for i in bib.findall('classification-locarno/further-classification'):

            subdict = dict()
            subdict['type'] ='further'
            subdict['edition'] = edition
            subdict['patnum'] = self.patnum
            #
            # WARN add clearn function here
            #
            subdict['locarno'] = i.text
            #
            #
            output.append(subdict)
        return output
# national
    def getNational(self, bib):
        output = []
        edition = ''
        additional_info = ''
        for i in bib.findall('classification-national'):
            o = dict()
            o['edition'] = self.getXMLPathData(i, 'edition')
            o['national'] = self.getXMLPathData(i, 'main-classification')
            o['country'] = self.getXMLPathData(i, 'couintry')
            o['text'] = self.getXMLPathData(i, 'text')
            o['type'] = 'main'
            edition = o['edition']
            o['patnum'] =self.patnum
            o['additional_info'] = self.getXMLPathData(i, 'additional-info')  # many to one here might nee to check
            output.append(o)
        for i in bib.findall('classification-national/further-classification'):
            subdict = dict()
            subdict['type'] ='further'
            subdict['edition'] = edition
            subdict['patnum'] = self.patnum
            #
            # WARN add clearn function here
            #
            subdict['national'] = i.text
            #
            #
            #output.append(subdict)
        return output


#
#  related documents
#
#addition | division | continuation | continuation-in-part | continuing-reissue | reissue | us-divisional-reissue | reexamination | us-reexamination-reissue-merger | substitution | us-provisional-application | utility-model-basis | correction | related-publication)
#
    def getRelatedDocuments(self, bib):
        output = []
        for i in bib.findall('us-related-documents'):
            children = i.getchildren()
            for c in children:
                tag = c.tag
                if tag in ['addition','division','continuation','continuation-in-part','continuing-reissue','reissue','reexamination','us-reexamination-reissue-merger','substitution',]:
                    #relation!  should always be one
                    rel = dict()
                    rel['type'] = tag
                    rel['patnum'] = self.patnum
                    rel['sub_xml_type'] = 'relation'
                    #parent
                    rel['parent_country'] = self.getXMLPathData(c, 'relation/parent-doc/document-id/country')
                    rel['parent_doc_number'] = self.getXMLPathData(c, 'relation/parent-doc/document-id/doc-number')
                    rel['parent_kind'] = self.getXMLPathData(c, 'relation/parent-doc/document-id/kind')
                    rel['parent_name'] = self.getXMLPathData(c, 'relation/parent-doc/document-id/name')
                    rel['parent_date'] = self.getXMLPathData(c, 'relation/parent-doc/document-id/date')
                    rel['parent_status'] = self.getXMLPathData(c, 'relation/parent-doc/parent-status')
                    #parent grant
                    rel['parent_grant_country'] = self.getXMLPathData(c, 'relation/parent-doc/parent-grant-document/document-id/country')
                    rel['parent_grant_doc_number'] = self.getXMLPathData(c, 'relation/parent-doc/parent-grant-document/document-id/doc-number')
                    rel['parent_grant_kind'] = self.getXMLPathData(c, 'relation/parent-doc/parent-grant-document/document-id/kind')
                    rel['parent_grant_name'] = self.getXMLPathData(c, 'relation/parent-doc/parent-grant-document/document-id/name')
                    rel['parent_grant_date'] = self.getXMLPathData(c, 'relation/parent-doc/parent-grant-document/document-id/date')
                    #parent pct
                    rel['parent_pct_country'] = self.getXMLPathData(c, 'relation/parent-doc/parent-pct-document/document-id/country')
                    rel['parent_pct_doc_number'] = self.getXMLPathData(c, 'relation/parent-doc/parent-pct-document/document-id/doc-number')
                    rel['parent_pct_kind'] = self.getXMLPathData(c, 'relation/parent-doc/parent-pct-document/document-id/kind')
                    rel['parent_pct_name'] = self.getXMLPathData(c, 'relation/parent-doc/parent-pct-document/document-id/name')
                    rel['parent_pct_date'] = self.getXMLPathData(c, 'relation/parent-doc/parent-pct-document/document-id/date')
                    #child
                    rel['child_country'] = self.getXMLPathData(c, 'relation/child-doc/document-id/country')
                    rel['child_doc_number'] = self.getXMLPathData(c, 'relation/child-doc/document-id/doc-number')
                    rel['child_kind'] = self.getXMLPathData(c, 'relation/child-doc/document-id/kind')
                    rel['child_name'] = self.getXMLPathData(c, 'relation/child-doc/document-id/name')
                    rel['child_date'] = self.getXMLPathData(c, 'relation/child-doc/document-id/date')
                    output.append(rel)
                elif tag in ['us-divisional-reissue']:

                    subdict = dict()
                    subdict['type'] = tag
                    subdict['sub_xml_type'] = 'us-relation'
                    subdict['patnum'] = self.patnum
                    subdict['parent_country'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/country')
                    subdict['parent_doc_number'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/doc-number')
                    subdict['parent_kind'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/kind')
                    subdict['parent_name'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/name')
                    subdict['parent_date'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/date')
                    subdict['parent_status'] = self.getXMLPathData(c, 'us-relation/parent-doc/parent-status')
                    child_docs = c.findall('us-relation/child-doc')
                    #check if there are child-docs if not return only parent info
                    if len(child_docs) > 0:
                        for cc in child_docs:
                            o = dict()
                            o['child_country'] = self.getXMLPathData(cc, 'document-id/country')
                            o['child_doc_number'] = self.getXMLPathData(cc, 'document-id/doc-number')
                            o['child_kind'] = self.getXMLPathData(cc, 'document-id/kind')
                            o['child_name'] = self.getXMLPathData(cc, 'document-id/name')
                            o['child_date'] = self.getXMLPathData(cc, 'document-id/date')
                            output.append(dict(subdict.items() +o.items()) )
                    else:
                        output.append(subdict)
                elif tag in ['us-provisional-application']:
                    prov = dict()
                    prov['type'] = tag
                    prov['sub_xml_type'] = 'us-provisional-application'
                    prov['patnum'] = self.patnum
                    prov['parent_country'] = self.getXMLPathData(c, 'document-id/country')
                    prov['parent_doc_number'] = self.getXMLPathData(c, 'document-id/doc-number')
                    prov['parent_kind'] = self.getXMLPathData(c, 'document-id/kind')
                    prov['parent_name'] = self.getXMLPathData(c, 'document-id/name')
                    prov['parent_date'] = self.getXMLPathData(c, 'document-id/date')
                    prov['parent_status'] = self.getXMLPathData(c, 'us-provisional-application-status')
                    output.append(prov)
                elif tag in ['correction']:
                    cor = dict()
                    cor['type'] = tag
                    cor['sub_xml_type'] = 'correction'
                    cor['patnum'] = self.patnum
                    cor['parent_country'] = self.getXMLPathData(c, 'document-corrected/document-id/country')
                    cor['parent_doc_number'] = self.getXMLPathData(c, 'document-corrected/document-id/doc-number')
                    cor['parent_kind'] = self.getXMLPathData(c, 'document-corrected/document-id/kind')
                    cor['parent_name'] = self.getXMLPathData(c, 'document-corrected/document-id/name')
                    cor['parent_date'] = self.getXMLPathData(c, 'document-corrected/document-id/date')
                    cor['correction_type'] = self.getXMLPathData(c, 'type-of-correction')
                    cor['correction_gazette_reference_num'] = self.getXMLPathData(c, 'gazette-reference/gazette-num')
                    cor['correction_gazette_reference_date'] = self.getXMLPathData(c, 'gazette-reference/date')
                    cor['correction_gazette_reference_text'] = self.getXMLPathData(c, 'gazette-reference/text')
                    cor['correction_text'] = self.getXMLPathData(c, 'text')
                    output.append(cor)
                elif tag in ['related-publication']:

                    rel_text = util.clean(c.text)

                    for d in c.findall('document-id'):
                        relpub = dict()
                        relpub['type'] = tag
                        relpub['sub_xml_type'] = 'related-publication-doc'
                        relpub['patnum'] = self.patnum
                        relpub['parent_country'] = self.getXMLPathData(d, 'country')
                        relpub['parent_doc_number'] = self.getXMLPathData(d, 'doc-number')
                        relpub['parent_kind'] = self.getXMLPathData(d, 'kind')
                        relpub['parent_name'] = self.getXMLPathData(d, 'name')
                        relpub['parent_date'] = self.getXMLPathData(d, 'date')
                        relpub['related_publication_text'] = rel_text
                        output.append(relpub)
                else:
                    assert 1==0

        return output



#
#  claims
#
#
#
    def getClaims(self, root):
        output =[]
        claims = root.findall('claims/claim')
        for c in claims:
            claim_text = c.findall('claim-text')
            o = dict()
            o['patnum'] = self.patnum
            o['num'] = c.attrib['num']
            o['raw'] = util.clean(util.traverse(c))
            output.append(o)
        return output


    def parse(self, data):
        self.patnum = ''
        root = ET.fromstring(data)
        bib = root.find('us-bibliographic-data-grant')
        writedata = dict()
        writedata['patents'] = self.getPatent(root)
        writedata['parties'] = self.getParties(bib)
        writedata['abstract'] = self.getAbstract(root)
        writedata['pri_claims'] = self.getPriClaims(bib)
        writedata['patent_terms'] = self.getPTerms(bib)
        writedata['us_citations'] = self.getCitations(bib)
        writedata['us_IPCR'] = self.getIPCR(bib)
        writedata['us_CPC'] = self.getCPC(bib)
        writedata['us_locarno'] = self.getLocarno(bib)
        writedata['us_national'] = self.getNational(bib)
        writedata['rel_documents'] = self.getRelatedDocuments(bib)
        writedata['claims'] = self.getClaims(root)


        for key in writedata.keys():
            for subitem in writedata[key]:
                self.writeData(key, subitem)
        self.patnum = None
        self.close()

if __name__ == '__main__':

    f = codecs.open('/Users/matthewharrison/PycharmProjects/cuddlenuggets/PatentZephyr/src/python/etl/templates/DTD/sample_pg2014.xml','r', encoding='UTF' )
    path = '/Users/matthewharrison/PycharmProjects/cuddlenuggets/PatentZephyr/PatentDisplayBuild'
    data = f.read()

    p =parser(path)
    p.parse(data)