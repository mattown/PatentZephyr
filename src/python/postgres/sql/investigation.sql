SELECT
   relname as "Table",
   pg_size_pretty(pg_total_relation_size(relid)) As "Size",
   pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) as "External Size"
   FROM pg_catalog.pg_statio_user_tables ORDER BY relname, pg_total_relation_size(relid) DESC;


                    Table                     |   Size   | External Size
----------------------------------------------+----------+---------------
 in_tacurrent_case_file_event_statement       | 34 GB    | 8720 kB
 in_tacurrent_case_file_statements            | 12 GB    | 296 MB
 in_tacurrent_trademark                       | 10199 MB | 3064 kB
 in_tacurrent_case_file_owners                | 7014 MB  | 3112 kB
 in_tacurrent_classifications                 | 2860 MB  | 744 kB
 in_tacurrent_design_search                   | 906 MB   | 256 kB
 in_tacurrent_prior_registration_applications | 445 MB   | 136 kB
 in_tacurrent_madrid_history_events           | 298 MB   | 104 kB
 in_tacurrent_foreign_applications            | 113 MB   | 56 kB
 in_tacurrent_madrid_filing_requests          | 50 MB    | 40 kB



SELECT nspname || '.' || relname AS "relation",
    pg_size_pretty(pg_relation_size(C.oid)) AS "size"
  FROM pg_class C
  LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace)
  WHERE nspname NOT IN ('pg_catalog', 'information_schema')
  ORDER BY pg_relation_size(C.oid) DESC;


-- total size
  SELECT
    pg_size_pretty(sum(pg_relation_size(C.oid))) AS "size"
  FROM pg_class C
  LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace)
  WHERE nspname NOT IN ('pg_catalog', 'information_schema');
 150 GB




select count(distinct party_name) from in_tacurrent_case_file_owners;
  count
---------
 3136840
(1 row)

-- email detector

select party_name, address_1, address_2 from in_tacurrent_case_file_owners where
address_1 ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or address_2 ~'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b' limit 10;


select count(distinct party_name)  from in_tacurrent_case_file_owners where
address_1 ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or address_2 ~'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'


PERFORM upsert_tapp_taCurrent_madrid_filing_requests();  BAD
--PERFORM upsert_tapp_taCurrent_foreign_applications();
--PERFORM upsert_tapp_taCurrent_madrid_history_events();
PERFORM upsert_tapp_taCurrent_classifications(); BAD dates

--PERFORM upsert_tapp_taCurrent_design_search();
PERFORM upsert_tapp_taCurrent_case_file_owners();
PERFORM upsert_tapp_taCurrent_case_file_statements();
PERFORM upsert_tapp_taCurrent_case_file_event_statement();
PERFORM upsert_tapp_taCurrent_trademark();
--PERFORM upsert_tapp_taCurrent_prior_registration_applications()


select count(*) from in_taCurrent_classifications;
31047505


select count(*) from in_taCurrent_classifications where first_use_anywhere_date != '' and first_use_anywhere_date is not null and first_use_anywhere_date !~ '\d\d\d\d\d\d\d\d' and status_date != 'status_date' and first_use_anywhere_date != '0';
511

Select count(*) from in_taCurrent_classifications where first_use_in_commerce_date != '' and first_use_in_commerce_date is not null and first_use_in_commerce_date !~ '\d\d\d\d\d\d\d\d' and status_date != 'status_date' and first_use_in_commerce_date != '0';
922

select version_date, creation_datetime, transaction_date, filing_date from in_taCurrent_trademark limit 10;
 version_date | creation_datetime | transaction_date | filing_date
--------------+-------------------+------------------+-------------
 version_date | creation_datetime | transaction_date | filing_date
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |
 20041108     | 201301162104      | appl-1.t         |


select registration_date, status_date, published_for_opposition_date, amend_to_register_date from in_taCurrent_trademark limit 10;





