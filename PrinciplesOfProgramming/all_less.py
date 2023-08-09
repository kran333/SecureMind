def all_less(list1, list2):
    if len(list1) != len(list2):
        return False
    opt = True
    for x in range(len(list1)):
        if list1[x] > list2[x]:
            opt = False
    return opt

a, b = [51, 20, 700] , [50, 41, 600],

print(all_less(a,b))