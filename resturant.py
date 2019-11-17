import sys
import re
import os.path

dataFile = 'data.csv'
items = ['burger', 'coke']

## checking file existance
if not os.path.isfile(dataFile):
    print("ERROR: Please provide a valid data file")
    exit()

parsed_data = dict()

fr = open(dataFile, "r")
header = fr.readline()

# read each lines
for line in fr.readlines():
    valid_entry = re.match(r'^\s*(\d+)\s*,\s*(\d+\.\d+)\s*,\s*(.+)$', line)
    # skip invalid data
    if not valid_entry:
        continue

    # keep items in a list
    items_list = re.split(r'\s*,\s*', valid_entry.group(3))
    # fetch restraunt id & item price
    restr_id = valid_entry.group(1)
    item_price = valid_entry.group(2)

    # if not parsed_data.has_key(restr_id):
    if restr_id not in parsed_data:
        parsed_data[restr_id] = {}

    # prepare data for easy processing
    # restraunt_id -> item_label -> price
    for item in items_list:
        parsed_data[restr_id][item.strip()] = item_price
fr.close()

print("\n\n");

# print(parsed_data)
# exit()

price_dict = {}
for restraunt in parsed_data:
    # print(restraunt)
    # check if all the items are available in restraunt
    if set(items).issubset(set(parsed_data[restraunt].keys())):
        price_dict[restraunt] = 0

        # calculate amount for our items
        for item in items:
            price_dict[restraunt] += float(parsed_data[restraunt][item])

# print(price_dict)

if len(price_dict) == 0:
    print("nill")
else:
    # to check if multiple restraunts providing lowest cost
    lowest = sorted(price_dict.values())[0]
    # get the lowest priced restraunt first, acending order
    for key, value in sorted(price_dict.items(), key=lambda item: (item[1], item[0])):
        # print(key, value)
        # break once all lowest priced restraunts processing is done
        if lowest != value:
            break
        else:
            print("Restraunt ID ", key, "Price - ", value)
            lowest = value

