password = str(input())
if 6 <= len(password) <= 15:
    resultado = 'True.'

    for k in password:
        if 48 <= ord(k) <= 57 or 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122: pass
        else:
            resultado = 'False.'
            break
        if k != password[0]:
            if ord(k) - 1 == ord(p):
                resultado = 'False.'
                break
        p = k
else: resultado = 'False.'