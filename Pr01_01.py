#sustituir dígitos de una cadena

cadena=input('¿Cual es la cadena?')
cadena_nueva=''

for caracter in cadena:
    if 'A'< caracter:
        cadena_nueva += caracter
    elif '0'<=caracter<='9':
        doble=int(caracter)*2
        cadena_nueva+=str(doble)
print(cadena_nueva)
        
