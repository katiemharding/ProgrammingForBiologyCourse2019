#!/usr/bin/env python3

# 1) for loops

# my favorites list :
myfav  =  ["chocolet", "border collies", "swimming", "douglas fir", "blue"]
middle = myfav[round(len(myfav)/2)]
print("My Faves: ", myfav)
print("Middle Fav ",middle)
myfav[round(len(myfav)/2)] = "Don't Worry, Be Happy"
print("My Faves: ", myfav)
myfav.append("ocean")
print("My Faves: ", myfav)
myfav.insert(0,"data")
print("My Faves: ", myfav)
myfav.insert(4, "geek")
print("My Faves: ", myfav)
print("Last element", myfav.pop())
print("My Faves after pop: ", myfav)
print("first element", myfav.pop(0))
print("My Faves after pop: ", myfav)

joined = ",".join(myfav)
print(joined,"this is really odd", sep= ", comment:")

# 2) strings to list
print("problem two, strings to list")
taxa = 'sapiens, erectus, neanderthalensis'
print(taxa)
print(taxa[0], "the first letter")

type(taxa)
print(type(taxa), "its a string, I did it right")
species = taxa.split(', ')
print(species, "species list")
print(species[1], "the first species")
print(type(species), "I did it right again")
species_sort = sorted(species)
print(species_sort, "Sorted species")
species_bylen = sorted(species, key = len)
print(species_bylen, "sorted by number of characters")





