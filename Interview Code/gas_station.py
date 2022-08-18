# @author   Lucas Cardoso de Medeiros
# @since    08/06/2022
# @version  1.0

# GAS STATION ()

# Rules:
# Given a circular list of gas stations, from s station i to the i + 1, and the last onde goes back do the
# first, find the index of the station from where we start to be able to traverse all the stations and go back to the
# initial one without running out of gas

# gas[i] = amount of gas at the station i
# cost[i] = cost to go from station i to the next one

# Only move forward
# Gas tank starts empty
# Answer is unique
# If station doesn't exist return -1

# Example:
# gas = [1,5,3,3,5,3,1,3,4,5]
# cost = [5,2,2,8,2,4,2,5,1,2]

# output = 8


# Solution 1: brute force
# O(n^2) complexity
def can_traverse_brute_force(gas, cost, start):
    if len(gas) != len(cost):
        return False
    n = len(gas)
    tank = 0
    station = start
    started = False
    while station != start or not started:
        started = True
        tank += gas[station] - cost[station]
        if tank < 0:
            return False
        station = (station + 1) % n
    return True


def find_start_brute_force(gas, cost):
    if len(gas) != len(cost):
        return -1
    for i in range(len(gas)):
        if can_traverse_brute_force(gas, cost, i):
            return i
    return -1


# Solution 1: optimized
# O(n) complexity
def gas_station(gas, cost):
    if len(gas) != len(cost):
        return -1
    tank, prev_tank, candidate = 0, 0, 0
    n = len(gas)
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            candidate = i + 1
            prev_tank += tank
            tank = 0
    if candidate < n and tank + prev_tank >= 0:
        return candidate
    else:
        return -1


if __name__ == '__main__':
    # Example:
    gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
    cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
    # start = find_start_brute_force(gas, cost)
    start = gas_station(gas, cost)
    print(f"Start: {start}")
