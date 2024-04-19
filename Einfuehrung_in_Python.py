# SEN P1: Einfuehrung_in_Python.py

# Einführung in die Programmiersprache Python

###############################################################################

# Als Entwicklungsumgebung wird Spyder empfohlen. (Teil der Anaconda-
# Distribution, kostenlos erhältlich hier: https://www.anaconda.com/distribution/)

###############################################################################



# Alle offenen Diagrammfenster schließen:
import matplotlib.pyplot as plt
plt.close('all')    



# Allgemeine Python-Befehle
###############################################################################

# Variablen anlegen und verwenden: 
a = 1
b = 15.5
c = a+b
print(c)        # Ausgabe auf der Konsole
erg1 = c*b      # Multiplikation
erg2 = c**b     # Potenz
print('-------------------\n')


# Strings
str1 = "Hello"
str2 = 'World'
str3 = str1 + ", " + str2 + "!"
print(str3)
print(2*str1)
str4 = str(c)       # Umwandlung in String
print("Die Zahl c: " + str4)
print(str1[2:5])
print('-------------------\n')


# Abfragen des Datentyps
print(type(a))
print(type(str1))
print(type(float(str4)))    # Umwandlung von String in Float
print(type(4))              # Integer
print(type(4.))             # Der Punkt nach der Zahl macht aus Integer Float
# => Fazit: Der Datentyp ergibt sich implizit aus der Zuweisung
print('-------------------\n')


# Boolesche Variablen
b1 = 4>3
print(b1)
print(type(b1))
b2 = False
print("OR:", b1 or b2, "; AND:", b1 and b2)
print('-------------------\n')


# Containers (Listen) und Adressierung
v1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(v1)
print(v1[0])        # Adressierung beginnt mit Index 0
print(v1[-1])       # Adressierung des letzten Elements
print(v1[2:4])      # Adressierung einer Submenge (hier: drittes und viertes Element)
print(v1[1:7:2])    # sog. Slicing. Syntax: v1[start:stop:step] -> jeder Parameter ist optional. 
print(v1[:3])       # Alle bis zum dritten Element (d.h. bis einschl. zweites Element)
print(v1[3:])       # Alle nach dem dritten Element
print(v1[::3])      # Jedes dritte Element

v1[4] = 17          # Zuweisung eines neuen Elements
v1[6:8] = [-4, -5]  # Zuweisung zweier neuer Elemente
v1[-1] = "Hallo"    # Die Elemente einer Liste können unterschiedliche Datentypen haben
print(v1)
print(v1[-1])
print(type(v1))
print('-------------------\n')


# Besonderheit bei Listen (gilt auch für NumPy-Arrays - siehe weiter unten)
a = [1, 2, 3, 4]    # Anlegen der Liste
b = a               # Speichern der Liste in eine weitere Variable
print(a)            # Was steht in a?
print(b)            # Was steht in b?
a[2] = -1           # Ändern eines Elements in a
print(a)            # Was steht in a?
print(b)            # Was steht in b?
# => Fazit: a und b sind nur zwei Zeiger auf denselben Speicherbereich!
c = a.copy()        # Will man eine Liste in einen neuen Speicherberiech kopieren, so geht dies mit der Funktion copy()
a[3] = 99
print(a)            # Was steht in a?
print(c)            # Was steht in c?
print(a is b)       # Zeigen a und b auf denselben Speicherbereich?
print(a is c)       # Zeigen a und c auf denselben Speicherbereich?
print('-------------------\n')



# if-else-Anweisung
a = 5
if a == 10:
    print("Pfad if")
elif a == 2:
    print("Pfad elif")
else:               # "elif" und "else" sind optional
    print("Pfad else")
print('-------------------\n')
    

# for-Schleife
for i in range(2,6):     # Schleife von 2 bis 6 (nicht einschließlich)
    print(i)
        
# Doppelte for-Schleife
for m in range(3):
    for n in range(2,5):
        print(m,n)
                
print('-------------------\n')
          
        
# while und break
x = 5
while x < 15:
    x = x + 1
    print(x)
    if (x == 11):
        break
    
