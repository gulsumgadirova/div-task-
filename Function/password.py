def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("ən azı 8 simvol olmalıdır")

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char >= "A" and char <= "Z":
            has_upper = True

        if char >= "a" and char <= "z":
            has_lower = True

        if char >= "0" and char <= "9":
            has_digit = True

    if not has_upper:
        errors.append("ən azı 1 böyük hərf olmalıdır")

    if not has_lower:
        errors.append("ən azı 1 kiçik hərf olmalıdır")

    if not has_digit:
        errors.append("ən azı 1 rəqəm olmalıdır")

    if " " in password:
        errors.append("boşluq olmamalıdır")

    return errors


attempt = 0

while attempt < 3:
    password = input("Şifrə daxil et: ")

    errors = check_password(password)

    if len(errors) == 0:
        print("Şifrə qəbul olundu")
        break

    else:
        for error in errors:
            print(error)

        attempt += 1

if attempt == 3:
    print("Cəhdlər bitdi")