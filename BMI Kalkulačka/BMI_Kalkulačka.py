import eel  # import knihovny eel pro spojení Pythonu s webovými technologiemi

# Nastavení cesty k HTML souborům
eel.init(".")  

@eel.expose  # vyvolání funkce z JavaScriptu
def bmi_calculator(height, weight):  # funkce přijímá vstupy height (výška) a weight (hmotnost)
    if height != "":
        if weight != "":
            bmi = int(weight)/((int(height)/100)**2)  # výpočet BMI
            if bmi < 18.5:
                return "Vaše BMI je " + format(bmi, ".1f") + " (Podváha)"  
            elif bmi > 18.5 and bmi < 24.9:
                return "Vaše BMI je " + format(bmi, ".1f") + " (Normální)"
            elif bmi > 24.9 and bmi < 29.9:
                return "Vaše BMI je " + format(bmi, ".1f") + " (Nadváha)" 
            elif bmi > 30 and bmi < 200:
                return "Vaše BMI je " + format(bmi, ".1f") + " (Obezita)"
            else:
                return "Něco se pokazilo."
        else:
            return "Nezadali jste váhu." 
    else:
        return "Nezadali jste výšku."

# Spuštění webové aplikace
eel.start("index.html", size=(800, 600))