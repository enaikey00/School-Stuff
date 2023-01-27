'''
Creare un file con un testo a scelta suddiviso in righe e colonne (vedi ad esempio: https://it.lipsum.com/) 
Il file potrebbe essere potenzialmente enorme
Fino a che l'utente non scrive la singola lettera 'q’
Leggere Una Parola Da Input
Se la parola è presente nel file indicare la riga e la Colonna
Altrimentiscrivere'Parolanonpresente’
Suggerimento: Aprire e chiudere il file ad ogni ciclo (non caricare il file in memoria) 
Una parola non è spezzabile in due righe
'''

## --- Modules --------------------------------
from colorama import Fore, Back, Style

## --- Functions -------------------------------

# Prepare text file for later
def setInputFile():
    f = open("ipsum.txt", 'r')
    line = f.readline()
    f.close()

    # split string into words
    line = line.split()
    # del period dots. Alternative: use regex later to find word
    line = [w.replace('.','') for w in line]

    # divide text into list of lists, each sentence with 10 words.
    line = [ line[x:x+10] for x in range(0, len(line), 10) ]
    
    return line

## --- Main --------------------------------------

while True:

    parola = input("Quale parola vuoi cercare? ('q' per interrompere): ")
    if parola.lower() == 'q':
        break
    
    print(f"\nHere we go, looking for word: {parola}...\n")
    lines = setInputFile()
    #print(Fore.RED + lines[0][1])
    
    for sentence in lines:
        if parola in sentence:

            print("Origin Sentence:", end = '')
            [ print(Style.RESET_ALL, word, end = '') if word != parola else print(Fore.RED, word, end = '') for word in sentence]
            print(Style.RESET_ALL)
            print(f"Word position:\n\tcolumn: {sentence.index(parola)} row: {lines.index(sentence)}")
            print("")
        else:
            print(f"{parola} non presente.")