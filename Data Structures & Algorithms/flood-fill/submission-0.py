class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ini_color = image[sr][sc]

        if ini_color == color:
            return image

        def dfs(sr,sc,ini_col,image):
            rlen = len(image)
            clen = len(image[0])

            if min(sr, sc) <0 or sr == rlen or sc == clen:
                return
            
            if image[sr][sc] != ini_color:
                return
            
            image[sr][sc] = color

            dfs(sr+1, sc, ini_col, image)
            dfs(sr-1, sc, ini_col, image)
            dfs(sr, sc+1, ini_col, image)
            dfs(sr, sc-1, ini_col, image)

        
        dfs(sr,sc,ini_color,image)
        return image