""" 
  __  __          _____   _____    _____   ____  ____   ____ _______ 
 |  \/  |   /\   |  __ \ / ____|  |  __ \ / __ \|  _ \ / __ \__   __|
 | \  / |  /  \  | |__) | (___    | |__) | |  | | |_) | |  | | | |   
 | |\/| | / /\ \ |  _  / \___ \   |  _  /| |  | |  _ <| |  | | | |   
 | |  | |/ ____ \| | \ \ ____) |  | | \ \| |__| | |_) | |__| | | |   
 |_|  |_/_/    \_\_|  \_\_____/   |_|  \_\\____/|____/ \____/  |_|   
                                                                    
"""  

# IT Betyar 2023.09 | Mars jaro robot

# Definialjuk, hogy a felhasználó milyen karaktereket adhat meg majd:
allowed_characters = 'edkn'
#Észak-dél-kelet-nyugat

# Bekerjuk az irany karaktereket a vezerlo szemelytol
dir = input("Add meg a robot irányát: ")
# dir -> direction

# Ellenorizzuk nincs e ervenyetelen karakter
# Itt jön képbe a python ALL funkciója -> a teljes "dir" tartalmon végigmegy
if all(char in allowed_characters for char in dir):  # --> ennek vagy true v false lesz az eredménye
    count_e = 0
    count_d = 0
    count_k = 0
    count_n = 0
    # ha true (minden karaker oké, akkor létrehozunk számoló konténereket
    # ha FALSE, akkor ez egész IF rész nem igaz:
    # így a ~65sor környéki --> print("Érvénytelen iránymegadás. Kérés megtagadva") részhez ugrik a kód

# majd megszamoljuk a karaktereket
    for letter in dir:
        # print(letter)
        if letter == "e":
            count_e += 1
        if letter == "d":
            count_d += 1
        if letter == "k":
            count_k += 1
        if letter == "n":
            count_n += 1

# Az ellentetes iranyokat semlegesitjuk
    sum_ed = count_e - count_d
    sum_kn = count_k - count_n

# Kiirjuk a vegeredmenyt
    if sum_ed > 0:
        print(F"Észak felé ennyit mozdulunk: {sum_ed}")
    if sum_ed < 0:
        positive_ed = abs(sum_ed)
        print(F"Dél felé ennyit mozdulunk: {positive_ed}")
    if sum_ed == 0:
        print("Észak Dél felé nem mozdulunk!")

    if sum_kn > 0:
        print(F"Kelet felé ennyit mozdulunk: {sum_kn}")
    if sum_kn < 0:
        positive_kn = abs(sum_kn)
        print(F"Nyugat felé felé ennyit mozdulunk: {positive_kn}")
    if sum_kn == 0:
        print("KN felé nem mozdulunk!")

else:

    print("Érvénytelen iránymegadás. Kérés megtagadva")

# itbetyar.hu 2023
# itbetyar.hu 2023
# itbetyar.hu 2023
