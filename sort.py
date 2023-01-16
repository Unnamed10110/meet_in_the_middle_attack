import timeit #modulo con los metodos para calcular el tiempo
import os #modulo para comandos de sistema, usado durante el desarrolloimport sys
#file=sys.argv
#file=file.pop(1)

start = timeit.default_timer()
# invocacion al comando sort de cygwin64
os.system('c:/cygwin64/bin/sort.exe -u encrypted0.txt> f:/enc-sort-unique.txt')
elapsed = timeit.default_timer() - start
print("--- %s segundos ---" % elapsed)
print("--- %2.20f horas ---" % (float(elapsed) / 3600))

#llamada python sort.py