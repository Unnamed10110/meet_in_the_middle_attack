# meet_in_the_middle_attack

## Características de la máquina 
 
### -	Información del Sistema 
 
Nombre de la máquina: ACER 
 
Sistema Operativo: Windows 10 Pro 64-bit 
 
Idioma: español (Configuración regional: español) 
 
Fabricante del Sistema: HACER 
 
Modelo del Sistema:  TravelMate P246M-M 
 
BIOS: V1.06 
 
Procesador: Intel(R) Core(TM) i7-4712MQ CPU @ 2.30GHz (8 CPUs), ~2.3GHz 
 
Memoria: 8192MB RAM 
 
Memoria de SO disponible: 8116MB RAM 
 
 	 
### -	Códigos:(* Los archivos fuentes se adjuntan al archivo .zip, en subcarpeta 
‘codigo’) 
 
-	bin-search.py: realiza la búsqueda binaria sobre el archivo que contiene los textos intermedios descifrados. 
 
-	keygen2.py:genera todas las claves posible para realizar el ataque (2^28 claves ) 
 
-	sort.py: realiza la invocación al comando sort para el ordenamiento e indica el tiempo de ejecución. 
 
-	try-dec.py: realiza el descifrado con las claves generadas con keygen2.py y el texto cifrado dado. 
 
-	try-enc.py: realiza el cifrado con las claves generadas con keygen2.py y el texto plano dado. 
 
-	OBS.: Los códigos se encuentran documentados con comentarios explicativos de la implementación. 
Detalles de implementación: 
-	Lenguaje: Python3.5 (para la generación de claves, invocación de ordenamiento y búsqueda) y Python2.7 (para el cifrado y descifrado) 
 
-	Entorno de Desarrollo (IDE): PyCharm 2016.1 
 
-	Extensiones:  	.py (pueden leerse como texto plano) 
 
### -	Configuración de Python (módulos y sus versiones):  
o	Crypto==1.4.1  	(contiene la implementación de DES) 
 
o	numpy==1.11.0(requerido para multiprocessing) 
 
o	pycrypto==2.6.1 (configuración de Crypto) 
 
o	virtualenv==15.0.1 (entorno virtual para pruebas con otras configuraciones) 
 
-	Cygwin: colección de herramientas GNU para Windows (se utilizó la herramienta “sort” para el ordenamiento (ordenamiento externo-merge)) 
 
-	EmEditor: editor de texto, similar a notepad++ pero con capacidad de manejo de archivos superiores a 1GB. Utilizado para verificar las posiciones de las claves encontradas. 
### Descripción breve del proceso 
 
1-	) Se generan las 2^28 claves posibles (descartando los bits innecesarios). 
 
2-	) Con ellas se generan los textos cifrados intermedios y los texto descifrados intermedios, en archivos separados. Para ello se utiliza el módulo Pycrypto, con su método DES en modo ECB. 
 
3-	) Luego, se ordena uno de los archivos (encrypted2.txt) para realizar la búsqueda binaria sobre él y encontrar una coincidencia. Para ello se utiliza el comando sort de Cygwin64, que realiza el ordenamiento (ordenamiento externo. 
 
4-	) Entonces se realiza la búsqueda binaria con cada texto posible hasta encontrar una coincidencia. 
 
5-	) Una vez obtenida la coincidencia, es decir, el texto intermedio del texto cifrado dado y el texto plano dado, se buscan las claves correspondientes de acuerdo a sus posiciones en los archivos originales. 
 
### Tiempos de Ejecución: 
-	keygen2.py (generador de claves): 
 
  ![image](https://user-images.githubusercontent.com/28940464/212666398-012d38e4-11b1-46b0-8c72-910713d6b1e9.png)

 	 
 
-	try-enc.py (generador de los textos intermedios cifrados a partir del texto plano dado) 
 
  ![image](https://user-images.githubusercontent.com/28940464/212666446-10bdef9a-16fd-483d-bf79-fa5f8537bab4.png)

 
-	try-dec.py (generador de los textos intermedios descifrados a partir del texto cifrado dado ) 
 ![image](https://user-images.githubusercontent.com/28940464/212666917-00e0d37e-fd65-4312-82e7-3ced12f1a727.png)

 
-	sort.py (invoca a la herramienta sort de Cygwin, para el ordenamiento y indica el tiempo de ejecución) 
  ![image](https://user-images.githubusercontent.com/28940464/212666796-ed486c4b-0a63-4c99-950c-ce755135e743.png)

 
-	bin-search.py (realiza una búsqueda binaria sobre el archivo ordenado e indica el texto intermedio que coincide) 
 ![image](https://user-images.githubusercontent.com/28940464/212667283-77fd57b7-8473-4e75-bf46-d69d60375f8e.png)

  
 
### Detalles de los archivos generados 
  ![image](https://user-images.githubusercontent.com/28940464/212667313-b891ca79-f5db-49fd-98e9-36f236fde926.png)

-	‘keys2.txt’: Contiene todas la claves generadas por keygen2.py (2^28 líneas) 
 
-	‘encrypted2.txt’: Contiene todos los textos cifrados intermedios, obtenidos con las claves de keys2.txt y el texto plano dado. (2^28 líneas) 
 
-	‘decrypted2.txt’: Contiene todos los textos descifrados intermedios, obtenidos con las claves de keys2.txt y el texto cifrado dado. (2^28 líneas) 
 
-	‘middle2.txt’: Contiene la coincidencia encontrada entre ‘decrypted2.txt’ y ‘encsort2.txt’, la cual es el texto intermedio buscado a partir del cual se saben las claves. 
 	 
### Coincidencia encontrada 
-	El texto intermedio obtenido es:[766a7d4a9886bce1] 
 ![image](https://user-images.githubusercontent.com/28940464/212667337-b2ba217e-85de-480e-920f-3debac7c3af2.png)

  
-	Posición de la primera clave (se deduce de la posición original de la coincidencia en ‘encrypted2.txt’, es decir, la clave está en la misma posición en ‘keys2.txt’) 
Posición de la coincidencia (‘encrypted2.txt’): 

  ![image](https://user-images.githubusercontent.com/28940464/212667362-97260772-c96c-4ee5-9c6f-47444810b80c.png)

Clave1 (‘keys2.txt’): [00000000606EC89E] 

  ![image](https://user-images.githubusercontent.com/28940464/212667407-6dee8116-6300-4786-b89b-12a4bfdcf0b9.png)

 
-	Posición de la segunda clave (se deduce de la posición original de la coincidencia en ‘decrypted2.txt’, es decir, la clave está en la misma posición en ‘keys2.txt’) 
Posición de la coincidencia (‘decrypted2.txt’) 

  ![image](https://user-images.githubusercontent.com/28940464/212667434-36dd37c0-4eac-469d-9583-74bccaf13a25.png)

Clave2 (‘keys2.txt’): [00000000A256EE8C] 

  ![image](https://user-images.githubusercontent.com/28940464/212667445-87871e17-f42d-4ae9-9f30-b8cc7f71d790.png)

 
*Obs.: Para obtener las posiciones de la coincidencia en ‘encrypted2.txt’ y ‘decrypted2.txt’, simplemente se utilizó el EmEditor. 
### Resumen 
-	Texto plano: ABCDEF1234567899 
Claves: 
	[00000000606EC89E] 
	[00000000A256EE8C] 
 
-	Texto cifrado: 089CD1AEBAC3B557 
### - Verificación 
  
![image](https://user-images.githubusercontent.com/28940464/212667485-3ad13f0d-d144-4529-9db4-c281bef7bfe6.png)
