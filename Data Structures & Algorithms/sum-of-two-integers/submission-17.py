class Solution:
  def getSum(self, a: int, b: int) -> int:
    # Let´s use bitwise operations and and bit mask to get the latest digit
    if a == -b:
      return 0
    if a == 0 or b == 0:
      return a | b

    total = 0
    up = 0
    mask = 1
    negative = False
    # sum
    # 20 + 30 = 10100 + 11110 => 
    if (a < 0 and b < 0) or (a > 0 and b > 0):
      if a < 0:
        negative = True
        a = -a
        b = -b
      if (a & b) == 0:
        if negative:
          return - (a | b)
        else:
          return a | b
      while mask <= a or mask <= b:
        print(a & mask, b & mask, up)
        if ((a & mask) ^ (b & mask) ^ up) | ((a & mask) & (b & mask) & up):
          print('1')
          total |= mask
        else:
          print('0')
        if ((a & mask) & (b & mask)) | (up & (b & mask)) | ((a & mask) & up):
          print('up')
          up = mask << 1
        else:
          print('no up')
          up = 0
        mask = mask << 1
      print(total, up)
      total |= up
      if negative:
        return -total
      else: 
        return total
    else:
      print('else')
      a, b = max(a,b), min(a,b)
      print(a, b)
      if abs(a) < abs(b):
        negative = True
        a, b = -b, a
      else:
        b = -b
      print(a, b)
      total = 0
      # 'a' has the highest abs value
      # Let's do a - b
      print(bin(a), bin(b))
      while mask <= a:
        ma = a & mask
        mb = b & mask
        print(total, ma, mb, up, mask)
        if (ma & (mb ^ up)) | (ma == 0 and mb == 0 and up == 0):
          print('1 - 1 or 0 - 0')
          up = 0
        elif ma and mb == 0 and up == 0:
          print('1 - 0')
          total |= mask
          print('up = 0')
        elif ma & mb & up:
          print('1 - 10 =up=> 11 - 10')
          total |= mask
          up = mask << 1
        elif (mb ^ up) and ma == 0:
          print('0 - 1 => 10 - 1')
          total |= mask
          up = mask << 1
        else: # ~ma & mb & up
          print('0 - 10 =up=> 10 - 10')
          up = mask << 1
        mask <<= 1
    return -total if negative else total
    '''
    11110100
    128+64+32+16 0 4 0 0
    11111010
    128+64+32+16+8+2
    
    750 - 500
    1011101110
    0111110100
    '''