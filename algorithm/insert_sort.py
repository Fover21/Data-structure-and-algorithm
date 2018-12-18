# __author: ward
# data: 2018/12/17


def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)


li = [3, 2, 9, 0, 0, 2, 4, 1, 2]
insert_sort(li)
