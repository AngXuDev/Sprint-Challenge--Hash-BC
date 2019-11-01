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
    hashtable = HashTable(length)
    route = [None] * length

    # Build hash table by inserting the source as key and destination as value
    for i in range(length):
        start = tickets[i].source
        end = tickets[i].destination
        hash_table_insert(hashtable, start, end)

    # create initial element of route list by grabbing the ticket with NONE key/source
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    # loop and add tickets to the route by using the destination/value of prior ticket as
    # the key/source for the current ticket
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
