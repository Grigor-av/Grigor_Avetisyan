def function(lst):
    l = []
    for i in lst:
        if i % 2 == 0:
            l.append(i)
    return l
lst1 = [1,2,3,4]
print(function(lst1))