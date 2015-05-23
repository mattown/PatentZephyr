
CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_foreign_applications()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_foreign_applications IN EXCLUSIVE MODE;

INSERT INTO taCurrent_foreign_applications
(
tradenum,
filing_date,
registration_date,
registration_expiration_date,
registration_renewal_date,
registration_renewal_expiration_date,
entry_number,
application_number,
country,
other,
registration_number,
renewal_number,
foreign_priority_claim_in
)
SELECT
tradenum,
to_date(filing_date,'YYYYMMDD'),
to_date(registration_date,'YYYYMMDD'),
to_date(registration_expiration_date,'YYYYMMDD'),
to_date(registration_renewal_date,'YYYYMMDD'),
to_date(registration_renewal_expiration_date,'YYYYMMDD'),
entry_number,
application_number,
country,
other,
registration_number,
renewal_number,
foreign_priority_claim_in
FROM
in_taCurrent_foreign_applications a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_foreign_applications b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_classifications()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_classifications IN EXCLUSIVE MODE;

INSERT INTO taCurrent_classifications
(
tradenum,
international_code_total_no,
us_code_total_no,
international_code_concat,
us_code_concat,
status_code,
status_date,
first_use_anywhere_date,
first_use_in_commerce_date,
primary_code
)
SELECT
tradenum,
international_code_total_no,
us_code_total_no,
international_code_concat,
us_code_concat,
status_code,
to_date(status_date,'YYYYMMDD'),
first_use_anywhere_date,
first_use_in_commerce_date,
primary_code
FROM
in_taCurrent_classifications a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_classifications b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_trademark()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_trademark IN EXCLUSIVE MODE;

