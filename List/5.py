arr2 = [100,"Brad",-10,1,10.4,True,[123,21,51],3,4,[1,3,-10],70,24,-9, "Hello", "How"]
only_ints = []
list_of_strings = []
float_nums = []
array_of_bools = []
list_of_lists = []
for elem in arr2:
    if isinstance(elem, str):
        list_of_strings.append(elem)
    elif isinstance(elem, float):
        float_nums.append(elem)
    elif isinstance(elem, bool):
        array_of_bools.append(elem)
    elif isinstance(elem, int):
        only_ints.append(elem)
    elif isinstance(elem, list):
        list_of_lists.append(elem)
print(arr2)
print(only_ints)
print(list_of_strings)
print(float_nums)
print(array_of_bools)
print(list_of_lists)

only_ints.sort()
print(only_ints)
list_1d = []
list_2d = []
for arr1 in list_of_lists:
    for el in arr1:
        list_1d.append(el)
print(list_1d)
for i in range(0, len(list_1d) - 1, 2):
    temp = []
    temp.append(list_1d[i])
    temp.append(list_1d[i + 1])
    list_2d.append(temp)
print(list_2d)

list_1st = []
for i in list_of_lists:
    list_1st.append(i[0])
print(list_1st)

list_2nd = []
for i in list_of_lists:
    list_2nd.append(i[1])
print(list_2nd)

list_3rd = []
for i in list_of_lists:
    list_3rd.append(i[2])
print(list_3rd)

for i in range(len(list_of_lists) + 1):
    for j in range(2):
        print(list_of_lists[j][i], )
    print()
