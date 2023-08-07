"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
"""

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    # Drop any duplicate salary values to avoid counting duplicates as separate salary ranks
    unique_salaries = employee['salary'].drop_duplicates()

    # Sort the unique salaries in descending order and get the Nth highest salary
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    # If N exceeds the number of unique salaries, return None
    if N > len(sorted_salaries):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    
    # Get the Nth highest salary from the sorted salaries
    nth_highest = sorted_salaries.iloc[N - 1]
    
    return pd.DataFrame({'Nth Highest Salary': [nth_highest]})