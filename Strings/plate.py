plate = input("Avtomobilin nomresini daxil edin:")
if len(plate) == 9 and plate[2] == "-" and plate[5] == "-":
    print ("Nomre duzgundur")
else:
    print ("Nomre yanlisdir")
