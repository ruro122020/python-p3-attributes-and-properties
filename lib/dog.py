#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

    def get_name(self):
        print('Get Name')
        return self._name
    
    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            print('Set Name')
            self._name = name
        else:
             print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        print('Get Breed')
        return self._breed
    
    def set_breed(self, breed):
        if APPROVED_BREEDS.count(breed) == 0:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
   




