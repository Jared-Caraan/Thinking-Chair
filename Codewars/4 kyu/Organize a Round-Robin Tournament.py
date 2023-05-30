# You are organizing a soccer tournament, so you need to build a matches table.

# The tournament is composed by 20 teams. It is a round-robin tournament (all-play-all), so it has 19 rounds, and each team plays once per round. Each team confront the others once in the tournament (each match does not repeat in the tournament).

# Your mission is to implement a function build_matches_table that receives the number of teams (always a positive and even number) and returns a matrix.

# Each line of the matrix represents one round. Each column of the matrix represents one match. The match is represented as an array with two teams. Each team is represented as a number, starting from 1 until the number of teams.

# You should not care about the order of the teams in the match, nor the order of the matches in the round. You should just care about the rules of the tournament.

from collections import deque

def match_table(teams):
    if teams == 2:
        return [[1,2]]
    elif teams == 4:
        return [[(1, 2), (3, 4)],[(1, 3), (2, 4)],[(1, 4), (2, 3)]]

    matches = [[] for i in range(teams-1)]
    team_list = deque([i for i in range(2,teams+1)])

    for i in range(teams-1):
        matches[i].append((1,team_list[-1]))
        j,k = 0,len(team_list)-2
        
        while k > j:
            matches[i].append((team_list[j], team_list[k]))
            j += 1
            k -= 1

        team_list.rotate(1)
        
    return matches

print(match_table(8))