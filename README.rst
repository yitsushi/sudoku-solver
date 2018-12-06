sudoku-solver
-------------

Example usage::

  from sudoku_solver import Board

  board = Board()

  board.from_file('input/simple-full-valid')
  print("Board:")
  board.draw()
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")

  print()

  board.from_file('input/simple-full-not-valid')
  print("Board:")
  board.draw()
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")

  print()

  board.from_file('input/simple-fill')
  print("Board:")
  board.draw()
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")
  print("Solving...")
  board.solve()
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")
  board.draw()

  print()

  board.from_file('input/medium-fill')
  print("Board:")
  board.draw()
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")
  print("Solving...")
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")
  board.solve()
  board.draw()

  print()

  board.from_file('input/real-0001')
  print("Board:")
  board.draw()
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")
  print("Solving...")
  if board.validate():
      print("Board is valid!")
  else:
      print("Board is not valid!")
  board.solve()
  board.draw()
