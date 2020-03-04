import pprint
message = 'dhuasibijsdbjionvioavbijfaosvbih'
character = {}
for ch in message:
    character.setdefault(ch, 0)
    character[ch] = character[ch] + 1
pprint.pprint(character)