# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.
 

# Table: Orders

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

# Write a solution to find all customers who never order anything.

# Return the result table in any order.

# The result format is in the following example.

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers.rename(columns = {'name':'Customers'}, inplace = True)
    id_who_ordered = orders['customerId'].unique().tolist()
    filter_ordered = customers['id'].isin(id_who_ordered)
    return customers.loc[~filter_ordered][['Customers']]

    # alternative solution
    # df = customers[~customers['id'].isin(orders['customerId'])]
    # return df[['name']].rename(columns={'name': 'Customers'})