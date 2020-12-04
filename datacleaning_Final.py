import pandas as pd 
import csv
import os

#First lets find the maximum column for all the rows
with open("2020-11-13-15-33-10/_slash_detection_slash_vision_objects_slash_front.csv", 'r') as temp_f:
    # get No of columns in each line
    col_count = [ len(l.split(",")) for l in temp_f.readlines() ]

### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
column_names = [i for i in range(max(col_count))] 

import pandas as pd
# inside range set the maximum value you can see in "Expected 4 fields in line 2, saw 8"
# here will be 8 
data = pd.read_csv("2020-11-13-15-33-10/_slash_detection_slash_vision_objects_slash_front.csv",header = None,names=column_names )
data.to_csv("_slash_detection_slash_vision_objects_slash_front.csv", index=False)

f = pd.read_csv("_slash_detection_slash_vision_objects_slash_front.csv", usecols=[0,15,90,91,92,93,95,118,193,194,195,196,198,221,296,297,298,299,301,324,399,400,401,402,404,427,502,503,504,505,507])

f.to_csv("cleaned.csv", index=False)

f["15"] = f["15"].map({'"RedLeft"':0,'"Red"':1,'"RedRight"':2,'"GreenLeft"':3,'"Green"':4,'"GreenRight"':5,'"Yellow"':6,'"Off"':'7','"YellowRight"':8})
f["118"] = f["118"].map({'"RedLeft"':0,'"Red"':1,'"RedRight"':2,'"GreenLeft"':3,'"Green"':4,'"GreenRight"':5,'"Yellow"':6,'"Off"':'7','"YellowRight"':8})
f["221"] = f["221"].map({'"RedLeft"':0,'"Red"':1,'"RedRight"':2,'"GreenLeft"':3,'"Green"':4,'"GreenRight"':5,'"Yellow"':6,'"Off"':'7','"YellowRight"':8})
f["324"] = f["324"].map({'"RedLeft"':0,'"Red"':1,'"RedRight"':2,'"GreenLeft"':3,'"Green"':4,'"GreenRight"':5,'"Yellow"':6,'"Off"':'7','"YellowRight"':8})
f["427"] = f["427"].map({'"RedLeft"':0,'"Red"':1,'"RedRight"':2,'"GreenLeft"':3,'"Green"':4,'"GreenRight"':5,'"Yellow"':6,'"Off"':'7','"YellowRight"':8})
f["0"] = "x"
f.to_csv("cleaned.csv", index=False)

with open("cleaned.csv",'r') as f:
    with open("updated_cleaned.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)


try:
    if not os.path.exists('txt'):
        os.makedirs('txt')
except OSError:
    print ('Error: Creating directory of data')


with open("updated_cleaned.csv", "r", ) as f:
    reader = csv.reader(f)

    rownumber = 0
    for row in reader:
        g=open('txt'+ '/'+str(rownumber-1)+".txt","w")
        for i in row:
            if(i == 'x'):
                g.write('')
            elif(i!=''):
                g.write(i + ' ')
            else:
                g.write('\n')
        rownumber = rownumber + 1
        g.close()
        
os.remove("txt/-1.txt")


