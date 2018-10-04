def recurrance_relation(n, k):

    month = 1
    rabbits = {0: (0, 1)}  # tuple of mature, 1, 0 month.

    while month < n:
        rabbits = {month: ((rabbits[month-1][0]+rabbits[month-1][1]),
                           rabbits[month - 1][0]*k
        )}

        print(rabbits[month], sum(rabbits[month]))


        print(rabbits[month][0]+rabbits[month][-1])
        month += 1

recurrance_relation(33, 5)
