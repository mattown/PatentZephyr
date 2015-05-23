#!/bin/sh
# simple shell script to run some Db scripts and get us our bloody maps!!
set -e


# trademark maps

# 145
psql -c "select distinct status_code from tacurrent_trademark order by status_code;" > $OUTPUT_PATH/trademark_status_code.map

# 409
psql -c "select distinct mark_drawing_code from tacurrent_trademark order by mark_drawing_code;" >  $OUTPUT_PATH/trademark_mark_drawing_code.map
# 17
psql -c "select distinct cancellation_code from tacurrent_trademark order by cancellation_code;" > $OUTPUT_PATH/trademark_cancellation_code.map
# 50
psql -c "select distinct law_office_assigned_location_code from tacurrent_trademark order by law_office_assigned_location_code;" > $OUTPUT_PATH/trademark_law_office_assigned_location_code.map
# 4
psql -c "select distinct action_keys from tacurrent_trademark order by action_keys;" > $OUTPUT_PATH/trademark_action_keys.map

# case file statements
# 468
psql -c "Select distinct type_code from tacurrent_case_file_statements order by type_code;"  > $OUTPUT_PATH/trademark_case_file_statements_type_code.map

# case file event statements
#640
psql -c "Select distinct code from tacurrent_case_file_event_statement order by code;" > $OUTPUT_PATH/trademark_case_file_event_statement_code.map
#27
psql -c "Select distinct type from tacurrent_case_file_event_statement order by type;" > $OUTPUT_PATH/trademark_case_file_event_statement_type.map



# prior registration applications
# 6
psql -c "select distinct relationship_type from tacurrent_prior_registration_applications order by relationship_type;" > $OUTPUT_PATH/trademark_prior_registration_applications_relationship_type.map

# classifications


#49
psql -c "select distinct international_code_concat from tacurrent_classifications order by international_code_concat;" > $OUTPUT_PATH/trademarks_classifications_international_code_concat.map
#64
psql -c "select distinct us_code_concat from tacurrent_classifications order by us_code_concat;" > $OUTPUT_PATH/trademarks_classifications_us_code_concat.map
#20
psql -c "select distinct status_code from tacurrent_classifications order by status_code;" > $OUTPUT_PATH/trademarks_classifications_status_code.map
#66
psql -c "select distinct primary_code from tacurrent_classifications order by primary_code;" > $OUTPUT_PATH/trademarks_classifications_primary_code.map


# case file owner

#91
psql -c "select distinct party_type from tacurrent_case_file_owners order by party_type;" > $OUTPUT_PATH/trademark_case_file_owner_party_type.map

#24
psql -c "select distinct legal_entity_type_code from tacurrent_case_file_owners order by legal_entity_type_code;" > $OUTPUT_PATH/trademark_case_file_owner_legal_entity_type_code.map



# design search (DONE)
# 1382
psql -c "select distinct code from tacurrent_design_search order by code;" > $OUTPUT_PATH/trademark_design_search_code.map


# madrid inernational filings requests
# 14
psql -c "select distinct international_status_code from tacurrent_madrid_filing_requests order by international_status_code;" > $OUTPUT_PATH/trademark_madrid_filing_requests_international_status_code.map

# madrid historical filings
# 72
psql -c "select distinct code from  tacurrent_madrid_history_events order by code;" > $OUTPUT_PATH/trademark_madrid_history_events_code.map

