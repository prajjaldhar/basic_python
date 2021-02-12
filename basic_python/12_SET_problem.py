#same number with two different data types inside set treated as different
sets={18,"18",18.0}
print(sets)


#what will be the length of set
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))