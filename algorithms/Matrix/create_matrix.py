
def create_matrix():
    matrix = [[1 for _ in range(5)] for _ in range(4)]
    print(matrix)
    copied_matrix = [row[:] for row in matrix]
    print(copied_matrix)
    transpose_matrix = zip(*matrix)
    print(transpose_matrix)

def main():
    create_matrix()
    row = {i:set() for i in range(9)}
    col = {i:set() for i in range(9)}
    box = {i:set() for i in range(9)}
    print(row, col, box)

if __name__ == "__main__":
    main()

"""
[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]
"""