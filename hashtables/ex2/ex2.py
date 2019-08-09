#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)



class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    # loop through and put each ticket in ht
    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)
       
    # Need first ticket
    # "None" is key of start ticket, set to route first index
    first_ticket = hash_table_retrieve(ht, "NONE")
    route[0] = first_ticket
    
    # check the rest of the tickets
    for i in range(1, length):
        next_ticket = hash_table_retrieve(ht, route[i-1])
        
        # save the returned value as ith ticket
        route[i] = next_ticket

    return route

    # O(n)
