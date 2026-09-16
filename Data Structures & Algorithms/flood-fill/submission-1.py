class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit_hash = set()
        ini_color = image[sr][sc]
        rlen = len(image)
        clen = len(image[0])

        def dfs(image, sr, sc):
            if min(sr,sc) < 0 or sr == rlen or sc == clen:
                return
            
            if (sr,sc) in visit_hash:
                return
            
            if image[sr][sc] != ini_color:
                return
            
            visit_hash.add((sr,sc))

            image[sr][sc] = color

            dfs(image, sr+1, sc)
            dfs(image, sr-1, sc)
            dfs(image, sr, sc+1)
            dfs(image, sr, sc-1)
        
        dfs(image, sr, sc)
        return image
            