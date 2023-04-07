import os
import time
#importing sudoku solver code
import sudoku

start_time = time.time()

#input
input_sudoku = [[[6,0,0], [0,0,9], [0,0,0]],
                [[0,0,0], [0,0,0], [0,0,4]],
                [[0,0,7], [6,4,8], [0,0,2]],
                [[0,0,2], [0,5,0], [8,0,0]],
                [[0,0,1], [8,0,0], [0,2,3]],
                [[7,0,4], [0,0,0], [0,0,0]],
                [[0,0,0], [3,0,0], [0,4,0]],
                [[0,0,0], [0,6,0], [5,0,0]],
                [[0,2,3], [0,1,0], [0,0,0]]]

#setting sudoku which should be soved
sudoku.work_sudoku = input_sudoku
#solves as much as possible using simple solving strategies 
sudoku.solve()
#bruteforces
sudoku.brute_force()

#prints input and output
print("started with")
sudoku.print_sudoku(input_sudoku)
print("\nended with")
sudoku.print_sudoku(sudoku.output_sudoku)

#prints execution time
print("execution time: " + str(round(time.time() - start_time, 3)) + "s")
os.system("pause")