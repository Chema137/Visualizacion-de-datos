import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Alumnos_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Almazan\OneDrive\Escritorio\4TO SEMESTRE\VISUALIZACION\Evidencia 3\Alumnos.ui", self)
        

       
    def fn_activar(self):

        self.chk_activo.setChecked(True)
        self.chk_inactivo.setChecked(False)
        self.btn_Desactivar.setEnabled(True)
        self.btnActivar.setEnabled(False)
        self.lbl_estado.setText("ACTIVADO")
        self.edt_info.setText("ACTIVADO")
    def fn_desactivar(self):
        
        self.chk_activo.setChecked(False)
        self.chk_inactivo.setChecked(True)

        self.btn_Desactivar.setEnabled(False)
        self.btnActivar.setEnabled(True)

        self.lbl_estado.setText("DESACTIVADO")
        self.edt_info.setText("DESACTIVADO")   
         
#Generacion de Funcion Grabar CSV
    def fn_limpiar(self):
        self.edt_matricula.clear()
        self.edt_nombre.clear()
        self.edt_apppat.clear()
        self.edt_appmat.clear()
        self.edt_domicilio.clear()
        self.chk_prog.setChecked(False)
        self.chk_bd.setChecked(False)
        self.chk_contab.setChecked(False)                
        self.chk_estadistica.setChecked(False)
        self.chk_inv_op.setChecked(False)                
        self.chk_foraneo.setChecked(False)
        self.chk_ingles.setChecked(False)
        self.radio_hombre.setChecked(False)
        self.radio_mujer.setChecked(False)        
        self.radio_cero.setChecked(False)        
        self.radio_50.setChecked(False)        
        self.radio_80.setChecked(False)        
        self.radio_100.setChecked(False)       
        #self.cbx_carrera.itemText(0) 
        self.edt_matricula.setFocus()
        
    
        
    #Generacion de Funcion Eliminar
    def fn_eliminar(self):
        #self.spinEdad.setValue(21)

        fila_seleccionada = self.Tabla_Datos.selectedItems()

        if fila_seleccionada:

            fila = fila_seleccionada[0].row()
            self.Tabla_Datos.removeRow(fila)
            self.Tabla_Datos.clearSelection()
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Alumnos_GUI()
    GUI.show()
    sys.exit(app.exec_())