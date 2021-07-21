# The given code includes a list of heights for various basketball players.
# You need to calculate and output how many players are in the range of one standard deviation from the mean.
import math
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
c = len(players)
s = 0
for i in range(c):
    s += players[i]
m = s/c
d = 0
for i in range(c):
    d += (players[i] - m)**2
v = d/c
sd = math.sqrt(v)
dvi = m-sd
dvs = m+sd
cont = 0
for i in range(c):
    if players[i] >= dvi and players[i] <= dvs:
        cont += 1

#print(sd, "/", v, "/", dvi, "/", dvs)
print(cont)
