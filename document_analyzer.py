with open("document.txt", 'r', encoding="utf-8") as f:
    for line in f:
        tokens = line.split()

dict1 = {}
for t in tokens:
    if t.lower() in dict1:
        dict1[t.lower()] = dict1[t.lower()] + 1
    else:
        dict1[t.lower()] = 1
sorted_dict = {k:v for k, v in sorted(dict1.items(), key=lambda item: item[1], reverse=True)}
count = 1
for key, value in sorted_dict.items():
    print(f' {key} : {value}')
    if count == 5:
        break
    count += 1

