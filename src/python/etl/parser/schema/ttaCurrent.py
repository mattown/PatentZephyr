
#Trial and Appeal Board

desc = 'trade_t_ab'
data = {

    'ttab' : [
        #global header fields
        ['version_no', 'string'], #version/version-no
        ['version_date', 'string'], #version/version-date
        ['action_key_code', 'string'], #action-key-code
        ['transaction_date', 'string'], #transaction-date
        ['data_available_code', 'string'], #proceeding-information/data-available-code


        # iterate over #proceeding-information/proceeding-entry
        ['number', 'string'], #number
        ['type_code', 'string'], # type-code
        ['ttab_id', 'string'], # number + type_code

        ['filing_date', 'string'], #filing-date
        ['employee_number', 'string'], #employee-number
        ['interlocutory_attorney_name', 'string'], #interlocutory-attorney-name
        ['location_code', 'string'], #location-code
        ['day_in_location', 'string'], #day-in-location
        ['charge_to_location_code', 'string'], #charge-to-location-code
        ['charge_to_employee_name', 'string'], #charge-to-employee-name
        ['status_update_date', 'string'], #status-update-date
        ['status_code', 'string'] #status-code

    ],

    # iterate over prosecution-history/prosecution-entry
    'ttab_prosecution_history' : [
        ['ttab_id', 'string'],
        ['identifier', 'string'] ,#identifier
        ['code', 'string'] ,# code
        ['type_code', 'string'] ,# type-code
        ['due_date', 'string'] ,# due-date
        ['date', 'string'] ,#  date
        ['history_text', 'string'] ,#  history-text

    ],
    # next 3 interate after each other

    # iterate over party-information/party
    'ttab_party' : [
        ['ttab_id', 'string'],
        ['party_id', 'string'], # identifer
        ['identifier', 'string'], #identifier
        ['role_code', 'string'], #role-code
        ['name', 'string'], #name
        ['orgname', 'string']#orgname

    ],
    # iterate over property-information/property
    'ttab_party_property' : [
        ['ttab_id', 'string'],
        ['party_id', 'string'], # identifer
        ['identifier', 'string'], #identifier
        ['serial_number', 'string'], #serial-number
        ['registration_number', 'string'], #registration-number
        ['mark_text', 'string']#mark-text
    ],



    #iterate over  address-information/proceeding-address
    'ttab_party_proceeding_address' : [
        ['ttab_id', 'string'],
        ['party_id', 'string'],
        ['identifier', 'string'] , #identifier
        ['type_code', 'string'] , #type-code
        ['name', 'string'] , #name
        ['orgname', 'string'] , #orgname
        ['address_1', 'string'] ,  #address-1
        ['city', 'string'] , #city
        ['state', 'string'] , #state
        ['country', 'string'] , #country
        ['postcode', 'string']  #postcode
    ]

}