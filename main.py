# coding=utf-8
from clases.cliente import Cliente
from clases.etapas import Etapa
from clases.oportunidad import Oportunidad
from clases.prioridad import Prioridad
from clases.riesg import Riesgo

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
        confirmacion = input()

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

        confirmacion = input()

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
        confirmacion = input()

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

        confirmacion = input()

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
              "4-Añadir Cliente a la oportunidad\n"
              "5-Eliminar Cliente a la  oportunidad\n"
              "6-Salir")
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
            meter_cliente_en_oportunidad()

        elif eleccion_number_oportunidad == '5':
            eliminar_cliente_en_oportunidad()

        elif eleccion_number_oportunidad == '6':
            print("Saliste del menu de Oportunidades")
            menu_oportunidad = True

        else:
            print("por favor seleccione una opción correcta")


def crear_oportunidad():
    prio = 0
    ries = 0
    etap = 0
    rep_oport = False

    while not rep_oport:
        print("Escribe el nombre de la oportunidad")
        nombre = input()

        etapaBoolean = False
        while not etapaBoolean:
            try:
                print("Selecciona la etapa  de la prioridad:\n"
                      "0-nuevo\n"
                      "1-Calificado\n"
                      "2-propuesta\n"
                      "3-ganada\n"
                      "4-perdida\n")
                etapaSeleccion = input()

                if etapaSeleccion == "0":
                    etap = Etapa.nuevo
                    etapaBoolean = True
                elif etapaSeleccion == "1":
                    etap = Etapa.calificado.value
                    etapaBoolean = True
                elif etapaSeleccion == "2":
                    etap = Etapa.propuesta.value
                    etapaBoolean = True
                elif etapaSeleccion == "3":
                    etap = Etapa.ganada.value
                    etapaBoolean = True
                elif etapaSeleccion == "4":
                    etap = Etapa.perdida.value
                    etapaBoolean = True
                else:
                    print("Selecciona una de las siguientes opciones: ")


            except:
                print("Error controlado, selecciona una de las opciones: ")

        prioridadBoolean = False
        while not prioridadBoolean:
            try:
                print("Selecciona el tipo de prioridad:\n"
                      "0-Alta\n"
                      "1-Media\n"
                      "2-Baja\n")
                prioridadSeleccion = input()

                if prioridadSeleccion == "0":
                    prio = Prioridad.alta.value
                    prioridadBoolean = True
                elif prioridadSeleccion == "1":
                    prio = Prioridad.alta.value
                    prioridadBoolean = True
                elif prioridadSeleccion == "2":
                    prio = Prioridad.alta.value
                    prioridadBoolean = True
                else:
                    print("Selecciona una de las siguientes opciones: ")
            except:
                print("Error controlado, selecciona una de las opciones: ")

        riesBoolean = False
        while not riesBoolean:
            try:
                print("Selecciona el tipo de riesgo:\n"
                      "0-leve\n"
                      "1-moderado\n"
                      "2-excesivo\n")
                riesgoSeleccion = input()

                if riesgoSeleccion == "0":
                    ries = Riesgo.leve.value
                    riesBoolean = True
                elif riesgoSeleccion == "1":
                    ries = Riesgo.moderado.value
                    riesBoolean = True
                elif riesgoSeleccion == "2":
                    ries = Riesgo.excesivo.value
                    riesBoolean = True
                else:
                    print("Selecciona una de las siguientes opciones:")
            except:
                print("Error controlado, selecciona una de las opciones:")

        print("Escribe el email de la oportunidad")
        email = input()

        oport = Oportunidad(len(oportunidades) + 1, nombre, etap, prio, ries, email)

        print("¿Seguro que quieres crear esta oportunidad?(escribe 's' si quieres que se cree o 'n' si no)")
        confirmacion = input()

        if confirmacion == "s":
            if len(oportunidades) == 0:

                oportunidades[len(oportunidades) + 1] = oport

                print("oportunidad creada con exito")

                print("-id:" + str(
                    oport.id_oportunidad) + ", nombre:" + oport.nombre + ", etapa: " + oport.etapa + ", "
                                                                                                     "prioridad:" + oport.prioridad + ", riesgo:" + oport.riesgo +
                      ",Correo :" + oport.correo + ";")

                rep_oport = True
            else:
                respuesta = 0
                for o in oportunidades.values():
                    if o.nombre == oport.nombre:
                        respuesta = 1
                        break
                if respuesta == 0:
                    oportunidades[len(oportunidades) + 1] = oport

                    print("oportunidad creado con exito")

                    print("-id:" + str(
                        oport.id_oportunidad) + ", nombre:" + oport.nombre + ", etapa: " + oport.etapa + ", "
                                                                                                         "prioridad:" + oport.prioridad + ", riesgo:" + oport.riesgo +
                          ",Correo :" + oport.correo + ";")

                    rep_oport = True

                elif respuesta == 1:
                    print("La oportunidad ya existe por favor ingresa otra oportunidad")

        elif confirmacion == "n":
            print("Acción de crear oportunidad denegada con exito")
            rep_oport = True
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

        confirmacion = input()

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
    if len(oportunidades) <= 0:
        print("No hay oportunidades, por favor introduzca alguna")
    else:
        print("Lista de oportunidades:")
        for o in oportunidades.values():
            print("-id:" + str(
                o.id_oportunidad) + ", nombre:" + o.nombre + ", etapa: " + o.etapa + ", "
                                                                                     "prioridad:" + o.prioridad + ", riesgo:" + o.riesgo +
                  ",Correo :" + o.correo + ";")

            print("     Listado de Clientes de la oportunidad:")

            if len(o.listaClientes.values()) <= 0:
                print("      No hay clientes")
            else:
                for clie in o.listaClientes.values():
                    print("         -id:" + str(
                        clie.id_clie) + ", nombre:" + clie.nombre + ", apellido: " + clie.apellido + " , email:" + clie.email + ";")

            print("     Listado de Actividades de la oportunidad:")

            if len(o.listaActividades.values()) <= 0:
                print("      No hay Actividades")
            else:
                for a in o.listaActividades.values():
                    print("         -id:" + str(
                        a.id_actividad) + ", nombre:" + a.nombre + ", fecha inicio: " + a.fecha_inicio + " , fecha fin:" + a.fecha_fin +
                          " , Resumen:" + a.resumen + " , descripcion:" + a.descripcion + ";")


