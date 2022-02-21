from tkinter import *
from math import sqrt

def nayta(txt):
    """Näyttää tekstin otsikkokohdassa"""
    naytto = Label(text=txt)
    naytto.place(relx=0.5, rely=0.5,anchor=CENTER)
    naytto.pack

def tarkistus():
    """Tarkistaa, haluaako käyttäjä korvata vai lisätä merkin"""
    global txt
    lista = "+-*/"
    utext = ""
    tpituus = len(txt)-1
    if txt[-1] in lista:
        for i in range(0,tpituus):
            utext += str(txt[i])
        txt = utext
        nayta(txt)

def yhteen():
    """Lisää + stringiin"""
    global txt
    tarkistus()
    txt += "+"
    nayta(txt)

def vahennys():
    """Lisää - stringiin"""
    global txt
    txt += "-"
    nayta(txt)


def jako():
    """Lisää / stringiin"""
    global txt
    tarkistus()
    txt += "/"
    nayta(txt)


def kerto():
    """Lisää * stringiin"""
    global txt
    tarkistus()
    txt += "*"
    nayta(txt)

def kirjain_nolla():
    """Lisää 0 stringiin"""
    lisatarkistus()
    global txt
    txt += "0"
    nayta(txt)

def kirjain_yksi():
    """Lisää 1 stringiin"""
    lisatarkistus()
    global txt
    txt += "1"
    nayta(txt)

def kirjain_kaksi():
    """Lisää 2 stringiin"""
    lisatarkistus()
    global txt
    txt += "2"
    nayta(txt)

def kirjain_kolme():
    """Lisää 3 stringiin"""
    lisatarkistus()
    global txt
    txt += "3"
    nayta(txt)

def kirjain_nelja():
    """Lisää 4 stringiin"""
    lisatarkistus()
    global txt
    txt += "4"
    nayta(txt)

def kirjain_viisi():
    """Lisää 5 stringiin"""
    lisatarkistus()
    global txt
    txt += "5"
    nayta(txt)

def kirjain_kuusi():
    """Lisää 6 stringiin"""
    lisatarkistus()
    global txt
    txt += "6"
    nayta(txt)

def kirjain_seiska():
    """Lisää 7 stringiin"""
    lisatarkistus()
    global txt
    txt += "7"
    nayta(txt)

def kirjain_kasi():
    """Lisää 8 stringiin"""
    lisatarkistus()
    global txt
    txt += "8"
    nayta(txt)

def kirjain_ysi():
    """Lisää 9 stringiin"""
    lisatarkistus()
    global txt
    txt += "9"
    nayta(txt)

def pilkku():
    """Lisää . stringiin"""
    global txt
    txt += "."
    nayta(txt)

def neliojuuri():
    """Laskee stringistä neliöjuuren"""
    global txt
    try:
        vastaus = sqrt(float(txt))
        nayta(" "*300)
        nayta(vastaus)
        txt = ""
    except:
        nayta(" "*300)
        nayta("Et voi kertoa nollalla tai käyttää muita laskutoimituksia")

def potenssiinkaks():
    """Laskee stringin potenssiin 2"""
    global txt
    try:
        vastaus = float(txt) * float(txt)
        nayta(" "*300)
        nayta(vastaus)
        txt = ""
    except:
        nayta(" "*300)
        nayta("Et voi kertoa nollalla tai käyttää muita laskutoimituksia")

def pyyhi():
    """Kummaa viimeisen merkin stringistä"""
    global txt
    utext = ""
    tpituus = len(txt)-1
    for i in range(0,tpituus):
        utext += txt[i]
    txt = utext
    nayta(txt)

def tyhjaksi():
    """Tyhjentää stringin täysin"""
    global txt
    nayta(" "*300)
    txt = ""
    nayta(txt)

def sulut():
    """Lisää sulun oikein päin"""
    global txt
    lisatarkistus()
    if txt.count("(") > txt.count(")"):
        txt += ")"
        nayta(txt)
    else:
        txt += "("
        nayta(txt)

