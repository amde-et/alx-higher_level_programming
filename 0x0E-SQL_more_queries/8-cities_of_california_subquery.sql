-- script that lists all the cities of california that can be found in the db
SELECT id, name FROM cities WHERE state_id = (
SELECT id FROM states WHERE name = 'California') ORDER BY id;
