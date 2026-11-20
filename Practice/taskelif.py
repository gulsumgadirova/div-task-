cpu = int(input("CPU istifade faizini daxil edin:"))
if 0 <= cpu <= 100:
    #ternary operator 
    result = True if cpu < 80 else False
    print (result)
    if 90 <= cpu <= 100:
        print ("Kritik yuk -derhal mudaxile lazimdir:")
    elif 75 <= cpu <= 89:
        print ("Yuksek yuk-monitoringi artirin:")
    elif 40 <= cpu <= 74:
        print ("normal is rejimi")
    else:
        print ("Asagi yuk:")
else:
    print ("CPU istifadesi 0-100 araliginda olmalidir:")










gelir = float(input("Aylig gelirinizi daxil edin:"))
xerc = float(input("Umumi xerclerinizi daxil edin:"))
if xerc < 0 or gelir < 0:
    qalan_pul = gelir - xerc
    if gelir == 0:
        if xercler > 0:
            print ("Budce kesiri var:")
        else:
            print ("Gelir ve xercler sifirdir")
            qenaet_faizi = 0
elif xercler >= gelir * 0.8:
    print ("Xerclere diqqet et:")
elif xercler >= gelir * 0.5:
    print ("Budce normaldir")

