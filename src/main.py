import re
import os
import sudoku

def fileToMatrix(text):
    fullPath = os.path.join('..\\test', text)
    filename = open(fullPath, 'r+')
    Matrix = [[0 for j in range(9)] for i in range(9)]
    content = filename.read()
    k = 0
    for i in range(9):
        for j in range(9):
            if(content[k] != '#'):
                Matrix[i][j] = int(content[k])
            k += 2
    
    return Matrix

# Memasukkan nama file
text = input('Masukkan file sudoku: ')
print('Sudoku sebelum terisi: ')
problem = fileToMatrix(text)
sudoku.printSudoku(problem)

# Menampilkan jawaban
print('Sudoku setelah diisi: ')
if (sudoku.solveSudoku(problem)): 
    sudoku.printSudoku(problem) 
else: 
    print("Tidak ada solusi")

print("Koordinat dari area bernomor 5 adalah: ")
sudoku.findFive(problem)