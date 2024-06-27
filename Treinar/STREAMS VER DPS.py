'''
stream = open("C:\\Users\\Will-T\\Desktop\\ver_dps.txt","rt")
print(stream.read())
'''

from os import strerror

a = open("007-agent", "wt")
for i in range(10):
    string = "Sla," + " vou escrever qualquer coisa " + str(i) + " vezes\n"
    for f in string:
        a.write(f) #or a.write("Sla," + " vou[...] " + str(i) + " vezes\n")
a.close()
#WRITE


a = open("007-agent", "rt")
ch = a.read() #or read(1) in a loop for
a.close()
print(ch)
#READ
