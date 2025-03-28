def createUsers () -> dict:
    l, p = [], []

    while True:
        login = input("Podaj login")
        if login == "STOP": 
            break
        passw = input("Podaj haslo")
        if passw == "STOP":
            break
        l.append(login)
        p.append(passw)

    return {login: passw for login, passw in zip(l, p)}
