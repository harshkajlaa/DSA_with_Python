class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        matrix1=[]
        n=len(matrix)
        c=len(matrix[0])
        count=0
        total=n*c

        rowstart=0
        colstart=0
        rowend=n-1
        colend=c-1

        while count<total:
            for i in range(colstart,colend+1):
                matrix1.append(matrix[rowstart][i])
                count+=1
            rowstart+=1

            if count==total:
                break


            for i in range(rowstart,rowend+1):
                matrix1.append(matrix[i][colend])
                count+=1
            colend-=1

            if count==total:
                break


            for i in range(colend,colstart-1,-1):
                matrix1.append(matrix[rowend][i])
                count+=1
            rowend-=1

            if count==total:
                break


            for i in range(rowend,rowstart-1,-1):
                matrix1.append(matrix[i][colstart])
                count+=1
            colstart+=1

            if count==total:
                break

        return matrix1