#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    map   = {}

    for ticket in tickets:
        source = ticket.source
        destination = ticket.destination
        map[source] = destination

    current = map["NONE"]
    while current != "NONE":
        route.append(current)
        current = map[current]

    route.append("NONE")

    return route
