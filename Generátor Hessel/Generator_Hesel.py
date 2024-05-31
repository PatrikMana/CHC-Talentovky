import eel  # import knihovny eel pro spojení Pythonu s webovými technologiemi
import random #import knihovny random pro náhodné generování

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}$@/*()%.,!?:_&#"

string =  lower + upper + numbers + symbols

eel.init(".")

@eel.expose # vyvolání funkce z JavaScriptu
def password_generator(length):
    if length != "":
        password = "".join(random.sample(string,int(length))) # vygenerování náhodného hesla
        if int(length) <= 7:
            return "Každé heslo musí obsahovat alespoň 8 znaků."
        return "Vaše nové heslo je: " + password
    else:
        return "Nezadali jste počet znaků."

# Spuštění webové aplikace
eel.start("index.html", size=(800, 600))