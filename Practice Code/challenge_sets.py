from sets_data import * 


things_that_bite = scorpions.union(spiders)
thingss_that_bite = snakes | spiders | vespas

print(thingss_that_bite)

things_that_sting = vespas.union(snakes)
print(things_that_sting)

things_that_stings = vespas | snakes.union(spiders)
print(things_that_stings)


arachnids = scorpions | spiders
# arachnids = scorpions.union(spiders)
