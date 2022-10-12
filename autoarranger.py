import numpy as np
import pandas as pd
import openpyxl as pp
lec = pd.DataFrame(columns = ['name','age','roll'])
d = input("Enter day:")
x = int(input("Starting period:"))
y = int(input("Ending period:"))
for i in range(0,n):
  table = df.iloc[7*i+0:7*i+6]
  table.index = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
  table.columns = [1,2,3,4,5,6,7]
  particulars = df.iloc[7*i+6:7*i+7,0:3]
  particulars.index = ['PARTICULARS']
  particulars.columns = ['name','age','roll']
  j = x
  c = 0
  while(j<=y):
    if ((table[j][d.upper()]) == 1):
      print(particulars.iloc[0,0],"is not free")
      break
    else:
      j += 1
      c += 1
  if(c == (y-x+1)):
    print(particulars.iloc[0,0],"is free")
    lec = lec.append({'name':particulars.iloc[0,0]
                      ,'age':particulars.iloc[0,1]
                      ,'roll':particulars.iloc[0,2]}
                      ,ignore_index=True)
new_lec = lec.sort_values('age')
new_lec.to_excel("arranged.xlsx",index=False)
