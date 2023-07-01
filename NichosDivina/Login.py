from PyQt5 import QtWidgets, uic
import sqlite3
#from PyQt5 import QMainWindow



import sys

app = QtWidgets.QApplication([])
#conexion bd
conexion = sqlite3.connect('NichosDivina.db')

login = uic.loadUi("V1.ui")
entrar = uic.loadUi("V2.ui")
error = uic.loadUi("V3.ui")
gestion = uic.loadUi("V5.ui")



#ingreso de datos

def gui_login():
    user = login.lineEdit.text()
    password = login.lineEdit_2.text()
    if len(user)==0 or len(password)==0:
        login.label_5.setText("Ingrese todos los datos")
        
    elif user == "America" and password == "12345":
        gui_entrar()
    else :
        gui_error()

def gui_entrar():
    login.hide()
    entrar.show()
    
def gui_error():
    login.hide()
    error.show()
    entrar.hide()
    
def gui_gestion():
    entrar.hide()
    gestion.label_31.setText("")
    gestion.show()
    #pruebas
    gestion.lineEdit.clear()
    gestion.lineEdit_2.clear()
    gestion.lineEdit_3.clear()
    gestion.lineEdit_4.clear()
    gestion.lineEdit_5.clear()
    gestion.lineEdit_6.clear()
    gestion.lineEdit_7.clear()
    gestion.lineEdit_8.clear()
    gestion.lineEdit_9.clear()
    gestion.lineEdit_10.clear()
    gestion.lineEdit_11.clear()
    gestion.lineEdit_12.clear()
    gestion.lineEdit_14.clear()
    gestion.label_31.clear()
    gestion.lineEdit_13.clear()
    
    
def gui_regresarError ():
    error.hide()
    login.label_5.setText("")
    login.show()
def gui_regresarGestion ():
    gestion.hide()
    entrar.show()
    
def gui_regresarEntrar():
    entrar.hide()
    login.show()
    
def salir():
    app.exit()
    
def bton_limpiar():
    gestion.lineEdit.clear()
    gestion.lineEdit_2.clear()
    gestion.lineEdit_3.clear()
    gestion.lineEdit_4.clear()
    gestion.lineEdit_5.clear()
    gestion.lineEdit_6.clear()
    gestion.lineEdit_7.clear()
    gestion.lineEdit_8.clear()
    gestion.lineEdit_9.clear()
    gestion.lineEdit_10.clear()
    gestion.lineEdit_11.clear()
    gestion.lineEdit_12.clear()
    gestion.lineEdit_14.clear()
    gestion.label_31.clear()
    gestion.lineEdit_13.clear()
    
    
def bton_guardar():

    NumeroNicho1 = gestion.lineEdit.text()
    NombrePropietario1 = gestion.lineEdit_2.text()
    TelefonoPropietario1 = gestion.lineEdit_3.text()
    DomicilioPropietario1 = gestion.lineEdit_4.text()
    NombreContactoReferencia1 = gestion.lineEdit_6.text()
    TelefonoContactoReferencia1 = gestion.lineEdit_5.text()
    NombreFinado1 = gestion.lineEdit_8.text()
    DatosFinado1 = gestion.lineEdit_7.text()
    FechaIngreso1 = gestion.lineEdit_10.text()
    FechaSalida1 = gestion.lineEdit_9.text()
    EstatusNicho1 = gestion.lineEdit_12.text()
    PagoNicho1 = gestion.lineEdit_11.text()
    Notas1 = gestion.lineEdit_14.text()
    
  
    cursor = conexion.cursor()
    if cursor.execute("SELECT * FROM Nichos WHERE NumeroNicho = ?", ((NumeroNicho1),)).fetchone():
        gestion.label_31.setText("El nicho ya esta registrado")
        
    elif len(NombrePropietario1) <= 2:
        gestion.label_31.setText("Introduzca un nombre de propietario valido!!")
    elif len(TelefonoPropietario1) <= 2:
        gestion.label_31.setText("Introduzca un telefono del propietario valido!!")
    elif len(DatosFinado1) <= 2:
        gestion.label_31.setText("Introduzca los datos del finado !!")
    elif len(NumeroNicho1) >= 1:
        cursor.execute("INSERT INTO Nichos Values (?,?,?,?,?,?,?,?,?,?,?,?,?)",(NumeroNicho1, NombrePropietario1, TelefonoPropietario1, DomicilioPropietario1, NombreContactoReferencia1, 
                                                                            TelefonoContactoReferencia1, NombreFinado1, DatosFinado1, FechaIngreso1, FechaSalida1, EstatusNicho1, 
                                                                            PagoNicho1, Notas1,))
        conexion.commit()
        cursor.close()
    #conexion.close()
        bton_limpiar()

def bton_buscar(numeroNichoBuscar):
    numeroNichoBuscar = gestion.lineEdit_13.text()
    numeroNichoBuscar = str("'" + numeroNichoBuscar + "'")
     
    #busqueda en sqlite
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Nichos WHERE NumeroNicho = '{}'".format(numeroNichoBuscar))
    numeroNichoB = cursor.fetchall()
    cursor.close()
    if numeroNichoB:
        gestion.label_32.setText(f'Nombre propietario: {numeroNichoB[0][1]}')
    else:
        gestion.label_32.setText('No se encontro')
        
        
    
    

    
    
    
    
    
    
    
    

    
    
#def bton_buscar():
    
      
    
#funcines


login.pushButton.clicked.connect(gui_login)

login.pushButton_2.clicked.connect(salir)

error.pushButton_3.clicked.connect(gui_regresarError)
error.pushButton_2.clicked.connect(salir)

entrar.pushButton_3.clicked.connect(gui_gestion)
entrar.pushButton_2.clicked.connect(salir)
gestion.pushButton_2.clicked.connect(salir)
gestion.pushButton_3.clicked.connect(gui_regresarGestion)
entrar.pushButton_4.clicked.connect(gui_regresarEntrar)

gestion.pushButton_5.clicked.connect(bton_limpiar)
gestion.pushButton_4.clicked.connect(bton_guardar)
gestion.pushButton.clicked.connect(bton_buscar)





    



#ejecucion de app
login.show()
app.exec()
