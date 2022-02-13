# coding=utf-8
from clases.cliente import Cliente
from clases.oportunidad import Oportunidad
from clases.actividade import Actividad

clientes = {}
oportunidades = {}
actividades = {}
menu_1 = False
tipo_actividades = ["compra", "venta"]


def submenus(eleccionNumber):
    global menu_1

    if eleccionNumber == 0:
        menu_clientes()
    elif eleccionNumber == 1:
        menu_oportunidades()

    elif eleccionNumber == 2:
        menu_1 = True
    else:
        print("por favor seleccione una opción correcta")


def menu_clientes():
    menu_cliente = False
    while not menu_cliente:
        print("Menu Cliente:\n"
              "0-Crear nuevo cliente\n"
              "1-Borrar Cliente\n"
              "2-Editar Cliente\n"
              "3-Listar Clientes\n"
              "4-Salir")
        eleccion_number_cliente = int(input())

        if eleccion_number_cliente == 0:
            crear_Cliente()

        elif eleccion_number_cliente == 1:
            borrar_Cliente()


        elif eleccion_number_cliente == 2:
            editar_cliente()

        elif eleccion_number_cliente == 3:
            listar_clientes()


        elif eleccion_number_cliente == 4:
            print("Saliste del menu de cliente")
            menu_cliente = True


def crear_Cliente():
    rep_clie = False
    while not rep_clie:
        print("Escribe el nombre del cliente")
        nombre = input()

        print("Escribe el apellido del cliente")
        apelllido = input()

        print("Escribe el teléfono del cliente")
        telf = input()

        print("Escribe el email del cliente")
        email = input()

        new_clie = Cliente(len(clientes) + 1, nombre, apelllido, telf, email)

        print("¿Seguro que quieres crear este cliente?(escribe 's' si quieres que se cree o 'n' si no)")
        confirmacion = input().lower()

        if confirmacion == "s":
            if len(clientes) == 0:

                clientes[len(clientes) + 1] = new_clie

                print("cliente creado con exito")

                print("-id:" + str(new_clie.id_clie) + ", nombre:" + new_clie.nombre + ", apellido: " + new_clie.apellido +" , email:" + new_clie.email+";")

                rep_clie = True

            else:
                respuesta = 0
                for cliente in clientes.values():
                    if cliente.telefono == new_clie.telefono or cliente.email == new_clie.email:
                        respuesta = 1
                        break
                if respuesta == 0:
                    clientes[len(clientes) + 1] = new_clie

                    print("cliente creado con exito")

                    print("-id:" + str(
                        new_clie.id_clie) + ", nombre:" + new_clie.nombre + ", apellido: " + new_clie.apellido + " , email:" + new_clie.email + ";")

                    rep_clie = True

                elif respuesta == 1:
                    print("El cliente ya existe por favor ingresa otro cliente")
        elif confirmacion == "n":
            print("Acción de crear cliente denegada con exito")
            rep_clie = True


def borrar_Cliente():
    listar_clientes()
    print("Selecciona el id del cliente que quieres eliminar: ")

    id_clie_del = int(input())

    print("¿Seguro que quieres eliminar este cliente?(escribe 's' si quieres que se cree o 'n' si no)")

    cliente = clientes[id_clie_del]

    print("-id:" + str(cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")

    confirmacion = input().lower()

    if confirmacion == "s":
        if clientes.keys().__contains__(id_clie_del):
            clientes.pop(id_clie_del)
            print("cliente eliminado con exito")
            listar_clientes()
        else:
            print("Error el id del cliente no se encuentra en registrado, por favor intentelo otra vez")

    elif confirmacion == "n":
        print("Acción de crear cliente denegada con exito")


def editar_cliente():
    listar_clientes()
    print("selecciona el id del cliente que quieres editar")
    id_clie_del = int(input())

    print("¿Seguro que quieres eliminar este cliente?(escribe 's' si quieres que se cree o 'n' si no)")
    confirmacion = input().lower()
    cliente = clientes[id_clie_del]
    print("-id:" + str(
        cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")

    if confirmacion == "s":
        if clientes.keys().__contains__(id_clie_del):
            print("editado cliente con estos valores")
        else:
            print("Error el id del cliente no se encuentra en registrado, por favor intentelo otra vez")

    elif confirmacion == "n":
        print("Acción de editar cliente denegada con exito")


def listar_clientes():
    print("Lista de clientes:")
    for cliente in clientes.values():
        print("-id:" + str(
            cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")


def menu_oportunidades():
    print("oportunidades")


print("Bienvenido al CRM")

while not menu_1:
    print("Menu Principal:\n"
          "0-Menu Clientes\n"
          "1-Menu Oportunidades\n"
          "2-Salir")
    eleccion_number = int(input())
    submenus(eleccion_number)

print("Gracias por usar el programa adios")
