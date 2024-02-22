class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        
        # # the time complexity is O(T + n).
        # # the space complexity is O(n).
        # if n == 1 and not trust:
        #     return 1

        # judge = -1
   
        # people_who_trust = set()
        # trusted_count = defaultdict(int)  # default value of 0 for any new key
        
        # for (a,b) in trust:
        #     trusted_count[b] += 1
        #     people_who_trust.add(a)

        
        # for t in trusted_count.keys():
        #     if t not in people_who_trust and trusted_count[t] == n-1:
        #         return t
    
        # return judge

        '''
        The space complexity is slightly improved to O(n) due to the use of a list with direct indexing instead of a set and a dictionary,
        though the asymptotic space complexity classification remains the same. 
        This version also improves cache locality by using an array (list in Python), which might offer practical performance benefits.
        '''
        if n == 1 and not trust:
            return 1

        trusted_count = [0] * (n+1) # Using a list for direct indexing

        for a,b in trust:
            trusted_count[a] -= 1
            trusted_count[b] += 1

        for i in range(1,n+1):
            if trusted_count[i] == n-1:
                return i

        return -1            

        
