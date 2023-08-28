# Esercizio 1 per 25.01
# Scrivere su un file 'proverbio.txt' un proverbio a scelta
# Aprire il file proverbio.txt
# Leggerne tutto il contenuto
# scrivere i caratteri in posizione pari su un file 'file_proverbio_dispari.txt ' 
# Scrivere i caratteri in posizione dispari su un file ‘file_proverbio_dispari.txt

# Open proverbio.txt and write, then close
f = open("proverbio.txt", 'w')
proverbio = "Buon sangue non mente."
f.write(proverbio)
f.close()

# Open dispari and pari files
dispari = open("file_proverbio_dispari.txt",'w')
pari = open("file_proverbio_pari.txt", 'w')

# open proverbio.txt, read length of file
f = open("proverbio.txt", 'r')
pr = f.readline()
fileLength = len(pr)

# Iterate over file and write to pari and dispari files
for i in range(fileLength):
    if(pr[i] != '\n'):
        if i%2 == 0:
            pari.write(pr[i])
        else:
            dispari.write(pr[i])

# close files
dispari.close()
pari.close()
