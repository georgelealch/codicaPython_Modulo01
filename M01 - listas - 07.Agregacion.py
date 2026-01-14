def calculate_sum(coll):
    if coll == []:
        return 0

    sum = 0
    num = 0

    for i in range(len(coll)):
        num = coll[i] / 3
        if num == int(num):
            sum += coll[i]
        else:
            sum += 0
    
    return sum
    

coll = [2, 0, 17, 3, 9, 15, 4]
print(calculate_sum(coll))