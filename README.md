# Sudoku Solver
oleh Fadhil Muhammad Rafi' 13518079

## Cara Penggunaan
1. Buka terminal
2. Pergi ke direktori dimana source code program berada
3. Jalankan command: python main.py
4. Masukkan nama file eksternal yang berisi sudoku (Tiap elemen sebaris dipisahkan oleh whitespace, tiap baris dipisahkan oleh newline). Contoh: tc1.txt

## Algoritma
Penyelesaian Sudoku ini menggunakan Algoritma Backtracking. Alasan penggunaan algoritma ini karena mudah dan tidak membutuhkan waktu selama Brute Force karena
terdapat pengeliminasian kandidat angka yang dapat diisi dalam satu petak. Algoritma ini mengecek petak-petak lain yang telah terisi sehingga untuk mengisi petak selanjutnya kandidat angka yang mungkin sudah dikurangi. Algoritma ini juga akan mundur satu petak, ketika pada petak yang akan diisi tidak ditemukan solusi. Berbeda dengan Brute Force yang menguji tiap petak dengan angka 1 hingga 9. Berdasarkan tabel yang tertera pada referensi kedua, dapat terlihat bahwa kompleksitas waktunya adalah O(n<sup>3</sup>)

## Referensi
https://www.stmikasia.ac.id/laravel-filemanager/files/shares/5976b38e60cb2.pdf
http://repositori.usu.ac.id/bitstream/handle/123456789/4643/141421126.pdf?sequence=1&isAllowed=y
