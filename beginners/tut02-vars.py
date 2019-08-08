#!/usr/bin/env python3
var_str = "Mt"
var_int = 12
var_bool = True
var_float = 56.898
var_tuple = (212, 200, 4999, "hhhh")
var_list = ["Hello","MT","Pol","Warsaw",200]
print (var_str)
print (var_tuple)
print (var_list)
print (var_list[2])
print (var_tuple[1])
var_list2 = list()
var_list2.append("hello")
var_list2.append("world")
var_list2.append("Pol")
var_list2.append(2019)
var_list2[2] = var_list2[2] + "Warsaw"
var_list2[2] += "Konstruktorska7"
var_list2.remove("hello")
print (var_list2)
print (var_list2[1])
var_list2.remove(var_list2[1])
print (var_list2)
# in the tuple type you cant change at all you can only view its contnent
# this cant be done ------>>>>>>   var_tuple[2] += 1000
print var_tuple[2]
# lets talk now about the directory vars
var_dir = {
    "Key1": 2019,
    "Key2": "Pol",
    "Key3": "Warsaw",
    "Key4": "MT"
}
print (var_dir.get("Key1"))
print (var_dir["Key2"] +" "+ var_dir["Key3"])