print('-------------------\n')



# Funktionen
def test_function_1():              # Definition der Funktion
    print("In test_function_1")
    
test_function_1()       # Aufruf der Funktion

print('-------------------\n')



def add_function(x1, x2):           # Definition einer Funktion mit Übergabeparametern
    return x1 + x2

print(add_function(5, 7))

print('-------------------\n')


import function_file                  # Importieren eines Moduls
function_file.test_function_2(1, 2)   # Aufrufen einer Funktion in diesem Modul

print('-------------------\n')


# Numerische Berechnungen mit NumPy
###############################################################################

# Anlegen von Arrays
import numpy as np                  # NumPy Bibliothek laden
a = np.array([1, 2, 3, 4, 5])       # Anlegen eines 1D-Arrays
print(a)
print(type(a))
print(a[2]/2)

b = np.arange(5, 16, 2)             # Linear skalierter Vektor. Syntax: np.arange(start, stop, step)
print(b)

c = np.linspace(1, 7, 15)           # Weitere Möglichkeit. Syntax: np.linspace(start, stop, NumberOfElements)
print(c)

d = np.array([[1, 2, 3], [4, 5, 6]])    # Anlegen eines 2D-Arrays. Wichtig sind die doppelten eckigen Klammern.
print(d)
print(d[1,2])                       # Adressierung
print(np.transpose(d))              # Matrix transponieren

a = np.array([1, 2, 3, 4, 5])       # Anlegen eines 1D-Arrays
a_list = [1, 2, 3, 4, 5]            # Liste zum Vergleich anlegen
print(2*a)
print(2*a_list)                     # Man beachte den Unterschied von np-Arrays zu gewöhnlichen Listen
b = a + 1                           # Durch die Rechnung (+1) wird das Ergebnis an einen neuen Speicherplatz geschrieben
print(a)
print(b)
print(a*b)
print(np.mean(a))                   # Mittelwert

print('-------------------\n')

# Spezielle Matrizen und Formen
e = np.ones((3,3)); print(e)        # Matrix aus Einsen
f = np.zeros(4); print(f)           # Vektor aus Nullen
g = np.eye(5); print(g)             # Einheitsmatrix
h = np.random.rand(5)               # Zufallsvariablen (gleichverteilt zwischen 0 und 1)
i = np.random.randn(5)              # Zufallsvariablen (normalverteilt)
j = np.random.randint(3,13,8)       # Zufallsvariablen (Integerwerte: 8 Werte zwischen 3 und 13 (exklusive) )
print(e.shape)                      # Abmessungen der Matrx
print(e.shape[0])                   # Anzahl der Zeilen in der Matrix
print(e.size)                       # Anzahl der Elemente in der Matrix

print('-------------------\n')

# Vektor transponieren
a2 = a[:, np.newaxis]				# Aus Zeilenvektor Spaltenvektor machen
print(a)
print(a2)

print('-------------------\n')


# Dictionaries
###############################################################################
tel = {"Heinz" : 28197, "Fritz" : 39877}    # Hash-Tabelle mit Schlüsseln (Keys) und dazugehörigen Werten (Values)
print(tel)
tel["Eva"] = 32988          # Neuer Eintrag 
print(tel)

print(tel["Fritz"])         # Adressierung mittels Key

print(tel.keys())           # Keys
print(tel.values())         # Values

# Schleife über ein Dictionary
for i in tel:
    print("Name:", i, "=> Telefonnummer:", tel[i])
    
print('-------------------\n')



# Data-Frames mit Pandas
###############################################################################
import pandas as pd
# Erstelle einen einfachen Datensatz mit Personen
data = {'Name': ["John", "Anna", "Peter", "Linda"],
'Location' : ["New York", "Paris", "Berlin", "London"],
'Age' : [24, 13, 53, 33]
}
print(data)
data_pandas = pd.DataFrame(data)    # Umwandeln in ein Pandas Data-Frame
print(data_pandas)

# Beispiel für eine einfache Anfrage an den Data-Frame: Wähle alle Zeilen mit 
# einem Wert für age größer 30 aus
print('Older than 30: \n', data_pandas[data_pandas.Age > 30])

