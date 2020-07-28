import re
import os
import sudoku
from PIL import Image
import pytesseract  as tess


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
def pngToMatrix(text):
    tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    fullPath = os.path.join('..\\test', text)
    img = Image.open(fullPath)
    width, height = img.size
    arr = [[0 for i in range(9)] for i in range(9)]

    img = img.crop((1, 1, width - 1, height - 1))

    for i in range(9):
        for j in range(9):
            left = 32 * j + 4
            top = 32 * i + 2.5
            right = left + 32 - 9
            bottom = top + 32 - 7

            img1 = img.crop((left, top, right, bottom))
            text = tess.image_to_string(img1, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            
            if (text == ''):
                arr[i][j] = 0
            else:
                arr[i][j] = int(text)  

    return arr 

def answer(text, opt):
    print('Sudoku sebelum terisi: ')
    if (opt == 1):
        problem = fileToMatrix(text)
        sudoku.printSudoku(problem)
    elif (opt == 0):
        problem = pngToMatrix(text)
        sudoku.printSudoku(problem)

    # Menampilkan jawaban
    print('Sudoku setelah diisi: ')
    if (sudoku.solveSudoku(problem)): 
        sudoku.printSudoku(problem) 
    else: 
        print("Tidak ada solusi")

    print("Koordinat dari area bernomor 5 adalah: ")
    sudoku.findFive(problem)

check = False
print("Masukkan 0 untuk memasukkan file png")
print("Masukkan 1 untuk memasukkan file txt")
opt = int(input("Masukkan pilihan: "))
while (check == False):
    if opt != 0 and opt != 1:
        print("Masukkan salah! Silakan masukkan 0 atau 1!")
        print("Masukkan 0 untuk memasukkan file png")
        print("Masukkan 1 untuk memasukkan file txt")
        opt = int(input("Masukkan pilihan: "))
    else:
        text = input('Masukkan file sudoku: ')
        answer(text, opt)
        check = True

