-- There is an events table used to track different key activities taken on a website. 
-- For this task you need to:
--   1. find the entries whose name equals "trained"
--   2. group them by the day the activity happened (the date part of the created_at timestamp) and their description's
--   3. the 2 aforementioned fields should be returned together with the number of grouped entries in a column called count
--   4. the result should also be sorted by day

-- "events" table schema
-- id (bigint)
-- name (text)
-- created_at (timestamp)
-- description (text)

-- expected result schema
-- day (date)
-- description (text)
-- count (numeric)

SELECT
  created_at::timestamp::date AS day,
  description,
  COUNT(name) AS count
FROM events
WHERE name = 'trained'
GROUP BY 1,2;
