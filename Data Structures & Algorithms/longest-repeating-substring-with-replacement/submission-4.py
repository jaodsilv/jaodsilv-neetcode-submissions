from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1 or k >= len(s) - 1:
            return len(s)

        '''
        using a counter to keep the number of characters
        We also keep track of the most common character in a range
        the range mustr be of length k + count of the most common of that range
        '''
        longest = k + 1
        if k == 0:
            cur = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cur += 1
                else:
                    longest = max(cur, longest)
                    cur = 1
            return max(cur, longest)

        i = 0
        counter = Counter(s[0:k+1])

        # maxDist = counterOfMostCommon + k
        mostCommon = counter.most_common(1)[0][0]

        # Let's first find the first candidate

        j = k

        longest = k + 1
        # print(f'Counter = {counter}, i = {i}, j = {j}, longest = {longest}, mostCommon = {mostCommon}')
        while j < len(s):
            while j < len(s)-1 and (j + 1 < counter[mostCommon] + k + i or s[j+1] == mostCommon):
                #print(f'{j} < {len(s)}-1 and ({j}+1 < {counter[mostCommon]} + {k} + {i} or {s[j+1]} == {mostCommon}). {counter}')
                # We move j to the right as much as we can
                j += 1
                counter.update(s[j])
                if counter[mostCommon] <= counter[s[j]]:
                    mostCommon = s[j]
            # It is a valid configuration, thus we may update the longest sequence
            longest = max(longest, j - i + 1)
            #print(f'Counter = {counter}, i = {i}, j = {j}, longest = {longest}, mostCommon = {mostCommon}')

            # Now we attempt to move j to the right one more time
            j += 1
            if j >= len(s):
                break
            counter.update(s[j])
            # Since it is not the most common, then we added a non-mostCommon, now having k+1 non-mostCommons
            # Therefore we must remove 1 non-mostCommon
            if counter[s[j]] > counter[mostCommon]:
                mostCommon = s[j]
            while counter[mostCommon] + k <= j - i:
                #print(f'{counter[mostCommon]} + {k} >= {j} - {i} + 1')
                counter.subtract(s[i])
                if s[i] == mostCommon:
                    mostCommon = counter.most_common(1)[0][0]
                i += 1

            # if s[i] was the mostCommon, then:
            # 1. We need to check if it has changed
            # 2. If it has not changed we actually did not remove any non-mostCommon
            # Therefore we must keep removing until one of the conditions have changed
            #if mostCommon == s[i-1]:
                #prev = mostCommon
             #   mostCommon = counter.most_common(1)[0][0]

                #print(f'Counter = {counter}, i = {i}, j = {j}, longest = {longest}, mostCommon = {mostCommon}')
                #while i < j and prev == mostCommon or s[i-1] == prev:
                #    counter.subtract(s[i])
                #    i += 1
                #    prev = mostCommon
                #    mostCommons = counter.most_common(2)
                #    # If there is a draw we can conveniectly remove choose a different one the be the most common
                #    if mostCommons[0][1] == mostCommons[1][1]:
                #        mostCommon = mostCommons[0][0] if mostCommon == mostCommons[1][0] else mostCommons[1][0]
                #        counter.subtract(s[i])
                #        i += 1
                #        break
                #    mostCommon = mostCommons[0][0]
            #i += 1
                    
        return longest