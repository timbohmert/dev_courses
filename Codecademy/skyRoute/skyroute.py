#Vancouver’s public metro system has asked you to help create a program to help commuters get from one landmark to another. You’ll be building out “SkyRoute,” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat. For the purposes of this project, you can assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.

#imports
from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices


#prints off the landmark_choices
landmark_string = ''
for key, landmark in landmark_choices.items():
    landmark_string += '{0}: {1} \n'.format(key, landmark)

stations_under_construction = ['Richmond-Brighouse', 'Patterson', 'Lincoln']

def get_active_stations():
    updated_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station in vc_metro.keys():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])
    return updated_metro

            


def greet() :
    print('Hi there and welcome to SkyRoute!')
    print("We'll help you find the shortest route between the following Vancouver Landmarks:\n{0}".format(landmark_string))


def skyroute():
    greet()
    new_route()
    goodbye()


#handles setting selected origin and destination
def set_start_and_end(start_point, end_point):
    if start_point:
        change_point = input('What would you like to change? You can enter \'o\' for \'origin\', \'d\' for \'destination\', or \'b\' for \'both\': ')
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            print('Oops, that isn\'t \'o\', \'d\', or \'b\'...')
            set_start_and_end(start_point, end_point)
    
    else:
        start_point = get_start()
        end_point = get_end()
    
    return start_point, end_point


#used to request origin from user
def get_start():
    start_point_letter = input('Where are you coming from? Type in the corresponding letter: ')
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print('Sorry, that\'s not a landmark we have data on. Let\'s try this again...')
        get_start()


#used to request destination from user
def get_end():
    end_point_letter = input('Ok, where are you headed? Type in the corresponding letter: ')
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print('Sorry, that\'s not a landmark we have data on. Let\'s try this again...')
        get_end()


#wrapper function to get and set origin and destination, call search to get the recommended route, and allow users to search for other routes
def new_route(start_point = None, end_point = None):
    start_point, end_point = set_start_and_end(start_point, end_point)

    shortest_route = get_route(start_point, end_point)

    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print('The shortest metro route from {0} to {1} is :\n{2}.'.format(start_point, end_point, shortest_route_string))
    
    else:
        print('Unfortunately, there is currently no path between {0} and {1} due to maintenance.'.format(start_point, end_point))

    again = input('Would you like to see another route? Enter y/n: ')
    if again == 'y':
        show_landmarks()
        new_route(start_point, end_point)


#used to determine the shortest metro route between two landmarks
def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    #used to collect all of the possible shortest routes when multiple start_stations and end_stations
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            if len(stations_under_construction) > 0:
                possible_route = dfs(metro_system, start_station, end_station)
                if not possible_route:
                    return None
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)

    #determines the shortest length route based on the number of stops in the route
    shortest_route = min(routes, key=len)
    return shortest_route


#when user requrest, prints the list of landmarks
def show_landmarks():
    see_landmarks = input('Would like to see the list of landmarks again? Enter y/n: ')
    if see_landmarks == 'y':
        print(landmark_string)
    

#prints goodbye message if the user does not want to complete any more actions
def goodbye():
    print('Thanks for using SkyRoute!')

skyroute()