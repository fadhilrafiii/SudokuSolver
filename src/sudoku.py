def printSudoku(arr): 
    for i in range(9): 
        for j in range(9): 
            print(arr[i][j], end=" ")
        print('\n')
  
          
# Fungsi untuk mencari petak yang kosong pada sudoku
def findEmpty(arr, l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]== 0): 
                l[0]= row 
                l[1]= col 
                return True
    return False

# Mengecek apakah pada suatu petak dapat diisi dengan 'num'
# Tidak ada petak dalam baris, kolom, dan tiap kotak 3x3 
def canFillWithNum(arr, row, col, num): 
    return not isMatchInBox(arr, row - row % 3, col - col % 3, num) and not isMatchInRow(arr, row, num) and not isMatchInCol(arr, col, num)   

# Fungsi untuk mencocokan petak tiap pada kotak 3x3 dengan nilai 'num'
def isMatchInBox(arr, row, col, num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i + row][j + col] == num): 
                return True
    return False
  
# Fungsi untuk mencocokan petak pada baris dengan nilai 'num'
def isMatchInRow(arr, row, num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
# Fungsi untuk mencocokan petak pada kolom dengan nilai 'num'
def isMatchInCol(arr, col, num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
  
#Algoritma Sudoku Solbver
def solveSudoku(arr): 
    l =[0, 0]    
    if(not findEmpty(arr, l)): 
        return True
      
    # Menyimpan nilai baris dan kolom yang kosong
    row = l[0] 
    col = l[1] 
      
    # Mencoba mengisi petak dengan nilai 1 sampai 9
    for num in range(1, 10): 
        if(canFillWithNum(arr, row, col, num)): 
            arr[row][col]= num 
            
            if (solveSudoku(arr)):
                return True
            else:
                arr[row][col] = 0
    #Ini return False agar rekursif          
    return False 

def findFive(matrix):
    for i in range(9): 
        for j in range(9): 
            if (matrix[i][j] == 5):
                print("(", end='')
                print(str(i),",", str(j), end='')
                print(")")
