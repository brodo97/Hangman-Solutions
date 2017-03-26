import os
clear = lambda: os.system("clear")

def check_words(lista,stringa):
    nuovaLista = []
    for parola in lista:
        count = 0
        for x,lettera in enumerate(parola):
            if len(parola)==len(stringa):
                if lettera == stringa[x]:
                    count += 1
                else:
                    if lettera in "aeiou":
                        if not parola[x] == "+" and stringa[x] == "+":
                            count += 1
                    else:
                        if not parola[x] == "-" and stringa[x] == "-":
                            count += 1
        if count == len(parola):
            nuovaLista.append(parola)
    return nuovaLista

def get_diz():
    lista = []
    try:
        with open("dictionary.txt","r") as f:
            for line in f:
                lista.append(line.rstrip("\n"))
    except IOError:
        print "Error: Missing dictionary.txt"
    return lista

def printList(lista):
    if len(lista) == 0:
        print "No words found in the dictionary"
    else:
        for i in xrange(0,len(lista)-1):
            print lista[i]+",",
        print lista[len(lista)-1]

if __name__ == '__main__':
    dictionary = get_diz()
    if len(dictionary)==0:
        exit()
    while True:
        stringa = str(raw_input("Insert the searching string or 'END' to stop the execution: "))
        if stringa == "END":
            break
        lista = check_words(dictionary,stringa)
        searchAgain = ""
        if len(lista)>1:
            searchAgain = str(raw_input("Found " + str(len(lista)) + " word, search again? Y/n: "))
            if searchAgain == "":
                searchAgain = "y"
        clear()
        if len(lista)==0 or searchAgain.lower() == "n":
            printList(lista)
