#indexed
#mutubale
#unordered
#must have unique keys
mydict={
    "fast":"car",
    "mahatma":"Gandhi",
    "knowledge":"vivekenand",
    "pacer":"cheeta",
    "captain":"prajjal",
    "honest":"harsihchandra",
    "marks":[1,3,5],
     "anotherdict":{"brothers":"Prajjal,Abhra,Shubra"},
     "anothertuple":(1,2,3)
}
print(mydict)
print(mydict["honest"])
print(mydict["anotherdict"]["brothers"])
print(mydict.values())
print(mydict["anotherdict"].values())#printing values of dict inside dict
print(mydict["anothertuple"][0])#printing value of tuple inside dict using indexing
print(mydict.keys())
print(mydict.items())#prints key value pair in tuple format
update_dict={
    "Friends_list":["abhitesh","raj","terminal-xd"],
    "Enemy_list":["thanos","gogo"]
}
mydict.update(update_dict)
print(mydict)
print(mydict.get("prajjal",-1))#.get method never throughs an error,if key is not present-->dict.get("value",default_value)
#print(mydict["prajjal"])#returns keyerror
