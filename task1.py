import maskpass
passwd_1 = maskpass.advpass(prompt="Введите пароль: ", mask="*")
passwd_2 = maskpass.advpass(prompt="Введите пароль еще раз: ", mask="*")
if passwd_1 == passwd_2:
    print('Пароль принят')
else:
    print('Пароль не принят')
