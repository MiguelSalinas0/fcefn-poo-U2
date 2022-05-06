from ManejadorCama import ManejadorCama
from ManejadorMedicamento import ManejaMedicamento
import time

if __name__ == '__main__':
    
    manejaCama = ManejadorCama()
    manejaMedi = ManejaMedicamento()
    
    manejaCama.testArchivo()
    manejaMedi.testArchivo()
    
    paciente = input('Ingrese nombre y apellido de un paciente: ')
    pos = manejaCama.buscarPaciente(paciente)
    
    if(pos != None):
        cama = manejaCama.getIdCama(pos)
        print('\nPaciente: {} \t\t Cama: {} \t Habitación: {}'.format(manejaCama.getApellidoYnombre(pos), cama, manejaCama.getHabitacion(pos)))
        print('Diagnóstico: {} \t Fecha de internación: {}'.format(manejaCama.getDiagnostico(pos), manejaCama.getFechaInternacion(pos)))
        fecha = time.strftime('%d/%m/%Y', time.localtime())
        manejaCama.setFechaAlta(pos, fecha)
        print('Fecha de Alta: {}'.format(manejaCama.getFechaAlta(pos)))
        manejaMedi.buscarMedicamento(cama)
    else:
        print('ERROR: No se encontró el paciente')
        
    diag = input('Ingrese un diagnóstico para listar los pacientes: ')
    manejaCama.listarPacientes(diag)