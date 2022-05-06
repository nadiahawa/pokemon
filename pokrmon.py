import requests as r
import os

pokes = r.get('https://pokeapi.co/api/v2/pokemon/')

pokes = pokes.json()
print(type(pokes))

# abilities = info_on_poke['abilities'][0]['ability']['name']
#like index += for each iteration along with name.. couldnt figure it out

pokename = pokes['results'][0]['name']
pokurl0 = pokes['results'][0]['url']
bulbasaur = r.get(pokurl0)
bulbasaur = bulbasaur.json()
name = bulbasaur['name']
weight = bulbasaur['weight']
all_abilities = [v['ability']['name']for v in bulbasaur['abilities']]
pok_typ = [v['type']['name']for v in bulbasaur['types']]
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')
print(f'type: {pok_typ}')





pokename = pokes['results'][1]['name']
pokurl1 = pokes['results'][1]['url']
ivysaur = r.get(pokurl1)
ivysaur = ivysaur.json()
name = ivysaur['name']
weight = ivysaur['weight']
all_abilities = [v['ability']['name']for v in ivysaur['abilities']]
pok_typ = [v['type']['name']for v in ivysaur['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][2]['name']
pokurl2 = pokes['results'][2]['url']
venusaur = r.get(pokurl2)
venusaur = venusaur.json()
name = venusaur['name']
weight = venusaur['weight']
all_abilities = [v['ability']['name']for v in venusaur['abilities']]
pok_typ = [v['type']['name']for v in venusaur['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][3]['name']
pokurl3 = pokes['results'][3]['url']
charmander = r.get(pokurl3)
charmander = charmander.json()
name = charmander['name']
weight = charmander['weight']
all_abilities = [v['ability']['name']for v in charmander['abilities']]
pok_typ = [v['type']['name']for v in charmander['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')
#some kind of list of names that could loop through to get all this info through..for pokemon name and index



#charmeleon
pokename = pokes['results'][4]['name']
pokurl4 = pokes['results'][4]['url']
charmeleon = r.get(pokurl4)
charmeleon = charmeleon.json()
name = charmeleon['name']
weight = charmeleon['weight']
all_abilities = [v['ability']['name']for v in charmeleon['abilities']]
pok_typ = [v['type']['name']for v in charmeleon['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][5]['name']
pokurl5 = pokes['results'][5]['url']
charizard = r.get(pokurl5)
charizard = charizard.json()
name = charizard['name']
weight = charizard['weight']
all_abilities = [v['ability']['name']for v in charizard['abilities']]
pok_typ = [v['type']['name']for v in charizard['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')



pokename = pokes['results'][6]['name']
pokurl6 = pokes['results'][6]['url']
squirtle = r.get(pokurl6)
squirtle = squirtle.json()
name = squirtle['name']
weight = squirtle['weight']
all_abilities = [v['ability']['name']for v in squirtle['abilities']]
pok_typ = [v['type']['name']for v in squirtle['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][7]['name']
pokurl7 = pokes['results'][7]['url']
wartortle = r.get(pokurl7)
wartortle = wartortle.json()
name = wartortle['name']
weight = wartortle['weight']
all_abilities = [v['ability']['name']for v in wartortle['abilities']]
pok_typ = [v['type']['name']for v in wartortle['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][8]['name']
pokurl8 = pokes['results'][8]['url']
blastoise = r.get(pokurl8)
blastoise = blastoise.json()
name = blastoise['name']
weight = blastoise['weight']
all_abilities = [v['ability']['name']for v in blastoise['abilities']]
pok_typ = [v['type']['name']for v in blastoise['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][9]['name']
pokurl9 = pokes['results'][9]['url']
caterpie = r.get(pokurl9)
caterpie = caterpie.json()
name = caterpie['name']
weight = caterpie['weight']
all_abilities = [v['ability']['name']for v in caterpie['abilities']]
pok_typ = [v['type']['name']for v in caterpie['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')





pokename = pokes['results'][10]['name']
pokurl10 = pokes['results'][10]['url']
metapod = r.get(pokurl10)
metapod = metapod.json()
name = metapod['name']
weight = metapod['weight']
all_abilities = [v['ability']['name']for v in metapod['abilities']]
pok_typ = [v['type']['name']for v in metapod['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][11]['name']
pokurl11 = pokes['results'][11]['url']
weedle = r.get(pokurl11)
weedle = weedle.json()
name = weedle['name']
weight = weedle['weight']
all_abilities = [v['ability']['name']for v in weedle['abilities']]
pok_typ = [v['type']['name']for v in weedle['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][12]['name']
pokurl12 = pokes['results'][12]['url']
kakuna = r.get(pokurl12)
kakuna = kakuna.json()
name = kakuna['name']
weight = kakuna['weight']
all_abilities = [v['ability']['name']for v in kakuna['abilities']]
pok_typ = [v['type']['name']for v in kakuna['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')





pokename = pokes['results'][13]['name']
pokurl13 = pokes['results'][13]['url']
beedrill = r.get(pokurl13)
beedrill = beedrill.json()
name = beedrill['name']
weight = beedrill['weight']
all_abilities = [v['ability']['name']for v in beedrill['abilities']]
pok_typ = [v['type']['name']for v in beedrill['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')




pokename = pokes['results'][14]['name']
pokurl14 = pokes['results'][14]['url']
pidgey = r.get(pokurl14)
pidgey = pidgey.json()
name = pidgey['name']
weight = pidgey['weight']
all_abilities = [v['ability']['name']for v in pidgey['abilities']]
pok_typ = [v['type']['name']for v in pidgey['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')





pokename = pokes['results'][15]['name']
pokurl15 = pokes['results'][15]['url']
pidgeotto = r.get(pokurl15)
pidgeotto = pidgeotto.json()
name = pidgeotto['name']
weight = pidgeotto['weight']
all_abilities = [v['ability']['name']for v in pidgeotto['abilities']]
pok_typ = [v['type']['name']for v in pidgeotto['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')






pokename = pokes['results'][16]['name']
pokurl16 = pokes['results'][16]['url']
pidgeot = r.get(pokurl16)
pidgeot = pidgeot.json()
name = pidgeot['name']
weight = pidgeot['weight']
all_abilities = [v['ability']['name']for v in pidgeot['abilities']]
pok_typ = [v['type']['name']for v in pidgeot['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')







pokename = pokes['results'][17]['name']
pokurl17 = pokes['results'][17]['url']
rattata = r.get(pokurl17)
rattata = rattata.json()
name = rattata['name']
weight = rattata['weight']
all_abilities = [v['ability']['name']for v in rattata['abilities']]
pok_typ = [v['type']['name']for v in rattata['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')






pokename = pokes['results'][18]['name']
pokurl18 = pokes['results'][18]['url']
raticate = r.get(pokurl13)
raticate = raticate.json()
name = raticate['name']
pok_typ = [v['type']['name']for v in raticate['types']]
weight = raticate['weight']
all_abilities = [v['ability']['name']for v in raticate['abilities']]
pok_typ = [v['type']['name']for v in raticate['types']]
print(f'type: {pok_typ}')
print(f'name: {name}')
print(f'weight: {weight}')
print(f'abilities: {all_abilities}')











# types = info_on_poke['types'][0]['type']['name']
# weight = info_on_poke['weight']
# print(weight)

# print('\nworking on functions\n')


def first_step():
    types_1 = r.get('https://pokeapi.co/api/v2/type/')
    types_1 = types_1.json()
    # types_dict = {types_1}
    print(f'these be the yer types: {types_1} .')
    #iterate over the response
    #for each result.name create new entry in dict where name == type
    dict_typ = {}
    types_1 = types_1['results']
    dict_everything = {}
    for typ in types_1:
        # typ = typ['name']
        dict_typ[typ['name']] = {}
    print(dict_typ)
first_step()





# def second_step():
#     pokemon_info = r.get('https://pokeapi.co/api/v2/pokemon/')
#     pokemon_info = pokemon_info.json()

#     print(f'pokes: {pokemon_info} .')
#     #iterate over the response
#     #for each result.name create new entry in dict where name == type
#     dict_poke_info = {}
#     pokemon_info = pokemon_info['results']
#     for nam in pokemon_info:
#         # typ = typ['name']
#         dict_poke_info[nam['name']] = {}
#     print(dict_poke_info)
# second_step()

# # def third_step():
#     # for url in poke_info:
#     #     if url == 'url':
#     # #for every url we need to .json it
#     # # and then go  through and find the info we need and
#     # # then add it as values the main  name list
#     # # #that should then also call a function to determine the type as well
#     # #        

# def ability_extractor():
#     poke_attributes = r.get('https://pokeapi.co/api/v2/pokemon/1/')
#     ability_list = []
#     for data in info_on_poke:
#         if data == 'abilities':
#             for l in all_abilities:
#                 print(f'l: {l}')
#                 return l['ability']['name']
#                 print('\n')
#     return(ability_list)
# abils = ability_extractor()
# print(abils)
   
    