INSERT INTO taCurrent_trademark
(
version_no,
version_date,
creation_datetime,
data_available_code,
file_segments,
action_keys,
serial_number,
registration_number,
transaction_date,
tradenum,
filing_date,
registration_date,
status_code,
status_date,
mark_identification,
mark_drawing_code,
mark_drawing_code_is_old,
mark_drawing_code_position_1,
mark_drawing_code_position_2,
mark_drawing_code_position_3,
published_for_opposition_date,
amend_to_register_date,
abandonment_date,
cancellation_code,
cancellation_date,
republished_12c_date,
domestic_representative_name,
attorney_docket_number,
attorney_name,
principal_register_amended_in,
supplemental_register_amended_in,
trademark_in,
collective_trademark_in,
service_mark_in,
collective_service_mark_in,
collective_membership_mark_in,
certification_mark_in,
cancellation_pending_in,
published_concurrent_in,
concurrent_use_in,
concurrent_use_proceeding_in,
interference_pending_in,
opposition_pending_in,
section_12c_in,
section_2f_in,
section_2f_in_part_in,
renewal_filed_in,
section_8_filed_in,
section_8_partial_accept_in,
section_8_accepted_in,
section_15_acknowledged_in,
section_15_filed_in,
supplemental_register_in,
foreign_priority_in,
change_registration_in,
intent_to_use_in,
intent_to_use_current_in,
filed_as_use_application_in,
amended_to_use_application_in,
use_application_currently_in,
amended_to_itu_application_in,
filing_basis_filed_as_44d_in,
amended_to_44d_application_in,
filing_basis_current_44d_in,
filing_basis_filed_as_44e_in,
amended_to_44e_application_in,
filing_basis_current_44e_in,
without_basis_currently_in,
filing_current_no_basis_in,
color_drawing_filed_in,
color_drawing_current_in,
drawing_3d_filed_in,
drawing_3d_current_in,
standard_characters_claimed_in,
filing_basis_filed_as_66a_in,
filing_basis_current_66a_in,
renewal_date,
law_office_assigned_location_code,
current_location,
location_date,
employee_name,
corr_add_1,
corr_add_2,
corr_add_3,
corr_add_4,
corr_add_6,
international_registration_number,
international_registration_date,
international_publication_date,
international_renewal_date,
auto_protection_date,
international_death_date,
international_status_code,
international_status_date,
priority_claimed_in,
priority_claimed_date,
first_refusal_in
)
SELECT
version_no,
to_date(version_date,'YYYYMMDD'),
to_date(creation_datetime,'YYYYMMDD'),
data_available_code,
file_segments,
action_keys,
serial_number,
registration_number,
transaction_date,
tradenum,
to_date(filing_date,'YYYYMMDD'),
to_date(registration_date,'YYYYMMDD'),
status_code,
to_date(status_date,'YYYYMMDD'),
mark_identification,
mark_drawing_code,
mark_drawing_code_is_old,
mark_drawing_code_position_1,
mark_drawing_code_position_2,
mark_drawing_code_position_3,
to_date(published_for_opposition_date,'YYYYMMDD'),
to_date(amend_to_register_date,'YYYYMMDD'),
to_date(abandonment_date,'YYYYMMDD'),
cancellation_code,
to_date(cancellation_date,'YYYYMMDD'),
to_date(republished_12c_date,'YYYYMMDD'),
domestic_representative_name,
attorney_docket_number,
attorney_name,
principal_register_amended_in,
supplemental_register_amended_in,
trademark_in,
collective_trademark_in,
service_mark_in,
collective_service_mark_in,
collective_membership_mark_in,
certification_mark_in,
cancellation_pending_in,
published_concurrent_in,
concurrent_use_in,
concurrent_use_proceeding_in,
interference_pending_in,
opposition_pending_in,
section_12c_in,
section_2f_in,
section_2f_in_part_in,
renewal_filed_in,
section_8_filed_in,
section_8_partial_accept_in,
section_8_accepted_in,
section_15_acknowledged_in,
section_15_filed_in,
supplemental_register_in,
foreign_priority_in,
change_registration_in,
intent_to_use_in,
intent_to_use_current_in,
filed_as_use_application_in,
amended_to_use_application_in,
use_application_currently_in,
amended_to_itu_application_in,
filing_basis_filed_as_44d_in,
amended_to_44d_application_in,
filing_basis_current_44d_in,
filing_basis_filed_as_44e_in,
amended_to_44e_application_in,
filing_basis_current_44e_in,
without_basis_currently_in,
filing_current_no_basis_in,
color_drawing_filed_in,
color_drawing_current_in,
drawing_3d_filed_in,
drawing_3d_current_in,
standard_characters_claimed_in,
filing_basis_filed_as_66a_in,
filing_basis_current_66a_in,
to_date(renewal_date,'YYYYMMDD'),
law_office_assigned_location_code,
current_location,
to_date(location_date,'YYYYMMDD'),
employee_name,
corr_add_1,
corr_add_2,
corr_add_3,
corr_add_4,
corr_add_6,
international_registration_number,
to_date(international_registration_date,'YYYYMMDD'),
to_date(international_publication_date,'YYYYMMDD'),
to_date(international_renewal_date,'YYYYMMDD'),
to_date(auto_protection_date,'YYYYMMDD'),
to_date(international_death_date,'YYYYMMDD'),
international_status_code,
to_date(international_status_date,'YYYYMMDD'),
priority_claimed_in,
to_date(priority_claimed_date,'YYYYMMDD'),
first_refusal_in
FROM
in_taCurrent_trademark a
WHERE
action_keys != 'action_keys' and
 NOT EXISTS (SELECT 1 FROM taCurrent_trademark b WHERE b.action_keys = a.action_keys) and
serial_number != 'serial_number' and
 NOT EXISTS (SELECT 1 FROM taCurrent_trademark b WHERE b.serial_number = a.serial_number) and
registration_number != 'registration_number' and
 NOT EXISTS (SELECT 1 FROM taCurrent_trademark b WHERE b.registration_number = a.registration_number) and
