# %%
import pandas as pd

# Location of csv file
csvFile = (r'D:\WorkDev\python-jupyter\csvFile\File\csvTest.csv')

# Read using pandas
myData = pd.read_csv(csvFile)
data1 = myData['2'].tolist()
data2 = myData['1'].tolist()

out = []

# loop for search equal values in coloumn
for val1 in data1:
    for val2 in data2:
        if(val1 == val2):
            out.append(val1)

print("Equal values are:",out)

# %%



