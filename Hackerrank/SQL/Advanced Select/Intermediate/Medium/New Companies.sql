SELECT 
    COMP.company_code, 
    COMP.founder, 
    COUNT(LEAD.lead_manager_code), 
    COUNT(SENIOR.senior_manager_code),
    COUNT(MANAGER.manager_code),
    COUNT(EMP.employee_code)
FROM Company COMP
INNER JOIN Lead_Manager LEAD
ON COMP.company_code = LEAD.company_code
INNER JOIN Senior_Manager SENIOR
ON COMP.company_code = LEAD.company_code AND
LEAD.lead_manager_code = SENIOR.lead_manager_code
INNER JOIN Manager MANAGER
ON COMP.company_code = LEAD.company_code AND
SENIOR.senior_manager_code = MANAGER.senior_manager_code
INNER JOIN Employee EMP
ON MANAGER.manager_code = EMP.manager_code
GROUP BY 
    COMP.company_code,
    COMP.founder
ORDER BY COMP.company_code