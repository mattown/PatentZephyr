import codecs
import xml.etree.ElementTree as ET
import os

import PatentZephyr.src.python.CFPAPIconfig as config
import PatentZephyr.src.python.etl.parser.schema.aCurrent as schema
import ParserUtils as util



#
#
#  includes Revisions
#           us-patent-application-v44-2014-04-03.dtd
#
#
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
        self.app_num = None
        self.us_claim_statement = None
        self.headerdata = {
            'h_lang' : '',
            'h_dtd_version' : '',
            'h_file' : '',
            'h_status' : '',
            'h_id' : '',
            'h_country' : '',
            'h_file_reference_id' : '',
            'h_date_produced' : '',
            'h_date_publ' : '' ,
            'seq_list_p' : '',
            'seq_list_p_id' : '',
            'seq_list_p_num' : '' ,
            'seq_list_p_carriers' : '',
            'seq_list_p_file' : '',
            'seq_list_p_file_type' : ''
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
        #try:
        self.filewriters[filename].write(config.file_delimiter.join(output)+config.file_newline)
        #except:
        #    print 'error',output, ddict,self.headers[filename]
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
                return self.getNode(node)
        else:
            return config.null_value

    def getNode(self, node):
        return util.clean(util.traverse(node))



#
#  Parser
#


    def getApplication(self, b):
        o = {}

        o['h_lang'] = self.headerdata['h_lang']
        o['h_dtd_version'] = self.headerdata['h_dtd_version']
        o['h_file'] = self.headerdata['h_file']
        o['h_status'] = self.headerdata['h_status']
        o['h_id'] = self.headerdata['h_id']
        o['h_country'] = self.headerdata['h_country']
        o['h_file_reference_id'] = self.headerdata['h_file_reference_id']
        o['h_date_produced'] = self.headerdata['h_date_produced']
        o['h_date_publ'] = self.headerdata['h_date_publ']

        pub_ref = b.find('publication-reference')
        pub_ref_doc = b.find('publication-reference/document-id')
        if 'id' in pub_ref.keys():
            o['pub_h_id'] = pub_ref.attrib['id']
        if 'lang' in pub_ref_doc.keys():
            o['pub_lang'] = pub_ref_doc.attrib['lang']
        o['pub_country'] = self.getXMLPathData(b,'publication-reference/document-id/country')
        o['pub_no'] = self.getXMLPathData(b,'publication-reference/document-id/doc-number')
        o['pub_kind'] = self.getXMLPathData(b,'publication-reference/document-id/kind')
        o['pub_name'] = self.getXMLPathData(b,'publication-reference/document-id/name')
        o['pub_date'] = self.getXMLPathData(b,'publication-reference/document-id/date')



        app_ref = b.find('application-reference')
        if 'id' in app_ref.keys():
            o['app_h_id'] = app_ref.attrib['id']
        if 'appl-type' in app_ref.keys():
            o['app_h_type'] = app_ref.attrib['appl-type']
        o['app_country'] = self.getXMLPathData(b,'application-reference/document-id/country')
        o['app_no'] = self.getXMLPathData(b,'application-reference/document-id/doc-number')
        o['app_kind'] = self.getXMLPathData(b,'application-reference/document-id/kind')
        o['app_name'] = self.getXMLPathData(b,'application-reference/document-id/name')
        o['app_date'] = self.getXMLPathData(b,'application-reference/document-id/date')



        #status codes

        o['us_application_series_code'] = self.getXMLPathData(b, 'us-application-series-code')

        t = b.find('us-publication-filing-type')
        if t != None:
            o['us_publication_filing_type'] = t.tag

        t = b.find('us-publication-of-continued-prosecution-application')
        if t != None:
            o['us_publication_of_continued_prosecution_application'] = 'This is a publication of a continued prosecution application (CPA) filed under 37 CFR 1.53(d).'

        t = b.find('rule-47-flag')
        o['rule_47_flag'] = 'N'
        if t != None:
            o['rule_47_flag'] = 'Y'

        #invention
        t = b.find('invention-title')
        if t != None:
            o['invention_title'] = self.getXMLPathData(b, 'invention-title')
            if 'id' in t.keys():
                o['invention_title_id'] = t.attrib['id']
            if 'lang' in t.keys():
                o['invention_title_lang'] = t.attrib['lang']

        # us botanic
        o['us_botanic_latin_name'] = self.getXMLPathData(b, 'us-botanic/latin-name')
        o['us_botanic_variety'] = self.getXMLPathData(b, 'us-botanic/variety')

        # pct-or-regional-filing-data

        o['pctrf_country'] = self.getXMLPathData(b,'pct-or-regional-filing-data/document-id/country')
        o['pctrf_date'] = self.getXMLPathData(b,'pct-or-regional-filing-data/document-id/date')
        o['pctrf_doc_num'] = self.getXMLPathData(b,'pct-or-regional-filing-data/document-id/doc-number')
        o['pctrf_kind'] = self.getXMLPathData(b,'pct-or-regional-filing-data/document-id/kind')
        o['pctrf_name'] = self.getXMLPathData(b,'pct-or-regional-filing-data/document-id/name')
        o['us_371c124_date'] = self.getXMLPathData(b,'pct-or-regional-filing-data/us-371c124-date/date')
        o['us_371c12_date'] = self.getXMLPathData(b,'pct-or-regional-filing-data/us-371c12-date/date')


        o['pctrp_country'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/document-id/country')
        o['pctrp_date'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/document-id/date')
        o['pctrp_doc_num'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/document-id/doc-number')
        o['pctrp_kind'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/document-id/kind')
        o['pctrp_name'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/document-id/name')
        o['pctrp_gazette_num'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/gazette-reference/gazette-num')
        o['pctrp_gazette_date'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/gazette-reference/date')
        o['pctrp_gazette_text'] = self.getXMLPathData(b,'pct-or-regional-publishing-data/gazette-reference/text')





        # sequence list
        seq_list = b.find('us-sequence-list-doc')
        if seq_list != None:
            o['seq_list_p'] = self.getXMLPathData(b,'us-sequence-list-doc/p')
            if 'id' in seq_list.keys():
                o['seq_list_p_id'] = seq_list.attrib['id']
            if 'num' in seq_list.keys():
                o['seq_list_p_num'] = seq_list.attrib['num']

        carrier = b.find('us-sequence-list-doc/sequence-list')
        if carrier != None:
            if 'carriers' in seq_list.keys():
                o['seq_list_p_carriers'] = carrier.attrib['carriers']
            if 'file' in seq_list.keys():
                o['seq_list_p_file'] = carrier.attrib['file']
            if 'seq-file-type' in seq_list.keys():
                o['seq_list_p_file_type'] = carrier.attrib['seq-file-type']

        o['us_claim_statement'] = self.us_claim_statement

        self.app_num = '%s%s%s' % (o['pub_country'],o['pub_no'],o['pub_kind'])

        o['app_num'] = self.app_num
        #print o
        return [o]


    # non bib stuff

    def getAbstracts(self, r):

        o = []

        for a in r.findall('abstract'):
            k = a.keys()
            h_id = None
            if 'id' in k:
                h_id = a.attrib['id']
            for c in a.findall('p'):

                u = {}
                u['app_num'] = self.app_num
                u['h_id'] = h_id
                u['adata'] = self.getNode(c)
                kk = c.keys()
                if 'id' in kk:
                    u['id'] = c.attrib['id']
                if 'num' in kk:
                    u['num'] = c.attrib['num']
                o.append(u)
        return o


    def getDrawings(self, r):
        o = []
        for item in r.findall('drawings/figure/img'):
            u = {}
            k = item.keys()
            u['app_num'] = self.app_num
            if 'id' in k:
                u['h_id'] = item.attrib['id']
            if 'he' in k:
                u['h_he'] = item.attrib['he']
            if 'wi' in k:
                u['h_wi'] = item.attrib['wi']
            if 'file' in k:
                u['h_file'] = item.attrib['file']
            if 'alt' in k:
                u['h_alt'] = item.attrib['alt']
            if 'img-content' in k:
                u['h_img_content'] = item.attrib['img-content']
            if 'img-format' in k:
                u['h_img_format'] = item.attrib['img-format']
            if 'orientation' in k:
                u['h_orientation'] = item.attrib['orientation']
            if 'inline' in k:
                u['h_inline'] = item.attrib['inline']
            o.append(u)
        return o

    def getDescriptions(self,r):
        o =[]
        for item in r.findall('description/description-of-drawings/p'):
            u = {}
            u['app_num'] = self.app_num
            k = item.keys()
            u['is_description_of_drawing'] = 'T'
            u['is_heading'] = 'F'
            if 'id' in k:
                u['h_id'] = item.attrib['id']
            if 'he' in k:
                u['h_p_num'] = item.attrib['num']
            if 'wi' in k:
                u['h_header_level'] = item.attrib['level']
            u['ddata'] = self.getNode(item)
            o.append(u)
        for item in r.findall('description/description-of-drawings/heading'):
            u = {}
            u['app_num'] = self.app_num
            k = item.keys()
            u['is_description_of_drawing'] = 'T'
            u['is_heading'] = 'T'
            if 'id' in k:
                u['h_id'] = item.attrib['id']
            if 'he' in k:
                u['h_p_num'] = item.attrib['num']
            if 'wi' in k:
                u['h_header_level'] = item.attrib['level']
            u['ddata'] = self.getNode(item)
            o.append(u)
        for item in r.findall('description/p'):
            u = {}
            u['app_num'] = self.app_num
            k = item.keys()
            u['is_description_of_drawing'] = 'F'
            u['is_heading'] = 'F'
            if 'id' in k:
                u['h_id'] = item.attrib['id']
            if 'he' in k:
                u['h_p_num'] = item.attrib['num']
            if 'wi' in k:
                u['h_header_level'] = item.attrib['level']
            u['ddata'] = self.getNode(item)
            o.append(u)
        for item in r.findall('description/heading'):
            u = {}
            u['app_num'] = self.app_num
            k = item.keys()
            u['is_description_of_drawing'] = 'F'
            u['is_heading'] = 'T'
            if 'id' in k:
                u['h_id'] = item.attrib['id']
            if 'he' in k:
                u['h_p_num'] = item.attrib['num']
            if 'wi' in k:
                u['h_header_level'] = item.attrib['level']
            u['ddata'] = self.getNode(item)
            o.append(u)

        return o



    def getChemistry(self,r):

        o = []
        for item in r.findall('us-chemistry'):
            u={}
            u['app_num'] = self.app_num
            k = item.keys()
            if 'idref' in k:
                u['idref'] = item.attrib['idref']
            if 'cdx-file' in k:
                u['cdx_file'] = item.attrib['cdx-file']
            if 'mol-file' in k:
                u['mol_file'] = item.attrib['mol-file']
            o.append(u)
        return o


    def getMath(self, r):
        o = []
        for item in r.findall('us-math'):
            u = {}
            u['app_num'] = self.app_num
            k = item.keys()
            if 'idrefs' in k:
                u['idrefs'] = item.attrib['idrefs']
            if 'cdx-file' in k:
                u['cdx_file'] = item.attrib['cdx-file']
            if 'nb-file' in k:
                u['nb_file'] = item.attrib['nb-file']
            img = item.find('img')
            if img != None:
                k = img.keys()

                if 'he' in k:
                    u['h_he'] = img.attrib['he']
                if 'wi' in k:
                    u['h_wi'] = img.attrib['wi']
                if 'nb-file' in k:
                    u['nb_file'] = img.attrib['nb-file']
                if 'alt' in k:
                    u['h_alt'] = img.attrib['alt']
                if 'img-content' in k:
                    u['h_img_content'] = img.attrib['img-content']
                if 'img-format' in k:
                    u['h_img_format'] = img.attrib['img-format']
                if 'orientation' in k:
                    u['h_orientation'] = img.attrib['orientation']
                if 'inline' in k:
                    u['h_inline'] = img.attrib['inline']
            o.append(u)
        return o



    def getClaims(self, r):
        o = []
        for claim in r.findall('claims/claim'):
            id, num, type = '','',''
            k = claim.keys()
            if 'id' in k:
                id = claim.attrib['id']
            if 'num' in k:
                num = claim.attrib['num']
            if 'claim-type ' in k:
                type = claim.attrib['claim-type ']
            for claim_text in claim.findall('claim-text'):
                u = {}
                u['app_num'] = self.app_num
                u['id'] = id
                u['num'] =num
                u['type'] =type
                u['raw'] = self.getNode(claim_text)
                o.append(u)
        return o


    # bib stuff

    # IPCR
    def getIPCR(self,b):
        output = []

        for c in b.findall('classifications-ipcr/classification-ipcr'):
            o = dict()
            k = c.keys()
            o['app_num'] =self.app_num
            if 'id' in k:
                o['h_id'] = c.attrib['id']
            if 'sequence' in k:
                o['h_sequence'] = c.attrib['sequence']

            o['ipc_version_date'] =self.getXMLPathData(c,'ipc-version-indicator/date')
            o['classification_level'] =self.getXMLPathData(c,'classification-level')
            o['section'] =self.getXMLPathData(c,'section')
            o['class'] =self.getXMLPathData(c,'class')
            cc = c.find('class')
            if 'class-type' in cc.keys():
                o['class_type'] = cc['class-type']
            o['subclass'] =self.getXMLPathData(c,'subclass')
            o['main_group'] =self.getXMLPathData(c,'main-group')
            o['subgroup'] =self.getXMLPathData(c,'subgroup')
            o['symbol_position'] =self.getXMLPathData(c,'symbol-position')
            o['action_date'] =self.getXMLPathData(c,'action-date/date')
            o['classification_value'] =self.getXMLPathData(c,'classification-value')
            o['generating_office_coutnry'] =self.getXMLPathData(c,'generating-office/country')

            o['classification_status'] =self.getXMLPathData(c,'classification-status')
            o['classification_data_source'] =self.getXMLPathData(c,'classification-data-source')

            output.append(o)
        return output



# CPC
    def getCPC(self,b):
        output = []

        for c in b.findall('classifications-cpc/main-cpc/classification-cpc'):

            o = dict()
            o['app_num'] =self.app_num
            k = c.keys()
            if 'id' in k:
                o['h_id'] = c.attrib['id']
            if 'sequence' in k:
                o['h_sequence'] = c.attrib['sequence']


            o['type'] = 'main-cpc'
            o['cpc_version_date'] =self.getXMLPathData(c,'cpc-version-indicator/date')
            o['section'] =self.getXMLPathData(c,'section')
            o['class'] =self.getXMLPathData(c,'class')
            cc = c.find('class')
            if 'class-type' in cc.keys():
                o['class_type'] = cc['class-type']
            o['subclass'] =self.getXMLPathData(c,'subclass')
            o['main_group'] =self.getXMLPathData(c,'main-group')
            o['subgroup'] =self.getXMLPathData(c,'subgroup')
            o['symbol_position'] =self.getXMLPathData(c,'symbol-position')
            o['action_date'] =self.getXMLPathData(c,'action-date/date')
            o['classification_value'] =self.getXMLPathData(c,'classification-value')
            o['generating_office_coutnry'] =self.getXMLPathData(c,'generating-office/country')
            o['classification_status'] =self.getXMLPathData(c,'classification-status')
            o['classification_data_source'] =self.getXMLPathData(c,'classification-data-source')
            o['scheme_origination_code'] = self.getXMLPathData(c,'scheme-origination-code')
            output.append(o)
        for c in b.findall('classifications-cpc/further-cpc/classification-cpc'):
            o = dict()
            o['app_num'] =self.app_num
            k = c.keys()
            if 'id' in k:
                o['h_id'] = c.attrib['id']
            if 'sequence' in k:
                o['h_sequence'] = c.attrib['sequence']
            o['type'] = 'further-cpc'
            o['cpc_version_date'] =self.getXMLPathData(c,'cpc-version-indicator/date')
            o['section'] =self.getXMLPathData(c,'section')
            o['class'] =self.getXMLPathData(c,'class')
            cc = c.find('class')
            if 'class-type' in cc.keys():
                o['class_type'] = cc['class-type']
            o['subclass'] =self.getXMLPathData(c,'subclass')
            o['main_group'] =self.getXMLPathData(c,'main-group')
            o['subgroup'] =self.getXMLPathData(c,'subgroup')
            o['symbol_position'] =self.getXMLPathData(c,'symbol-position')
            o['action_date'] =self.getXMLPathData(c,'action-date/date')
            o['classification_value'] =self.getXMLPathData(c,'classification-value')
            o['generating_office_coutnry'] =self.getXMLPathData(c,'generating-office/country')
            o['classification_status'] =self.getXMLPathData(c,'classification-status')
            o['classification_data_source'] =self.getXMLPathData(c,'classification-data-source')
            o['scheme_origination_code'] = self.getXMLPathData(c,'scheme-origination-code')
            output.append(o)
        for c in b.findall('classifications-cpc/further-cpc/combination-set'):
            o = dict()
            o['app_num'] =self.app_num
            k = c.keys()
            if 'id' in k:
                o['h_id'] = c.attrib['id']
            if 'sequence' in k:
                o['h_sequence'] = c.attrib['sequence']
            o['type'] = 'combination-set'
            o['combination_group_number'] = self.getXMLPathData(c,'group-number')
            for sc in c.findall('combination-rank'):
                sub =dict()
                sub['combination_rank_number'] = self.getXMLPathData(sc,'rank_number')

                sub['cpc_version_date'] =self.getXMLPathData(sc,'classification-cpc/cpc-version-indicator/date')
                sub['section'] =self.getXMLPathData(sc,'classification-cpc/section')
                sub['class'] =self.getXMLPathData(sc,'classification-cpc/class')
                cc = c.find('class')
                if 'class-type' in cc.keys():
                    o['class_type'] = cc['class-type']
                sub['subclass'] =self.getXMLPathData(sc,'classification-cpc/subclass')
                sub['main_group'] =self.getXMLPathData(sc,'classification-cpc/main-group')
                sub['subgroup'] =self.getXMLPathData(sc,'classification-cpc/subgroup')
                sub['symbol_position'] =self.getXMLPathData(sc,'classification-cpc/symbol-position')
                sub['action_date'] =self.getXMLPathData(sc,'classification-cpc/action-date/date')
                sub['classification_value'] =self.getXMLPathData(sc,'classification-cpc/classification-value')
                sub['generating_office_coutnry'] =self.getXMLPathData(sc,'classification-cpc/generating-office/country')
                sub['classification_status'] =self.getXMLPathData(sc,'classification-cpc/classification-status')
                sub['classification_data_source'] =self.getXMLPathData(sc,'classification-cpc/classification-data-source')
                sub['scheme_origination_code'] = self.getXMLPathData(sc,'classification-cpc/scheme-origination-code')
                output.append(dict(o.items() + sub.items()))
        return output


# locarno
    def getLocarno(self, bib):
        output = []
        for i in bib.findall('classification-locarno'):
            o = dict()

            o['edition'] = self.getXMLPathData(i, 'edition')
            o['locarno'] = self.getXMLPathData(i, 'main-classification')
            o['text'] = self.getXMLPathData(i, 'text')
            o['type'] = 'main'
            o['app_num'] =self.app_num
            output.append(o)
            edition = o['edition']

            for i in bib.findall('classification-locarno/further-classification'):

                subdict = dict()
                subdict['type'] ='further'
                subdict['edition'] = edition
                subdict['app_num'] = self.app_num
                k = i.keys()
                if 'id' in k:
                    subdict['h_id'] = i.attrib['id']
                if 'sequence' in k:
                    subdict['h_sequence'] = i.attrib['sequence']

                subdict['locarno'] = self.getNode(i)

                output.append(subdict)
        return output


# national
    def getNational(self, bib):
        output = []
        edition = ''
        additional_info = ''
        country = ''
        for i in bib.findall('classification-national'):
            o = dict()
            o['edition'] = self.getXMLPathData(i, 'edition')
            o['national'] = self.getXMLPathData(i, 'main-classification')
            o['country'] = self.getXMLPathData(i, 'couintry')
            o['text'] = self.getXMLPathData(i, 'text')
            o['type'] = 'main'
            edition = o['edition']
            country = o['country']
            o['app_num'] =self.app_num
            o['additional_info'] = self.getXMLPathData(i, 'additional-info')  # many to one here might nee to check
            output.append(o)
        for i in bib.findall('classification-national/further-classification'):
            subdict = dict()
            subdict['type'] ='further'
            subdict['edition'] = edition
            subdict['country'] = country
            subdict['app_num'] = self.app_num

            k = i.keys()
            if 'id' in k:
                subdict['h_id'] = i.attrib['id']
            if 'sequence' in k:
                subdict['h_sequence'] = i.attrib['sequence']
            #
            # WARN add clearn function here
            #
            subdict['national'] = self.getNode(i)
            #
            #
            output.append(subdict)
        return output



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
                    rel['app_num'] = self.app_num
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
                    rel['parent_international_filing_date'] = self.getXMLPathData(c, 'relation/parent-doc/international-filing-date/date')
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
                    rel['child_international_filing_date'] = self.getXMLPathData(c, 'relation/child-doc/international-filing-date/date')

                    output.append(rel)
                elif tag in ['us-divisional-reissue']:

                    subdict = dict()
                    subdict['type'] = tag
                    subdict['sub_xml_type'] = 'us-relation'
                    subdict['app_num'] = self.app_num
                    subdict['parent_country'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/country')
                    subdict['parent_doc_number'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/doc-number')
                    subdict['parent_kind'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/kind')
                    subdict['parent_name'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/name')
                    subdict['parent_date'] = self.getXMLPathData(c, 'us-relation/parent-doc/document-id/date')
                    subdict['parent_status'] = self.getXMLPathData(c, 'us-relation/parent-doc/parent-status')
                    subdict['parent_international_filing_date'] = self.getXMLPathData(c, 'us-relation/parent-doc/international-filing-date/date')
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
                            o['child_international_filing_date'] = self.getXMLPathData(c, 'international-filing-date/date')
                            output.append(dict(subdict.items() +o.items()) )
                    else:
                        output.append(subdict)
                elif tag in ['us-provisional-application']:
                    prov = dict()
                    prov['type'] = tag
                    prov['sub_xml_type'] = 'us-provisional-application'
                    prov['app_num'] = self.app_num
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
                    cor['app_num'] = self.app_num
                    cor['parent_country'] = self.getXMLPathData(c, 'document-corrected/document-id/country')
                    cor['parent_doc_number'] = self.getXMLPathData(c, 'document-corrected/document-id/doc-number')
                    cor['parent_kind'] = self.getXMLPathData(c, 'document-corrected/document-id/kind')
                    cor['parent_name'] = self.getXMLPathData(c, 'document-corrected/document-id/name')
                    cor['parent_date'] = self.getXMLPathData(c, 'document-corrected/document-id/date')
                    rel['parent_international_filing_date'] = self.getXMLPathData(c, 'relation/parent-doc/international-filing-date/date')
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
                        relpub['app_num'] = self.app_num
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
#  party table
#
#
#
    def getPeople(self,apps,type):
        output = []
        for person in apps:
            persond =dict()
            if 'sequence' in person.keys():
                persond['sequence'] = person.attrib['sequence']
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
            persond['residence'] = self.getXMLPathData(person, 'residence/country')
            if len(person.findall('addressbook')) ==0:
                adddict = dict()
                adddict['app_num'] = self.app_num
                adddict['party_type'] = "special_assignee"
                output.append(dict(persond.items() +adddict.items()+self.parsePerson(person).items() ))

            for subitems in person.findall('addressbook'):
                adddict = dict()
                adddict['app_num'] = self.app_num
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
        o['suffix'] = self.getXMLPathData(lelements,'suffix')
        o['iid'] = self.getXMLPathData(lelements,'iid')
        o['role'] = self.getXMLPathData(lelements,'role')
        o['department'] = self.getXMLPathData(lelements,'department')
        o['synonym'] = self.getXMLPathData(lelements,'synonym')
        o['registered_number'] = self.getXMLPathData(lelements,'registered-number')

        return o

    def parseAddress(self, aelement):
        o = dict()
        o['address_1'] = self.getXMLPathData(aelement, 'address/address-1')
        o['address_2'] = self.getXMLPathData(aelement, 'address/address-2')
        o['address_3'] = self.getXMLPathData(aelement, 'address/address-3')
        o['country'] = self.getXMLPathData(aelement, 'address/country')
        o['city'] = self.getXMLPathData(aelement, 'address/city')
        o['state'] = self.getXMLPathData(aelement, 'address/state')
        o['county'] = self.getXMLPathData(aelement, 'address/county')
        o['street'] = self.getXMLPathData(aelement, 'address/street')
        o['mailcode'] = self.getXMLPathData(aelement, 'address/mailcode')
        o['pobox'] = self.getXMLPathData(aelement, 'address/pobox')
        o['room'] = self.getXMLPathData(aelement, 'address/room')
        o['address-floor'] = self.getXMLPathData(aelement, 'address/address-floor')
        o['building'] = self.getXMLPathData(aelement, 'address/building')
        o['postcode'] = self.getXMLPathData(aelement, 'address/postcode')
        o['atext'] = self.getXMLPathData(aelement, 'address/text')
        return o

    def getParties(self,bib):
        output = list()
        us_applicants = bib.findall('us-parties/us-applicants/us-applicant')
        agents = bib.findall('us-parties/agents/agent')
        inventors = bib.findall('us-parties/inventors/inventor')
        dead_inventors = bib.findall('us-parties/inventors/deceased-inventor')
        assignees = bib.findall('assignees/assignee')
        #add dead inventors
        for d in dead_inventors:
            o = dict()
            o['app_num'] = self.app_num
            o['party_type'] = 'deceased-inventor'
            o['deceased_inventor_raw'] = util.clean(util.traverse(d))


            output.append(dict(o.items() + self.parsePerson(d).items() ))

        dead_inventors_old = bib.findall('us-deceased-inventor')
        output += self.getPeople(us_applicants,'us-applicants')
        output += self.getPeople(agents,'agent')
        output += self.getPeople(inventors,'inventor')
        output += self.getPeople(dead_inventors_old,'deceased-inventor')
        output += self.getPeople(assignees, 'assignee')
        # sometimes assignees don't have addressbooks, they just have a name_group



        return output






    def updateHeaders(self, r):

        self.us_claim_statement = self.getXMLPathData(r, 'us-claim-statement')
        k = r.keys()

        if 'lang' in k:
            self.headerdata['h_lang'] = r.attrib['lang']
        if 'dtd-version' in k:
            self.headerdata['h_dtd_version'] = r.attrib['dtd-version']
        if 'file' in k:
            self.headerdata['h_file'] = r.attrib['file']
        if 'status' in k:
            self.headerdata['h_status'] = r.attrib['status']
        if 'id' in k:
            self.headerdata['h_id'] = r.attrib['id']
        if 'country' in k:
            self.headerdata['h_country'] = r.attrib['country']
        if 'file-reference-id' in k:
            self.headerdata['h_file_reference_id'] = r.attrib['file-reference-id']
        if 'date-produced' in k:
            self.headerdata['h_date_produced'] = r.attrib['date-produced']
        if 'date-publ' in k:
            self.headerdata['h_date_publ'] = r.attrib['date-publ']

        #get sequence list info now

        seq_p = r.find('us-sequence-list-doc/p')
        seq_list = r.find('us-sequence-list-doc/sequence-list')
        self.headerdata['seq_list_p'] = self.getXMLPathData(r, 'us-sequence-list-doc/p')
        if seq_p != None:
            k = seq_p.keys()
            if 'id' in k:
                self.headerdata['seq_list_p_id'] = seq_p.attrib['id']
            if 'num' in k:
                self.headerdata['seq_list_p_num'] = seq_p.attrib['num']
        if seq_list != None:
            k = seq_list.keys()
            if 'carriers' in k:
                self.headerdata['seq_list_p_carriers'] = seq_list.attrib['carriers']
            if 'file' in k:
                self.headerdata['seq_list_p_file'] = seq_list.attrib['file']
            if 'seq-file-type' in k:
                self.headerdata['seq_list_p_file_type'] = seq_list.attrib['seq-file-type']

    def parse(self, data):

        root = ET.fromstring(data)
        #root = ET.fromstring(data)

        writedata = dict()
        self.app_num = None
        self.us_claim_statement =  None
        #setup global headers
        self.updateHeaders(root)

        bib = root.find('us-bibliographic-data-application')
        if bib == None:
            print data
        # bib info
        writedata['application'] = self.getApplication(bib)


        # all the pre bib info

        writedata['abstract'] = self.getAbstracts(root)
        writedata['drawing']  = self.getDrawings(root)
        writedata['description']  = self.getDescriptions(root)
        writedata['us_chemistry']  = self.getChemistry(root)
        writedata['us_math']  = self.getMath(root)
        writedata['claims']  = self.getClaims(root)

        # all bib info
        writedata['application_ipcr'] = self.getIPCR(bib)
        writedata['application_cpc']  = self.getCPC(bib)
        writedata['application_locarno']  = self.getLocarno(bib)
        writedata['application_national']  = self.getNational(bib)
        writedata['rel_documents']  = self.getRelatedDocuments(bib)
        writedata['parties']  = self.getParties(bib)



        for key in writedata.keys():
            for subitem in writedata[key]:
                self.writeData(key, subitem)



if __name__ == '__main__':
    f = codecs.open('/Users/matthewharrison/PatentDisplayBuild/unzip_tmp/ipa150129.xml','r', encoding='UTF' )
    path = '/Users/matthewharrison/PycharmProjects/cuddlenuggets/PatentZephyr/PatentDisplayBuild'
    data = f.read().encode('utf-8')
    #root = ET.fromstring(data)


    p =parser(path,'aCurrent')
    p.parse(data)
