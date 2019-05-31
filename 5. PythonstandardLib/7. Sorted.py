pointsinaGame = [0,-10,15,-2,1,12]

print(sorted(pointsinaGame))

children = ["Sue", "jerry","Linda"]
print(sorted(children))

print(sorted("My favourite child is Linda".split(), key = str.upper))

print(sorted(pointsinaGame, reverse=True))

leaderBoard = {231:"CKL",123: "ABC", 432: "JKC"}
print(sorted(leaderBoard, reverse=True))