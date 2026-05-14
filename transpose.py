import sys

def transpose_matrix(matrix):
    """
    Transpose a given matrix.
    """
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with swapped dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def main():
    lines = sys.stdin.readlines()
    
    if not lines:
        print("No input provided")
        return
    
    # First line: N M
    first_line = lines[0].strip().split()
    if len(first_line) != 2:
        print("Invalid first line")
        return
    N = int(first_line[0])
    M = int(first_line[1])
    
    if len(lines) != N + 1:
        print("Invalid number of lines")
        return
    
    # Read the matrix
    matrix = []
    for i in range(1, N+1):
        row = list(map(int, lines[i].strip().split()))
        if len(row) != M:
            print("Invalid row length")
            return
        matrix.append(row)
    
    # Transpose
    transposed = transpose_matrix(matrix)
    
    # Print the transposed matrix
    for row in transposed:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()