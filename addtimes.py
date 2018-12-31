import sys


def addtime(thistotal, thisin):
    # time string should be checked
    
    # split and set up time lists
    totnums = thistotal.split(":")
    innums = thisin.split(":")
    
    # print(totnums, innums)
    # print(totnums[-1], innums[-1])
    # print(totnums[-2], innums[-2])
    
    if len(totnums) != len(innums):
        if len(totnums) < len(innums):
            totnums.insert(0, "00")
        else:
            innums.insert(0, "00")
        # print(totnums[-3], innums[-3])
        
    for i in range(0, (-1 * len(innums)), -1):
        slicetotal = int(totnums[i - 1]) + int(innums[i - 1]) 
        
        if (slicetotal > 60) and ((i - 1) != -3):
            slicetotal = slicetotal % 60
            totnums[i - 2] = int(totnums[i - 2]) + (slicetotal // 60) + 1
        
        totnums[i - 1] = str(slicetotal).zfill(2)
    
    newtotal = ":".join(totnums)

    return newtotal


myin = "x"
total = "00:00:00"

while myin != "0":
    mystr = "Enter HH:MM:SS or MM:SS; 0 to end: "

    if sys.version_info[0] >= 3:
        myin = input(mystr)
    else:
        myin = raw_input(mystr)

    if myin != "0":
        # total = 
        total = addtime(total, myin)
        print(total)
