email = input("emailinizi daxil edin:")
if " " in email:
    print ("Emailde bosluq var")
elif email.count("@") != 1:
    print ("Email yanlisdir")
elif "." not in email:
    print ("Emailde nuqte yoxdur")
else:
    print ("Email duzgundur")
