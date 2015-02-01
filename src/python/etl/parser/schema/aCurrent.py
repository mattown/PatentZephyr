


data = {

    # root/us-bibliographic-data-application
    'application' : [
        ['app_num', 'string'] ,
        # header level stuff from attribute
        ['h_lang', 'string'] , #root @lang
        ['h_dtd_version', 'string'] ,#root @dtd-version
        ['h_file', 'string'] ,#root @file
        ['h_status', 'string'] ,#root @status
        ['h_id', 'string'] ,#root @id
        ['h_country', 'string'] ,#root @country
        ['h_file_reference_id', 'string'] ,#root @file-reference-id
        ['h_date_produced', 'string'] ,#root @date-produced
        ['h_date_publ', 'string'] ,#root @date-publ
        #publication reference

        ['pub_h_id', "string"] ,#us-bibliographic-data-application/publication-reference @id
        ['pub_lang', 'string'] ,#us-bibliographic-data-application/publication-reference/document-id @lang
        ['pub_country', 'string'] ,#us-bibliographic-data-application/publication-reference/document-id/country
        ['pub_no', 'string'] ,#us-bibliographic-data-application/publication-reference/document-id/doc-number
        ['pub_kind', 'string'] ,#us-bibliographic-data-application/publication-reference/document-id/kind
        ['pub_name', 'string'] ,#us-bibliographic-data-application/publication-reference/document-id/name
        ['pub_date', 'string'] ,#us-bibliographic-data-application/publication-reference/document-id/date

        # application reference
        ['app_h_id', 'string'] ,#us-bibliographic-data-application/application-reference @id
        ['app_h_type', 'string'] ,#us-bibliographic-data-application/application-reference @appl-type
        ['app_country', 'string'] ,#us-bibliographic-data-application/application-reference/document-id/country
        ['app_no', 'string'] ,#us-bibliographic-data-application/application-reference/document-id/doc-number
        ['app_kind', 'string'] ,#us-bibliographic-data-application/application-reference/document-id/kind
        ['app_name', 'string'] ,#us-bibliographic-data-application/application-reference/document-id/name
        ['app_date', 'string'] ,#us-bibliographic-data-application/application-reference/document-id/date



        ['us_application_series_code', 'string'] ,#us-bibliographic-data-application/us-application-series-code
        ['us_publication_filing_type', 'string'] ,#us-bibliographic-data-application/us-publication-filing-type  # **super special parser here

        ['us_publication_of_continued_prosecution_application', 'string'] ,#us-bibliographic-data-application/us-publication-of-continued-prosecution-application # if existss This is a publication of a continued prosecution application (CPA) filed under 37 CFR 1.53(d).
        ['rule_47_flag', 'string'] ,#us-bibliographic-data-application/rule-47-flag

        #invention-title

        ['invention_title', 'string'] ,#invention-title
        ['invention_title_id', 'string'] ,#invention-title @id
        ['invention_title_lang', 'string'] ,#invention-title @lang

        #us-botanic
        ['us_botanic_latin_name', 'string'] ,#us-bibliographic-data-application/us-botanic/latin-name
        ['us_botanic_variety', 'string'] ,#us-bibliographic-data-application/us-botanic/variety

        # bio-deposit doesn't seemed to be used

        # pct_region_filing
        # pct-or-regional-filing-data

        ['pctrf_country', 'string'] ,#document-id/country
        ['pctrf_date', 'string'] ,#document-id/date
        ['pctrf_doc_num', 'string'] ,#document-id/doc-number
        ['pctrf_kind', 'string'] ,#document-id/kind
        ['pctrf_name', 'string'] ,#document-id/name
        ['us_371c124_date', 'string'] ,#us-371c124-date/date
        ['us_371c12_date', 'string'], #us-371c12-date/date

        #pct-or-regional-publishing-data
        ['pctrp_country', 'string'] ,#pct-or-regional-publishing-data/document-id/country
        ['pctrp_date', 'string'] ,#pct-or-regional-publishing-data/document-id/date
        ['pctrp_doc_num', 'string'] ,#pct-or-regional-publishing-data/document-id/doc-number
        ['pctrp_kind', 'string'] ,#pct-or-regional-publishing-data/document-id/kind
        ['pctrp_name', 'string'] ,#pct-or-regional-publishing-data/document-id/name
        ['pctrp_gazette_num', 'string'] ,#pct-or-regional-publishing-data/gazette-reference/gazette-num
        ['pctrp_gazette_date', 'string'], #pct-or-regional-publishing-data/gazette-reference/date
        ['pctrp_gazette_text', 'string'], #pct-or-regional-publishing-data/gazette-reference/text


        #sequence-list  get it from us-sequence-list-doc below bib info


        ['seq_list_p', 'string'] ,#p
        ['seq_list_p_id', 'string'] ,#p@id
        ['seq_list_p_num', 'string'] ,#p@num
        ['seq_list_p_carriers', 'string'] ,#sequence-list@carriers
        ['seq_list_p_file', 'string'] ,#sequence-list@file
        ['seq_list_p_file_type', 'string'] ,#sequence-list@seq-file-type


        #pct-or-regional-publishing-data
        #us-appendix-data none in schema
        ['us_claim_statement']   # get it us-claim-statement at one level below the bib parse first!



],

    #IPCR

    # iterate over #us-bibliographic-data-application/classifications-ipcr/classification-ipcr
    'application_ipcr' : [
        ['app_num', 'string'] ,
        ['h_id', 'string'] , # @ id
        ['h_sequence', 'string'] , # @ sequence
        ['ipc_version_date', 'string'] , #ipc-version-indicator/date
        ['classification_level', 'string'] , #classification-level
        ['section', 'string'] , #section
        ['class', 'string'] , #class
        ['class_type', 'string'] , #class @class-type
        ['subclass', 'string'] , #subclass
        ['main_group', 'string'] , #main-group
        ['subgroup', 'string'] , #subgroup
        ['symbol_position', 'string'] , #symbol-position
        ['classification_value', 'string'] , #classification-value
        ['action_date', 'string'] , #action-date/date
        ['generating_office_coutnry', 'string'] , #generating-office/country
        ['classification_status', 'string'] , #classification-status
        ['classification_data_ource', 'string']  #classification-data-source
],

    # CPC

    # iterate over #us-bibliographic-data-application/classifications-cpc/main-cpc/classification-cpc once
    # then iterate over #us-bibliographic-data-application/classifications-cpc/further-cpc/classification-cpc
    'application_cpc' : [
        ['app_num', 'string'] ,
        ['h_id', 'string'] , # @ id
        ['h_sequence', 'string'] , # @ sequence
        ['type', 'string'] , #if main-cpc further-cpc or combination-set
        ['cpc_version_date', 'string'] , #cpc-version-indicator/date
        ['section', 'string'] , #section
        ['class', 'string'] , #class
        ['class_type', 'string'] , #class @class-type
        ['subclass', 'string'] , #subclass
        ['main_group', 'string'] , #main-group
        ['subgroup', 'string'] , #subgroup
        ['symbol_position', 'string'] , #symbol-position
        ['classification_value', 'string'] , #classification-value
        ['action_date', 'string'] , #action-date/date
        ['generating_office_coutnry', 'string'] , #generating-office/country
        ['classification_status', 'string'] , #classification-status
        ['classification_data_source', 'string'] , #classification-data-source
        ['scheme_origination_code', 'string'] #scheme-origination-code
],


    #locarno

    #iterate over classification-locarno/main-classification once
    # then iterate over classification-locarno/further-classification
    # both data goes in "data" here, text and edition are global headers
    'application_locarno' : [
        ['app_num', 'string'] ,
        ['edition', 'string'] , #edition  this is a header
        ['type', 'string'] , #if main or furtherda
        ['h_id', 'string'] , #further-classification@id
        ['h_sequence', 'string'] , #further-classification@sequence
        ['text', 'string'] , #text
        ['locarno', 'string']  #cpc-version-indicator/date

],




    #national classification
    #iterate over classification-national/main-classification once
    # then iterate over classification-national/further-classification
    # both data goes in "data" here, text and edition are global headers

    'application_national' : [
        ['app_num', 'string'] ,
        ['edition', 'string'] , #edition  this is a header
        ['country', 'string'] , #country  this is a header
        ['type', 'string'] , #if main-cpc or further-cpc
        ['h_id', 'string'] , #further-classification@id
        ['h_sequence', 'string'] , #further-classification@sequence
        ['text', 'string'] , #text
        ['national', 'string']  #cpc-version-indicator/date

],


    # ref cited not in applications!!

    #    related documents
    #
    # iterate 'relations' or 'us-relations' or '' over addition | division | continuation | continuation-in-part | continuing-reissue | reissue | us-divisional-reissue | reexamination | us-reexamination-reissue-merger | substitution | us-provisional-application | utility-model-basis | correction | related-publication
    #

'rel_documents' : [
    ['app_num', 'string'],
    ['type', 'string'],  #
    ['sub_xml_type', 'string'],  # some are us-relation "us
    ['parent_country', 'string'],
    ['parent_doc_number', 'string'],
    ['parent_kind', 'string'],
    ['parent_name', 'string'],
    ['parent_date', 'string'],
    ['parent_status', 'string'],

    ['parent_grant_country', 'string'],
    ['parent_grant_doc_number', 'string'],
    ['parent_grant_kind', 'string'],
    ['parent_grant_name', 'string'],
    ['parent_grant_date', 'string'],

    ['parent_pct_country', 'string'],
    ['parent_pct_doc_number', 'string'],
    ['parent_pct_kind', 'string'],
    ['parent_pct_name', 'string'],
    ['parent_pct_date', 'string'],
    ['parent_international_filing_date', 'string'],   #parent-doc/international-filing-date/date

    ['child_country', 'string'],
    ['child_doc_number', 'string'],
    ['child_kind', 'string'],
    ['child_name', 'string'],
    ['child_date', 'string'],
    ['child_international_filing_date', 'string'],  # new field

    ['correction_type','string'],
    ['correction_gazette_reference_num'],
    ['correction_gazette_reference_date'],
    ['correction_gazette_reference_text'],
    ['correction_text','string'],

    ['related_publication_text', 'string']
],

    # parties

    #
    #  Us parties us-applicants, inventors, agents
    #

'parties' : [
    ['app_num', 'string'],
    ['party_type', 'string'],
    #person name_group
    ['sequence', 'int'],
    ['name', 'string'],
    ['prefix','string'],
    ['first_name', 'string'],
    ['middle_name', 'string'],
    ['last_name', 'string'],
    ['orgname', 'string'],
    ['suffix', 'string'],   #suffix
    ['iid', 'string'], #idd
    ['role', 'string'], #role
    ['department', 'string'], #department
    ['synonym', 'string'], #synonym
    ['registered_number', 'string'], #registered-number

    #address group
    ['address_1', 'string'],
    ['address_2', 'string'],
    ['address_3', 'string'],
    ['city', 'string'],
    ['country', 'string'],
    ['state', 'string'],
    ['county', 'string'],
    ['street', 'string'],
    ['mailcode', 'string'],
    ['pobox', 'string'],
    ['room', 'string'],
    ['address-floor', 'string'],
    ['building', 'string'],
    ['postcode', 'string'],
    ['atext', 'string'],

    ['phone', 'string'],
    ['fax', 'string'],
    ['email', 'string'],
    ['url', 'string'],
    ['ead', 'string'],
    ['dtext', 'string'],
    ['residence', 'string'],   # this was added
    ['us_rights', 'string'],
    ['app_type', 'string'],
    ['rep_type', 'string'],
    ['designation', 'string'],
    ['assignee_type', 'string'],
    ['applicant_authority_category', 'string'],
    ['deceased_inventor_raw', 'string']
],




    #abstract


    #
    #
    #
    'abstract' : [
    ['app_num', 'string'],
    ['h_id', 'string'], #@id
    ['adata', 'string'], #p
    ['id', 'string'], #p@id
    ['num','string'] #p@num
],



    # drawings

    #
    #    iterate over  drawings/figure
    #
    'drawing' : [
        ['app_num', 'string'],
         ['h_id', 'string'],       #@id
         ['h_he', 'string'],       #@he
         ['h_wi', 'string'],       #@wi
         ['h_file', 'string'],     #@file
         ['h_alt', 'string'],      #@alt
         ['h_img_content', 'string'],       #@img-content
         ['h_img_format', 'string'],       #@img-format
         ['h_orientation', 'string'],       #@orientation
         ['h_inline', 'string'],       #@inline
    ],


    #Descriptions


    #  either look for header or p at description/description-of-drawings/p+ or heading*
    #    or description/p+ or heading*
    #
    #
    'description' : [
    ['app_num', 'string'],
    ['is_description_of_drawing', 'string'], #
    ['is_heading', 'string'],
    ['h_id','string'],  # heading@id or p@id
    ['h_p_num', 'string'], #p@num
    ['h_header_level', 'string'], #heading@level
    ['ddata','string']

],


    # US chemistry

    'us_chemistry' : [
        ['app_num' , 'string'],   #
        ['idref' , 'string'],   #  @idref
        ['cdx_file' , 'string'],   # @cdx-file
        ['mol_file' , 'string']    #@mol-file


    ],


    # US math

       # US math

    'us_math' : [
        ['app_num' , 'string'],   #
        ['idrefs' , 'string'],   #  @idrefs
        ['cdx_file' , 'string'],   # @cdx-file
        ['nb_file' , 'string'] ,   #@nb-file
        ['h_he', 'string'],       #img@he
        ['h_wi', 'string'],       #img@wi
        ['h_file', 'string'],     #img@file
        ['h_alt', 'string'],      #img@alt
        ['h_img_content', 'string'],       #img@img-content
        ['h_img_format', 'string'],       #img@img-format
        ['h_orientation', 'string'],       #img@orientation
        ['h_inline', 'string']       #img@inline

    ],

    #claims     claims/claim*/claim-text*
    'claims' : [
    ['app_num', 'string'],
    ['id', 'string'], #claim@id
    ['num', 'string'],# claim@num
    ['type', 'string'],# claim@claim-type
    ['raw', 'string'] #claim/claim-text

],






}