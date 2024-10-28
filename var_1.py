import pandas as pd
import random
              
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
ohe_simulation = []
for i in range(0, len(data)):
    check = data.iloc[i].to_string(header=False, index=False) 
    if check == 'human':
        temp = [1,0]
    else:
        temp = [0,1]
    ohe_simulation.append(temp)
df = pd.DataFrame(ohe_simulation, columns = ['human', 'robot'])
print (data)
print(df)