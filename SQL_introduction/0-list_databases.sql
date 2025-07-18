-- 0. Listing all databases on the MySQL server in alphabetical order
SELECT SCHEMA_NAME AS `Database` 
FROM information_schema.SCHEMATA 
ORDER BY SCHEMA_NAME;
