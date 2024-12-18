from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # [00],  [01],[02]     ,[12],[22]     ,[21],[20]      ,[10],[00]
    # i=j=0   j+1  j+2(j=n)  i+1  i+1(i=n)  j-1  j-1(j=0)  i-1  i=0 X
    #
    # For each layer do:
    #     top side
    #     j++
    #     right side
    #     i++
    #     bottom
    #     j--
    #     left
    #     i--
    #
    # layer = 2
    # i,j= 0
    [print (" ".join(map(str,row))) for row in square_matrix]
    result =[]
    n=len(square_matrix)
    no_of_layers = n//2 if n%2 ==0 else n//2+1 
    for l in range(no_of_layers):
        if l ==  len(square_matrix)-l -1:
            result.append(square_matrix[l][l])
        else:
            i =j =l
            for j in range(l,n-1-l):
                result.append(square_matrix[i][j])
            j +=1
            for i in range(l,n-1-l):
                #1,1
                result.append(square_matrix[i][j])
            #1,0 = 1
            i +=1
            for j in range(n-1-l,l,-1):
                #0
                result.append(square_matrix[i][j])
            j -=1
            for i in range(n-1-l,l,-1):
                result.append(square_matrix[i][j])

    return result

# def visit(row_index: int, column_index: int):
#     result.append(kkj)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
