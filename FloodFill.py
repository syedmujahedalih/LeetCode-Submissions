class Solution:
        def floodFill(self, image, sr: int, sc: int, newColor: int):
                oldval=image[sr][sc]
                rows,cols = len(image),len(image[0])
                if oldval == newColor:
                        return image
                def paint(r,c):
                        if image[r][c]==oldval:
                                image[r][c]=newColor
                                if r>=1: paint(r-1,c)
                                if r+1<rows: paint(r+1,c)
                                if c>=1: paint(r,c-1)
                                if c+1<cols: paint(r,c+1)
                paint(sr,sc)
                return image