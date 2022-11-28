import random
import math


def create_state(n):
    res = []
    s = set()
    while len(s) < n:
        x = random.randint(0, n - 1)
        s.add(x)
    for i in s:
        res.append(int(i))
    return res


def find_cost(city_map, t):
    l = len(city_map)
    x = random.randint(0, len(city_map) - 1)
    y = random.randint(0, len(city_map) - 1)
    while x == y:
        x = random.randint(0, len(city_map) - 1)
        y = random.randint(0, len(city_map) - 1)
    city_map[x], city_map[y] = city_map[y], city_map[x]
    cost = 0
    for i in range(len(city_map)):
        if t[city_map[i]][city_map[(i + 1) % l]] == 0:
            city_map[x], city_map[y] = city_map[y], city_map[x]
            return -1
        cost = cost + t[city_map[i]][city_map[(i + 1) % l]]
    return cost


def stimulated_annealing(curr_cost, city_map, t):
    for _ in range(100):
        temperature = pow(10, 10)
        cooling_factor = 0.99
        ending_temperature = 0.0001
        while temperature > ending_temperature:
            new_cost = find_cost(city_map, t)
            if new_cost == -1:
                continue
            difference = new_cost - curr_cost
            if difference < 0 or math.exp((-1 * difference) // temperature) > random.randint(0, 1):
                curr_cost = new_cost
            temperature = temperature * cooling_factor
    print("Final path with minimum cost :-")
    print(city_map)
    return curr_cost


if __name__ == "__main__":
    n = int(input("Enter the number of cities : "))
    t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            print('Enter the distance between city ', i + 1, ' and ', j + 1)
            x = int(input())
            t[i][j] = x
            t[j][i] = x
    city = create_state(n)
    cos = find_cost(city, t)
    result = stimulated_annealing(cos, city, t)
    print("The resulting cost of the final path :-")
    print(result)