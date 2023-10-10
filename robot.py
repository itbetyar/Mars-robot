# IT Betyar 2023.09 | Mars jaro robot

# a megadhato karakterek:
allowed_characters = 'edkn'

# Bekerjuk az irany karaktereket a vezerlo szemelytol
dir = input("Add meg a robot irányát: ")

# Ellenorizzuk nincs e ervenyetelen karakter
if all(char in allowed_characters for char in dir):
    count_e = 0
    count_d = 0
    count_k = 0
    count_n = 0

# megszamoljuk a karaktereket
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