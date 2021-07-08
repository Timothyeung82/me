TODO: Reflect on what you learned this week and what is still unclear.


another way i try to do pokedex

def pokedex(low=1, high=5):
    """ Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.
    
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    template = "https://pokeapi.co/api/v2/pokemon/{id}"

    pokemon = []
    for n in range(low, high):
        url = template.format(id=n)
        r = requests.get(url)
        if r.status_code is 200:
            the_json = json.loads(r.text)
            name = the_json["name"]
            weight = the_json["weight"]
            height = the_json["height"]
            stats = {"name": name, "weight": weight, "height": height}
            print(stats)
            pokemon.append(stats)
    print(pokemon)
    pokemon_height = sorted(pokemon, key=lambda k: k['height'])
    print(pokemon_height)

    return pokemon_height[-1]



--------------------------------------------------------------------------

learn a quicker and shorter way of doing pew

    with open("set4/Trispokedovetiles(laser).gcode", "r") as g_code:
        m_code_count = g_code.read().count("M10 P1")
    
    with open("set4/lasers.pew", "w") as pew:
        pew.write(str(m_code_count))