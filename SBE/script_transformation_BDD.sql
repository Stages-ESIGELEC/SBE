-- code that searching for duplicates
SELECT nom,adresse,telephone,secteur, COUNT(*)
FROM structure
GROUP BY nom,adresse,telephone,secteur
HAVING COUNT(*) > 1
LIMIT 25;


-- code that removes duplicates
DELETE FROM structure
WHERE id NOT IN (
                SELECT MIN(id)
                FROM (SELECT * FROM structure) AS structure_test
                GROUP BY nom,adresse,telephone,secteur)


