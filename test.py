import math

f = open("score.txt", "r")
score = f.readline()
print(score)
f.close()

f = open("score.txt", "w")
f.write("10")
print(score)
f.close()
