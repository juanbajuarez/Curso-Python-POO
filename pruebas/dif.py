def move_zeros(lst):
    cont=0
    for car in lst:
        if car==0:
            lst.remove(car)
            cont+=1
    for i in range(1,cont):
        lst.append(0)
    return lst

if __name__ == '__main__':
    print(move_zeros( [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))