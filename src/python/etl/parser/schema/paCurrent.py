


data = {

     'patent_assignment' : [
         # header items

         ['dtd_version', 'string'] ,  # dtd-version root level attribute
         ['date_produced', 'string'] ,  # date-produced root level attribute
         ['action_key_code', 'string'] ,  #action-key-code
         ['transaction_date', 'string'] ,  #transaction-date/date

         # iterate over patent-assignments/patent-assignment
         ['reel_no', 'string'] ,  #assignment-record/reel-no
         ['frame_no', 'string'] ,  #assignment-record/frame-no
         ['assign_id', 'string'], #unique id reel-no + frame-no

         ['last_update_date', 'string'] ,  #assignment-record/last-update-date/date
         ['purge_indicator', 'string'] ,  #assignment-record/purge-indicator
         ['recorded_date', 'string'] ,  #assignment-record/recorded-date/date
         ['page_count', 'string'] ,  #assignment-record/page-count
         ['corr_name', 'string'] ,  #assignment-record/correspondent/name
         ['corr_add1', 'string'] ,  #assignment-record/correspondent/address-1
         ['corr_add2', 'string'] ,  #assignment-record/correspondent/address-2
         ['corr_add3', 'string'] ,  #assignment-record/correspondent/address-3
         ['corr_add4', 'string'] ,  #assignment-record/correspondent/address-4
         ['conveyance_text', 'string'],   #assignment-record/conveyance-text
         ['corr_name_type','string'] # assignment-record/correspondent/name@name_type
     ],

    # iterate over patent-assignors/patent-assignor
     'patent_assignment_assignor' : [
         ['assign_id', 'string'], #unique id reel-no + frame-no
         ['name', 'string'], #name
         ['execution_date', 'string'], #execution-date/date
         ['date_acknowledged', 'string'], #date-acknowledged/date
         ['name_type','string'] #name@name_type
     ],
    # iterate over patent-assignees/patent-assignee
     'patent_assignment_assignee' : [
         ['assign_id', 'string'], #unique id reel-no + frame-no
         ['name', 'string'], #name
         ['address_1', 'string'], #address-1
         ['address_2', 'string'], #address-2
         ['city', 'string'], #city
         ['state', 'string'], #state
         ['country_name', 'string'], #country-name
         ['postcode','string'], #postcode
         ['name_type','string'] #name@name_type
     ],

    # iterate over patent-properties/patent-property
     'patent_assignment_property' : [
         ['assign_id', 'string'], #unique id reel-no + frame-no
         # header level
         ['invention_title', 'string'], #invention-title
        # iterate over document-id
         ['country', 'string'], #document-id/country
         ['doc_number', 'string'], #document-id/doc-number
         ['kind', 'string'], #document-id/kind
         ['name', 'string'], #document-id/name
         ['date', 'string'], #document-id/date
         ['name_type','string'] #name@name_type
     ]

      }