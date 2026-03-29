class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Luck us it is already sorted
        L = 0
        R = len(numbers)-1
        s = numbers[L] + numbers[R]
        while s != target:
            if s < target:
                L += 1
            if s > target:
                R -= 1
            s = numbers[L] + numbers[R]

        return [L+1,R+1]
