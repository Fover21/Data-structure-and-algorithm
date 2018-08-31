#方式一
l1 = [1, 2, 333, 7, 1, 8, 19, 1, 2, 333]
res = list(set(l1))
res.sort(key=l1.index)
print(res)


#方式2
l1 = [1, 2, 333, 7, 1, 8, 19, 1, 2, 333]
res = []
for i in l1:
    if i not in res:
        res.append(i)
print(res)

#方式三
 l1 = [1, 2, 333, 7, 1, 8, 19, 1, 2, 333]
 s = set(l1)
 res = []
 for i in l1:
     if i in s:
         res.append(i)
         s.remove(i)
 print(res)






