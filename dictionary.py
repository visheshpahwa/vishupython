# dictionary is nothing but key value pairs
d1 = { }
d2 = {"vishu" : "burger","mukul" : "chowmein","bhavya" : "french fries" , "mansi": {"b":"maggie", "l":"roti","d":"dal"} }
d2["soumya"]="gol gappe"
d2["vansh"]="momos"
# del d2["vansh"]
d3=d2.copy()
del d3["mansi"]
# print(d3)
d2.update({"charu":"chap"})
#print(d2.values())
#print(d2.keys())


#print(d2.items())

