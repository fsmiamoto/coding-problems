DELETE FROM Person WHERE id NOT IN (
    SELECT tmp.id FROM (
        SELECT MIN(id) AS id FROM Person GROUP BY email
    ) tmp
)
