class Solution:
    def getSum(self, a: int, b: int) -> int:
        negative = False
        add = True
        if a < 0 and b < 0:
            negative = True
            a = -a
            b = -b
        elif -max(abs(a), abs(b)) == min(a, b):
            # Only one of them is negative and it is the one with the highest abs value
            negative = True
            add = False
        elif -min(abs(a), abs(b)) == min(a, b):
            # Only one of them is negative and it is the one with the smallest abs value
            add = False

        print(a, b, negative, add)
        if add:
            amp = (a & b) << 1
            xor = a ^ b

            while amp > 0:
                a = amp
                b = xor
                amp = (a & b) << 1
                xor = a ^ b
        else:
            # Let's do max(abs(a), abs(b)) - min(abs(a), abs(b))
            a = abs(a)
            b = abs(b)
            a, b = max(a, b), min(a, b)
            namp = ((~a) & b) << 1
            xor = a ^ b
            print(a, b, ~a, namp, xor)
            while namp > 0:
                a = max(xor, namp)
                b = min(xor, namp)
                namp = ((~a) & b) << 1
                xor = a ^ b
                print(a, b, namp, xor)

        return -xor if negative else xor
        '''
        Let's take their binary representation then
        e.g., 100110 + 111010 =
        when it's 0 + 0 => 0
        when its 1 + 0 or 0 + 1 => 1
        when its 1 + 1 => 10
        The first operation would be a xor
          100110
        ^ 111010
        = 011100

        But when its 1 + 1, then we have an extra to the left
          100110
        & 111010
        =1000100 (adding one 0 to the right)

        Repeating the process:
           011100
        + 1000100

        ^ 1011000
        &00001000

        Again
        Repeating the process:
          1011000
        + 0001000

        ^ 1010000
        &00010000

        Again
          1010000
        +00010000

        ^ 1000000
        & 0100000

        Finally
          1000000
        ^ 0100000
        = 1100000
        ---
        Now let's do A - B
          111010
        - 100110
        = 010100

        similarly:
        1 - 1 = 0
        1 - 0 = 1
        0 - 1 = 1, but we get one from the next power of 2
        0 - 0 = 0

          111010
        ^ 100110
        = 011100
       
        not 000101
          & 100110
          = 000100 << 2
     
             011100
           + 001000
           ^ 010100
        not& 000000


            10000
            01100
          ^ 11100
        not&01100

        '''