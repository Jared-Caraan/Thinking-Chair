-- Write a query to print all prime numbers less than or equal to 1000. Print your result on a single line, and use the ampersand (&) character as your separator (instead of a space).

-- https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true

DELIMITER //

CREATE PROCEDURE P()
BEGIN
DECLARE str VARCHAR(5000);
DECLARE counter INT;
DECLARE num INT;
DECLARE ans INT;
DECLARE factor INT;

SET factor = 0;
SET num = 1;
SET counter = 11;
SET str = '2&3&5&7&';

WHILE counter < 1000 DO

    WHILE num < counter + 1 DO
        IF counter % num = 0 THEN
            SET factor = factor + 1;
        END IF;
        SET num = num + 1;
    END WHILE;
    
    IF factor = 2 THEN
        SET str = CONCAT(str,counter,'&');
    END IF;
    
    SET num = 1;
    SET factor = 0;
    SET counter = counter + 1;
    
END WHILE;
SET str = SUBSTR(str, 1, LENGTH(str)-1);
SELECT str;
END//

DELIMITER ;

call P();