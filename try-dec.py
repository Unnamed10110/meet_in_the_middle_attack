import timeit #modulo con los metodos para calcular el tiempo
import os #modulo para comandos de sistema, usado durante el desarrollo
from Crypto.Cipher import DES #modulo de implementacion de DES
#import DES
#Texto claro: ABCDEF1234567899
#Texto cifrado: 089CD1AEBAC3B557
c1=0
cipher="089CD1AEBAC3B557".decode('hex')#texto cifrado dado
start = timeit.default_timer()
with open('keys2.txt', 'r') as file:
    with open('decrypted2.txt', 'w') as fdec:
        while True:
			#lectura de linea
            linea=file.readline()
			#condicion de fin de ciclo
            if not linea: break
            key=linea
			#se quita el salto de linea
            key=key.strip()
            key = key.decode('hex')
			#configuracion de parametros del descifrado
            d = DES.new(key, DES.MODE_ECB)
			#generacion de texto cifrado intermedio
            des = d.decrypt(cipher)
			#escritura el el archivo
            fdec.write(des.encode('hex'))
            fdec.write('\n')

elapsed = timeit.default_timer() - start
print("--- %s segundos ---" % elapsed)
print("--- %2.20f horas ---" % (float(elapsed)/3600))


'''
print "--encrypted(hex): %s" % d.encode('hex')
print "--decrypted(hex): %s" % k.decrypt(d).encode('hex')
print "Encrypted: %r" % d
print "Decrypted: %r" % k.decrypt(d)

assert k.decrypt(d, padmode=PAD_NORMAL) == plain
'''