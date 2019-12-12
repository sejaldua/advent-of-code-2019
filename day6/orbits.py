# get orbit strings from input file
def get_orbits(fpath):
    return [line.strip() for line in open(fpath, 'r')]

# parse input file strings to make a dictionary of all the direct orbits
# NOTE: keys are the outer planet, values are the planets being orbittted
def parse_orbits(orbits):
    orbit_dict = {}
    for line in orbits:
        planets = line.split(")")
        orbit_dict[planets[1]] = planets[0]
    return orbit_dict
        
# recursive function to get the number of direct and indirect orbits for given planet
def get_num_orbits(orbit_dict, planet):
    if planet not in orbit_dict.keys():
        return 0
    return 1 + get_num_orbits(orbit_dict, orbit_dict[planet])

# function to get a path of orbits from specified outer planet to innermost planet
def get_orbital_path(orbit_dict, start_planet):
    planet = start_planet
    path = []
    while planet in orbit_dict.keys():
        path.append(planet)
        planet = orbit_dict[planet]
    return path
        

if __name__ == "__main__":

    # parse input file and make a dictionary of direct orbit relationships
    orbits = get_orbits('input.txt')
    orbit_dict = parse_orbits(orbits)

    # PART 1: get total number of direct and indirect orbits by summing full orbital paths for each planet
    print(sum(get_num_orbits(orbit_dict, planet) for planet in orbit_dict.keys()))
    
    # PART 2: finding the number of orbital transfers needed for YOU to orbit the same planet as SANta
    # add orbital distance from YOU to closest shared orbit planet and from SAN to closest shared orbit planet
    you_path = get_orbital_path(orbit_dict, 'YOU')
    santa_path = get_orbital_path(orbit_dict, 'SAN')
    shared = [p for p in you_path if p in santa_path]
    print(you_path.index(shared[0]) + santa_path.index(shared[0]) - 2)
