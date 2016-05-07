import lexicon
import entities

words_to_strip = lexicon.tokens['filler']
verbs = lexicon.tokens['verbs']
nouns = lexicon.tokens['nouns']
direction = lexicon.tokens['directions']
synonyms = lexicon.synonyms

for mob in entities.Mob.index:
    if mob.name not in nouns:
        nouns.append(mob.name.upper())


print(nouns)
# print(words_to_strip)

def parse_input(input):
    output_dictionary = {}
    input = input.split()
    input = [token.upper() for token in input]
    for token in input:
        if token in words_to_strip:
            input.remove(token)
        if token in synonyms:
            token = synonyms[token]
        if token in verbs:
            output_dictionary['verb'] = token
        if token in nouns:
            output_dictionary['noun'] = token
        if token in direction:
            output_dictionary['direction'] = token
            
    return output_dictionary, input

while 1:
    query = input('> ')
    print(parse_input(query))
