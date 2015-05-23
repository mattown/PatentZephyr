#
#  Current Trade mark templates
#

# structure

# this is the prefix for the db functions
desc = 'tapp'
#
data = {

    # Array format
    #Index 0:
    # table name = key
    # Index 1:
    # data is list with the format
    # Index 2:
    # field_name, type, flags*, function*

    # *flags
    #    pk = primary key
    #    i = index
    #    u = unique
    #    s = searchable
    #    m = nao

    # Index 3:
    # *functions

    #    functions to apply during postgres
    #       injestion phase
    #
    #


    # Index 4:

    #   Map_name



    'trademark' : [
        #global header fields
        ['version_no', 'string','',''],  #version/version-no
        ['version_date', 'date','',"to_date(%s,'YYYYMMDD')"], #version/version-date
        ['creation_datetime', 'datetime','',"to_date(%s,'YYYYMMDD')"], #creation-datetime
        ['data_available_code', 'string','',''], #application-information/data-available-code
        ['file_segments', 'string','',''], #application-information/file-segments/file-segment* (concatentated)
        ['action_keys', 'string','mi',''], #application-information/file-segments/action-keys/action-key* (concatentated)
        # case-file (application data) iterated over case-files
        ['serial_number', 'string','is',''], #serial-number
        ['registration_number', 'string','is',''], #registration-number
        ['transaction_date', 'string','is',''], #transaction-date

        ['tradenum', 'string','i',''],  #tradenum  serial-number + registation-number + transaction-date


        #case header file #case-file-header/ (below)
        ['filing_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/filing-date
        ['registration_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/registration-date
        ['status_code', 'string','sm',''], 	#case-file-header/status-code
        ['status_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/status-date
        ['mark_identification', 'string','s',''], 	#case-file-header/mark-identification
        ['mark_drawing_code', 'string','sm',''], 	#case-file-header/mark-drawing-code   map
        ['mark_drawing_code_is_old', 'string','',''],
        ['mark_drawing_code_position_1', 'string','sm',''],
        ['mark_drawing_code_position_2', 'string','sm',''],
        ['mark_drawing_code_position_3', 'string','sm',''],
        ['published_for_opposition_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/published-for-opposition-date
        ['amend_to_register_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/amend-to-register-date
        ['abandonment_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/abandonment-date
        ['cancellation_code', 'string','sm',''], 	#case-file-header/cancellation-code   map
        ['cancellation_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/cancellation-date
        ['republished_12c_date', 'date','s',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/republished-12c-date
        ['domestic_representative_name', 'string','s',''], 	#case-file-header/domestic-representative-name
        ['attorney_docket_number', 'string','s',''], 	#case-file-header/attorney-docket-number
        ['attorney_name', 'string','s',''], 	#case-file-header/attorney-name
        ['principal_register_amended_in', 'string','',''], 	#case-file-header/principal-register-amended-in
        ['supplemental_register_amended_in', 'string','',''], 	#case-file-header/supplemental-register-amended-in
        ['trademark_in', 'string','',''], 	#case-file-header/trademark-in
        ['collective_trademark_in', 'string','',''], 	#case-file-header/collective-trademark-in
        ['service_mark_in', 'string','',''], 	#case-file-header/service-mark-in
        ['collective_service_mark_in', 'string','',''], 	#case-file-header/collective-service-mark-in
        ['collective_membership_mark_in', 'string','',''], 	#case-file-header/collective-membership-mark-in
        ['certification_mark_in', 'string','',''], 	#case-file-header/certification-mark-in
        ['cancellation_pending_in', 'string','',''], 	#case-file-header/cancellation-pending-in
        ['published_concurrent_in', 'string','',''], 	#case-file-header/published-concurrent-in
        ['concurrent_use_in', 'string','',''], 	#case-file-header/concurrent-use-in
        ['concurrent_use_proceeding_in', 'string','',''], 	#case-file-header/concurrent-use-proceeding-in
        ['interference_pending_in', 'string','',''], 	#case-file-header/interference-pending-in
        ['opposition_pending_in', 'string','',''], 	#case-file-header/opposition-pending-in
        ['section_12c_in', 'string','',''], 	#case-file-header/section-12c-in
        ['section_2f_in', 'string','',''], 	#case-file-header/section-2f-in
        ['section_2f_in_part_in', 'string','',''], 	#case-file-header/section-2f-in-part-in
        ['renewal_filed_in', 'string','',''], 	#case-file-header/renewal-filed-in
        ['section_8_filed_in', 'string','',''], 	#case-file-header/section-8-filed-in
        ['section_8_partial_accept_in', 'string','',''], 	#case-file-header/section-8-partial-accept-in
        ['section_8_accepted_in', 'string','',''], 	#case-file-header/section-8-accepted-in
        ['section_15_acknowledged_in', 'string','',''], 	#case-file-header/section-15-acknowledged-in
        ['section_15_filed_in', 'string','',''], 	#case-file-header/section-15-filed-in
        ['supplemental_register_in', 'string','',''], 	#case-file-header/supplemental-register-in
        ['foreign_priority_in', 'string','',''], 	#case-file-header/foreign-priority-in
        ['change_registration_in', 'string','',''], 	#case-file-header/change-registration-in
        ['intent_to_use_in', 'string','',''], 	#case-file-header/intent-to-use-in
        ['intent_to_use_current_in', 'string','',''], 	#case-file-header/intent-to-use-current-in
        ['filed_as_use_application_in', 'string','',''], 	#case-file-header/filed-as-use-application-in
        ['amended_to_use_application_in', 'string','',''], 	#case-file-header/amended-to-use-application-in
        ['use_application_currently_in', 'string','',''], 	#case-file-header/use-application-currently-in
        ['amended_to_itu_application_in', 'string','',''], 	#case-file-header/amended-to-itu-application-in
        ['filing_basis_filed_as_44d_in', 'string','',''], 	#case-file-header/filing-basis-filed-as-44d-in
        ['amended_to_44d_application_in', 'string','',''], 	#case-file-header/amended-to-44d-application-in
        ['filing_basis_current_44d_in', 'string','',''], 	#case-file-header/filing-basis-current-44d-in
        ['filing_basis_filed_as_44e_in', 'string','',''], 	#case-file-header/filing-basis-filed-as-44e-in
        ['amended_to_44e_application_in', 'string','',''], 	#case-file-header/amended-to-44e-application-in
        ['filing_basis_current_44e_in', 'string','',''], 	#case-file-header/filing-basis-current-44e-in
        ['without_basis_currently_in', 'string','',''], 	#case-file-header/without-basis-currently-in
        ['filing_current_no_basis_in', 'string','',''], 	#case-file-header/filing-current-no-basis-in
        ['color_drawing_filed_in', 'string','',''], 	#case-file-header/color-drawing-filed-in
        ['color_drawing_current_in', 'string','',''], 	#case-file-header/color-drawing-current-in
        ['drawing_3d_filed_in', 'string','',''], 	#case-file-header/drawing-3d-filed-in
        ['drawing_3d_current_in', 'string','',''], 	#case-file-header/drawing-3d-current-in
        ['standard_characters_claimed_in', 'string','',''], 	#case-file-header/standard-characters-claimed-in
        ['filing_basis_filed_as_66a_in', 'string','',''], 	#case-file-header/filing-basis-filed-as-66a-in
        ['filing_basis_current_66a_in', 'string','',''], 	#case-file-header/filing-basis-current-66a-in
        ['renewal_date', 'date','',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/renewal-date
        ['law_office_assigned_location_code', 'string','m',''], 	#case-file-header/law-office-assigned-location-code
        ['current_location', 'string','',''], 	#case-file-header/current-location
        ['location_date', 'date','',"to_date(%s,'YYYYMMDD')"], 	#case-file-header/location-date
        ['employee_name', 'string','',''],	#case-file-header/employee-name


        # correspondent #correspondent
        ['corr_add_1', 'string','',''],  ##correspondent/address-1
        ['corr_add_2', 'string','',''], #correspondent/address-2
        ['corr_add_3', 'string','',''], #correspondent/address-3
        ['corr_add_4', 'string','',''], #correspondent/address-4
        ['corr_add_6', 'string','',''], #correspondent/address-5




        # international registration  Missing????

        #international-registration
        ['international_registration_number', 'string','s',''], #international-registration/international-registration-number
        ['international_registration_date', 'date','s',"to_date(%s,'YYYYMMDD')"], #international-registration/international-registration-date
        ['international_publication_date', 'date','s',"to_date(%s,'YYYYMMDD')"], #international-registration/international-publication-date
        ['international_renewal_date', 'date','s',"to_date(%s,'YYYYMMDD')"], #international-registration/international-renewal-date
        ['auto_protection_date', 'date','s',"to_date(%s,'YYYYMMDD')"], #international-registration/auto-protection-date
        ['international_death_date', 'date','s',"to_date(%s,'YYYYMMDD')"], #international-registration/international-death-date
        ['international_status_code', 'string','s',''], #international-registration/international-status-code
        ['international_status_date', 'string','s',"to_date(%s,'YYYYMMDD')"], #international-registration/international-status-date
        ['priority_claimed_in', 'string','',''], #international-registration/priority-claimed-in
        ['priority_claimed_date', 'date','s',"to_date(%s,'YYYYMMDD')"], #international-registration/priority-claimed-date
        ['first_refusal_in', 'string','',''] #international-registration/first-refusal-in

    ],


    # case file statements   EMTPY?????

    # iterated over
    #case-file-statements/case-file-statement*
    'case_file_statements' : [
        ['tradenum', 'string','i',''],
        ['type_code_raw', 'string','m',''],  #case-file-statements/case-file-statement/type-code
        ['type_code', 'string','m',''],  #case-file-statements/case-file-statement/type-code
        ['prime_class', 'string','',''],
        ['af_code', 'string','m',''],
        ['gs_code', 'string','m',''],
        ['tr_code', 'string','m',''],
        ['sequential_number', 'string','',''],
        ['year_of_entry', 'string','',''],
        ['month_of_entry', 'string','',''],
        ['text', 'string','',''] #case-file-statements/case-file-statement/text

    ],

    # case file events statements   EMPTY??????

    # iterated over
    #case-file-event-statements/case-file-event-statement*
    'case_file_event_statement' : [
        ['tradenum', 'string','i',''],
        ['code', 'string','m',''],  #case-file-event-statements/case-file-event-statement/code
        ['type', 'string','',''],  #case-file-event-statements/case-file-event-statement/type
        ['description_text', 'string','',''],  #case-file-event-statements/case-file-event-statement/description-text
        ['date', 'date','',"to_date(%s,'YYYYMMDD')"],  #case-file-event-statements/case-file-event-statement/date
        ['number', 'string','',''],  #case-file-event-statements/case-file-event-statement/number

   ],

    # prior registration applications


    # iterated over
    #prior-registration-applications/prior-registration-application
    'prior_registration_applications' : [
        ['tradenum', 'string','i',''],
        ['other_related_in', 'string','',''],  #prior-registration-applications/other-related-in *check once
        ['relationship_type', 'string','m',''],  #prior-registration-applications/prior-registration-application/relationship-type
        ['number', 'string','','']  #prior-registration-applications/prior-registration-application/number

   ],

    # foreign applications

    # iterated over
    #foreign-applications/foreign-application
    'foreign_applications' : [
        ['tradenum', 'string','i',''],
        ['filing_date','date','',"to_date(%s,'YYYYMMDD')"], #/filing-date
        ['registration_date','date','',"to_date(%s,'YYYYMMDD')"], #/registration-date
        ['registration_expiration_date','date','',"to_date(%s,'YYYYMMDD')"], #/registration-expiration-date
        ['registration_renewal_date','date','',"to_date(%s,'YYYYMMDD')"], #/registration-renewal-date
        ['registration_renewal_expiration_date','date','',"to_date(%s,'YYYYMMDD')"], #/registration-renewal-expiration-date
        ['entry_number','string','',''], #/entry-number
        ['application_number','string','',''], #/application-number
        ['country','string','',''], #/country
        ['other','string','',''], #/other
        ['registration_number','string','',''], #/registration-number
        ['renewal_number','string','',''], #/renewal-number
        ['foreign_priority_claim_in','string','',''] #/foreign-priority-claim-in
    ],


    #classifications

    # iterated over
    #classifications/classification*
    'classifications' : [
        ['tradenum', 'string','i',''],
        ['international_code_total_no', 'string','',''], #/international-code-total-no
        ['us_code_total_no', 'string','',''], #/us-code-total-no
        ['international_code_concat', 'string','',''], #/international-code*
        ['us_code_concat', 'string','',''], #/us-code*
        ['status_code', 'string','',''], #/status-code
        ['status_date', 'date','',"to_date(%s,'YYYYMMDD')"], #/status-date
        ['first_use_anywhere_date', 'string','',''], #/first-use-anywhere-date
        ['first_use_in_commerce_date', 'string','',''], #/first-use-in-commerce-date
        ['primary_code', 'string','',''] #/primary-code

        ],

    # case file owner

    # iterated over
    #case-file-owners/case-file-owner*
    'case_file_owners' : [
        ['tradenum', 'string','i',''],
        ['entry_number', 'string','',''], #/entry-number
        ['party_type', 'string','m',''], #/party-type
        ['nationality', 'string','',''], #/nationality
        ['legal_entity_type_code', 'string','m',''], #/legal-entity-type-code
        ['entity_statement', 'string','',''], #/entity-statement
        ['party_name', 'string','',''], #/party-name
        ['address_1', 'string','',''], #/address-1
        ['address_2', 'string','',''], #/address-2
        ['city', 'string','',''], #/city
        ['state', 'string','',''], #/state
        ['country', 'string','',''], #/country
        ['other', 'string','',''], #/other
        ['postcode', 'string','',''], #/postcode
        ['dba_aka_text', 'string','',''], #/dba-aka-text
        ['composed_of_statement', 'string','',''], #/composed-of-statement
        ['name_change_explanation_concat', 'string','',''], #/name-change-explanation*
        ['increment', 'int','','']  #special value that records the order of the case files, 1st
    ],

    # design search

    # iterated over
    #design-searches/design-search*
    'design_search' : [
        ['tradenum', 'string','i',''],
        ['code', 'string','m',''] #code   maping

    ],

    # madrid international filing requests

    #iterated over
    #madrid-international-filing-requests/madrid-international-filing-record
    'madrid_filing_requests' : [
        ['tradenum', 'string','i',''],
        ['entry_number', 'string','',''], #/entry-number
        ['reference_number', 'string','',''], #/reference-number
        ['original_filing_date_uspto', 'date','',"to_date(%s,'YYYYMMDD')"], #/original-filing-date-uspto
        ['international_registration_number', 'string','',''], #/international-registration-number
        ['international_registration_date', 'date','',"to_date(%s,'YYYYMMDD')"], #/international-registration-date
        ['international_status_code', 'string','m',''], #/international-status-code
        ['international_status_date', 'date','',"to_date(%s,'YYYYMMDD')"], #/international-status-date
        ['international_renewal_date', 'date','',"to_date(%s,'YYYYMMDD')"], #/international-renewal-date
        ['history_id', 'text','',''] # history id

    ],

    # madrid historical filings

    # iterate over
    # madrid-history-events/madrid-history-event

    'madrid_history_events' : [
        ['tradenum', 'string','i',''], #
        ['history_id', 'string','',''], #
        ['code','string','m',''], #code
        ['date','date','',"to_date(%s,'YYYYMMDD')"], #date
        ['description_text','string','',''], #description-text
        ['entry_number', 'string','',''] #entry-number

    ]



}

