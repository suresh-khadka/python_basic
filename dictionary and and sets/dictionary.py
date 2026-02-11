d={}   #empty dictionary
marks={      #dictionary
    "a":21,
    "b":34,
    "list":["syresh",21,"loves","very much"],
    0: 21
}
print(type(marks))  #print type of marks i.e. dict
print(marks)   
print(marks["list"])   #print list key
print(marks[0])   #pront marks with zero key
print(marks.items())  #print all items
print(marks.keys())   #print keys
marks.update({"a":29,"harry":99})   #add and update dict
marks.update({"harry":98})      #oly update hary"s marks
marks.update({"inesh":"topper"})  #only add to dict
print(marks) #mutable, indexed,and unordered..........
#.........contd ............cant contain duplicate keys
print(marks.get("suresh"))  #no key named suresh..
print(marks.get("harry")) #get fun gets the values of keys,..
print(len(marks))     #to find the length oh dict