print('-------------------\n')


# Graphiken darstellen mit Matplotlib
###############################################################################
import matplotlib.pyplot as plt     # Import der Bibliothek
x = np.linspace(-np.pi, np.pi, 256) # Anlegen eines np-Arrays
c, s = np.cos(x), np.sin(x)         # Berechnen von Vektoren 
plt.figure()                        # Neue Figure öffnen
plt.plot(x, c, label="cosinus")     # Plotten der ersten Kurve
plt.plot(x, s, label="sinus")       # Plotten der zweiten Kurve
plt.legend()                        # Legende
plt.xlabel('t [s]')
plt.ylabel('U [V]')
                                     
x = np.linspace(1,10,100)           # Vektor
y1 = 5*np.random.randn(x.size)+5    # Zufallsvektor 
y2 = -3*np.random.randn(x.size)-7   # Anderer Zufallsvektor 
plt.figure()
plt.scatter(x, y1, color="green")
plt.scatter(x, y2, color="red")




# Übungen: 
###############################################################################

# Vektoren: 

# Geben Sie den Vektor (1, 2, 3, ..., 15) als np-Array mit dem Variablennamen "v1" in Python ein. 
v1 = np.arange(1., 16, 1)   # Der Punkt nach der 1 ist wichtig, damit die Elemente des Vektors als "Float"-Variable angelegt werden.

# Stellen Sie v1 rückwärts dar.
print(v1[::-1])         # Vorsicht: v1[-1:0:-1] funktioniert nicht, da die '0' nicht mitgezählt wird. v1[-1::-1] hingegen funktioniert.
print(np.flip(v1))      # Andere Möglichkeit

# Überschreiben Sie in v1 den dritten Wert mit der Zahl -12,33.
v1[2] = 12.33
print(v1)

## Überschreiben Sie das vorletzte Element in v1 mit der Zahl 99.
v1[-2] = 99
print(v1)

# Welchen Datentyp hat v1?
print(type(v1))

# Welchen Datentyp hat das vierte Element von v1?
print(type(v1[3]))

# Finden Sie heraus, wie Sie ein neues Element mit dem Wert 2,5 am Ende des Vektors v1 einfügen können. 
v1 = np.append(v1, [2.5])
print(v1)

# Finden Sie heraus, wie sich das dritte bis fünfte Element des Vektors v1 löschen lässt. 
v1 = np.delete(v1, [2,3,4])
#v1 = np.delete(v1, np.array([2,3,4]))      # Andere Möglichkeit
#v1 = np.delete(v1, np.arange(2,5))         # Andere Möglichkeit
print(v1)

# Wieviele Elemente besitzt v1?
print(v1.size)

print('-------------------\n')

# ------------------------------------------------------

# Komplexe Zahlen:

# Finden Sie heraus, wie sich die komplexe Zahl z = 3,5-7j in Python eingeben lässt.
z = 3.5-7j
print(z)

# Welchen Datentyp hat die Variable z?
print(type(z))

print('-------------------\n')

# ------------------------------------------------------

# Matrizen: 

# Erzeugen Sie (möglichst elegant) eine 4x4-Matrix mit lauter Nullen und den Zahlen (1, 2, 3, 4) in der Hauptdiagonalen.
A = np.eye(4) * (np.arange(4)+1)
print(A)

# Ändern Sie das Element in Spalte 3 und Zeile 2 auf den Wert 7.
A[1,2] = 7
print(A)

print('-------------------\n')

# ------------------------------------------------------
#
# Graphik:

# Erzeugen Sie die Vektoren s1 = x^2 und s2 = x^3 für Werte von x zwischen -3 und 3.
x = np.linspace(-3, 3, 200)
s1 = x**2
s2 = x**3

# Stellen Sie sowohl s1 als auch s2 als Funktion von x in demselben Diagramm dar.
plt.figure()
plt.plot(x, s1)
plt.plot(x, s2)

# Beschriften Sie die Achsen mit "x-Achse" und "y-Achse".
plt.xlabel("x-Achse")
plt.ylabel("y-Achse")