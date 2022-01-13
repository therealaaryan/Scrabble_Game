letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points={key:value for key,value in zip(letters,points)}
letter_to_points.update({" ":0})
def score_word(word):
  point_total=0
  for l in word:
    point_total+=letter_to_points.get(l,0)
  return point_total

def play_word(player,word):
  lst=[]
  lst.append(word)
  player_to_words.update({player:lst})

brownie_points=score_word("BROWNIE")
print(brownie_points)

player_to_words={"player1":["BLUE","TENNIS","EXIT"],"wordNErd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}
res1=input("Enter name of player:")
res2=input("Enter word in uppercase:")
play_word(res1,res2)
player_to_points={}
player_points=0
for player,words in player_to_words.items():
  for word in words:
    player_points+=score_word(word)
  player_to_points[player]=player_points
print(player_to_points)
