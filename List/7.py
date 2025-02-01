arr = [7] * 3
print(arr)

barr = []
for i in range(3):
    barr.append(7)
print(barr)

list_1 = [1,2,[3,4,"Able"]]
for i in range(len(list_1)):
    if isinstance(list_1[i], list):
        for j in range(len(list_1[i])):
            if list_1[i][j] == "Able":
                list_1[i][j] = "Academy"
print(list_1)

list_2 = [5,3,4,6,1]
list_2.sort()
print(list_2)

d = {'simple_key':'Able'}
print(d['simple_key'])

d1 = {'k1':{'k2':'Able'}}
print(d1['k1']['k2'])

d2 = {'k1':[{'k2':['k3',['Able']]}]}
t1 = d2['k1'][0]['k2'][1][0]
print(t1)

d3 = {'k1':[1,2,{'k2':['k3',{'k4':[1,2,['Able']]}]}]}
print(
    d3['k1'][2]['k2'][1]['k4'][2][0]
)