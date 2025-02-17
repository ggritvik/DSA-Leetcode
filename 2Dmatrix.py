matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 23

def searchMatrix(matrix, target):
        # find the row or the index of the row where the target is present

        start = 0
        end = len(matrix) - 1

        while start <= end :
            mid  = (start + end) // 2
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif matrix[mid][0] > target:
                end = mid - 1 
            else:
                start = mid + 1
        
        row = (start + end) // 2

        # find the target in the respective row

        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid-1
            else:
                left = mid + 1
        return False

print(searchMatrix(matrix, target))