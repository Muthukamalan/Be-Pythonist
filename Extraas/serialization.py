# Serialization
# It is the process of converting an object or data structure into a sequence of bytes or a stream of data, so that it can be stored or transmitted as a file or over a network. This process allows an object or data structure to be reconstructed from the serialized data at a later time.


# https://www.youtube.com/watch?v=uS37TujnLRw&list=WL&index=24&pp=gAQBiAQB
# why pickle? python natively supports all type in pickle

import pickle
import  toml
import json 

#Here's an example dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 ,'fruits':
          [
              {'fruit1':{'name':'apple','color':'red'}},          # 🍎
              {'fruit2':{    'name':'watermelon','size':'big','color':'lightgreenish'}} # 🍉
          ]
    }

#Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps( grades )

#Use loads to de-serialize an object
received_grades = pickle.loads( serial_grades )

print(serial_grades)
print(received_grades)


with open("assets/data.toml", "w") as f:
    # Serialize the data to TOML format
    toml.dump(grades, f)

with open("assets/data.json", "w") as f:
    # Serialize the data to TOML format
    json.dump(grades, f)