import data

# Write your functions for each part in the space below.

# Part 1

def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle: #creates a rectangle given 2 of its points
    #sets right and left
    if point1.x > point2.x:
        right = point1.x
        left = point2.x
    else:
        right = point2.x
        left = point1.x

    #sets top and bottom
    if point1.y > point2.y:
        top = point1.y
        bottom = point2.y
    else:
        top = point2.y
        bottom = point1.y
    
    top_left = data.Point(left, top)
    bottom_right = data.Point(right, bottom)

    rectangle = data.Rectangle(top_left, bottom_right)

    return rectangle

# Part 2

def shorter_duration_than(duration1: data.Duration, duration2: data.Duration) -> bool: #tests whether 1 given duration is shorter than another
    total_seconds_1 = (duration1.minutes) * 60 + duration1.seconds
    total_seconds_2 = (duration2.minutes) * 60 + duration2.seconds
    return total_seconds_1 < total_seconds_2

# Part 3

def songs_shorter_than(songs: list[data.Song], max_length: data.Duration) -> list[data.Song]: #returns all songs shorter than a given duration from a given list of songs
    return [] if songs == [] else [song for song in songs if shorter_duration_than(song.duration, max_length)]

# Part 4

def add_durations(durations: list[data.Duration]) -> data.Duration: #adds up a list of durations into one duration
    if durations == []:
        return 0
    total_minutes = sum([duration.minutes for duration in durations])
    total_seconds = sum([duration.seconds for duration in durations])
    while total_seconds >= 60:
        total_seconds -=60
        total_minutes += 1
    return data.Duration(total_minutes, total_seconds)

def running_time(songs: list[data.Song], nums: list[int]) -> data.Duration: #returns the total running time of a playlist given a list of songs and an order
    return 0 if songs == [] else add_durations([songs[num].duration for num in nums])

# Part 5

def validate_route(city_links: list[list[str]], route: list[str]) -> bool: #tests whether a given route is valid given a list of city links (ie. there are links from each city to the next in the route)
    if city_links == []:
        return False
    for i in range(len(route) - 1): # -1 b/c last city doesn't need a link to a next city
        if not([route[i], route[i + 1]] in city_links or [route[i + 1], route[i]] in city_links): #this is fine b/c 2 cities in each link -- don't need to make a permutations thing
            return False
    return True
    #False if there isn't a direct link (i.e. you need to travel through another city)

# Part 6
