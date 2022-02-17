# coding=utf-8
from clases.cliente import Cliente
from clases.oportunidad import Oportunidad
from clases.actividad import Actividad

clientes = {}
oportunidades = {}
actividades = {}
menu_1 = False


def submenus(eleccionNumber):
    global menu_1

    if eleccionNumber == '0':
        menu_clientes()
    elif eleccionNumber == '1':
        menu_oportunidades()
    elif eleccionNumber == '2':
        menu_actividades()
    elif eleccionNumber == '3':
        menu_1 = True
    else:
        print("por favor seleccione una opción correcta")


def menu_actividades():
    menu_actividad = False
    while not menu_actividad:
        print("Menu Actividades:\n"
              "0-Crear nuevo Actividad\n"
              "1-Borrar Actividad\n"
              "2-Editar Actividad\n"
              "3-Listar Actividad\n"
              "4-Salir")
        eleccion_number_actividad = input()

        if eleccion_number_actividad == '0':
            crear_actividad()

        elif eleccion_number_actividad == '1':
            borrar_actividad()

        elif eleccion_number_actividad == '2':
            editar_actividad()

        elif eleccion_number_actividad == '3':
            listar_actividad()

        elif eleccion_number_actividad == '4':
            print("Saliste del menu de actividades")
            menu_actividad = True

        else:
            print("por favor seleccione una opción correcta")


def crear_actividad():
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

                print("-id:" + str(
                    new_clie.id_clie) + ", nombre:" + new_clie.nombre + ", apellido: " + new_clie.apellido + " , email:" + new_clie.email + ";")

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
        else:
            print("Error no seleccionaste nada se volvera al punto anterior")


