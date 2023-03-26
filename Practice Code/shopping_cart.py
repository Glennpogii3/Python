from data_set import data #Import data from Data set

UNITS_LIST_INDEX = 3 
UNIT_PARTS_INDEX = 1

parts_list_selected = []
# for i in range(data): 
#     pass
while True: 
    print("Please choose your parts (invalid choice exits):")
    for index, (parts, brands, year, units) in enumerate(data):
        print("{}: {}".format(index + 1, parts))
    choice = int(input())
    
    if 1 <= choice <= len(data):
        units_list = data[choice -1][UNITS_LIST_INDEX]
    else:
        break
    
    print("Please choose your unit (invalid choice exits):")
    for index, (track_number, unit, price ) in enumerate(units_list):
        print("{}: {} P.{}".format(index + 1, unit, price))
  
    unit_choice = int(input())
    
    if 1 <= unit_choice <= len(units_list): 
        parts = units_list[unit_choice - 1][UNIT_PARTS_INDEX]
        print("Playing {}".format(parts))
    
    print("="*30)        
