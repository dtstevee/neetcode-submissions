class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] < target:
                continue
            elif i[-1] > target:
                temp_array = i
                while temp_array:
                    if temp_array[-1] != target:
                        temp_array.pop()
                    else:
                        return True
            else:
                return True
        return False