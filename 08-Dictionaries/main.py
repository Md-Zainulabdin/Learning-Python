# Dictionaries (Objects) in  Python

# my_dict = {"key1": value1, "key2": value2, "key3": value3}

dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

dict['country'] = 'USA'

print(dict['name'])

# get( ) method - returns the value of a specific key. If the key is not found it will return None.

print(dict.get('country'))

# keys()  method - returns a view object that contains all the keys.

print(dict.keys())

# values() method - returns a view object that contains all the values from dictionary.

print(dict.values())

# update() method - updatw an existing Key-Value pair or adding new one to the Dictionary

dict.update( {'salary':'5000'} )  

print( dict )

dict.pop( 'age' )                     # remove the specified key along with its value and return the removed value
# items() Method - Returns a view object that contains tuples of key and value.

print(dict.items())

# remove() method - removes the specified item from the dictionary.

del dict['salary']