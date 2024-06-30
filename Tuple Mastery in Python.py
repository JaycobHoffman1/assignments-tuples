# Task 1: Formatting Flight Itineraries

flight_itineraries = [
('Alice', 'New York', 'London'), 
('Bob', 'Tokyo', 'San Francisco'),
('Jaycob', 'Portland', 'Las Vegas'),
('Cory', 'Portland', 'San Francisco'),
('Adam', 'Milan', 'Shanghai')]

def display_itineraries(itineraries):
    print('Flight itineraries:')
    
    for i, itinerary in enumerate(itineraries):
        traveler_name, origin, destination = itinerary

        print(f'Itinerary {i + 1}: {traveler_name} - From {origin} to {destination}')

display_itineraries(flight_itineraries)