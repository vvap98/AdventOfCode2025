import re

zeroCount = 0
position = 50
#pilko string jokaista 0 kohden laske nollat
def turnDial(rotation, position):
    zeroCount = 0
    
    s = re.findall("[a-zA-Z]+", rotation)[0]  # Otetaan L tai R
    n = int(re.findall("[0-9]+", rotation)[0])  # Otetaan numerot stringistä 
    
    for i in range(1,n +1):
        if s == "R":
            position += 1
        if s == "L":
            position -= 1
        if position == 100:
            position = 0
        if position == -1:
            position = 99
    if position == 0:
        zeroCount = zeroCount + 1
        #KUINKA MONTA KERTAA DIAL JÄTETÄÄN 0 EI KUINKA MONTA KERTAA SE OHITTAA SEN
    return(zeroCount, position)





with open('code.txt', 'r') as file:
    for line in file:
        s,x = turnDial(line.strip(), position)
        zeroCount = zeroCount + s
        position = x

    print(zeroCount)

#palauta joka kierroksella positio ja nollien määrä