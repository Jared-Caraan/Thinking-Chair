-- P(R) represents a pattern drawn by Julia in R rows. Write a query to print the pattern P(20).

-- https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true

DELIMITER //

CREATE PROCEDURE P()
BEGIN
DECLARE str VARCHAR(5000);
DECLARE counter INT;

SET counter = 20;

WHILE counter <> 0 DO
    SET str = REPEAT('* ', counter);
    SET counter = counter - 1;
    SELECT str;
END WHILE;
    
END//

DELIMITER ;

call P();