


desc = 'trade_ass'
data = {

    'trademarkassignment' : [
        #global headers
        ['version_no','string'], # version/version-no
        ['version_date','string'], # version/version-date
        ['action_key_code','string'], #action-key-code
        ['transaction_date','string'], #transaction-date
        ['data_available_code','string'], # assignment-information/data-available-code
        #iterate over assignment-information/assignment-entry

        ['reel_no','string'], # assignment/reel-no
        ['frame_no','string'], # assignment/frame-no
        ['assign_id','string'], # special reel-no + frame-no identifier
        ['last_update_date','string'], # assignment/last-update-date
        ['purge_indicator','string'], # assignment/purge-indicator
        ['date_recorded','string'], # assignment/date-recorded
        ['page_count','string'], # assignment/page-count
        ['cor_name','string'], # assignment/correspondent/person-or-organization-name
        ['cor_add1','string'], # assignment/correspondent/address-1
        ['cor_add2','string'], # assignment/correspondent/address-2
        ['cor_add3','string'], # assignment/correspondent/address-3
        ['cor_add4','string'], # assignment/correspondent/address-4

        ['conveyance_text','string'] # assignment/conveyance-text

    ],


    'trademarkassignment_assignors' : [


        #iterate over assignors/assignor
        ['assign_id','string'], # special reel-no + frame-no identifier
        ['assignor_id','string'], # assign_id + aid + R
        ['name','string'], #person-or-organization-name
        ['formerly_statement','string'], #  formerly-statement
        ['dba_aka_ta_statement','string'], #dba-aka-ta-statement
        ['address_1','string'], # address-1
        ['address_2','string'], # address-2
        ['city','string'], # city
        ['state','string'], # state
        ['country_name','string'], # country-name
        ['postcode','string'], # postcode
        ['execution_date','string'], # execution-date
        ['date_acknowledged','string'], # date-acknowledged
        ['legal_entity_text','string'], # legal-entity-text
        ['nationality','string'] # nationality
    ],



     'trademarkassignment_assignor_composed_of' : [


        #iterate over composed-of-statement/sub-party
        ['assign_id','string'], # special reel-no + frame-no identifier
        ['assignor_id','string'], # assign_id + aid + R
        ['name','string'], #name
        ['entity','string'], #entity
        ['stctry','string'], #stctry
        ['composed_of','string'] #composed-of
    ],


     'trademarkassignment_assignees' : [


        #iterate over assignees/assignee
        ['assign_id','string'], # special reel-no + frame-no identifier
        ['assignor_id','string'], # assign_id + aid + E
        ['name','string'], #person-or-organization-name
        ['dba_aka_ta_statement','string'], #dba-aka-ta-statement
        ['formerly_statement','string'], #formerly-statement
        ['address_1','string'], #address-1
        ['address_2','string'], #address-2
        ['city','string'], #city
        ['state','string'], #state
        ['country_name','string'], #country-name
        ['postcode','string'], #postcode
        ['legal_entity_text','string'], #legal-entity-text
        ['nationality','string'] #nationality

    ],


     'trademarkassignment_assignee_composed_of' : [


        #iterate over composed-of-statement/sub-party
        ['assign_id','string'], # special reel-no + frame-no identifier
        ['assignor_id','string'], # assign_id + aid + E
        ['name','string'], #name
        ['entity','string'], #entity
        ['stctry','string'], #stctry
        ['composed_of','string'] #composed-of
    ],


        'trademarkassignment_properties' : [


        #iterate over properties/property
        ['assign_id','string'], # special reel-no + frame-no identifier
        ['serial_no','string'], # serial-no
        ['registration_no','string'], # registration-no
        ['law_treaty_tlt_mark_name','string'], # trademark-law-treaty-property/tlt-mark-name
        ['law_treaty_tlt_mark_description','string'], # trademark-law-treaty-property/tlt-mark-description
        ['intl_reg_no','string'], # intl-reg-no
    ],

}