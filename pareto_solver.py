
import numpy as np

def fast_non_dominated_sort(population):
    fronts = [[]]
    domination_count = [0 for _ in population]
    dominates = [set() for _ in population]

    for i, p in enumerate(population):
        for j, q in enumerate(population):
            if all(p <= q) and any(p < q):
                dominates[i].add(j)
            elif all(q <= p) and any(q < p):
                domination_count[i] += 1
        if domination_count[i] == 0:
            fronts[0].append(i)

    current = 0
    while current < len(fronts) and fronts[current]:
        next_front = []
        for i in fronts[current]:
            for j in dominates[i]:
                domination_count[j] -= 1
                if domination_count[j] == 0:
                    next_front.append(j)
        current += 1
        fronts.append(next_front)
    return fronts[:-1]
