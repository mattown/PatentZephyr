
CREATE OR REPLACE FUNCTION tapp()
 RETURNS VOID AS $$

BEGIN
SELECT upsert_tapp_taCurrent_madrid_filing_requests();
SELECT upsert_tapp_taCurrent_foreign_applications();
SELECT upsert_tapp_taCurrent_madrid_history_events();
SELECT upsert_tapp_taCurrent_classifications();
SELECT upsert_tapp_taCurrent_design_search();
SELECT upsert_tapp_taCurrent_case_file_owners();
SELECT upsert_tapp_taCurrent_case_file_statements();
SELECT upsert_tapp_taCurrent_case_file_event_statement();
SELECT upsert_tapp_taCurrent_trademark();
SELECT upsert_tapp_taCurrent_prior_registration_applications();
END;
$$ LANGUAGE plpgsql;