def laske():
    global txt
    """Laskee stringistä poimituilla tiedoilla tarvittavat laskutoimitukset"""

    if "/" in txt:  # Tarkistaa minkä laskutoimitus halutaan
        txtlista = txt.split("/")  # Tekee stringistä listan
        ulista = []
        for i in txtlista:
            nro = i.strip("()")  # Putsaa sulut numeroiden ympäriltä
            ulista.append(nro)
        try:  # Koittaa tehdä laskutoimituksen, muuten antaa palautetta
            vastaus = float(ulista[0]) / float(ulista[1])
            nayta(" "*300)
            nayta(vastaus)
            txt = ""
        except TypeError: 
            nayta("Nyt meni jotain pieleen, olenhan vain nelilaskin.")

    elif "*" in txt:  # Tarkistaa minkä laskutoimitus halutaan
        txtlista = txt.split("*")  # Tekee stringistä listan
        ulista = []
        for i in txtlista:
            nro = i.strip("()")  # Putsaa sulut numeroiden ympäriltä
            ulista.append(nro)    
        try:  # Koittaa tehdä laskutoimituksen, muuten antaa palautetta
            vastaus = float(ulista[0]) * float(ulista[1])
            nayta(" "*300)
            nayta(vastaus)
            txt = ""
        except TypeError:
            nayta("Nyt meni jotain pieleen, olenhan vain nelilaskin.")

    elif "+" in txt:  # Tarkistaa minkä laskutoimitus halutaan
        txtlista = txt.split("+")  # Tekee stringistä listan
        ulista = []
        for i in txtlista:
            nro = i.strip("()")  # Putsaa sulut numeroiden ympäriltä
            ulista.append(nro)    
        try:  # Koittaa tehdä laskutoimituksen, muuten antaa palautetta
            vastaus = float(ulista[0]) + float(ulista[1])
            nayta(" "*300)
            nayta(vastaus)
            txt = ""
        except TypeError:
            nayta("Nyt meni jotain pieleen, olenhan vain nelilaskin.")

    elif "-" in txt:  # Tarkistaa minkä laskutoimitus halutaan
        if "(" not in txt:  # Jos laskutoimituksessa ei ole sulkuja
            txtlista = txt.split("-")  # tekee stringistä listan
            try:  # Kokeilee suorittaa laskutoimituksen, muuten antaa palautetta
                vastaus = float(txtlista[0]) - float(txtlista[1])
                nayta(" "*300)
                nayta(vastaus)
                txt = ""
            except TypeError:
                nayta("Nyt meni jotain pieleen, olenhan vain nelilaskin.")
        else:  # Jos on sulkeita
            pituus = len(txt) - 1  # Luo apumuuttujan
            if txt.find(")", 2, pituus) > 0: # Jos sulkeita on ekassa luvussa
                lista = []  # Luo apulistan
                apunro = txt.find(")") + 1  # Luo apumuuttujan alijonon indeksille
                alkio1 = txt[0:apunro]  # Poimii ekan nron stringistä
                lista.append(alkio1.strip("()"))  # ja lisää sen puhtaana listaan
                alkio2 = txt[apunro + 1:]  # Poimii tokan nron stringistä
                lista.append(alkio2.strip("()"))  # ja lisää sen puhtaana listaan
                # Tekee laskutoimituksen ja näyttää sen ruudulla
                vastaus = float(lista[0]) - float(lista[1])
                nayta(" "*300)
                nayta(vastaus)
            else:  # Jos ekassa luvussa ei ole sulkua
                # Tekee samat kuin edellä, mutta putsailee vain viimeisen alkion
                lista = [] 
                apunro = txt.find("(") - 1
                alkio1 = txt[:apunro]
                lista.append(alkio1)
                alkio2 = txt[apunro + 1:]
                lista.append(alkio2.strip("()"))
                vastaus = float(lista[0]) - float(lista[1])
                nayta(" "*300)
                nayta(vastaus)

def lisatarkistus():
    """Tarkastaa, jos stringi on tyhjä ja putsaa näytön aiemmasta"""
    global txt
    if len(txt) == 0:
        tyhjaksi()

