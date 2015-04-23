DROP TABLE IF EXISTS madrid_filing_requests ;
CREATE TABLE madrid_filing_requests (


tradenum text,
entry_number text,
reference_number text,
original_filing_date_uspto text,
international_registration_number text,
international_registration_date date,
international_status_code text,
international_status_date text,
international_renewal_date date,
history_id integer


);
