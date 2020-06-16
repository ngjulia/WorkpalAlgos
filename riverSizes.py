map = [
  [1,0,0,1,0],
  [1,0,1,0,0],
  [0,0,1,0,1],
  [1,0,1,0,1],
  [1,0,1,1,0]
]

def riverCount(grid):
  if not grid: return 0

  def dfs(i,j): 
    size = 1
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]==0:
      return 0
    grid[i][j] = 0
    size+=dfs(i+1,j)
    size+=dfs(i,j+1)
    size+=dfs(i-1,j)
    size+=dfs(i,j-1) 
    return size 
     
  sizes = []    
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]==1:
        sizes.append(dfs(i,j))
  print(sizes)

riverCount(map)
