import json


# make a dictionary
person_dict = {'name': 'Josh',
        'age': 32,
        'hobbies': ['fishin', 'games', 'chess']
        }

# add items to dictionary
person_dict.update({'address': 'irvine'})
person_dict['name'] = 'Fred'
person_dict['favorite foods'] = ['pizza', 'icecream', 'cheese']


# write dictionary to json file
with open('stuff.json', 'w') as json_file:
    json.dump(person_dict, json_file)


# pretty print json data
print(json.dumps(person_dict, indent=4, sort_keys=True))



# iterate over written json file and print data...
with open ('stuff.json', 'r') as myfile:
    data = json.load(myfile)

print(data)




