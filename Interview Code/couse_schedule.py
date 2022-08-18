# @author   Lucas Cardoso de Medeiros
# @since    09/06/2022
# @version  1.0

# COURSE SCHEDULE ()

# Rules
# Given an integer n representing the number of courses, label from 0 to n - 1
# And an array prerequisites[i]
# where prerequisites[i] = [a, b] means that you have to take the course b before taking the course a, determine if
# it's possible to finish all the courses

# Example:

# n = 6
# prerequisites = [[0,1], [3,0], [1,3], [2,1], [4,1], [4,2], [5,3], [5,4]]
# output: False

# n = 6
# prerequisites = [[3,0], [1,3], [2,1], [4,1], [4,2], [5,3], [5,4]]
# output: True

from collections import deque


# Solution 1: topological search + dfs (?)
# O(n + m) complexity, with m = len(prerequisites)
def dfs(graph, vertex, path, order, visited):
    path.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False
    path.remove(vertex)
    order.append(vertex)
    return True


def top_sort(graph):
    visited = set()
    path = []
    order = []
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(graph, vertex, path, order, visited)
    return order[::-1]


def course_schedule1(n, prerequisites):
    graph = [[] for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
    visited = set()
    path = set()
    order = []
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False
    return True


# Solution 2: breadth-first search
# O(n + m) complexity, with m = len(prerequisites)
def course_schedule2(n, prerequisites):
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    order = []
    queue = deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == n


if __name__ == '__main__':
    # Examples:

    n = 6
    prerequisites = [[0, 1], [3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
    # output: False

    n = 6
    # prerequisites = [[3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
    # output: True

    if course_schedule1(n, prerequisites):
        print("Possible")
    else:
        print("Not possible")
