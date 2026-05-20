class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        paths = path.split('/')
        for p in paths:
            if p == '.' or p == '':
                continue
            if p == '..':
                if res:
                    res.pop()
            else:
                res.append(p)
        return '/' + '/'.join(res)