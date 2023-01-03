def create_puzzle(elements):
  puzzle = [[""] * 14 for _ in range(7)]
  element_index = 0
  for i in range(7):
    for j in range(14):
      puzzle[i][j] = elements[element_index]
      element_index += 1
  puzzle[0][0] = "?"
  return puzzle

def print_puzzle(puzzle):
  for row in puzzle:
    print(" ".join(str(x) if x != 0 else "?" for x in row))

def find_blank(puzzle):
  size = len(puzzle)
  for i in range(size):
    for j in range(size):
      if puzzle[i][j] == 0:
        return (i, j)
  return (0, 0)

def move(puzzle, direction):
  blank_i, blank_j = 0, 0  # Initialize blank space coordinates
  for i in range(7):  # Find blank space in puzzle
    for j in range(14):
      if puzzle[i][j] == 0:
        blank_i, blank_j = i, j
        break
    else:
      continue
    break
  if direction == "up":
    if blank_i == 0:  # Check if blank space is in top row
      return False
    puzzle[blank_i][blank_j] = puzzle[blank_i - 1][blank_j]
    puzzle[blank_i - 1][blank_j] = 0
  elif direction == "down":
    if blank_i == 6:  # Check if blank space is in bottom row
      return False
    puzzle[blank_i][blank_j] = puzzle[blank_i + 1][blank_j]
    puzzle[blank_i + 1][blank_j] = 0
  elif direction == "left":
    if blank_j == 0:  # Check if blank space is in leftmost column
      return False
    puzzle[blank_i][blank_j] = puzzle[blank_i][blank_j - 1]
    puzzle[blank_i][blank_j - 1] = 0
  elif direction == "right":
    if blank_j == 13:  # Check if blank space is in rightmost column
      return False
    puzzle[blank_i][blank_j] = puzzle[blank_i][blank_j + 1]
    puzzle[blank_i][blank_j + 1] = 0
  return True

def main():
  elements = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
  puzzle = [
      ["?"] + list(elements[:13]),
      list(elements[13:27]),
      list(elements[27:41]),
      list(elements[41:55]),
      list(elements[55:69]),
      list(elements[69:83]),
      list(elements[83:])
  ]
  print_puzzle(puzzle)
  while True:
    direction = input("Enter a direction to move (up, down, left, right): ")
    if not move(puzzle, direction):
      print("Invalid move!")
    print_puzzle(puzzle)

if __name__ == "__main__":
  main()
