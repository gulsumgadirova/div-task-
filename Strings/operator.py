number = input("Nomrenizi daxil edin:")
number = number.replace(" ", "")
number = number.replace("-","")
if len (number) != 10:
        print ("Nomre yanlisdir")
elif number[:3] == "050" or number[:3] == "051" or number[:3] == "010":
        print ("Azercell")
elif number[:3] == "055" or number[:3] == "099":
        print ("Bakcell")
elif number[:3] == "070" or number[:3] == "077":
        print ("Nar")
else:
 print ("Namelum nomre")
