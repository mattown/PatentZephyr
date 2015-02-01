
# no assignees?
# check extra address data
# add pct-or-regional-publishing-data
# add pct-or-regional-filing-data
# add us-publication-filing-type
# add drawings
# add descriptions
# check us-sequence-list-doc
# add us-chemistry
# add us-math
# check claims
# check abstracts
# check us-sequence-list-doc


data = {
'patents' : [
    ['patnum', 'string'],
    ['lang', 'string'],
    ['dtd-version', 'string'],
    ['file', 'string'],
    ['status', 'string'],
    ['doc_id', 'string'],
    ['country', 'string'],
    ['file_reference_id', ''],
    ['date_produced', 'string'],
    ['date_published', 'string'],
    ['pub_country', 'string'],
    ['pub_doc_number', 'string'],
    ['pub_kind', 'string'],
    ['pub_name', 'string'],
    ['pub_date', 'string'],
    ['app_country', 'string'],
    ['app_doc_number', 'string'],
    ['app_kind', 'string'],
    ['app_name', 'string'],
    ['app_date', 'string'],
    ['us_sir_flag', 'string'],
    ['us_app_series_code', 'string'],
    ['us_issue_ocpa', 'string'],
    ['rule_47_flag', 'string'],
    ['invention_title', 'string'],
    ['us_claim_statement', 'string'],
    ['us_references_cited', 'string']  # add
],
'parties' : [
    ['patnum', 'string'],
    ['party_type', 'string'],
    ['sequence', 'int'],
    ['name', 'string'],
    ['prefix','string'],
    ['first_name', 'string'],
    ['middle_name', 'string'],
    ['last_name', 'string'],
    ['orgname', 'string'],
    ['address_1', 'string'],
    ['address_2', 'string'],
    ['address_3', 'string'],
    ['city', 'string'],
    ['country', 'string'],
    ['phone', 'string'],
    ['fax', 'string'],
    ['email', 'string'],
    ['url', 'string'],
    ['ead', 'string'],
    ['dtext', 'string'],
    ['residence', 'string'],
    ['us_rights', 'string'],
    ['app_type', 'string'],
    ['rep_type', 'string'],
    ['designation', 'string'],
    ['assignee_type', 'string'],
    ['applicant_authority_category', 'string'],
    ['deceased_inventor_raw', 'string']
],
'abstract' : [
    ['patnum', 'string'],
    ['adata', 'string'],
    ['id', 'string'],
    ['num','string']
],
'pri_claims' : [
    ['patnum', 'string'],
    ['country', 'string'],
    ['sequence', 'int'],
    ['document_number', 'string'],
    ['priority_date', 'string'],
    ['kind', 'string'],
    ['office_of_filing_region', 'string'],
    ['office_of_filing_country', 'string']

],
'patent_terms' : [
    ['patnum', 'string'],
    ['text', 'string'],
    ['length_of_grant', 'string'],
    ['us_term_extension', 'string'],
    ['disclaimer', 'string'],
    ['lapse_of_patent_doc_id', 'string'],
    ['lapse_of_patent_text', 'string']
],
'us_citations' : [
    ['patnum', 'string'],
    ['num', 'string'],
    ['type', 'string'],
    ['nplcit_text', 'string'],
    ['patcit_text', 'string'],
    ['country', 'string'],
    ['doc_number', 'string'],
    ['kind', 'string'],
    ['name', 'string'],
    ['date', 'string'],
    ['rel_passage', 'string'],
    ['other_cit','string']
],
'us_IPCR' : [
    ['patnum', 'string'],
    ['version', 'string'],
    ['classification_level', 'string'],
    ['section', 'string'],
    ['class', 'string'],
    ['subclass', 'string'],
    ['main_group', 'string'],
    ['subgroup', 'string'],
    ['action_date', 'string'],
    ['symbol_position', 'string'],
    ['classification_value', 'string'],
    ['generating_office', 'string'],
    ['classification_status', 'string'],
    ['classification_data_source', 'string']
],
'us_CPC' : [
    ['patnum', 'string'],
    ['type','string'],
    ['version', 'string'],
    ['sequence', 'string'],
    ['classification_level', 'string'],
    ['section', 'string'],
    ['class', 'string'],
    ['subclass', 'string'],
    ['main_group', 'string'],
    ['subgroup', 'string'],
    ['symbol_position', 'string'],
    ['action_date', 'string'],
    ['classification_value', 'string'],
    ['generating_office', 'string'],
    ['classification_status', 'string'],
    ['classification_data_source', 'string'],
    ['scheme_origination', 'string'],
    ['combination_set', 'string'],
    ['combination_group_number'],
    ['combination_rank_number']
],
'us_locarno' : [
    ['patnum', 'string'],
    ['type', 'string'],
    ['edition', 'string'],
    ['locarno', 'string'],
    ['text', 'string']
],
'us_national' : [
    ['patnum', 'string'],
    ['edition', 'string'],
    ['country', 'string'],
    ['national', 'string'],
    ['text', 'string'],
    ['is_secondary', 'string'],
    ['additional_info', 'string']
],
'rel_documents' : [
    ['patnum', 'string'],
    ['type', 'string'],
    ['sub_xml_type', 'string'],
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

    ['child_country', 'string'],
    ['child_doc_number', 'string'],
    ['child_kind', 'string'],
    ['child_name', 'string'],
    ['child_date', 'string'],

    ['correction_type','string'],
    ['correction_gazette_reference_num'],
    ['correction_gazette_reference_date'],
    ['correction_gazette_reference_text'],
    ['correction_text','string'],

    ['related_publication_text', 'string']
],
'claims' : [
    ['patnum', 'string'],
    ['num', 'string'],
    ['raw', 'string']

]



}