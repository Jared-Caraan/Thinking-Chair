# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# | area        | int     |
# | population  | int     |
# | gdp         | bigint  |
# +-------------+---------+
# name is the primary key (column with unique values) for this table.
# Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
 

# A country is big if:

# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).
# Write a solution to find the name, population, and area of the big countries.

# Return the result table in any order.

# The result format is in the following example.

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filt = (world['area'] >= 3_000_000) | (world['population'] >= 25_000_000)

    return world.loc[filt, ['name', 'population', 'area']]