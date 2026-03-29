class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a

        if abs(a) < abs(b):
            a, b = b, a

        binA = bin(abs(a))[::-1]
        binB = bin(abs(b))[::-1]

        res = []
        up = False
        # If they have the same sign, let's do abs(a) + abs(b), then apply the sign
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            for i, j in zip(binA, binB):
                if i == 'b' or j == 'b':
                    break
                elif i == '1' and j == '1':
                    if up:
                        res.append('1')
                    else:
                        res.append('0')
                    up = True
                elif i == '1' or j == '1':
                    if up:
                        res.append('0')
                    else:
                        res.append('1')
                else:
                    if up:
                        res.append('1')
                        up = False
                    else:
                        res.append('0')
            #print('binA', binA)
            #print('binB', binB)
            #print('Partial', res)
            remainingSize = len(binA) - len(binB)
            tmp = None
            if remainingSize > 0: # if len(binA) > len(binB):
                tmp = binA[-remainingSize-2:]
            elif remainingSize < 0: # if len(binA) < len(binB):
                tmp = binB[remainingSize-2:]
            else:
                tmp = ''
            for i in tmp:
                if i == 'b':
                    break
                if i == '1' and up:
                    res.append('0')
                elif i == '1' or up:
                    up = False
                    res.append('1')
                else:
                    res.append('0')
            #print(res)
            if up:
                res.append('1')


            res.append('0b')
            if a < 0:
                res.append('-')
        else: # One is negative and the other positive, let's do a-b with a being the onme with the biggest abs value            
            for i, j in zip(binA, binB):
                if i == j and not up: # '0' '0' or '1' '1'
                    res.append('0')
                elif i == '1' and j == '0':
                    if up:
                        res.append('0')
                        up = False
                    else:
                        res.append('1')
                elif i == '0' and j == '1':
                    if up: # j is 10
                        res.append('0')
                    else:
                        res.append('1')
                    up = True
                elif i == j: # and up # it is the same as j being 1 more than i and  up = False
                    # up = True again
                    res.append('1')
            print()
            remainingSize = len(binA) - len(binB)
            tmp = binA[-remainingSize-2:] if remainingSize > 0 else ''
            for i in tmp:
                if i == 'b':
                    break
                if i == '1' and up:
                    res.append('0')
                    up = False
                elif i == '1' or up:
                    res.append('1')
                else: # i == '0' and up == False
                    res.append('0')
            res.append('0b')
            if a < 0:
                res.append('-')

        res = int(''.join(res[::-1]), 2)
        return res

        '''
        101100001  +  11100111 = 1001001000
        101100001 AND 11100111 = 0001100001
        101100001  OR 11100111 = 0111100111
        101100001 XOR 11100111 = 0110000110

           1 0 1 1 0 10 10 10 1
           - 1 1 1 0  1 10  1 1
                         0  1 0
        '''

