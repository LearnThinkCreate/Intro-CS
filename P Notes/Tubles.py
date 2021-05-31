def intersect(t1 , t2): 
    result = ()   
    for e in t1:
        if e in t1:
            result += (e,)
    return result

tub1 = (1 ,"two" , 3)
tub2 = (tub1 , 3.25)

print(intersect(tub1, tub2))
print(tub1)
print(tub2)