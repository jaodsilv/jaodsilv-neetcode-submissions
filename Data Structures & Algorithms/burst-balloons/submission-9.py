import heapq

# class Balloon:
#     def __init__(self, index, val, left):
#         self.index = index
#         self.val = val
#         if left:
#             left.right = self
#         self.left = left
#         self.right = None

#     def pop(self):
#         if self.left:
#             self.left.right = self.right
#         if self.right:
#             self.right.left = self.left
#         return self.coins
    
#     def unpop(self):
#         if self.left:
#             self.left.right = self
#         if self.right:
#             self.right.left = self

#     @property
#     def coins(self):
#         coins = self.val
#         if self.left:
#             coins *= self.left
#         if self.right:
#             coins *= self.right
#         return coins

#     def __repr__(self) -> str:
#         return self.__str__()

#     def __str__(self) -> str:
#         return str(self.val)

# class Balloons:
#     def __init__(self):
#         self.__head = None
#         self.__nodes = []
#         self.__length = 0
#         self.__tail = None
#         self.__popped = 0
#         self.__masks = []
#         self.__clean_key = 0
#         self.heap = []

#     def __repr__(self):
#         return self.__str__()

#     def __str__(self):
#         head = self.__head
#         out = ''
#         while head:
#             out = out + str(head) + ','
#             head = head.right
#         return f'{self.key}: [{out.strip(",")}]'

#     def append_balloon(self, num: int) -> None:
#         balloon = Balloon(self.__length, num, left=self.__tail)
#         self.__nodes.append(balloon)
#         self.__tail = balloon
#         self.__length += 1
#         if len(self.__nodes) == 1:
#             self.__head = balloon
#             self.__masks.append(1)
#             self.__clean_key = 1
#         else:
#             self.__masks.append(self.__masks[-1] << 1)
#             self.__clean_key <<= 1
#             self.__clean_key += 1

#     def pop_next(self):
#         minimum = 

#     def reverse_masks(self):
#         ones = self.clean_key
#         f = '0' + str(len(self.__masks)) + 'b'
#         return [format(mask^ones, f) for mask in self.__masks]

#     def pop_balloon(self, i: int) -> int:
#         balloon = self.__nodes[i]
#         coins = balloon.pop()

#         if balloon.left is None:
#             self.__head = balloon.right
#         if balloon.right is None:
#             self.__tail = balloon.left

#         self.__popped ^= self.__masks[i]
#         self.__length -= 1
#         return coins

#     def unpop_balloon(self, i: int) -> None:
#         balloon = self.__nodes[i]
#         balloon.unpop()
#         if balloon.left is None:
#             self.__head = balloon
#         if balloon.right is None:
#             self.__tail = balloon

#         self.__popped ^= self.__masks[i]
#         self.__length += 1
            
#     @property
#     def key(self) -> str:
#         return format(self.__popped, '0' + str(len(self.__masks)) + 'b')

#     def __hash__(self) -> int:
#         return self.key.__hash__()

#     def empty(self):
#         return self.__length == 0

#     @property
#     def length(self):
#         return self.__length

#     @property
#     def head(self):
#         return self.__head

#     @property
#     def clean_key(self):
#         return self.__clean_key

#     @property
#     def masks(self):
#         return self.__masks

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # The best strategy here is to burst them in ascending order,
        # so the bigger numbers multiply together
        # For that we can use a min-heap mapping the num[i] to i
        # balloons = Balloons()

        # since len(nums) <= 300 then each bitwise operations will take up to:
        # - ceil(300/64) = O(5) in a 64bit machine
        # - ceil(300/32) = O(10) in a 32bit machine
        # when we set a fixed size int, e.g., 32bit integer

        # Trim 0's
        # len(nums) >= 2
        # for v in nums:
        #     # Skip 0's, those should ALWAYS be the first to be popped
        #     if v == 0:
        #         continue

        #     balloons.append_balloon(v)

        # print(balloons)

        # if balloons.length == 0:
        if len(nums) == 0:
            return 0

        # if balloons.length == 1:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return nums[0]*nums[1] + max(nums)

        # return 0
        memo = {}

        # def dfs(balloons: Balloons, memo: dict, l: int, r :int) -> int:
        def dfs(l: int, r :int, memo: dict) -> int:
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            maxCoins = 0
            for i in range(l, r+1):
                # Coins from popping i last
                coins = nums[i]
                if l > 0:
                    coins *= nums[l-1]
                if r < len(nums) - 1:
                    coins *= nums[r+1]
                coins += dfs(l, i-1, memo) + dfs(i+1, r, memo)
                maxCoins = max(maxCoins, coins)
            memo[(l, r)] = maxCoins
            return maxCoins
            # node = balloons.head
            # coins = 0
            # while node:
            #     i = node.index
            #     sub = balloons.pop_balloon(i)
            #     coins = max(coins, sub + dfs(balloons, memo, depth + 1))
            #     balloons.unpop_balloon(i)
            #     node = node.right

            # print(f'{balloons}, {memo}')

            # memo[balloons.key] = coins
                
            # return coins

        # memo[(0,0)] = nums[0]*nums[1]
        # memo[(len(nums) - 1, len(nums) - 1)] = nums[-1]*nums[-2]

        # for i in range(1, len(nums) - 1):
        #     memo[(i, i)] = nums[i-1]*nums[i]*nums[i+1]

        # print(memo)
        # I need a more efficient way of doin that
        return dfs(0, len(nums) - 1, memo)

        # Using DP 
        # 

        # return memo[0]

        # coins = head.val*tail.val + max(head.val, tail.val)
        # # Pop the lowest value, unless we have 3 balloons
        # while balloons:
        #     _, i, balloon = heapq.heappop(balloons)
        #     coins += balloon.pop()
        #     print(f'popped {i}: {balloon}, coins = {coins}, LL: {llToStr(head)}')

        # return coins

'''
nums=[3,1,5,8]
Pop 1 => coins += 15, nums=[3,5,8]
Pop 3 => coins += 15, nums=[5, 8]
Pop 5 => coins += 40, nums=[8]
Pop 8 => coins +=  8, nums=[]

nums=[3,1,5,8]
Pop 1 => coins +=  15, nums=[3,5,8]
Pop 5 => coins += 120, nums=[3, 8]
Pop 3 => coins +=  24, nums=[8]
Pop 8 => coins +=   8, nums=[]
Final => coins  = 167

# We can think of a the sequence as a graph where the paths are popping actions
# And the cost of the path is - its prod.
# Problem: The costs and the paths changes at each pop time.
# And we want to maximize the cost.

# My current solutions gives the correct answer, but it is too inneficient.
# What if we use a memory from mapping the current state to an int?

'''

