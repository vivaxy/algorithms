/*
https://leetcode.com/problems/exchange-seats/

https://leetcode.com/submissions/detail/143029079/
*/

SELECT (
    CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END
) AS id, student
FROM seat, (
    SELECT COUNT(*) AS counts
    FROM seat
) AS seat_counts
ORDER BY id ASC;
