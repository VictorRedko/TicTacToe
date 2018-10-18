def printBoard(b):
  new = b.copy()
  for n in range(16): 
    if new[n] == None: new[n] = n+1
  print('')
  print(new[0],new[1],new[2],new[3],'\n',sep='\t')
  print(new[4],new[5],new[6],new[7],'\n',sep='\t')
  print(new[8],new[9],new[10],new[11],'\n',sep="\t")
  print(new[12],new[13],new[14],new[15],sep="\t")

def win(b):
  if b[0] == b[1] == b[2] == b[3] != None:
    if b[0] == 'X': return 1
    else: return 2
  elif b[4] == b[5] == b[6] == b[7] != None:
    if b[4] == 'X': return 1
    else: return 2
  elif b[8] == b[9] == b[10] == b[11] != None:
    if b[8] == 'X': return 1
    else: return 2
  elif b[12] == b[13] == b[14] == b[15] != None:
    if b[12] == 'X': return 1
  elif b[0] == b[4] == b[8] == b[12] != None:
    if b[0] == 'X': return 1
    else: return 2
  elif b[1] == b[5] == b[9] == b[13] != None:
    if b[1] == 'X': return 1
    else: return 2
  elif b[2] == b[6] == b[10] == b[14] != None:
    if b[2] == 'X': return 1
    else: return 2
  elif b[3] == b[7] == b[11] == b[15] != None:
    if b[3] == 'X': return 1
    else: return 2
  elif b[0] == b[5] == b[10] == b[15] != None:
    if b[0] == 'X': return 1
    else: return 2
  elif b[3] == b[6] == b[9] == b[12] != None:
    if b[3] == 'X': return 1
    else: return 2
  else: return 0

def tie(b):
  empty = [n for n in b if n == None]
  return len(empty) == 0

def alphabeta(b,p,alpha=(float('-inf'),16),beta=(float('inf'),16),ply=9):
  if ply == 0:
    if win(b) == 1: return (-1,100)
    if win(b) == 2: return (1,100)
    if win(b) == 0 or tie(b): return (0,100)
  if win(b) == 1: return (-1,100)
  if win(b) == 2: return (1,100)
  if tie(b): return (0,100)
  playSign = 'n'
  if p == 1:
    playSign = 'X'
  else:
    playSign = 'O'
  for n in [i for i in range(16) if b[i] == None]:
    b[n] = playSign
    val = (alphabeta(b,(p+1)%2,alpha,beta,ply-1)[0],n)
    b[n] = None
    if p == 0:
      if val[0] > alpha[0]: alpha = val
      if alpha[0] >= beta[0]: return beta
    else:
      if val[0] < beta[0]: beta = val
      if beta[0] <= alpha[0]: return alpha
  if p == 0: return alpha
  else: return beta

board = [None]*16
printBoard(board)
gOver = False
turns = 0
while not gOver:
  playerMove = int(input("\nPlayer: please pick a free space. "))
  while playerMove > 16 or playerMove < 1:
    playerMove = int(input("Invalid input, please pick a free space between 1 and 16. "))
  while board[playerMove-1] != None: playerMove = int(input("Space not free. "))
  board[playerMove-1] = 'X'
  if win(board) == 1:
    print("Congrats, X has won!")
    printBoard(board)
    break
  if tie(board):
    print("The game has ended in a tie!")
    printBoard(board)
    break
  board[alphabeta(board,0)[1]] = 'O'
  printBoard(board)
  if win(board) == 2:
    print("Congrats, O has won!")
    gOver = True
  turns+=1
  if turns == 8:
    print("The game has ended in a tie!")
    gOver = True
