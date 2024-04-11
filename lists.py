# LISTS
#lists are dennted using the []

fruits = ["mango","apple","orange","banana","grapes"]
for i in fruits:
    print(i)

# list with integer values

list = [54,45,34,3,56,76,86,865,34,6557,973]
# we can create a number list without the double inverted commas also like  list[2,4,5,6,7,6]
print(list[3])
print(list[-4])
print(list[3:7])
list.append(999)
print(list.count("34"))
print(list)
list.reverse()
print(list)
list.insert(3,786)
list.sort()
print(list)
print(list.index(34))
list3 = list.copy()
print(list3)
list.remove(54)
list.pop()  #removes the last element in the list
# list.clear()

list2 =[1,3,4,5,6]
list.extend (list2)
print(list2)