transaction_date != 'transaction_date' and
 NOT EXISTS (SELECT 1 FROM taCurrent_trademark b WHERE b.transaction_date = a.transaction_date) and
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_trademark b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_madrid_filing_requests()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_madrid_filing_requests IN EXCLUSIVE MODE;

INSERT INTO taCurrent_madrid_filing_requests
(
tradenum,
entry_number,
reference_number,
original_filing_date_uspto,
international_registration_number,
international_registration_date,
international_status_code,
international_status_date,
international_renewal_date,
history_id
)
SELECT
tradenum,
entry_number,
reference_number,
to_date(original_filing_date_uspto,'YYYYMMDD'),
international_registration_number,
to_date(international_registration_date,'YYYYMMDD'),
international_status_code,
to_date(international_status_date,'YYYYMMDD'),
to_date(international_renewal_date,'YYYYMMDD'),
history_id
FROM
in_taCurrent_madrid_filing_requests a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_madrid_filing_requests b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_case_file_owners()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_case_file_owners IN EXCLUSIVE MODE;

INSERT INTO taCurrent_case_file_owners
(
tradenum,
entry_number,
party_type,
nationality,
legal_entity_type_code,
entity_statement,
party_name,
address_1,
address_2,
city,
state,
country,
other,
postcode,
dba_aka_text,
composed_of_statement,
name_change_explanation_concat
)
SELECT
tradenum,
entry_number,
party_type,
nationality,
legal_entity_type_code,
entity_statement,
party_name,
address_1,
address_2,
city,
state,
country,
other,
postcode,
dba_aka_text,
composed_of_statement,
name_change_explanation_concat
FROM
in_taCurrent_case_file_owners a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_case_file_owners b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_madrid_history_events()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_madrid_history_events IN EXCLUSIVE MODE;

INSERT INTO taCurrent_madrid_history_events
(
tradenum,
history_id,
code,
date,
description_text,
entry_number
)
SELECT
tradenum,
history_id,
code,
to_date(date,'YYYYMMDD'),
description_text,
entry_number
FROM
in_taCurrent_madrid_history_events a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_madrid_history_events b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_case_file_statements()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_case_file_statements IN EXCLUSIVE MODE;

INSERT INTO taCurrent_case_file_statements
(
tradenum,
type_code_raw,
type_code,
prime_class,
af_code,
gs_code,
tr_code,
sequential_number,
year_of_entry,
month_of_entry,
text
)
SELECT
tradenum,
type_code_raw,
type_code,
prime_class,
af_code,
gs_code,
tr_code,
sequential_number,
year_of_entry,
month_of_entry,
text
FROM
in_taCurrent_case_file_statements a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_case_file_statements b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_case_file_event_statement()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_case_file_event_statement IN EXCLUSIVE MODE;

INSERT INTO taCurrent_case_file_event_statement
(
tradenum,
code,
type,
description_text,
date,
number
)
SELECT
tradenum,
code,
type,
description_text,
to_date(date,'YYYYMMDD'),
number
FROM
in_taCurrent_case_file_event_statement a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_case_file_event_statement b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_design_search()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_design_search IN EXCLUSIVE MODE;

INSERT INTO taCurrent_design_search
(
tradenum,
code
)
SELECT
tradenum,
code
FROM
in_taCurrent_design_search a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_design_search b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION upsert_tapp_taCurrent_prior_registration_applications()
 RETURNS VOID AS $$

BEGIN
LOCK TABLE taCurrent_prior_registration_applications IN EXCLUSIVE MODE;

INSERT INTO taCurrent_prior_registration_applications
(
tradenum,
other_related_in,
relationship_type,
number
)
SELECT
tradenum,
other_related_in,
relationship_type,
number
FROM
in_taCurrent_prior_registration_applications a
WHERE
tradenum != 'tradenum' and
 NOT EXISTS (SELECT 1 FROM taCurrent_prior_registration_applications b WHERE b.tradenum = a.tradenum) 
;

END;
$$ LANGUAGE plpgsql;