--SELECT count(to_date(version_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(creation_datetime ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(filing_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(registration_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(status_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(published_for_opposition_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(amend_to_register_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(abandonment_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(cancellation_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(republished_12c_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
--SELECT count(to_date(location_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';

SELECT count(to_date(international_registration_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
SELECT count(to_date(international_publication_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
SELECT count(to_date(international_renewal_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
SELECT count(to_date(auto_protection_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
SELECT count(to_date(international_death_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
SELECT count(to_date(international_status_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';
SELECT count(to_date(priority_claimed_date ,'YYYYMMDD')) from in_taCurrent_trademark WHERE tradenum != 'tradenum';


select count(*) from tacurrent_case_file_owners where (upper(address_1) like '%.COM%' or upper(address_2) like '%.COM%') ;
select party_name, address_1, address_2 from tacurrent_case_file_owners where (upper(address_1) like '%.COM%' or upper(address_2) like '%.COM%') limit 20;


select domestic_representative_name, attorney_name, corr_add_1,
 corr_add_2,
 corr_add_3,
 corr_add_4,
 corr_add_6

 from tacurrent_trademark where
  upper(corr_add_1) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_2) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_3) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_4) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_6) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
  limit 20;

  select count(*)

 from tacurrent_trademark where
  upper(corr_add_1) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_2) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_3) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_4) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
or upper(corr_add_6) ~ '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b';

select t.mark_identification, t.filing_date, o.party_name from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)
WHERE upper(o.party_name) like '%BIO MARIN%'
order by t.filing_date desc;


select t.mark_identification, t.filing_date, o.party_name from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)
WHERE upper(o.party_name) like '%MATTEL%'
order by t.filing_date desc;

select count(*) from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)
WHERE upper(o.party_name) like '%MATTEL%';


select c.primary_code, count(*) as cnt from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)
join tacurrent_classifications c on (c.tradenum = t.tradenum)
WHERE upper(o.party_name) like '%MATTEL%'
group by c.primary_code order by cnt desc ;

select c.us_code_concat count(*) as cnt from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)
join tacurrent_classifications c on (c.tradenum = t.tradenum)
WHERE upper(o.party_name) like '%MATTEL%'
group by c.us_code_concat order by cnt desc;

select c.international_code_concat, count(*) as cnt from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)
join tacurrent_classifications c on (c.tradenum = t.tradenum)
WHERE upper(o.party_name) like '%MATTEL%'
group by c.international_code_concat order by cnt desc;




Select party_name, count(*) as cnt from
(select o.party_name, t.tradenum from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)

where t.filing_date > to_Date('20130101','YYYYMMDD')
group by o.party_name, t.tradenum) distinct_trademarks
group by party_name order by cnt desc limit 500;



Select party_name, attorney_name, count(*) as cnt from
(select o.party_name, t.tradenum, t.attorney_name from tacurrent_trademark t join tacurrent_case_file_owners o on (o.tradenum = t.tradenum)

where t.filing_date > to_Date('20130101','YYYYMMDD')
group by o.party_name, t.tradenum, t.attorney_name) distinct_trademarks
group by party_name, attorney_name order by cnt desc limit 500;

-- Investigate dat Delta on dat Canadian Club son

--case file statements

Select sub.tradenum, sub.creation_datetime, sub.action_keys, q.type_code_raw, q.sequential_number, q.year_of_entry, q.month_of_entry, q.text
FROM in_tacurrent_case_file_statements q
JOIN
(
select tradenum, creation_datetime, action_keys from in_tacurrent_trademark where serial_number = '71080948' order by status_date
) sub
on q.tradenum = sub.tradenum
order by sub.creation_datetime, q.sequential_number
;
 71080948-TX-apc150120 | 201501202249      | TX          | GS0491        |                   |               |                | WHISKY
 71080948-TX-apc150120 | 201501202249      | TX          | CC0000        |                   |               |                | Color is not claimed as a feature of the mark.
 71080948-TX-apc150121 | 201501212242      | TX          | GS0491        |                   |               |                | WHISKY
 71080948-TX-apc150121 | 201501212242      | TX          | CC0000        |                   |               |                | Color is not claimed as a feature of the mark.
 71080948-TX-apc150125 | 201501252207      | TX          | GS0491        |                   |               |                | WHISKY
 71080948-TX-apc150125 | 201501252207      | TX          | CC0000        |                   |               |                | Color is not claimed as a feature of the mark.
 71080948-TX-apc150203 | 201502032307      | TX          | CC0000        |                   |               |                | Color is not claimed as a feature of the mark.
 71080948-TX-apc150203 | 201502032307      | TX          | GS0491        |                   |               |                | WHISKY
 71080948-TX-apc150204 | 201502042310      | TX          | CC0000        |                   |               |                | Color is not claimed as a feature of the mark.
 71080948-TX-apc150204 | 201502042310      | TX          | GS0491        |                   |               |                | WHISKY
 71080948-46-apc150310 | 201503102309      | 46          | GS0491        |                   |               |                | WHISKY
 71080948-46-apc150310 | 201503102309      | 46          | CC0000        |                   |               |                | Color is not claimed as a feature of the mark.
 --case_file_event_statement (seems added)
 Select sub.tradenum, sub.creation_datetime, sub.action_keys, q.code,  q.type, q.description_text, q.date, q.number
FROM in_tacurrent_case_file_event_statement q
JOIN
(
select tradenum, creation_datetime, action_keys from in_tacurrent_trademark where serial_number = '71080948' order by status_date
) sub
on q.tradenum = sub.tradenum
order by sub.creation_datetime, q.date
;


 Select sub.tradenum, sub.creation_datetime, sub.action_keys, q.entry_number,  q.party_type, q.legal_entity_type_code, q.entity_statement, q.party_name

FROM in_tacurrent_case_file_owners q
JOIN
(
select tradenum, creation_datetime, action_keys from in_tacurrent_trademark where serial_number = '71080948' order by status_date
) sub
on q.tradenum = sub.tradenum
order by sub.creation_datetime
;

select * from in_tacurrent_case_file_owners where name_change_explanation_concat is not null limit 10;

--