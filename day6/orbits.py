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

if __name__ == "__main__":
    orbits = get_orbits('input.txt')
    orbit_dict = parse_orbits(orbits)
    print(sum(get_num_orbits(orbit_dict, planet) for planet in orbit_dict.keys()))
    
