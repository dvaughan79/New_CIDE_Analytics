# Fecha: agosto 17 2015
# Autor: Daniel Vaughan
# Objetivo: escribir un primer programa sencillo en Python

#---------------------------
# NOTA: el simbolo de # sirve para hacer comentarios.
# Cuando Python ve un # sabe que esa linea no la tiene que ejecutar
# Es recomendable escribir codigos llenos de anotaciones y comentarios.
# ----> Pasa con mucha frecuencia que un tiempo despues de haber escrito el codigo (dias, semanas, meses o anios!)
#       necesitan volver a mirarlo y si no tiene comentarios y explicaciones es imposible entender que hicieron.
#---------------------------

# empecemos inicializando algunas variables
# Digamos que sabemos que la funcion de demanda es lineal: Q = a + bP, donde Q es cantidad, a el intercepto, b la pendiente
# y P el precio

precio     = 10    # tambien podemos comentar aca
pendiente  = -0.5  # Pendiente negativa!  Es una funcion de demanda!
intercepto = 2     # Si el precio es cero, yo solo quiero 2 unidades.

demanda = intercepto + pendiente*precio

# imprimamos la solucion:
print demanda

# Miremos un primer ejemplo de un condicional (veremos mas de esto mas adelante)
if demanda < 5:
    print "La demanda es muy baja, no es rentable entrar a este mercado."
else:
    print "Es rentable!"