def meter_cliente_en_oportunidad():
    id_clie_del = -1
    id_oport = -1
    validarIdOportunidad = False
    validarIdCliente = False

    if len(oportunidades) <= 0:
        print("No hay oportunidades para seleccionar")
    else:
        while not validarIdOportunidad:
            listar_oportunidades()
            try:
                print("Selecciona el id de la oportunidad a la que quieres meter un cliente  : ")
                id_oport = int(input())
            except:
                print("Error porfavor introduzca un número:")
            if oportunidades.keys().__contains__(id_oport):
                validarIdOportunidad = True
            else:
                print("La  oportunidad no existe por favor seleccione una que exista para agregar el cliente")

        if len(clientes) <= 0:
            print("No hay Clientes para seleccionar")
        else:
            while not validarIdCliente:
                listar_clientes()
                try:

                    print("Selecciona el Cliente que quieres añadir : ")
                    id_clie_del = int(input())

                except:
                    print("Error porfavor introduzca un número:")

                validarIdCliente = True

            if clientes.__contains__(id_clie_del):
                if oportunidades[id_oport].listaClientes.keys().__contains__(id_clie_del):
                    print("El cliente ya existe en la oportunidad por favor selecciona otro")
                else:
                    cliente = clientes[id_clie_del]
                    oport = oportunidades[id_oport]
                    print("-id:" + str(
                        cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")
                    print(
                        "¿Seguro que quieres Añadir este cliente a la oportunidad?(escribe 's' si quieres que se cree o 'n' "
                        "si "
                        "no)")

                    confirmacion = input()

                    if confirmacion == "s":

                        cliente.listaOportunidades[id_oport] = oport
                        oport.listaClientes[id_clie_del] = cliente
                        print("Cliente añadido correctamente a la oportunidad")

                    elif confirmacion == "n":
                        print("Acción de Añadir cliente a la oportunidad denegada con exito")
                    else:
                        print("Error no seleccionaste nada se saldra al punto anterior")
            else:
                print("El cliente no existe ")


def eliminar_cliente_en_oportunidad():
    id_clie_del = -1
    id_oport = -1
    validarIdOportunidad = False
    validarIdCliente = False

    if len(oportunidades) <= 0:
        print("No hay oportunidades para seleccionar")
    else:
        while not validarIdOportunidad:
            try:

                listar_oportunidades()

                print("Selecciona el id de la oportunidad a la que quieres eliminar un cliente  : ")

                id_oport = int(input())

                if oportunidades.keys().__contains__(id_oport):
                    validarIdOportunidad = True
                else:
                    print("La  oportunidad no existe por favor seleccione una que exista para eliminar el cliente")

            except:
                print("Error porfavor introduzca un número:")

        if len(clientes) <= 0:
            print("No hay Clientes para seleccionar")

        else:
            if len(oportunidades[id_oport].listaClientes) <= 0:
                print("No hay clientes en la oportunidad por favor ingrese alguno")
            else:
                while not validarIdCliente:
                    try:
                        print("Lista clientes de la oportunidad:")
                        for clie in oportunidades[id_oport].listaClientes.values():
                            print("id:" + str(
                                clie.id_clie) + ", nombre:" + clie.nombre + ", apellido: " + clie.apellido + " , email:" + clie.email + ";")

                        print("Selecciona el Cliente de la oportunidad  que quieres eliminar : ")
                        id_clie_del = int(input())

                        if clientes.__contains__(id_clie_del):
                            if oportunidades[id_oport].listaClientes.keys().__contains__(id_clie_del):
                                validarIdCliente = True
                            else:
                                print("El cliente no existe en la oportunidad por favor selecciona otro que si "
                                      "exista")

                        else:
                            print("Introduzca un cliente que exista en la lista de clientes ")

                    except:
                        print("Error porfavor introduzca un número:")

                cliente = clientes[id_clie_del]
                oport = oportunidades[id_oport]
                print("-id:" + str(
                    cliente.id_clie) + ", nombre:" + cliente.nombre + ", apellido: " + cliente.apellido + " , email:" + cliente.email + ";")
                print(
                    "¿Seguro que quieres Eliminar este cliente de la oportunidad?(escribe 's' si quieres que se cree "
                    "o 'n' "
                    "si "
                    "no)")

                confirmacion = input()

                if confirmacion == "s":

                    cliente.listaOportunidades.pop(id_oport)
                    oport.listaClientes.pop(id_clie_del)
                    print("Cliente eliminado correctamente de la oportunidad")

                elif confirmacion == "n":
                    print("Acción de eliminar cliente de la oportunidad denegada con exito")
                else:
                    print("Error no seleccionaste nada se saldra al punto anterior")


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
