# import json
# from urllib.request import urlopen


# f = open('data.json')
# # json.load loads the file
# data = json.load(f)

# # json_string = '''
#     # {
#     #     "people" :[
#     #         {
#     #             "name":"ellai dhurai",
#     #             "phone":"9987433443",
#     #             "emails":["e@gmail.com","m@gmail.com"],
#     #             "has_license": false
#     #         },
#     #         {
#     #             "name":"ellai dhurai",
#     #             "phone":"9987433443",
#     #             "emails":null,
#     #             "has_license": true
#     #         }
#     #     ]
#     # }

# # '''

# # # json.loads loads string representation of json object
# # # people_data = json.loads(json_string)

# # # access all objects in json key
# # for person in data['people']:
# #     print(person)

# # # access particular value in objects  
# # for person in data['people']:
# #     print(person['name'],person['emails'])
    
# # for person in data['people']:
# #     del person['phone']
    
# # The json.dumps() method allows us to convert a python object into an equivalent JSON object.
# # The dump() method is used when the Python objects have to be stored in a file.

# # dump/store new data to old file or old data to new file
# # new_string = json.dumps(data, indent=2, sort_keys=True)
# # with open('new_data.json', 'w') as f:
# #     json.dump(data, f, indent=2)
    

# with urlopen("https://randomuser.me/api/") as response:
#     source = response.read().decode('utf8')
    
# data = json.loads(source)
# with open('new_data.json', 'w') as f:
#     json.dump(data, f, indent=2)
    
# file = open('new_data.json')
# list = json.load(file)

# city = {}

# for results in list['results']:
#     # accessing json object
#     name = results['location']['street']['name']
#     number = results['location']['street']['number']
#     print(name,number)
    
#     city[name] = number

# # print(city['chennai']) this will return the city code