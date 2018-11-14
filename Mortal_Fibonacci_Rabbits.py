import numpy as np

def recurrance_relation(n, m):  # n months, m lifespan

    # creates array of mature rabbits that breed, length m-1
    rabbits = np.zeros(m-1, dtype="int")
    # creates array of young rabbits (not breeding)
    young_rabbits = np.array([1])

    for i in range(0, n-1):

        print("-----------", i + 2)

        # adds the newly matured rabbit
        rabbits = np.insert(rabbits, 0, young_rabbits[0])

        # breeding
        young_rabbits = np.insert(young_rabbits, 0, np.sum(rabbits[1:]))

        # ageing
        young_rabbits = np.delete(young_rabbits, -1)

        # kills the older generation
        rabbits = np.delete(rabbits, -1)
        print("rabbits", rabbits)
        print("young", young_rabbits)
        print("total rabbits", young_rabbits.sum() + rabbits.sum())



    return print(young_rabbits.sum()+rabbits.sum())


recurrance_relation(6, 3) # test (6, 3), answer =  4


