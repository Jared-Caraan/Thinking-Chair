-- Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, 
-- total number of senior managers, total number of managers, and total number of employees. 
-- Order your output by ascending company_code.

-- Note:

-- The tables may contain duplicate records.
-- The company_code is string, so the sorting should not be numeric. 
-- For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

SELECT 
    COMP.company_code, 
    COMP.founder, 
    COUNT(DISTINCT(LEAD.lead_manager_code)),
    COUNT(DISTINCT(SENIOR.senior_manager_code)),
    COUNT(DISTINCT(MANAGER.manager_code)),
    COUNT(DISTINCT(EMP.employee_code))
FROM Company COMP
INNER JOIN Lead_Manager LEAD
ON COMP.company_code = LEAD.company_code
INNER JOIN Senior_Manager SENIOR
ON LEAD.lead_manager_code = SENIOR.lead_manager_code
INNER JOIN Manager MANAGER
ON SENIOR.senior_manager_code = MANAGER.senior_manager_code
INNER JOIN Employee EMP
ON MANAGER.manager_code = EMP.manager_code
GROUP BY COMP.company_code, COMP.founder