import string


with open("document.txt", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.translate(line.maketrans("","",string.punctuation))
        tokens = line.split()
    

dict1 = {}
for t in tokens:
    if t in dict1:
        dict1[t] = dict1[t] + 1
    else:
        dict1[t] = 1

sorted_dict = sorted(dict1.items(), key=lambda x: (-x[1], x[0]))
final_sorted_dict =list(sorted_dict)[:5]

print()
for j in final_sorted_dict :
    print(j[0], ": ", j[1])
   
