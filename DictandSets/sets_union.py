from prescription_data import *
# farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
# wild_animals = {'lion', 'elephant', 'horse', 'goat', 'gorilla'}



# all_1_animals = farm_animals.union(wild_animals)
# print(all_1_animals)

# all_2_animals = wild_animals.union(farm_animals)
# print(all_2_animals)

# all_animals = wild_animals | farm_animals
# print(all_animals)

meds_to_watch = set()

# for interaction in adverse_interactions: 
#     # meds_to_watch = meds_to_watch | interaction 
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch.update(interaction)
#     meds_to_watch | interaction
    
# print(sorted(meds_to_watch))

meds_to_watch.update(*adverse_interactions)

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep="\n")



