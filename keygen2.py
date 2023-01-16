import timeit#modulo con los metodos para calcular el tiempo
import os#modulo para comandos de sistema, usado durante el desarrollo
from multiprocessing import *#modulo para multiprocesamiento
from multiprocessing import process
import multiprocessing as mp


def keygen():
    add1 = '10'#sumando binario
    c2 = 0
    # va='1111111*2222222*3333333*4444444*5555555*6666666*7777777*8888888*'  ->guia para las posiciones de los bits
    var = '0000000000000000000000000000000000000000000000000000000000000000'#variable a incrementar
    file = open('keys-prueba.txt', 'w')
    start = timeit.default_timer()
    # for c inss range(0,n):

    while var[31] != '1':
        #condiciones de desplazamiento de bits (para generar exactamente 2exp(28) claves)
        if var[55] == '1':
            var = int(bin(int('100000000', 2) + int(var, 2)), 2)
            var = '{:064b}'.format(var)
        if var[47] == '1':
            var = int(bin(int('10000000000000000', 2) + int(var, 2)), 2)
            var = '{:064b}'.format(var)
        if var[39] == '1':
            var = int(bin(int('1000000000000000000000000', 2) + int(var, 2)), 2)
            var = '{:064b}'.format(var)
        if var[31]=='1': break
		#se escribe la clave en el archivo
        file.write('%016X\n' % int(var, 2))
		#se incrementa la variable
        var = int(bin(int(add1, 2) + int(var, 2)), 2)
		
        #se reformatea la variable para tratarla de nuevo como un string
        var = '{:064b}'.format(var)
        if var[31] == '1':
            print("Todas la claves han sido generadas")

    elapsed = timeit.default_timer() - start
    print("---  %s segundos     ---" % elapsed)
    print("---  %2.20f horas    ---" % (float(elapsed) / 3600))
    os.system('pause')


if __name__ == '__main__':
    # p = Pool(4)
    # p.map(keygen(),'')
    p = Process(keygen())
    # p=mp.process(target=keygen())
    # p.daemon=True
    p.start()
    p.join()

    # keygen()
