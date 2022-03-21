-- INSERT INTO	dojos (name)
-- VALUES ("Chicago"), ("Seattle"), ("Online");

-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM dojos;

-- SELECT * FROM dojos;
-- SELECT * FROM ninjas;

-- INSERT INTO ninjas (first_name, last_name, age, dojos_id)
-- VALUES ("Michele", "Helm", 21, 7), ("Jack", "Sparrow", 21, 7), ("So", "Ji Sub", 21, 7),
-- 		("Kimura", "Takuya", 21, 8), ("Brad", "Pitt", 21, 8), ("Johnny", "Depp", 21, 8),
-- 		("Kate", "Winslet", 21, 9), ("Rachel", "McAdams", 21, 9), ("Jennifer", "Aniston", 21, 9);

-- SELECT * FROM dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id
-- WHERE dojos.id = 7;

-- SELECT * FROM dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id
-- 	WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojos_id DESC LIMIT 1);

SELECT * FROM dojos
WHERE dojos.id = (SELECT dojos_id FROM ninjas ORDER BY dojos_id DESC LIMIT 1);