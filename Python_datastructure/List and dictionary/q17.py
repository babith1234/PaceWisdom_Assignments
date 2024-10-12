d1,d2={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
if len(d1)>len(d2):
    for i in d1:
        if i in d2:
            if d1[i]==d2[i]:
                print(i,":",d1[i])
else:
    for i in d2:
        if i in d1:
            if d1[i]==d2[i]:
                print(i,":",d1[i])