# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
 

# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

import pandas as pd

def calculate_bonus(df):
    if df['name'].startswith("M") or df['employee_id'] % 2 == 0:
        return 0
    return df['salary']

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda row: calculate_bonus(row), axis = 1)

    return employees[['employee_id', 'bonus']].sort_values('employee_id')