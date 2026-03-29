from collections import defaultdict
import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mem = [set(string.ascii_uppercase)]
        chars = defaultdict(int)
        print(len(s), k)
        # initial word
        i = 0
        while i < len(s) and len(mem) + k - 1 >= i:
            print(len(mem) - 1, i, s[i])
            if chars[s[i]] == len(mem) - 1:
                mem.append(set())
                mem[-1].add(s[i])
                if len(mem) > 1:
                    mem[-2].remove(s[i])
            else:
                if len(mem) > 1:
                    mem[chars[s[i]]].remove(s[i])
                mem[chars[s[i]] + 1].add(s[i])
            
            chars[s[i]] += 1
            i += 1
        print(len(mem) - 1, i)

        if i == len(s):
            if len(mem) + k - 1 >= i:
                return i
            else:
                return i - 1
        res = i - 1 if i < len(s) else i
        print(f'res={res}')
        j = 0
        while i < len(s):
            while len(mem) + k - 1 < i - j:
                print(f'remove {s[j]}')
                if chars[s[j]] == len(mem) - 1:
                    mem[-1].remove(s[j])
                    mem[-2].add(s[j])
                    if mem and len(mem[-1]) == 0:
                        mem.pop()
                else:
                    mem[chars[s[j]]].remove(s[j])
                    mem[chars[s[j]] - 1].add(s[j])
                chars[s[j]] -= 1
                j += 1
            print(f'i={i},j={j}')
            print(f'add {s[i]}')
            if chars[s[i]] == len(mem) - 1:
                mem.append(set())
                mem[-1].add(s[i])
                if len(mem) > 1:
                    mem[-2].remove(s[i])
            else:
                if len(mem) > 1:
                    mem[chars[s[i]]].remove(s[i])
                mem[chars[s[i]] + 1].add(s[i])
                
            chars[s[i]] += 1
            print(f'len(mem) + k - 1 >= i - j <= {len(mem)} + {k} - 1 <= {i} - {j}:')
            if len(mem) + k - 1 <= i - j:
                res = max(res, i - j)
            else:
                res = max(res, i - j + 1)
            i += 1
        return res

