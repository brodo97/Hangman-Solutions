def get_diz():
    lista = []
    try:
        with open("dictionary.txt","r") as f:
            for line in f:
                lista.append(line.rstrip("\n"))
    except IOError:
        print "Error: Missing dictionary.txt"
    return lista

if __name__ == '__main__':
    dictionary = get_diz()
    letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for word in dictionary:
        for char in word:
            letters[char] += 1

    tot = sum(letters.values())
    hz = 0
    for i in sorted(letters, key=letters.get, reverse=True):
        print '{0:>1} {1:>6} {2:>1} {3:>8}'.format(i, letters[i],":",str(letters[i]/(tot/100.))[:8]+"%")
    print ""
