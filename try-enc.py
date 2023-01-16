import timeit  #modulo con los metodos para calcular el tiempo
import os #modulo para comandos de sistema, usado durante el desarrollo
from multiprocessing import *
from multiprocessing import process
import multiprocessing as mp
import binascii
from Crypto.Cipher import DES#modulo de implementacion de DES
#Texto claro: ABCDEF1234567899
#Texto cifrado: 089CD1AEBAC3B557
c1=0
plain="ABCDEF1234567899".decode('hex')#texto plano dado
def enc():
    start = timeit.default_timer()
    with open('keys2.txt', 'r') as file:
        with open('encrypted2.txt', 'w') as fenc:
            while True:
				#lectura de linea
                linea=file.readline()
				#condicion de fin de ciclo
                if not linea: break
                key=linea
                key=key.strip()
                key=key.decode('hex')
				#configuracion de parametros del cifrado
                d = DES.new(key, DES.MODE_ECB)
				#generacion de texto descifrado intermedio
                des=d.encrypt(plain)
                fenc.write(des.encode('hex'))
                fenc.write('\n')

    elapsed = timeit.default_timer() - start
    print("--- %s segundos ---" % elapsed)
    print("--- %2.20f horas ---" % (float(elapsed)/3600))

if __name__ == '__main__':
    #p = Pool(4)
    #p.map(keygen(),'')
    p=Process(enc())
    #p=mp.process(target=keygen())
    #p.daemon=True
    p.start()
    p.join()

    #keygen()


'''
print "--encrypted(hex): %s" % d.encode('hex')
print "--decrypted(hex): %s" % k.decrypt(d).encode('hex')
print "Encrypted: %r" % d
print "Decrypted: %r" % k.decrypt(d)

assert k.decrypt(d, padmode=PAD_NORMAL) == plain
'''