# __author: ward
# data: 2018/12/17


def find_min(li):
    min_val = li[0]
    for i in range(1, len(li)):
        if li[i] < min_val:
            min_val = li[i]
    return min_val


def find_min_pos(li):
    min_pos = 0
    for i in range(1, len(li)):
        if li[i] < li[min_pos]:
            min_pos = i
    return min_pos


def select_sort(li):
    for i in range(len(li) - 1):
        # 无序区的范围i, n-1
        min_pos = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]
        print(li)


li = [1, 4, 5, 7, 9, 1, 2]
select_sort(li)
