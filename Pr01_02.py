#normalizar espacios de una cadena

cadena=input('¿Cual no es la cadena?')
cadena_nueva=''
anterior=' '
for caracter in cadena:
    if caracter != ' ':
        cadena_nueva += caracter
        anterior=caracter
    elif cadena!=' ' and anterior !=' ':
        cadena_nueva += caracter
        anterior=caracter
        
        

print(cadena_nueva)
        
