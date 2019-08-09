#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        # get difference
        diff = limit - weights[i]

        # check if it's already in ht
        match = hash_table_retrieve(ht, diff)
        if match is not None:
            return [i, match]
        
        # if it's not, insert it in the table
        hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
