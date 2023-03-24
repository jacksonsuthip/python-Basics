# %%
d = {
    "name":"anto",
    "sName":"jackson",
    1997:"year"
}
for i in d:
    print("loop---",i,d[i])

d["ajs"] = "suthip"
print("add---",d)

# del d[1997]
element = d.pop(1997)
print(element)
print(d)

e = {
    "a" : "aaa",
    "b" : "bbb"
}
d.update(e)
print("update---",d)



# %%
dist = {1:"one",2:"two"}
lst = list(dist.values())
print(lst)

# %%