# Luo ikkunan
ikkuna = Tk()
ikkuna.title("Nelilaskin")
ikkuna.geometry("500x500")

# Luo ekan otsikon vihreällä tekstillä
otsikko = Label(text="Ninan Nelilaskin", fg="green")
otsikko.pack()
txt = ""  # Luo globaalin muuttujan stringin josta poimitaan laskutoimitukset
# Lisää kaikki hienot nappulat näytölle komentoineen:
plussapainike = Button(ikkuna, text="+", fg="black", bg="grey", command=yhteen, height=2, width=5)
plussapainike.place(x=150,y=20)
miinuspainike = Button(ikkuna, text="-", fg="black", bg="grey", command=vahennys, height=2, width=5)
miinuspainike.place(x=195,y=20)
jakopainike = Button(ikkuna, text="/", fg="black", bg="grey", command=jako, height=2, width=5)
jakopainike.place(x=240,y=20)
kertopainike = Button(ikkuna, text="*", fg="black", bg="grey", command=kerto, height=2, width=5)
kertopainike.place(x=285,y=20)
nro1painike = Button(ikkuna, text="1", fg="black", bg="grey", command=kirjain_yksi, height=2, width=5)
nro1painike.place(x=150,y=61)
nro2painike = Button(ikkuna, text="2", fg="black", bg="grey", command=kirjain_kaksi, height=2, width=5)
nro2painike.place(x=195,y=61)
nro3painike = Button(ikkuna, text="3", fg="black", bg="grey", command=kirjain_kolme, height=2, width=5)
nro3painike.place(x=240,y=61)
nro3painike = Button(ikkuna, text="Kumi", fg="black", bg="grey", command=pyyhi, height=2, width=5)
nro3painike.place(x=285,y=61)
nro4painike = Button(ikkuna, text="4", fg="black", bg="grey", command=kirjain_nelja, height=2, width=5)
nro4painike.place(x=150,y=102)
nro5painike = Button(ikkuna, text="5", fg="black", bg="grey", command=kirjain_viisi, height=2, width=5)
nro5painike.place(x=195,y=102)
nro6painike = Button(ikkuna, text="6", fg="black", bg="grey", command=kirjain_kuusi, height=2, width=5)
nro6painike.place(x=240,y=102)
tyhjennapainike = Button(ikkuna, text="Tyhj", fg="black", bg="grey", command=tyhjaksi, height=2, width=5)
tyhjennapainike.place(x=285,y=102)
nro7painike = Button(ikkuna, text="7", fg="black", bg="grey", command=kirjain_seiska, height=2, width=5)
nro7painike.place(x=150,y=143)
nro8painike = Button(ikkuna, text="8", fg="black", bg="grey", command=kirjain_kasi, height=2, width=5)
nro8painike.place(x=195,y=143)
nro9painike = Button(ikkuna, text="9", fg="black", bg="grey", command=kirjain_ysi, height=2, width=5)
nro9painike.place(x=240,y=143)
summapainike = Button(ikkuna, text="=", fg="black", bg="grey", command=laske, height=2, width=5)
summapainike.place(x=285,y=184)
nro0painike = Button(ikkuna, text="0", fg="black", bg="grey", command=kirjain_nolla, height=2, width=5)
nro0painike.place(x=195,y=184)
pistepainike = Button(ikkuna, text=".", fg="black", bg="grey", command=pilkku, height=2, width=5)
pistepainike.place(x=150,y=184)
juuripainike = Button(ikkuna, text="Sqrt", fg="black", bg="grey", command=neliojuuri, height=2, width=5)
juuripainike.place(x=285,y=143)
potenssipainike = Button(ikkuna, text="^2", fg="black", bg="grey", command=potenssiinkaks, height=2, width=5)
potenssipainike.place(x=240,y=184)
sulutpainike = Button(ikkuna, text="( )", fg="black", bg="grey", command=sulut, height=2, width=5)
sulutpainike.place(x=330,y=184)

# Käynnistää mainloopin, jotta ohjelma näkyy
ikkuna.mainloop()

