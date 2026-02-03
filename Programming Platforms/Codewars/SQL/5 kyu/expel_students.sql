'''
Let us consider a case where we have a students table and a courses table. The tables have the following structure:

students:

| id  | name     | email               |
|-----|----------|---------------------|
| 1   | John     | john@example.com    |
| 2   | Sarah    | sarah@example.com   |
| 3   | Robert   | robert@example.com  |
...
courses:

| id  | student_id | course_name | score |
|-----|------------|-------------|-------|
| 1   | 1          | Math        | 90    |
| 2   | 1          | Science     | 85    |
| 3   | 1          | Physics     | 92    |
| 4   | 1          | Literature  | 80    |
...
  
The university is considering expelling students who either quit their studies or are consistently performing poorly in their courses. A student who quits is defined as a student with no records in the courses table. A student who is performing poorly is defined as a student with 3 or more courses with a grade less than 60.

Write a SQL query that retrieves a list of students who qualify for expulsion based on the criteria described above.

The query should return the following columns:

1. student_id: The ID of the student
2. name: The name of the student
3. reason: The reason for expelling the student. It should say either "quit studying" if the student has no records in the courses table, or "failed in [List of Courses]" where [List of Courses] is a comma-separated list of the courses that the student has failed. Each course in the list should be followed by the grade in parentheses. Failed courses should be sorted in ascending alphabetical order.

The result should be ordered by the student ID in ascending order.

Good Luck!

Desired Output
The desired output should look like this:

student_id	name	reason
10	James	failed in Math(59), Physics(57), Science(58)
11	David	failed in Literature(58), Math(55), Physics(57), Science(56)
12	Lucy	quit studying
13	Daniel	quit studying
14	Grace	quit studying
'''
-- Substitute with your SQL
with cte1 as (
  select s.id, s.name, c.course_name, c.score
  from students s
  left join courses c
  on s.id = c.student_id
  where c.student_id is null or score < 60
  order by s.id, c.course_name
)
select 
  id as student_id, 
  name,
  case
    when (
      case 
        when count(name) > 2 then string_agg(course_name || '(' || score || ')', ', ')
      end
    ) <> 'quit studying' then 'failed in ' || (
      case 
        when count(name) > 2 then string_agg(course_name || '(' || score || ')', ', ')
      end
    )
    else 'quit studying'
  end as reason
from cte1
group by 1,2
having count(name) > 2 or (count(name) < 2 and count(course_name) <= 0)
order by id

-- Clever
select 
    s.id as student_id
  , s.name
  , case 
      when count(c.id) = 0 then 'quit studying'
      else concat('failed in ', string_agg(c.course_name || '(' || c.score || ')', ', ' order by c.course_name))
    end as reason
from students s
left outer join courses c on c.student_id = s.id
where c.student_id is null or c.score < 60
group by s.id, s.name
having count(c.id) = 0 or count(c.id) > 2
order by s.id;
