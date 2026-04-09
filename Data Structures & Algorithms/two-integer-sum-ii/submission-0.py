class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left = 0
        right = len(numbers) - 1

        while left < right:

            if(numbers[left] + numbers[right]) == target:
                print("=")
                print(left)
                print(right)
                return [left + 1 , right + 1]
            elif (numbers[left] + numbers[right]) > target:
                print("right")
                print(left)
                print(right)
                right -= 1
            else:
                print("left")
                print(left)
                print(right)
                left += 1