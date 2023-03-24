# %%
import platform

x = platform.system()
print(x)

# %%
import datetime

x = datetime.datetime.now()
print(x)
print(x.strftime("%A"))

# %%
import math

x = math.ceil(1.4)
y = math.floor(1.4)
z = math.pi

print(x) # returns 2
print(y) # returns 1
print(z)

# %%
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# convert into JSON:
print(json.dumps({"name": "John", "age": 30}))

# %%



