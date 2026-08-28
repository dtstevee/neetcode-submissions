class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_store = {}

        for i,x in enumerate(strs):
            temp_hash = {}

            for i,y in enumerate(x):
                if y in temp_hash:
                    temp_hash[y] += 1
                else:
                    temp_hash[y] = 1
            
            key = tuple(sorted(temp_hash.items()))

            if key in hash_store:
                hash_store[key].append(x)
            else:
                hash_store[key] = [x]
            
        return list(hash_store.values())
