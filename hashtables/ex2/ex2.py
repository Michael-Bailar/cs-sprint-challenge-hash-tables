#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # instantiate a list of destination strings
    route = []
    #create a cache of tickets(route_cache) where:
    route_cache = {}
        #key = ticket.source
        #value = ticket.destination
    for ticket  in tickets:
        route_cache[ticket.source] = ticket.destination

    # generate route list
    # start with beginning
    route.append(route_cache["NONE"])
    # fill out rest of route
    for i in range(length - 1):
        route.append(route_cache[route[i]])
        
    return route