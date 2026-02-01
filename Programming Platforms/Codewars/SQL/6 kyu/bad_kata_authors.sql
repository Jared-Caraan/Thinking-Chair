'''
Task Description:
We have 2 tables:

kata_authors:

user_id (integer) - Represents the unique identifier for a user.
kata_id (integer) - Represents the unique identifier for a kata.
kata_votes:

kata_id (integer) - Represents the unique identifier for a kata. This is linked to the kata_id in the kata_authors table.
vote (float) - Represents the vote given to a kata. Can only be one of three values:
1: "very satisfied"
0.5: "somewhat satisfied"
0: "not satisfied"
Your task is to create a SQL query to identify bad kata authors.

A bad kata is defined as one which:

Has received at least three votes.
Has an average vote of strictly less than 0.7.
We want to identify authors who have created 5 or more bad katas.

The output should List user IDs (user_id) and the count of their bad katas (bad_kata_count). And be ordered first by the count of bad katas in descending order. 
In case of a tie - by user ID in descending order.

GLHF!

Desired Output
The desired output should look like this:

user_id	bad_kata_count
34	6
23	5
...
'''
-- Your SQL
WITH cte1 AS (
  SELECT auth.user_id, auth.kata_id, COUNT(auth.kata_id), AVG(v.vote)
  FROM kata_authors auth
  LEFT JOIN kata_votes v
  ON auth.kata_id = v.kata_id
  GROUP BY 1,2
  HAVING COUNT(auth.kata_id) >= 3 AND AVG(v.vote) < 0.7
  ORDER BY 1,2
)
SELECT user_id, COUNT(kata_id) AS bad_kata_count
FROM cte1
GROUP BY 1
HAVING COUNT(kata_id) >= 5
ORDER BY 2 DESC, 1 DESC;
