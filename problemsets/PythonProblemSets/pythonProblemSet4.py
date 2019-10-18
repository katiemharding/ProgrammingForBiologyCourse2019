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

#3) coppy issues
print ("  ")
print("3 copy issues")
my_list = ['a', 'bb', 'ccc']
my_list2= my_list
print(my_list, "coppy created using mylist=mylist2")
my_list2.append("something added")
print(my_list2, "appended list")
print(my_list, "origional list, note the addition")
print("another way to coppy")
list_copy2 = my_list.copy()
print(list_copy2, "created using my_list.copy()")
list_copy2.append("different")
print("oritional list", my_list, "real copy", list_copy2)
print(" ")

# 4) while loop
print("While loop")
count = 0
while count<10:
	print("count", count)
	count +=1
print("finished")

# 5) while loop factorial
print("factorial While")
count =1
answer=1
while count<10:
	answer = answer*(count+1)
	count += 1
print(count, answer)

# 6) for loop
print(" ")
print("prob 6 for loop")
randlist = [101,2,15,22,95,33,2,27,72,15,52]
for rand in randlist:
	if rand %2 == 0 :
		print(rand)
print("done")

print("  ")
print("prob 7 for loop sum evens")
sortedrand = sorted(randlist)
sum_ev = 0
sum_odd = 0
for rand in sortedrand:
	print(rand)
	if rand %2 ==0:
		sum_ev +=rand
	else:
		sum_odd +=rand
print("sum even =", sum_ev, "\nsum odd =", sum_odd)

print("prob 8, range 5")
for num in range(5):
	print(num)
print('done')

print("prob 9, range 5")
myrange = [print(ran) for ran in range(5)]
myrange



	
