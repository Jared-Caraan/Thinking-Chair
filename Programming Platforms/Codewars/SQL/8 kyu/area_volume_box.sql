-- # write your SQL statement here: 
-- you are given a table 'box' with columns: width (int), height (int), depth (int)
-- return a query with columns: width, height, depth, area (int), volume (int)
-- sort results by area ascending, then volume ascending, then width ascending, then height ascending
SELECT
  width,
  height,
  depth,
  (2*depth*width) + (2*depth*height) + (2*height*width) AS area,
  depth * width * height AS volume
FROM box
ORDER BY area ASC, volume ASC, width ASC, height ASC

-- Clever
select *, 2*(width*height+width*depth+height*depth) area, height*width*depth volume from box
order by 4,5,1,2
