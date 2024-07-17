class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        i,j=0,0
        m=len(matrix[0])
        n=len(matrix)

        DOWN,LEFT,RIGHT,UP=0,1,2,3
        direction=RIGHT

        UP_WALL=0
        RIGHT_WALL=m
        DOWN_WALL=n
        LEFT_WALL=-1

        while len(ans)!= m*n:

            if direction==RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                direction=DOWN
                RIGHT_WALL-=1

            elif direction==DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                direction=LEFT
                DOWN_WALL-=1

            elif direction==LEFT:
                while j>LEFT_WALL:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                direction=UP
                LEFT_WALL+=1

            elif direction==UP:
                while i>UP_WALL:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                direction=RIGHT
                UP_WALL+=1
        return ans
