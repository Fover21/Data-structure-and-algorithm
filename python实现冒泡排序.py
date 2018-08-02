l = [1, 4, 5, 2, 9, 7, 3]
for i in range(len(l)-1):
    for j in range(len(l)-1-i): #我们每循环一次都会将最大的数推到最右边，所以需要将最右边排好的数拿走
        if l[j] > l[j+1]:#前一个数与后一个数依次比较，直到将最大的数推到右边
            l[j], l[j+1] = l[j+1], l[j]
    #print(l)
print(l)