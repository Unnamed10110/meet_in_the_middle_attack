import timeit #modulo con los metodos para calcular el tiempo
import os #modulo para comandos de sistema, usado durante el desarrollo
from multiprocessing import * #modulo para multiprocesamiento
import mmap # modulo para mapear en memoria el archivo enc-sor2.txt
def search():
    result = open('middle2.txt', 'w') #archivo de resultado
    c1 = 0

    startt = timeit.default_timer() #variable de tiempo
    with open('decrypted2.txt', 'r') as file:
        fpt=open('enc-sort2.txt', 'rb')
        fptr = mmap.mmap(fpt.fileno(), 0, access=mmap.ACCESS_READ) # mapeo en memoria del archivo no ordenado
        while True:
			#posicionamiento de los punteros para la busqueda binaria
            start = pos = 0 
            end = os.path.getsize('enc-sort2.txt')
			#lectura de una linea del archivo
            matchvalue = file.readline()
			#condiciones de fin de ciclo
            if not matchvalue: break
            if c1==2: break
			#se quita del texto la \n
            matchvalue = matchvalue.strip()
			#ciclo de busqueda binaria, un maximo de busqueda,por cada clave, de  log2(2exp(28))=28
            for rpt in range(28):
				#ajuste de punteros
                last = pos
                pos = start + int(((end - start) / 2))
                fptr.seek(pos)

                fptr.readline()
                line = fptr.readline()
                linevalue = line.strip()
                linevalue=linevalue.decode("utf-8")
				#condicion de aceptacion de clave
                if linevalue == matchvalue or pos == last:

                    if linevalue == matchvalue:
                        print('::::::   coincidencia encontrada: ')
                        print('linevalue: ', linevalue, '\nmatchvalue: ', matchvalue)
                        result.write(linevalue)
                        result.write('\n')
                        c1=2
                        break
				#ajuste de punteros
                elif linevalue < matchvalue:
                    start=pos+1
                else:
                    assert linevalue > matchvalue
                    end=pos-1
	# tiempos de ejecucion en horas y segundos
    elapsed = timeit.default_timer() - startt
    print("---+ %s segundos ---" % elapsed)
    print("---+ %2.20f horas ---" % (float(elapsed)/3600))

#main
if __name__ == '__main__':
    # p = Pool(4)
    # p.map(keygen(),'')
    # p=mp.process(target=keygen())
    # p.daemon=True
    p = Process(search())
    p.start()
    p.join()
    #search()

    # keygen()


'''
print "--encrypted(hex): %s" % d.encode('hex')
print "--decrypted(hex): %s" % k.decrypt(d).encode('hex')
print "Encrypted: %r" % d
print "Decrypted: %r" % k.decrypt(d)

assert k.decrypt(d, padmode=PAD_NORMAL) == plain
'''