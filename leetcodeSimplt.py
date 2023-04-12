from typing import List
import math
from typing import Optional
import queue
from collections import defaultdict

class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split('/')
        stk = []
        for file in split:
            if file == '.' or file == '':
                continue
            if file != '..':
                stk.append(file)
            elif file == ".." and len(stk)>0:
                stk.pop()
        
        can = "/".join(stk)
        return "/"+can
            

obj = Solution()
print(obj.simplifyPath("/../abc//./def/"))
