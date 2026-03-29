class Solution:
    def getSum(self, a: int, b: int) -> int:
      # Make the b be the one with the lowest absolute values
      if abs(a) < abs(b):
        a, b = b, a

      # Special cases:
      # 1: a == -b
      if a == -b:
        return 0
      # 2: either is 0
      if b == 0:
        return a

      isNegative = a < 0
      isSub = (a < 0 < b) or (a > 0 > b)

      a = abs(a)
      b = abs(b)

      res = 0

      print(format(a, 'b'), format(b, 'b'), isSub, isNegative)
      if isSub:
        # We know 1-1 = 0, 0-0 = 0, 1-0 = 1, 10-1 = 1
        carry = False
        bins = []
        while b:
          da = a % 2
          db = b % 2
          # In this case carry sums in the value of b
          if da & (db ^ carry) or (1^(db | da | carry)): # 1 - 1 or 0-0
            bins.append('0')
            carry = 0
          elif da & (1^(db | carry)): # da => 1 - 0
            bins.append('1')
            carry = 0
          elif db ^ carry: # Only db or carry => 0 - 1 => 10 - 1
            bins.append('1')
            carry = 1
          elif db & da & carry: # All 3 of them => 1 - 10 => 11 - 10
            bins.append('1')
            carry = 1
          else: # db & carry, but not da => 0 - 10 => 10 - 10
            bins.append('0')
            carry = 1
          a >>= 1
          b >>= 1

        while a and carry:
          da = a % 2
          if da: # 1 - 1 = 0
            bins.append('0')
            carry = 0
          else: # ~da: # 0 - 1 => 10 - 1 = 1
            bins.append('1')
            carry = 1
          a >>= 1

        bins.append(format(a, "b"))
        bins.append('0b')
        bins.reverse()

        res = int(''.join(bins), 2)
      else:
        # We know 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1, and 1 + 1 = 10
        # This looks like a XOR operation for the current digit and AND operation to carry a digit
        # First let's check if it a - or + operation in terms of absolute values
        carry = 0
        bins = []
        while b:
          da = a % 2
          db = b % 2
          print(a, b, da, db, carry)
          print(db & da & carry, db ^ da ^ carry, db, ~da, ~carry)
          if db & da & carry: # All 3 of them => 11
            bins.append('1')
            carry = 1
          elif db ^ da ^ carry: # Only one of them => 01
            bins.append('1')
            carry = 0
          elif (1^(db|da|carry)): # None of them
            bins.append('0')
            carry = 0
          else: # Any 2 of them
            bins.append('0')
            carry = 1
          a >>= 1
          b >>= 1

        print(a, carry)
        while a and carry:
          da = a % 2
          if da: # Both them => 10
            bins.append('0')
            carry = 1
          else: # elif ~da & carry: # Only one of them => 01
            bins.append('1')
            carry = 0
          a >>= 1


        if carry:
          bins.append('1')
        else:
          bins.append(format(a, 'b'))
        bins.append('0b')
        bins.reverse()
        print(bins)
        res = int(''.join(bins), 2)
      return -res if isNegative else res
