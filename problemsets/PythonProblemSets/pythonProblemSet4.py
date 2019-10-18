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


