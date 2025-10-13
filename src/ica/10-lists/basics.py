def every_other(list1):
    list2=[]
    for x in range(0, len(list1),2 ):
        list2.append(list1[x])
    return list2
print(every_other([1,2,3,4,5,6]))

def sum_positive(list1):
    total =0
    for x in list1:
        if x>0:
            total += x
    return total
print(sum_positive([-1,2,-5,4,5,6]))

