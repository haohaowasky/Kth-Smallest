import heapq
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        queue= [(matrix[0][0], 0, 0)]
        m= len(matrix)
        n= len(matrix[0])
        check= [[False]* n for _ in range(m)]
        check[0][0]= True
        result= None
        for _ in range(k):
            result, i, j= heapq.heappop(queue)
            if i+ 1 < m and not check[i+1][j]:
                check[i+1][j]= True
                heapq.heappush(queue, (matrix[i+1][j],i+1,j))
            if j+ 1 < n and not check[i][j+1]:
                check[i][j+1]= True
                heapq.heappush(queue, (matrix[i][j+1],i,j+1))
        
        return result 
