array = [[1,2,3],
         [4,5,6],
         [7,8,9]]


if __name__ == '__main__':

    n=len(array)
    list=[]
    for i in range (0,n):
        for j in range (0,n):
            list.append(array[i][j])
            for k in range (n,0):
                list.append(array[k][j])
    print(list)