def newadd(*num):
    lastnum=0
    for data in num:
        lastnum+=data
    print(lastnum)

newadd(1)
newadd(1,2)
newadd(1,2,3)