#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Loop through the list and store each key value pair into a hash table
    # for i in range(length):
    #     difference = hash_table_retrieve(ht, weights[i])
    #     if difference is None:
    #         hash_table_insert(ht, limit-weights[i], weights[i])
    #     else:
    #         return (i, weights.index(difference))

    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i, w in enumerate(weights):
        difference = limit - w
        exist = hash_table_retrieve(ht, difference)
        if exist:
            return (max(i, exist), min(i, exist))

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
