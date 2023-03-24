# %%
lst = [10,30,40,70,80]
    
print("-",(10*3) in lst)
print("=",lst[-1]+lst[1])

print("length", len(lst))
print("max", max(lst))

# push
lst.append(5)
print(lst)

# %%
lst = [10,30,40,70,80]

lst.append(100)
print(lst)

lst.insert(1,110)
print(lst)

lst1 = [5,15,25,35]
lst.extend(lst1)
print(lst)

lst.remove(40)
print(lst)

element = lst.pop(0)
print(element)
print(lst)

# %%
lst2 = [1,2,3,5,4,2]

lst2.sort()
print(lst2)

lst2.sort(reverse=True)
print(lst2)

# %%
lst_3 = [10,20,30,40,50,60,70]

# lst_3[2] = "a"
# print(lst_3)

lst_3[2:4] = ["a","b"]
print(lst_3)

# %%
tup = (10,20,30,50)
# print(len(tup))

for i in range(len(tup)):
    print(tup[i])

# %%



