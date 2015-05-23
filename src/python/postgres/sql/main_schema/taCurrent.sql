DROP TABLE IF EXISTS taCurrent_madrid_filing_requests ;
CREATE TABLE taCurrent_madrid_filing_requests (
tradenum text,
entry_number text,
reference_number text,
original_filing_date_uspto date,
international_registration_number text,
international_registration_date date,
international_status_code text,
international_status_date date,
international_renewal_date date,
history_id text
);
DROP INDEX IF EXISTS taCurrent_madrid_filing_requests_k_idx;
CREATE INDEX taCurrent_madrid_filing_requests_k_idx
ON taCurrent_madrid_filing_requests ( tradenum );
DROP TABLE IF EXISTS taCurrent_case_file_statements ;
CREATE TABLE taCurrent_case_file_statements (
tradenum text,
type_code_raw text,
type_code text,
prime_class text,
af_code text,
gs_code text,
tr_code text,
sequential_number text,
year_of_entry text,
month_of_entry text,
text text
);
DROP INDEX IF EXISTS taCurrent_case_file_statements_k_idx;
CREATE INDEX taCurrent_case_file_statements_k_idx
ON taCurrent_case_file_statements ( tradenum );
DROP TABLE IF EXISTS taCurrent_case_file_event_statement ;
CREATE TABLE taCurrent_case_file_event_statement (
tradenum text,
code text,
type text,
description_text text,
date date,
number text
);
DROP INDEX IF EXISTS taCurrent_case_file_event_statement_k_idx;
CREATE INDEX taCurrent_case_file_event_statement_k_idx
ON taCurrent_case_file_event_statement ( tradenum );
DROP TABLE IF EXISTS taCurrent_case_file_owners ;
CREATE TABLE taCurrent_case_file_owners (
tradenum text,
entry_number text,
party_type text,
nationality text,
legal_entity_type_code text,
entity_statement text,
party_name text,
address_1 text,
address_2 text,
city text,
state text,
country text,
other text,
postcode text,
dba_aka_text text,
composed_of_statement text,
name_change_explanation_concat text
);
DROP INDEX IF EXISTS taCurrent_case_file_owners_k_idx;
CREATE INDEX taCurrent_case_file_owners_k_idx
ON taCurrent_case_file_owners ( tradenum );
DROP TABLE IF EXISTS taCurrent_classifications ;
CREATE TABLE taCurrent_classifications (
tradenum text,
international_code_total_no text,
us_code_total_no text,
international_code_concat text,
us_code_concat text,
status_code text,
status_date date,
first_use_anywhere_date text,
first_use_in_commerce_date text,
primary_code text
);
DROP INDEX IF EXISTS taCurrent_classifications_k_idx;
CREATE INDEX taCurrent_classifications_k_idx
ON taCurrent_classifications ( tradenum );
DROP TABLE IF EXISTS taCurrent_design_search ;
CREATE TABLE taCurrent_design_search (
tradenum text,
code text
);
DROP INDEX IF EXISTS taCurrent_design_search_k_idx;
CREATE INDEX taCurrent_design_search_k_idx
ON taCurrent_design_search ( tradenum );
DROP TABLE IF EXISTS taCurrent_madrid_history_events ;
CREATE TABLE taCurrent_madrid_history_events (
tradenum text,
history_id text,
code text,
date date,
description_text text,
entry_number text
);
DROP INDEX IF EXISTS taCurrent_madrid_history_events_k_idx;
CREATE INDEX taCurrent_madrid_history_events_k_idx
ON taCurrent_madrid_history_events ( tradenum );
DROP TABLE IF EXISTS taCurrent_foreign_applications ;
CREATE TABLE taCurrent_foreign_applications (
tradenum text,
filing_date date,
registration_date date,
registration_expiration_date date,
registration_renewal_date date,
registration_renewal_expiration_date date,
entry_number text,
application_number text,
country text,
other text,
registration_number text,
renewal_number text,
foreign_priority_claim_in text
);
DROP INDEX IF EXISTS taCurrent_foreign_applications_k_idx;
CREATE INDEX taCurrent_foreign_applications_k_idx
ON taCurrent_foreign_applications ( tradenum );
DROP TABLE IF EXISTS taCurrent_prior_registration_applications ;
CREATE TABLE taCurrent_prior_registration_applications (
tradenum text,
other_related_in text,
relationship_type text,
number text
);
DROP INDEX IF EXISTS taCurrent_prior_registration_applications_k_idx;
CREATE INDEX taCurrent_prior_registration_applications_k_idx
ON taCurrent_prior_registration_applications ( tradenum );
DROP TABLE IF EXISTS taCurrent_trademark ;
CREATE TABLE taCurrent_trademark (
version_no text,
version_date date,
creation_datetime text,
data_available_code text,
file_segments text,
action_keys text,
serial_number text,
registration_number text,
transaction_date text,
tradenum text,
filing_date date,
registration_date date,
status_code text,
status_date date,
mark_identification text,
mark_drawing_code text,
mark_drawing_code_is_old text,
mark_drawing_code_position_1 text,
mark_drawing_code_position_2 text,
mark_drawing_code_position_3 text,
published_for_opposition_date date,
amend_to_register_date date,
abandonment_date date,
cancellation_code text,
cancellation_date date,
republished_12c_date date,
domestic_representative_name text,
attorney_docket_number text,
attorney_name text,
principal_register_amended_in text,
supplemental_register_amended_in text,
trademark_in text,
collective_trademark_in text,
service_mark_in text,
collective_service_mark_in text,
collective_membership_mark_in text,
certification_mark_in text,
cancellation_pending_in text,
published_concurrent_in text,
concurrent_use_in text,
concurrent_use_proceeding_in text,
interference_pending_in text,
opposition_pending_in text,
section_12c_in text,
section_2f_in text,
section_2f_in_part_in text,
renewal_filed_in text,
section_8_filed_in text,
section_8_partial_accept_in text,
section_8_accepted_in text,
section_15_acknowledged_in text,
section_15_filed_in text,
supplemental_register_in text,
foreign_priority_in text,
change_registration_in text,
intent_to_use_in text,
intent_to_use_current_in text,
filed_as_use_application_in text,
amended_to_use_application_in text,
use_application_currently_in text,
amended_to_itu_application_in text,
filing_basis_filed_as_44d_in text,
amended_to_44d_application_in text,
filing_basis_current_44d_in text,
filing_basis_filed_as_44e_in text,
amended_to_44e_application_in text,
filing_basis_current_44e_in text,
without_basis_currently_in text,
filing_current_no_basis_in text,
color_drawing_filed_in text,
color_drawing_current_in text,
drawing_3d_filed_in text,
drawing_3d_current_in text,
standard_characters_claimed_in text,
filing_basis_filed_as_66a_in text,
filing_basis_current_66a_in text,
renewal_date date,
law_office_assigned_location_code text,
current_location text,
location_date date,
employee_name text,
corr_add_1 text,
corr_add_2 text,
corr_add_3 text,
corr_add_4 text,
corr_add_6 text,
international_registration_number text,
international_registration_date date,
international_publication_date date,
international_renewal_date date,
auto_protection_date date,
international_death_date date,
international_status_code text,
international_status_date text,
priority_claimed_in text,
priority_claimed_date date,
first_refusal_in text
);
DROP INDEX IF EXISTS taCurrent_trademark_k_idx;
CREATE INDEX taCurrent_trademark_k_idx
ON taCurrent_trademark ( action_keys,
serial_number,
registration_number,
transaction_date,
tradenum );
