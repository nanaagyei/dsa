
class City:

    def __init__(self, name):
        self.name = name
        self.routes = {}  # connected routes from the city with their prices

    def add_route(self, city, price):
        self.routes[city] = price


def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_table = {}

    unvisited_cities = []  # To keep track of the known cities we have not visited

    visited_cities = {}  # To keep track of the cities we have visited

    # Add the starting city's name as the first key inside the cheapest_prices_table with a value of 0 since it costs nothing to get there
    cheapest_prices_table[starting_city.name] = 0

    current_city = starting_city
    # print(f"Current city: {current_city.name}")

    while current_city:
        # Add th current_city's name to the visited_cities hash to show that we have officially visited it.
        visited_cities[current_city.name] = True
        # print(f"Visited Cities: {visited_cities}")
        # Loop through the current_city's routes
        for adjacent_city, price in current_city.routes.items():
            # If we discover a new city
            if not visited_cities.get(adjacent_city.name, False):
                # we append it to the list of unvisited cities
                unvisited_cities.append(adjacent_city)

            # print(f"Unvisited cities inside for loop: {unvisited_cities}")
            # Calculate the price of getting from the starting city to the adjacent city using the CURRENT city as the second-to-last stop
            price_through_current_city = cheapest_prices_table[current_city.name] + price

            # If the price from the STARTING city to the ADJACENT city is the cheapest one we have found so far...
            if (not cheapest_prices_table.get(adjacent_city.name, False)) or (price_through_current_city < cheapest_prices_table.get(adjacent_city.name)):
                # ...update the cheapest_prices_table to reflect the new, lower cost of getting to the adjacent city
                cheapest_prices_table[adjacent_city.name] = price_through_current_city

                # Also update the cheapest_previous_stopover_table to show that the current city is the previous stopover to the adjacent city
                cheapest_previous_stopover_table[adjacent_city.name] = current_city.name
        # print(f"Unvisited cities after for loop: {unvisited_cities}")

        # Find the next city to visit by looking at all the unvisited cities and picking the one with the cheapest price to get to from the starting_city.
        # We do this by looping through the unvisited_cities array and finding the city with the cheapest price in the cheapest_prices_table
        cheapest_price = None
        cheapest_city = None
        for city in unvisited_cities:
            if (not cheapest_price) or (cheapest_prices_table[city.name] < cheapest_price):
                cheapest_price = cheapest_prices_table[city.name]
                cheapest_city = city
        current_city = cheapest_city

        # Once we finish going through all of the current city's routes, we remove it from the list of unvisited cities and mark it as visited
        if current_city in unvisited_cities:
            unvisited_cities.remove(current_city)
    for destination, origin_city in cheapest_previous_stopover_table.items():
        print(
            f"Destination: {destination}, Origin City: {origin_city}")
    # Once we have visited all the cities, we can use the cheapest_previous_stopover_table to backtrack from the final destination to the starting city
    shortest_path = []
    current_city_name = final_destination.name

    while current_city_name != starting_city.name:
        # Add each current_city_name we encounter to the shortest path array
        shortest_path.append(current_city_name)
        # We use the cheapest_previous_city_table to follow each city to its previous stopover city
        current_city_name = cheapest_previous_stopover_table[current_city_name]

    # Finally, add the starting city to the shortest path array
    shortest_path.append(starting_city.name)

    # Reverse the array so that the cities are in the correct order
    return shortest_path[::-1]


if __name__ == "__main__":
    # Create the cities
    atlanta = City("Atlanta")
    boston = City("Boston")
    chicago = City("Chicago")
    denver = City("Denver")
    el_paso = City("El Paso")

    atlanta.add_route(boston, 100)
    atlanta.add_route(denver, 160)
    boston.add_route(chicago, 120)
    boston.add_route(denver, 180)
    chicago.add_route(el_paso, 80)
    denver.add_route(chicago, 40)
    denver.add_route(el_paso, 140)

    print(dijkstra_shortest_path(atlanta, el_paso))
