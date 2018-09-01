dict_1 = {"kartik":"chauhan",
          "saloni":"taneja"}

dict_2 = {"Kalpana":"Sharma",
          "kartik":"Sharma"}

key_1 = set(dict_1.keys())
key_2 = set(dict_2.keys())

print(key_1 & key_2)