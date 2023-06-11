f = open("words.txt", "r")
temp = f.read().splitlines()
for x in temp:
  # 🍉🥝🍅🥝🥦🍉🥝🍓🍍🥐
  if len(x) == 10 and x[1] == x[3] and x[1] == x[6] and x[0] == x[5]:
      print(x)