def borrar_actividad():
    id_clie_del = -1
    validarId = False
    if len(clientes) <= 0:
        print("No hay clientes para borrar")
    else:
        while not validarId:
            try:

                listar_clientes()
                print("Selecciona el id del cliente que quieres eliminar: ")
                id_clie_del = int(input())
                if clientes.keys().__contains__(id_clie_del):
                    validarId = True
                else:
                    print("El cliente no existe por favor seleccione uno que exista para ser eliminado")

            except:
                print("Error porfavor introduzca un número:")

        print("¿Seguro que quieres eliminar este cliente?(escribe 's' si quieres que se cree o 'n' si no)")

        cliente = clientes[id_clie_del]

        print("-id:" + str(
            cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")

        confirmacion = input().lower()

        if confirmacion == "s":
            if clientes.keys().__contains__(id_clie_del):

                for oportunidad in oportunidades:
                    if len(oportunidad.listaClientes) != 0:
                        if oportunidad.listaClientes.keys().__contains__(id_clie_del):
                            oportunidad.listaClientes(id_clie_del)

                clientes.pop(id_clie_del)
                print("cliente eliminado con exito")
                listar_clientes()
            else:
                print("Error el id del cliente no se encuentra en registrado, por favor intentelo otra vez")

        elif confirmacion == "n":
            print("Acción de crear cliente denegada con exito")
        else:
            print("Error no seleccionaste nada se saldra al punto anterior")


def editar_actividad():
    id_clie_edit = -1
    validarId = False

    if len(clientes) <= 0:
        print("No hay clientes para editar")
    else:
        while not validarId:
            try:

                listar_clientes()
                print("Selecciona el id del cliente que quieres editar: ")
                id_clie_edit = int(input())
                if clientes.keys().__contains__(id_clie_edit):
                    validarId = True
                else:
                    print("El cliente no existe por favor seleccione uno que exista para ser eliminado")

            except:
                print("Error porfavor introduzca un número:")

        menuEditarCliente = False
        while not menuEditarCliente:
            print("Menu Edicion de Cliente:\n"
                  "0-Editar nombre\n"
                  "1-Editar Apellido\n"
                  "2-Editar Telefono\n"
                  "3-Editar email\n"
                  "4-Salir de la edicion del cliente")

            seleccion_de_edicion = input()

            if seleccion_de_edicion == '0':
                print("Escriba el nuevo nombre del cliente: ")
                nuevoNombre = input()

                clientes[id_clie_edit].nombre = nuevoNombre

                print("Nombre cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '1':
                print("Escriba el nuevo Apellido del cliente: ")
                nuevoApellido = input()

                clientes[id_clie_edit].apellido = nuevoApellido

                print("Apellido cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '2':
                print("Escriba el nuevo telefono del cliente: ")
                nuevoTelefono = input()

                clientes[id_clie_edit].telefono = nuevoTelefono

                print("Telefono cambiado de forma satisfactoria")
            elif seleccion_de_edicion == '3':
                print("Escriba el nuevo email del cliente: ")
                nuevoEmail = input()

                clientes[id_clie_edit].email = nuevoEmail

                print("Email cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '4':
                print("Salir de la edicion del cliente")
                menuEditarCliente = True
            else:
                print("por favor seleccione una opción correcta ")


def listar_actividad():
    if len(clientes) <= 0:
        print("No hay clientes, por favor introduzca alguno")
    else:
        print("Lista de clientes:")
        for cliente in clientes.values():
            print("-id:" + str(
                cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ", telefono:" + cliente.telefono + ";")


def menu_clientes():
    menu_cliente = False
    while not menu_cliente:
        print("Menu Cliente:\n"
              "0-Crear nuevo cliente\n"
              "1-Borrar Cliente\n"
              "2-Editar Cliente\n"
              "3-Listar Clientes\n"
              "4-Salir")
        eleccion_number_cliente = input()

        if eleccion_number_cliente == '0':
            crear_Cliente()

        elif eleccion_number_cliente == '1':
            borrar_Cliente()

        elif eleccion_number_cliente == '2':
            editar_cliente()

        elif eleccion_number_cliente == '3':
            listar_clientes()

        elif eleccion_number_cliente == '4':
            print("Saliste del menu de cliente")
            menu_cliente = True

        else:
            print("por favor seleccione una opción correcta")


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

                print("-id:" + str(
                    new_clie.id_clie) + ", nombre:" + new_clie.nombre + ", apellido: " + new_clie.apellido + " , email:" + new_clie.email + ";")

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
        else:
            print("Error no seleccionaste nada se volvera al punto anterior")


def borrar_Cliente():
    id_clie_del = -1
    validarId = False
    if len(clientes) <= 0:
        print("No hay clientes para borrar")
    else:
        while not validarId:
            try:

                listar_clientes()
                print("Selecciona el id del cliente que quieres eliminar: ")
                id_clie_del = int(input())
                if clientes.keys().__contains__(id_clie_del):
                    validarId = True
                else:
                    print("El cliente no existe por favor seleccione uno que exista para ser eliminado")

            except:
                print("Error porfavor introduzca un número:")

        print("¿Seguro que quieres eliminar este cliente?(escribe 's' si quieres que se cree o 'n' si no)")

        cliente = clientes[id_clie_del]

        print("-id:" + str(
            cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")

        confirmacion = input().lower()

        if confirmacion == "s":
            if clientes.keys().__contains__(id_clie_del):

                for oportunidad in oportunidades:
                    if len(oportunidad.listaClientes) != 0:
                        if oportunidad.listaClientes.keys().__contains__(id_clie_del):
                            oportunidad.listaClientes(id_clie_del)

                clientes.pop(id_clie_del)
                print("cliente eliminado con exito")
                listar_clientes()
            else:
                print("Error el id del cliente no se encuentra en registrado, por favor intentelo otra vez")

        elif confirmacion == "n":
            print("Acción de crear cliente denegada con exito")
        else:
            print("Error no seleccionaste nada se saldra al punto anterior")


def editar_cliente():
    id_clie_edit = -1
    validarId = False

    if len(clientes) <= 0:
        print("No hay clientes para editar")
    else:
        while not validarId:
            try:

                listar_clientes()
                print("Selecciona el id del cliente que quieres editar: ")
                id_clie_edit = int(input())
                if clientes.keys().__contains__(id_clie_edit):
                    validarId = True
                else:
                    print("El cliente no existe por favor seleccione uno que exista para ser eliminado")

            except:
                print("Error porfavor introduzca un número:")

        menuEditarCliente = False
        while not menuEditarCliente:
            print("Menu Edicion de Cliente:\n"
                  "0-Editar nombre\n"
                  "1-Editar Apellido\n"
                  "2-Editar Telefono\n"
                  "3-Editar email\n"
                  "4-Salir de la edicion del cliente")

            seleccion_de_edicion = input()

            if seleccion_de_edicion == '0':
                print("Escriba el nuevo nombre del cliente: ")
                nuevoNombre = input()

                clientes[id_clie_edit].nombre = nuevoNombre

                print("Nombre cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '1':
                print("Escriba el nuevo Apellido del cliente: ")
                nuevoApellido = input()

                clientes[id_clie_edit].apellido = nuevoApellido

                print("Apellido cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '2':
                print("Escriba el nuevo telefono del cliente: ")
                nuevoTelefono = input()

                clientes[id_clie_edit].telefono = nuevoTelefono

                print("Telefono cambiado de forma satisfactoria")
            elif seleccion_de_edicion == '3':
                print("Escriba el nuevo email del cliente: ")
                nuevoEmail = input()

                clientes[id_clie_edit].email = nuevoEmail

                print("Email cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '4':
                print("Salir de la edicion del cliente")
                menuEditarCliente = True
            else:
                print("por favor seleccione una opción correcta ")


def listar_clientes():
    if len(clientes) <= 0:
        print("No hay clientes, por favor introduzca alguno")
    else:
        print("Lista de clientes:")
        for cliente in clientes.values():
            print("-id:" + str(
                cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ", telefono:" + cliente.telefono + ";")


def menu_oportunidades():
    menu_oportunidad = False
    while not menu_oportunidad:
        print("Menu Oportunidades:\n"
              "0-Crear nueva oportunidad\n"
              "1-Borrar oportunidad\n"
              "2-Editar oportunidad\n"
              "3-Listar oportunidad\n"
              "4-Salir")
        eleccion_number_oportunidad = input()

        if eleccion_number_oportunidad == '0':
            crear_oportunidad()

        elif eleccion_number_oportunidad == '1':
            borrar_oportunidad()

        elif eleccion_number_oportunidad == '2':
            editar_oportunidad()

        elif eleccion_number_oportunidad == '3':
            listar_oportunidades()

        elif eleccion_number_oportunidad == '4':
            print("Saliste del menu de Oportunidades")
            menu_oportunidad = True

        else:
            print("por favor seleccione una opción correcta")


def crear_oportunidad():
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

                print("-id:" + str(
                    new_clie.id_clie) + ", nombre:" + new_clie.nombre + ", apellido: " + new_clie.apellido + " , email:" + new_clie.email + ";")

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
        else:
            print("Error no seleccionaste nada se volvera al punto anterior")


def borrar_oportunidad():
    id_clie_del = -1
    validarId = False
    if len(clientes) <= 0:
        print("No hay clientes para borrar")
    else:
        while not validarId:
            try:

                listar_clientes()
                print("Selecciona el id del cliente que quieres eliminar: ")
                id_clie_del = int(input())
                if clientes.keys().__contains__(id_clie_del):
                    validarId = True
                else:
                    print("El cliente no existe por favor seleccione uno que exista para ser eliminado")

            except:
                print("Error porfavor introduzca un número:")

        print("¿Seguro que quieres eliminar este cliente?(escribe 's' si quieres que se cree o 'n' si no)")

        cliente = clientes[id_clie_del]

        print("-id:" + str(
            cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")

        confirmacion = input().lower()

        if confirmacion == "s":
            if clientes.keys().__contains__(id_clie_del):

                for oportunidad in oportunidades:
                    if len(oportunidad.listaClientes) != 0:
                        if oportunidad.listaClientes.keys().__contains__(id_clie_del):
                            oportunidad.listaClientes(id_clie_del)

                clientes.pop(id_clie_del)
                print("cliente eliminado con exito")
                listar_clientes()
            else:
                print("Error el id del cliente no se encuentra en registrado, por favor intentelo otra vez")

        elif confirmacion == "n":
            print("Acción de crear cliente denegada con exito")
        else:
            print("Error no seleccionaste nada se saldra al punto anterior")


def editar_oportunidad():
    id_clie_edit = -1
    validarId = False

    if len(clientes) <= 0:
        print("No hay clientes para editar")
    else:
        while not validarId:
            try:

                listar_clientes()
                print("Selecciona el id del cliente que quieres editar: ")
                id_clie_edit = int(input())
                if clientes.keys().__contains__(id_clie_edit):
                    validarId = True
                else:
                    print("El cliente no existe por favor seleccione uno que exista para ser eliminado")

            except:
                print("Error porfavor introduzca un número:")

        menuEditarCliente = False
        while not menuEditarCliente:
            print("Menu Edicion de Cliente:\n"
                  "0-Editar nombre\n"
                  "1-Editar Apellido\n"
                  "2-Editar Telefono\n"
                  "3-Editar email\n"
                  "4-Salir de la edicion del cliente")

            seleccion_de_edicion = input()

            if seleccion_de_edicion == '0':
                print("Escriba el nuevo nombre del cliente: ")
                nuevoNombre = input()

                clientes[id_clie_edit].nombre = nuevoNombre

                print("Nombre cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '1':
                print("Escriba el nuevo Apellido del cliente: ")
                nuevoApellido = input()

                clientes[id_clie_edit].apellido = nuevoApellido

                print("Apellido cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '2':
                print("Escriba el nuevo telefono del cliente: ")
                nuevoTelefono = input()

                clientes[id_clie_edit].telefono = nuevoTelefono

                print("Telefono cambiado de forma satisfactoria")
            elif seleccion_de_edicion == '3':
                print("Escriba el nuevo email del cliente: ")
                nuevoEmail = input()

                clientes[id_clie_edit].email = nuevoEmail

                print("Email cambiado de forma satisfactoria")

            elif seleccion_de_edicion == '4':
                print("Salir de la edicion del cliente")
                menuEditarCliente = True
            else:
                print("por favor seleccione una opción correcta ")


def listar_oportunidades():
    if len(clientes) <= 0:
        print("No hay clientes, por favor introduzca alguno")
    else:
        print("Lista de clientes:")
        for cliente in clientes.values():
            print("-id:" + str(
                cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ", telefono:" + cliente.telefono + ";")


print("Bienvenido al CRM")

while not menu_1:
    try:
        print("Menu Principal:\n"
              "0-Menu Clientes\n"
              "1-Menu Oportunidades\n"
              "2-Menu Actividades\n"
              "3-Salir")
        eleccion_number = input()
        submenus(eleccion_number)
    except:
        menu_1 = True

print("Gracias por usar el programa")
