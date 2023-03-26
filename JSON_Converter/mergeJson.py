list1 = [
    {
        "id": 1,
        "a":"qwert",
        "b":"asdfg",
        "c":"zxcv"
    },
    {
        "id": 2,
        "a":"qqqq",
        "b":"eeee",
        "c":"zzzz"
    },
    {
        "id": 2,
        "d":"qqqq",
        "e":"eeee",
    },
    {
        "id": 4,
        "a":"qwert",
        "b":"asdfg",
        "c":"zxcv"
    }
]

list2 = []

for val1 in list1:
    flag = True

    # if len(list2) == 0:
    #     list2.append(val1)
    #     flag = False
    # else:
    for i, val2 in enumerate(list2):
        # if old value update
        if val2["id"] == val1["id"]:
            list2[i].update(val1)
            flag = False

    # if new value append
    if flag:
        list2.append(val1)
    

print("-=", list2)