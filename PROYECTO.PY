#SISTEMA DE GESTION DE TORNEO DE FUTBOL 

#1 GESTOR DE EQUIPOS 
#ESTRUCTURA DE DATOS
equipos=[]  #LISTA PARA ALMACENAR EQUIPOS
#EQUIPO 1 DEPORTIVO INDEPENDIENTE MEDELLIN
equipo_1=       {
"equipo_id":"Team001",# ID DEL EQUIPO 1  
"nombre": "Deportivo Independiente Medellin", #NOMBRE DEL EQUIPO
"ciudad": "Medellin", # CIUDAD DEL EQUIPO
"dt" :"Alejandro Restrepo", # DIRECTOR TECNICO DEL EQUIPO 
"jugadores": ["Mender Garcia","Eder Chaux","Fainer Torijano","Luis Fernando Escorcia","Jherson Mosquera","Daniel Londono","Jimer Fory","Baldomero Perlaza","Homer Martinez","Francisco Chaverra","David Gonzales"],
"estadisticas": {
"puntos":16, # PUNTOS DEL EQUIPO 
"partidos": 14, #PARTIDOS JUGADOS
"ganados":3, #PARTIDOS GANADOS DEL EQUIPO 
"perdidos":4, #PARTIDOS PERDIDOS DEL EQUIPO
"empatados":7, #PARTIDOS EMPATADOS DEL EQUIPO
"goles a favor":11, #GOLES A FAVOR DEL EQUIPO
"goles en contra":11, #GOLES EN CONTRA DEL EQUIPO  
}
} 
equipos.append(equipo_1) #ANADIMOS EL EQUIPO A LA LISTA DE EQUIPOS



#EQUIPO 2 MILLONARIOS FUTBOL CLUB
equipo_2=           {
"equpipo_id":"Team002",# ID DEL EQUIPO 2  
"nombre": "Millonarios", #NOMBRE DEL EQUIPO
"ciudad": "Bogota", # CIUDAD DEL EQUIPO
"dt" :"Alberto Gamero", # DIRECTOR TECNICO DEL EQUIPO 
"jugadores": ["Radamel Falcao","Alvaro Montero","Andres Llinas","Leonardo Castro","Daniel Mantilla","Juan Pablo Vargas","Sergio Mosquera","Daniel Catano","Daniel Ruiz","Danovis Banguero","Mackalister Silva"],
"estadisticas": {
"puntos":24, # PUNTOS DEL EQUIPO 
"partidos": 14, #PARTIDOS JUGADOS
"ganados":7, #PARTIDOS GANADOS DEL EQUIPO
"perdidos":4, #PARTIDOS PERDIDOS DEL EQUIPO
"empatados":3, #PARTIDOS EMPATADOS DEL EQUIPO
"goles a favor":20, #GOLES A FAVOR DEL EQUIPO
"goles en contra":12, #GOLES EN CONTRA DEL EQUIPO  
}
} 
equipos.append(equipo_2) #ANADIMOS EL EQUIPO A LA LISTA DE EQUIPOS




#EQUIPO 3 AMERICA DE CALI
equipo_3=           {
"equipo_id":"Team003",# ID DEL EQUIPO 3  
"nombre": "America de Cali", #NOMBRE DEL EQUIPO
"ciudad": "Cali", # CIUDAD DEL EQUIPO
"dt" :"Jorge Da Silva", # DIRECTOR TECNICO DEL EQUIPO 
"jugadores": ["Jorge Soto","Nilson Castrillon","Daniel Bocanegra","Andres Mosquera","Edwin Velasco","Harlod Rivera","Eder Balanta","Franco Leys","Cristian Barrios","Adrian Ramos","Duvan Vergara"],
"estadisticas": {
"puntos":33, # PUNTOS DEL EQUIPO 
"partidos": 14, #PARTIDOS JUGADOS
"ganados":10, #PARTIDOS GANADOS DEL EQUIPO
"perdidos":1, #PARTIDOS PERDIDOS DEL EQUIPO
"empatados":3, #PARTIDOS EMPATADOS DEL EQUIPO
"goles a favor":22, #GOLES A FAVOR DEL EQUIPO
"goles en contra":9, #GOLES EN CONTRA DEL EQUIPO  
}
} 
equipos.append(equipo_3) #ANADIMOS EL EQUIPO A LA LISTA DE EQUIPOS



#EQUIPO 4 JUNIOR DE BARRANQUILLA
equipo_4=           {
"equipo_id":"Team004",# ID DEL EQUIPO 4  
"nombre": "Junior de Barranquilla", #NOMBRE DEL EQUIPO
"ciudad": "Barranquilla", # CIUDAD DEL EQUIPO
"dt" :"Cesar Farias", # DIRECTOR TECNICO DEL EQUIPO 
"jugadores": ["Jefersson Martinez","Yairo Moreno","Emanuel Olivera","Nicolas Zalazar","Ronny Navia","Didier Moreno","Jose Enamorado","Yimmi Chara","Jhon Velez","Bryan Castrillon","Carlos Bacca"],
"estadisticas": {
"puntos":22, # PUNTOS DEL EQUIPO 
"partidos": 14, #PARTIDOS JUGADOS
"ganados":6, #PARTIDOS GANADOS DEL EQUIPO
"perdidos":4, #PARTIDOS PERDIDOS DEL EQUIPO
"empatados":4, #PARTIDOS EMPATADOS DEL EQUIPO
"goles a favor":20, #GOLES A FAVOR DEL EQUIPO
"goles en contra":15, #GOLES EN CONTRA DEL EQUIPO  
}
} 
equipos.append(equipo_4) #ANDIMOS EL EQUIPO A LA LISTA DE EQUIPOS



#EQUIPO 5 ONCE CALDAS
equipo_5=           {
"equipo_id":"Team005",# ID DEL EQUIPO 5  
"nombre": "Once Caldas", #NOMBRE DEL EQUIPO
"ciudad": "Manizales", # CIUDAD DEL EQUIPO
"dt" :"Hernan Dario Herrera", # DIRECTOR TECNICO DEL EQUIPO 
"jugadores": ["James Aguirre","Juan David Cuesta","Jaider Riquett","Jorge Cardona","Juan Pablo Patino","Mateo Garcia","Alejandro Garcia","Lucas Rios","Luis Palacios","Dayro Moreno","Michael Barrios"],
"estadisticas": {
"puntos":29, # PUNTOS DEL EQUIPO 
"partidos": 14, #PARTIDOS JUGADOS
"ganados":9, #PARTIDOS GANADOS DEL EQUIPO
"perdidos":3, #PARTIDOS PERDIDOS DEL EQUIPO
"empatados":2, #PARTIDOS EMPATADOS DEL EQUIPO
"goles a favor":19, #GOLES A FAVOR DEL EQUIPO
"goles en contra":11, #GOLES EN CONTRA DEL EQUIPO  
}
}  
equipos.append(equipo_5) #AnADIMOS EL EQUIPO A LA LISTA DE EQUIPOS



#FUNCIONES GESTOR DE EQUIPOS

#FUNCION 1: REGISTRAR EQUIPOS
nueva_id=6  #SE DEFINE LA VARIABLE NUEVA_ID PARA GENERAR UN ID PARA EL NUEVO EQUIPO
#ESTA FUNCION REGISTRA EL NUEVO EQUIPO Y RETORNA UN DICCIONARIO CON LOS DATOS INGRESADOS
def registrar_equipo(nombre: str, ciudad: str, dt: str) -> dict: 
    global nueva_id  #SE USA EL GLOBAL PARA ACCEDER A LA NUEVA ID Y MODIFICARLA
    equipo_id = f"Team{nueva_id:03d}" #SE UTILIZA EL F-STRING PARA MODIFICAR LA CADENA
                                      #03D PARA AanaADIRLE 3 DIGITOS A NUEVA_ID 
   #DATOS DEL NUEVO EQUIPO REGISTRADO
    equipo = {         
        "equipo_id": equipo_id,
        "nombre": nombre,
        "ciudad": ciudad,
        "dt": dt,
        "jugadores": [],
        "estadisticas": {
            "puntos": 0,
            "partidos": 0,
            "ganados": 0,
            "perdidos": 0,
            "empatados": 0,
            "goles a favor": 0,
            "goles en contra": 0
        }
    }

    return equipo  #DEVUELVE LOS DATOS DEL EQUIPO
#EJEMPLO DE USO 
nuevo_equipo=registrar_equipo("Nacional", "Medellin", "Juan Perez")
print("EL NUEVO EQUIPO ES",nuevo_equipo)
equipos.append(nuevo_equipo)


# FUNCION 2: BUSCAR EQUIPO
#ESTA FUNCION VA A BUSCAR LOS EQUIPOS QUE CUMPLAN CON LOS PARAMETROS Y VA A DEVOLVER UNA LISTA
def buscar_equipo(criterio: str, valor: str) -> list: 
    resultados = []  # LISTA DE LOS EQUIPOS QUE CUMPLAN EL CRITERIO 
    for equipo in equipos:  # CICLO QUE RECORRE LA LISTA EQUIPOS 
       #CICLO QUE VERIFICA SI EL CRITERIO ESTA EN EQUIPO Y SI EL VALOR ES IGUAL AL CRITERIO 
        if criterio in equipo and equipo[criterio].lower() == valor.lower():  #SE ANADIO EL .LOWER() PARA FUNCIONE CON MAYUSCULAS Y MINUSCULAS
            resultados.append(equipo)  # PONE EL EQUIPO EN LOS RESULTADOS
    return resultados  # DEVUELVE LOS EQUIPOS ENCONTRADOS
# EJEMPLO DE USO DE LA FUNCION DE BUSQUEDA
resultados = buscar_equipo("ciudad", "Medellin")  # EQUIPOS QUE ESTEN EN MEDELLIN 
print("LOS EQUIPOS DE LA CIUDAD SOLICITADA SON:", resultados)  # LA LISTA DE LOS EQUIPOS QUE ESTAN EN MEDELLIN

#FUNCION 3: ACTUALIZAR ESTADISTICAS DE EQUIPO 
#FUNCION QUE ACTUALIZA EL RESULTADO DEL EQUIPO Y DEVUELVE UN DICCIONARIO CON EL RESULTADO
def actualizar_estadisticas_equipo(id_equipo: str, resultado: dict):
   #USAMOS LA i COMO UN TIPO DE CONTADOR QUE RECORRA LA LISTA EQUIPOS Y SE VERIFICA SI SI COINCIDE CON LOS PARAMETROS
    equipo = next((i for i in equipos if i['id'] == id_equipo), None)
   #VERIFICA SI SI ENCONTRO EL EQUIPO Y SI NO DEVUELVE NADA
    if equipo is not None: 
        
        #SE OBTIENE EL RESULTADO DEL PARTIDO
        goles_favor = resultado.get("goles_favor", 1)
        goles_contra = resultado.get("goles_contra", 1)
        
        #SE ACTUALIZAN LOS DATOS SEGUN LOS RESULTADOS EN LA LISTA EQUIPOS 
        equipo['estadisticas']['goles a favor'] += goles_favor
        equipo['estadisticas']['goles en contra'] += goles_contra
        equipo['estadisticas']['partidos'] += 1 

        #SE REALIZAN ESTOS CICLOS PARA DETERMINAR LOS PUNTOS DISTRIBUIDOS SEGUN LOS RESULTADOS
        if goles_favor > goles_contra:  # Si el equipo gano
         equipo['estadisticas']['ganados'] += 1
        equipo['estadisticas']['puntos'] += 3
    elif goles_favor < goles_contra:  # Si el equipo perdio
     equipo['estadisticas']['perdidos'] += 1
    else:  # Si fue un empate
     equipo['estadisticas']['empatados'] += 1
    equipo['estadisticas']['puntos'] += 1
    
    print(f"Equipo con ID {id_equipo} no encontrado.")


#2 GESTOR DE JUGADORES 

#ESTRUCTURA DE DATOS
jugadores = [] #LISTA QUE ALMACENA LOS JUGADORES 

#JUGADORES DEL DEPORTIVO INDEPENDIENTE MEDELLIN
jugador_1_MEDELLIN=          {
"id":"JP1MED", #ID UNICO DEL JUGADOR
"nombre":"Eder Chaux", #NOMBRE COMPLETO
"numero":"25", #NUMERO DE CAMISETA 
"posicion":"Portero", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1035, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_1_MEDELLIN)
jugador_2_MEDELLIN=          {
"id":"JP2MED", #ID UNICO DEL JUGADOR
"nombre":"Mender Garcia", #NOMBRE COMPLETO
"numero":"8", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":3, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":716, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_2_MEDELLIN)
jugador_3_MEDELLIN=          {
"id":"JP3MED", #ID UNICO DEL JUGADOR
"nombre":"Fainer Torijano", #NOMBRE COMPLETO
"numero":"25", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":4, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1080, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_3_MEDELLIN)
jugador_4_MEDELLIN=          {
"id":"JP4MED", #ID UNICO DEL JUGADOR
"nombre":"Luis Fernando Escorcia", #NOMBRE COMPLETO
"numero":"4", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":3, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":181, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_4_MEDELLIN)
jugador_5_MEDELLIN=          {
"id":"JP5MED", #ID UNICO DEL JUGADOR
"nombre":"Jherson Mosquera", #NOMBRE COMPLETO
"numero":"6", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":5, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":354, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_5_MEDELLIN)
jugador_6_MEDELLIN=          {
"id":"JP6MED", #ID UNICO DEL JUGADOR
"nombre":"Daniel Londono", #NOMBRE COMPLETO
"numero":"13", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":5, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":317, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_6_MEDELLIN)
jugador_7_MEDELLIN=          {
"id":"JP7MED", #ID UNICO DEL JUGADOR
"nombre":"Jimer Fory", #NOMBRE COMPLETO
"numero":"17", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":4, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":924, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_7_MEDELLIN)
jugador_8_MEDELLIN=          {
"id":"JP8MED", #ID UNICO DEL JUGADOR
"nombre":"Baldomero Perlaza", #NOMBRE COMPLETO
"numero":"14", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":584, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_8_MEDELLIN)
jugador_9_MEDELLIN=          {
"id":"JP9MED", #ID UNICO DEL JUGADOR
"nombre":"Homer Martinez", #NOMBRE COMPLETO
"numero":"18", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":11, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":525, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_9_MEDELLIN)
jugador_10_MEDELLIN=          {
"id":"JP10MED", #ID UNICO DEL JUGADOR
"nombre":"Francisco Chaverra", #NOMBRE COMPLETO
"numero":"13", #NUMERO DE CAMISETA 
"posicion":"Delantero ", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":5, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":619, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_10_MEDELLIN)
jugador_11_MEDELLIN=          {
"id":"JP11MED", #ID UNICO DEL JUGADOR
"nombre":"David Gonzales", #NOMBRE COMPLETO
"numero":"11", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team001", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":3, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":820, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_11_MEDELLIN)

#JUGADORES DEL MILLONARIOS
jugador_1_MILLONARIOS=          {
"id":"JP1MIL", #ID UNICO DEL JUGADOR
"nombre":"Leonardo Castro", #NOMBRE COMPLETO
"numero":"23", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":3, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":1,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":839, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_1_MILLONARIOS)
jugador_2_MILLONARIOS=          {
"id":"JP2MIL", #ID UNICO DEL JUGADOR
"nombre":"Radamel Falcao", #NOMBRE COMPLETO
"numero":"9", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":6, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":330, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_2_MILLONARIOS)
jugador_3_MILLONARIOS=          {
"id":"JP3MIL", #ID UNICO DEL JUGADOR
"nombre":"Alvaro Montero", #NOMBRE COMPLETO
"numero":"31", #NUMERO DE CAMISETA 
"posicion":"Portero", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":8, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":720, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_3_MILLONARIOS)
jugador_4_MILLONARIOS=          {
"id":"JP4MIL", #ID UNICO DEL JUGADOR
"nombre":"Andres Llinas", #NOMBRE COMPLETO
"numero":"26", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":9, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":4, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":600, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_4_MILLONARIOS)
jugador_5_MILLONARIOS=          {
"id":"JP5MIL", #ID UNICO DEL JUGADOR
"nombre":"Daniel Mantilla", #NOMBRE COMPLETO
"numero":"11", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":10, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":417, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_5_MILLONARIOS)
jugador_6_MILLONARIOS=          {
"id":"JP6MIL", #ID UNICO DEL JUGADOR
"nombre":"Juan Pablo Vargas", #NOMBRE COMPLETO
"numero":"4", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":10, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":900, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_6_MILLONARIOS)
jugador_7_MILLONARIOS=          {
"id":"JP7MIL", #ID UNICO DEL JUGADOR
"nombre":"Sergio Mosquera", #NOMBRE COMPLETO
"numero":"6", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":9, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":1,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":668, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_7_MILLONARIOS)
jugador_8_MILLONARIOS=          {
"id":"JP8MIL", #ID UNICO DEL JUGADOR
"nombre":"Daniel Catano", #NOMBRE COMPLETO
"numero":"10", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":5, #PARTIDOS JUGADOS
"goles":2, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":266, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_8_MILLONARIOS)
jugador_9_MILLONARIOS=          {
"id":"JP9MIL", #ID UNICO DEL JUGADOR
"nombre":"Daniel Ruiz", #NOMBRE COMPLETO
"numero":"18", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":9, #PARTIDOS JUGADOS
"goles":2, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":378, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_9_MILLONARIOS)
jugador_10_MILLONARIOS=          {
"id":"JP10MIL", #ID UNICO DEL JUGADOR
"nombre":"Danovis Banguero", #NOMBRE COMPLETO
"numero":"20", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":11, #PARTIDOS JUGADOS
"goles":2, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":5, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":952, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_10_MILLONARIOS)
jugador_11_MILLONARIOS=          {
"id":"JP11MIL", #ID UNICO DEL JUGADOR
"nombre":"Mackalister Silva", #NOMBRE COMPLETO
"numero":"14", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team002", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":2, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":751, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_11_MILLONARIOS)

#JUGADORES DEL AMERICA DE CALI
jugador_1_AMERICA=          {
"id":"JP1AME", #ID UNICO DEL JUGADOR
"nombre":"Adrian Ramos", #NOMBRE COMPLETO
"numero":"20", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":10, #PARTIDOS JUGADOS
"goles":2, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":382, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_1_AMERICA)
jugador_2_AMERICA=          {
"id":"JP2AME", #ID UNICO DEL JUGADOR
"nombre":"Jorge Soto", #NOMBRE COMPLETO
"numero":"12", #NUMERO DE CAMISETA 
"posicion":"Portero", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":6, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":500, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_2_AMERICA)
jugador_3_AMERICA=          {
"id":"JP3AME", #ID UNICO DEL JUGADOR
"nombre":"Nilson Castrillon", #NOMBRE COMPLETO
"numero":"13", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":5, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":450, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_3_AMERICA)
jugador_4_AMERICA=          {
"id":"JP4AME", #ID UNICO DEL JUGADOR
"nombre":"Daniel bocanegra", #NOMBRE COMPLETO
"numero":"2", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":3, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":992, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_4_AMERICA)
jugador_5_AMERICA=          {
"id":"JP5AME", #ID UNICO DEL JUGADOR
"nombre":"Andres Mosquera", #NOMBRE COMPLETO
"numero":"4", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1066, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_5_AMERICA)
jugador_6_AMERICA=          {
"id":"JP6AME", #ID UNICO DEL JUGADOR
"nombre":"Edwin Velasco", #NOMBRE COMPLETO
"numero":"21", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":2, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1162, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_6_AMERICA)
jugador_7_AMERICA=          {
"id":"JP7AME", #ID UNICO DEL JUGADOR
"nombre":"Harold Rivera", #NOMBRE COMPLETO
"numero":"17", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":14, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":3, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1034, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_7_AMERICA)
jugador_8_AMERICA=          {
"id":"JP8AME", #ID UNICO DEL JUGADOR
"nombre":"Eder Balanta", #NOMBRE COMPLETO
"numero":"3", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":9, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":658, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_8_AMERICA)
jugador_9_AMERICA=          {
"id":"JP9AME", #ID UNICO DEL JUGADOR
"nombre":"Franco Leys", #NOMBRE COMPLETO
"numero":"32", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":3, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":848, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_9_AMERICA)
jugador_10_AMERICA=          {
"id":"JP10AME", #ID UNICO DEL JUGADOR
"nombre":"Cristian Barrios", #NOMBRE COMPLETO
"numero":"7", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":4, #GOLES ANOTADOS
"asistencias":4, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":958, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_10_AMERICA)
jugador_11_AMERICA=          {
"id":"JP11AME", #ID UNICO DEL JUGADOR
"nombre":"Duvan Vergara", #NOMBRE COMPLETO
"numero":"11", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team003", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":7, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":3, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":976, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_11_AMERICA)


#JUGADORES DEL JUNIOR
jugador_1_JUNIOR=          {
"id":"JP1JUN", #ID UNICO DEL JUGADOR
"nombre":"Carlos Bacca", #NOMBRE COMPLETO
"numero":"70", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":5, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":3, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":893, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_1_JUNIOR)
jugador_2_JUNIOR=          {
"id":"JP2JUN", #ID UNICO DEL JUGADOR
"nombre":"Jefersson Martinez", #NOMBRE COMPLETO
"numero":"30", #NUMERO DE CAMISETA 
"posicion":"Portero", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":5, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":450, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_2_JUNIOR)
jugador_3_JUNIOR=          {
"id":"JP3JUN", #ID UNICO DEL JUGADOR
"nombre":"Yairo Moreno", #NOMBRE COMPLETO
"numero":"90", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":4, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":180, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_3_JUNIOR)
jugador_4_JUNIOR=          {
"id":"JP4JUN", #ID UNICO DEL JUGADOR
"nombre":"Emanuel Olivera", #NOMBRE COMPLETO
"numero":"18", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":10, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":1,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":900, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_4_JUNIOR)
jugador_5_JUNIOR=          {
"id":"JP5JUN", #ID UNICO DEL JUGADOR
"nombre":"Nicolas zalazar", #NOMBRE COMPLETO
"numero":"33", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":6, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":1,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":507, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_5_JUNIOR)
jugador_6_JUNIOR=          {
"id":"JP6JUN", #ID UNICO DEL JUGADOR
"nombre":"Ronny Navia", #NOMBRE COMPLETO
"numero":"26", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":5, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":362, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_6_JUNIOR)
jugador_7_JUNIOR=          {
"id":"JP7JUN", #ID UNICO DEL JUGADOR
"nombre":"Didier Moreno", #NOMBRE COMPLETO
"numero":"6", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":2, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":6, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1069, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_7_JUNIOR)
jugador_8_JUNIOR=          {
"id":"JP8JUN", #ID UNICO DEL JUGADOR
"nombre":"Jose Enamorado", #NOMBRE COMPLETO
"numero":"99", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":11, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":668, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_8_JUNIOR)
jugador_9_JUNIOR=          {
"id":"JP9JUN", #ID UNICO DEL JUGADOR
"nombre":"Yimmi Chara", #NOMBRE COMPLETO
"numero":"8", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":982, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_9_JUNIOR)
jugador_10_JUNIOR=          {
"id":"JP10JUN", #ID UNICO DEL JUGADOR
"nombre":"Jhon Velez", #NOMBRE COMPLETO
"numero":"13", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":10, #PARTIDOS JUGADOS
"goles":4, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":248, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_10_JUNIOR)
jugador_11_JUNIOR=          {
"id":"JP11JUN", #ID UNICO DEL JUGADOR
"nombre":"Bryan Castrillon", #NOMBRE COMPLETO
"numero":"88", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team004", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":10, #PARTIDOS JUGADOS
"goles":4, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":0, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":308, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_11_JUNIOR)


#JUGADORES DEL ONCE CALDAS 
jugador_1_ONCE=          {
"id":"JP1ONC", #ID UNICO DEL JUGADOR
"nombre":"Dayro Moreno", #NOMBRE COMPLETO
"numero":"17", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":6, #GOLES ANOTADOS
"asistencias":3, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1062, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_1_ONCE)
jugador_2_ONCE=          {
"id":"JP2ONC", #ID UNICO DEL JUGADOR
"nombre":"James Aguirre", #NOMBRE COMPLETO
"numero":"12", #NUMERO DE CAMISETA 
"posicion":"Portero", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":14, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1260, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_2_ONCE)
jugador_3_ONCE=          {
"id":"JP3ONC", #ID UNICO DEL JUGADOR
"nombre":"Juan David Cuesta", #NOMBRE COMPLETO
"numero":"22", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":14, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":2, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1260, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_3_ONCE)
jugador_4_ONCE=          {
"id":"JP4ONC", #ID UNICO DEL JUGADOR
"nombre":"Jaider Riquett", #NOMBRE COMPLETO
"numero":"18", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":4, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1130, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_4_ONCE)
jugador_5_ONCE=          {
"id":"JP5ONC", #ID UNICO DEL JUGADOR
"nombre":"Jorge Cardona", #NOMBRE COMPLETO
"numero":"34", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":781, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_5_ONCE)
jugador_6_ONCE=          {
"id":"JP6ONC", #ID UNICO DEL JUGADOR
"nombre":"Juan Pablo Patino", #NOMBRE COMPLETO
"numero":"33", #NUMERO DE CAMISETA 
"posicion":"Defensa", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":12, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":4, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":712,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1055, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_6_ONCE)
jugador_7_ONCE=          {
"id":"JP7ONC", #ID UNICO DEL JUGADOR
"nombre":"Mateo Garcia", #NOMBRE COMPLETO
"numero":"19", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":2, #GOLES ANOTADOS
"asistencias":3, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":5, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1132, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_7_ONCE)
jugador_8_ONCE=          {
"id":"JP8ONC", #ID UNICO DEL JUGADOR
"nombre":"Alejandro Garcia", #NOMBRE COMPLETO
"numero":"20", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":14, #PARTIDOS JUGADOS
"goles":1, #GOLES ANOTADOS
"asistencias":0, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":2, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":870, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_8_ONCE)
jugador_9_ONCE=          {
"id":"JP9ONC", #ID UNICO DEL JUGADOR
"nombre":"Lucas Rios", #NOMBRE COMPLETO
"numero":"10", #NUMERO DE CAMISETA 
"posicion":"Mediocampista", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":4, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":3, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":791, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_9_ONCE)
jugador_10_ONCE=          {
"id":"JP10ONC", #ID UNICO DEL JUGADOR
"nombre":"Luis Palacios", #NOMBRE COMPLETO
"numero":"24", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":14, #PARTIDOS JUGADOS
"goles":0, #GOLES ANOTADOS
"asistencias":1, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":1, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":934, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_10_ONCE)
jugador_11_ONCE=          {
"id":"JP11ONC", #ID UNICO DEL JUGADOR
"nombre":"Michael Barrios", #NOMBRE COMPLETO
"numero":"7", #NUMERO DE CAMISETA 
"posicion":"Delantero", #POSICION EN EL CAMPO
"equipo_id":"Team005", #EQUIPO AL QUE PERTENECE 
"estadisticas": {
"partidos":13, #PARTIDOS JUGADOS
"goles":5, #GOLES ANOTADOS
"asistencias":2, #ASISTENCIAS REALIZADAS 
"tarjetas_amarillas":5, #TARJETAS AMARILLAS RECIBIDAS
"tarjetas_rojas":0,#TARJETAS ROJAS RECIBIDAS 
"minutos_jugados":1123, #MINUTOS JUGADOS 
}
}
jugadores.append(jugador_11_ONCE)
#FUNCIONES JUGADORES 
#REGISTRAR JUGADOR

# CONTADOR PARA REGISTRAR LOS JUGADORES 
contador_jugadores = 1  #INICIA EN 1 

# FUNCION 1 PARA REGISTRAR UN JUGADOR NUEVO
def registrar_jugador(nombre: str, numero: int, posicion: str, equipo_id: str) -> dict:
    global contador_jugadores  # #SE USA EL GLOBAL PARA ACCEDER A LA NUEVA ID Y MODIFICARLA
    jugador_id = f"JUG{contador_jugadores:03d}"  # Generar el ID del jugador con formato JUG001, JUG002, ETC.
    
    # DICCIONARIO DEL NUEVO JUGADOR
    jugador = {
        "id": jugador_id,
        "nombre": nombre,
        "numero": numero,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "estadisticas": {
            "partidos": 0,
            "goles": 0,
            "asistencias": 0,
            "tarjetas_amarillas": 0,
            "tarjetas_rojas": 0,
            "minutos_jugados": 0
        }
    }
    
    # AGREGAR EL NUEVO JUGADOR A LA LISTA 
    jugadores.append(jugador)
    
    # INCREMENTA EL ID DEL JUGADOR 
    contador_jugadores += 1
    
    return jugador  # RETORNA EL JUGADOR CON LOS NUEVOS DATOS
# EJEMPLO DE USO
nuevo_jugador = registrar_jugador("Juan Perez", 10, "Delantero", "EQP001")
print("EL NUEVO JUGADOR REGISTRADO ES:", nuevo_jugador)

#FUNCION 2 PARA BUSCAR JUGADOR 
def buscar_jugador(criterio: str, valor: str) -> list:
    resultados = []  # LISTA PARA ALMACENAR LOS JUGADORES QUE TENGAN EL CRITERIO SOLICITADO 
    for jugador in jugadores: #RECORRE LA LISTA JUGADORES
        # VERIFICA SI EL CRITERIO ESTA EN EL DICCIONARIO Y SI COINCIDE CON EL VALOR
        if criterio in jugador and str(jugador[criterio]).lower() == valor.lower():
            resultados.append(jugador)  #AGREGAR EL JUGADOR A LOS RESULTADOS
    return resultados  # DEVUELVE LA LISTA DE LOS JUGADORES ENCONTRADOS
jugadores_encontrados = buscar_jugador("posicion", "Delantero")
print("LOS JUGADORES EN LA POSICION SOLICITADA SON:", jugadores_encontrados)

#FUNCION 3 ACTUALIZAR ESTADISTICAS 
def actualizar_estadisticas_jugador(id_jugador: str, estadisticas_partido: dict) -> dict: 
 for jugador in jugadores: #RECORRE LA LISTA JUGADORES
        if jugador["id"] == id_jugador: #BUSCA LOS JUGADORES POR SU ID
            
            for goles, valor in estadisticas_partido.items():  #recorre cada clave y valor en el diccionario estadisticas_partido
                if goles in jugador["estadisticas"]: #Las estadisticas se representan como goles  y valor es el numero que queremos sumar 
                    jugador["estadisticas"][goles] += valor
                else:
                    print(f"Estadistica '{goles}' no encontrada para el jugador {id_jugador}")

            # Retornar las estadisticas actualizadas del jugador
            return jugador["estadisticas"]
estadisticas_actualizadas = actualizar_estadisticas_jugador("JP1MED", {"goles": 1, "asistencias": 2})
print(estadisticas_actualizadas)
    

# 3 GESTOR DE PARTIDOS
#ESTRUCTURA DE DATOS
partidos = [] #LISTA QUE ALMACENA LOS PARTIDOS
#PARTIDO MEDELLIN VS MILLONARIOS
partido_1 = {
 "id_partido": "PAR001", # ID DEL PARTIDO 
 "fecha": "2024-7-24", # FECHA DEL PARTIDO
 "id_arbitro": "ARB001", #ID ARBITRO
 "equipo_local": "TEAM001", # ID DEL EQUIPO LOCAL
 "equipo_visitante": "TEAM002", # ID DEL EQUIPO VISITANTE
 "goles_local": 1, # GOLES DEL EQUIPO LOCAL
 "goles_visitante": 1, # GOLES DEL EQUIPO VISITANTE
 "alineacion_local": ["JP1MED","JP2MED","JP3MED","JP4MED","JP5MED","JP6MED","JP7MED","JP8MED","JP9MED","JP10MED","JP11MED",], # ID DE LOS JUGADORES DEL EQUIPO LOCAL
 "alineacion_visitante": ["JP1MIL","JP2MIL","JP3MIL","JP4MIL","JP5MIL","JP6MIL","JP7MIL","JP8MIL","JP9MIL","JP10MIL","JP11MIL",], # ID DE LOS JUGADORES DEL EQUIPO VISITANTE
 "eventos": [ # EVENTOS IMPORTANTES DEL PARTIDO
 {
 "minuto": 43,
 "tipo": "gol",
 "jugador": "JP2MED",
 "equipo": "TEAM001"
 },
 {
 "minuto": 90,
 "tipo": "gol",
 "jugador": "JP1MIL",
 "equipo": "TEAM002"
 },
 {
 "minuto": 25,
 "tipo": "Amonestacion",
 "jugador": "JP4MIL",
 "equipo": "TEAM002"
 },
 {
 "minuto": 86,
 "tipo": "Amonestacion",
 "jugador": "JP11",
 "equipo": "TEAM001"
 },
 ]
}
partidos.append(partido_1)
#PARTIDO JUNIOR DE BARRANQUILLA VS AMERICA DE CALI
partido_2 = {
 "id_partido": "PAR002", # ID DEL PARTIDO 
 "fecha": "2024-10-27", # FECHA DEL PARTIDO
 "id_arbitro": "ARB002", #ID ARBITRO
 "equipo_local": "TEAM004", # ID DEL EQUIPO LOCAL
 "equipo_visitante": "TEAM003", # ID DEL EQUIPO VISITANTE
 "goles_local": 3, # GOLES DEL EQUIPO LOCAL
 "goles_visitante": 1, # GOLES DEL EQUIPO VISITANTE
 "alineacion_local": ["JP1JUN","JP2JUN","JP3JUN","JP4JUN","JP5JUN","JP6JUN","JP7JUN","JP8JUN","JP9JUN","JP10JUN","JP11JUN",], # ID DE LOS JUGADORES DEL EQUIPO LOCAL
 "alineacion_visitante": ["JP1AME","JP2AME","JP3AME","JP4AME","JP5AME","JP6AME","JP7AME","JP8AME","JP9AME","JP10AME","JP11AME",], # ID DE LOS JUGADORES DEL EQUIPO VISITANTE
 "eventos": [ # EVENTOS IMPORTANTES DEL PARTIDO
 {
 "minuto": 45,
 "tipo": "gol",
 "jugador": "JP9JUN",
 "equipo": "TEAM004"
 },
 {
 "minuto": 47,
 "tipo": "gol",
 "jugador": "JP9JUN",
 "equipo": "TEAM004"
 },
 {
 "minuto": 59,
 "tipo": "gol",
 "jugador": "JP7AME",
 "equipo": "TEAM003"
 },
 {
 "minuto": 69,
 "tipo": "gol en contra",
 "jugador": "JPAME",
 "equipo": "TEAM004"
 },
 {
 "minuto": 56,
 "tipo": "Amonestacion",
 "jugador": "JP11AME",
 "equipo": "TEAM003"
 },
 {
 "minuto": 23,
 "tipo": "Amonestacion",
 "jugador": "JP8JUN",
 "equipo": "TEAM004"
 },
 ]
}
partidos.append(partido_2)
#PARTIDO ONCE CALDAS VS MEDELLIN
partido_3 = {
 "id_partido": "PAR003", # ID DEL PARTIDO 
 "fecha": "2024-9-28", # FECHA DEL PARTIDO
 "id_arbitro": "ARB003", #ID ARBITRO
 "equipo_local": "TEAM005", # ID DEL EQUIPO LOCAL
 "equipo_visitante": "TEAM001", # ID DEL EQUIPO VISITANTE
 "goles_local": 0, # GOLES DEL EQUIPO LOCAL
 "goles_visitante": 2, # GOLES DEL EQUIPO VISITANTE
 "alineacion_local": ["JP1ONC","JP2ONC","JP3ONC","JP4ONC","JP5ONC","JP6ONC","JP7ONC","JP8ONC","JP9NC","JP10ONC","JP11ONC",], # ID DE LOS JUGADORES DEL EQUIPO LOCAL
 "alineacion_visitante": ["JP1MED","JP2MED","JP3MED","JP4MED","JP5MED","JP6MED","JP7MED","JP8MED","JP9MED","JP10MED","JP11MED",], # ID DE LOS JUGADORES DEL EQUIPO VISITANTE
 "eventos": [ # EVENTOS IMPORTANTES DEL PARTIDO
 {
 "minuto": 13,
 "tipo": "gol",
 "jugador": "JP2MED",
 "equipo": "TEAM001"
 },
 {
 "minuto": 90,
 "tipo": "gol",
 "jugador": "JP10",
 "equipo": "TEAM001"
 },
 {
 "minuto": 23,
 "tipo": "Amonestacion",
 "jugador": "JP4ONC",
 "equipo": "TEAM005"
 },
 {
 "minuto": 67,
 "tipo": "Amonestacion",
 "jugador": "JP2MED",
 "equipo": "TEAM001"
 },
 ]
}
partidos.append(partido_3)

# FUNCION 1 REGISTRAR PARTIDO
partidos = [] #LISTA QUE ALMACENA EL PARTIDO REGISTRADO 
#FUNCION PARA REGISTRAR EL PARTIDO
def registrar_partido(fecha: str, equipo_local: str, equipo_visitante: str, id_arbitro: str) -> dict:
 # Genera un nuevo ID de partido
    id_partido = f"PAR{len(partidos) + 1:04}"  #PARA GENERAR EL ID DEL PARTIDO

    # DICCIONARIO NUEVO PARTIDO
    partido = {
        "id": id_partido,
        "fecha": fecha,
        "id_arbitro": id_arbitro,
        "equipo_local": equipo_local,
        "equipo_visitante": equipo_visitante,
        "goles_local": 0,
        "goles_visitante": 0,
        "alineacion_local": [],
        "alineacion_visitante": [],
        "eventos": []
    }

    # AGREGA EL PARTIDO A LA LISTA 
    partidos.append(partido)

    # RETORNA EL PARTIDO REGISTRADO
    return partido
# EJEMPLO DE USO
nuevo_partido = registrar_partido("2024-11-01", "EQP001", "EQP002", "ARB001")
print("EL NUEVO PARTIDO ES",nuevo_partido)

#FUNCION 2 ACTUALIZAR RESULTADO 
def actualizar_resultado(id_partido: str, goles_local: int, goles_visitante: int) -> dict:
   
    # BUSCA EL PARTIDO POR LA ID 
    for partido in partidos:
        if partido["id"] == id_partido:
            # ACTUALIZA GOLES DE VISITANTE Y LOCAL
            partido["goles_local"] = goles_local
            partido["goles_visitante"] = goles_visitante
            # RETORNA EL PARTIDO ACTUALIZADO
            return partido
# EJEMPLO DE USO
resultado_actualizado = actualizar_resultado("PAR001", 2, 1)
if resultado_actualizado:
    print("Resultado actualizado:", resultado_actualizado)

# FUNCION 3 REGISTRAR EVENTO 
def registrar_evento(id_partido: str, minuto: int, tipo: str, jugador: str, equipo: str) -> dict:
# BUSCA EL PARTIDO POR LA ID
    for partido in partidos:
        if partido["id"] == id_partido:
            # DICCIONARIO PARA ANADIR EL EVENTO
            nuevo_evento = {
                "minuto": minuto,
                "tipo": tipo,
                "jugador": jugador,
                "equipo": equipo
            }
            # AGREGA EL EVENTO A LA LISTA 
            partido["eventos"].append(nuevo_evento)
            # RETORNA EL EVENTO
            return nuevo_evento
# EJEMPLO DE USO 
evento_registrado = registrar_evento("PAR001", 30, "gol", "JUG001", "EQP001")
if evento_registrado:
    print("Evento registrado:", evento_registrado)



# 4 GENERADOR DE REPORTES 
import json
import os

# Ruta del archivo JSON
archivo_equipos = 'equipos.json'

# Si el archivo no existe, inicializamos la lista de equipos
def inicializar_equipos():
    if not os.path.exists(archivo_equipos):
        equipos = [
            {
                "id": "EQP001",
                "nombre": "Once Caldas",
                "ciudad": "Manizales",
                "dt": "Hernan Dario Herrera",
                "puntos": 0,
                "partidos_jugados": 0,
                "ganados": 0,
                "empatados": 0,
                "perdidos": 0,
                "goles_favor": 0,
                "goles_contra": 0
            },
            {
                "id": "EQP002",
                "nombre": "Nacional",
                "ciudad": "Medellin",
                "dt": "Juan Perez",
                "puntos": 0,
                "partidos_jugados": 0,
                "ganados": 0,
                "empatados": 0,
                "perdidos": 0,
                "goles_favor": 0,
                "goles_contra": 0
            }
        ]
        with open(archivo_equipos, 'w') as file:
            json.dump(equipos, file, indent=4)

# Cargar equipos desde el archivo JSON
def cargar_equipos():
    if os.path.exists(archivo_equipos):
        with open(archivo_equipos, 'r') as file:
            return json.load(file)
    else:
        return []

# Guardar equipos en el archivo JSON
def guardar_equipos(equipos):
    with open(archivo_equipos, 'w') as file:
        json.dump(equipos, file, indent=4)

# Función para registrar un equipo
def registrar_equipo():
    equipos = cargar_equipos()

    nombre = input("Ingrese el nombre del equipo: ")
    ciudad = input("Ingrese la ciudad del equipo: ")
    dt = input("Ingrese el nombre del director técnico: ")

    # Cálculos básicos
    ganados = int(input("Ingrese el número de partidos ganados: "))
    perdidos = int(input("Ingrese el número de partidos perdidos: "))
    empatados = int(input("Ingrese el número de partidos empatados: "))
    goles_favor = int(input("Ingrese el número de goles a favor: "))
    goles_contra = int(input("Ingrese el número de goles en contra: "))

    puntos = ganados * 3 + empatados

    # Crear el equipo
    nuevo_equipo = {
        "id": f"EQP{len(equipos) + 1:03}",
        "nombre": nombre,
        "ciudad": ciudad,
        "dt": dt,
        "puntos": puntos,
        "partidos_jugados": ganados + perdidos + empatados,
        "ganados": ganados,
        "empatados": empatados,
        "perdidos": perdidos,
        "goles_favor": goles_favor,
        "goles_contra": goles_contra
    }

    equipos.append(nuevo_equipo)
    guardar_equipos(equipos)
    print("Equipo registrado:", nuevo_equipo)

# Función para listar equipos
def listar_equipos():
    equipos = cargar_equipos()
    equipos.sort(key=lambda x: x["puntos"], reverse=True)  # Ordenar por puntos
    for equipo in equipos:
        print(f"ID: {equipo['id']} - Nombre: {equipo['nombre']} - Ciudad: {equipo['ciudad']} - DT: {equipo['dt']} - Puntos: {equipo['puntos']}")

# Función para actualizar las estadísticas de un equipo
def actualizar_estadisticas():
    equipos = cargar_equipos()
    equipo_id = input("Ingrese el ID del equipo a actualizar: ")
    for equipo in equipos:
        if equipo['id'] == equipo_id:
            resultado = input("¿El equipo ganó, empató o perdió? ").lower()
            goles_favor = int(input("Ingrese los goles a favor: "))
            goles_contra = int(input("Ingrese los goles en contra: "))

            if resultado == "ganó":
                equipo["ganados"] += 1
                equipo["puntos"] += 3
            elif resultado == "empató":
                equipo["empatados"] += 1
                equipo["puntos"] += 1
            elif resultado == "perdió":
                equipo["perdidos"] += 1
            else:
                print("Resultado no válido.")
                return

            equipo["goles_favor"] += goles_favor
            equipo["goles_contra"] += goles_contra
            equipo["partidos_jugados"] += 1

            guardar_equipos(equipos)
            print("Estadísticas actualizadas:", equipo)
            return

    print("Equipo no encontrado.")

# Menú de interacción básica
def menu():
    while True:
        print("\nMenu:")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Actualizar estadísticas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            actualizar_estadisticas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Iniciar el menú
inicializar_equipos()  # Inicializar equipos si no existen en el archivo
menu()


# 5 LOGICA ADICIONAL DEL SISTEMA 
#ARCHIVO JSON ADJUNTO


# 6 GESTOR DE ARBITROS

#ESTRUCTURA DE DATOS 
arbitros=[] #LISTA DE ARBITROS 
#DATOS DEL ARBITRO 1
arbitro_1 = {
 "id_arbitro": "ARB001", # Identificador unico del arbitro
 "nombre": "Carlos Rodriguez", # Nombre completo
 "experiencia": 5, # Anos de experiencia
 "categoria": "FIFA", # Categoria del arbitro
 "partidos_dirigidos": 14 # 
}
arbitros.append(arbitro_1)
# DATOS DEL ARBITRO 2 
arbitro_2 = {
 "id_arbitro": "ARB002", # Identificador unico del arbitro
 "nombre": "Wiliam Roldan", # Nombre completo
 "experiencia": 15, # Anos de experiencia
 "categoria": "FIFA", # Categoria del arbitro
 "partidos_dirigidos": 14 # Numero de partidos dirigidos
}
arbitros.append(arbitro_2)
# DATOS DEL ARBITRO 3
arbitro_3 = {
 "id_arbitro": "ARB003", # Identificador unico del arbitro
 "nombre": "Carlos Ortega", # Nombre completo
 "experiencia": 10, # Anos de experiencia
 "categoria": "FIFA", # Categoria del arbitro
 "partidos_dirigidos": 14 #
}
arbitros.append(arbitro_3)

# FUNCION 1 REGISTRAR ARBITRO 

# LISTA PARA ALMACENAR EL NUEVO ARBITRO
arbitros = []

def registrar_arbitro(nombre: str, experiencia: int, categoria: str) -> dict:

    # GENERA ID PARA EL ARBITRO 
    id_arbitro = f"ARB{len(arbitros) + 1:03d}" 

    # GENERA LOS DATOS PARA EL NUEVO ARBITRO
    nuevo_arbitro = {
        "id": id_arbitro,
        "nombre": nombre,
        "experiencia": experiencia,
        "categoria": categoria,
        "partidos_dirigidos": 0 
    }
    
    # GUARDA EL NUEVO ARBITRO EN LA LISTA "ARBITROS"
    arbitros.append(nuevo_arbitro)

    # RETORNA EL ARBITRO REGISTRADO
    return nuevo_arbitro

# EJEMPLO DE USO
arbitros = registrar_arbitro("Nicolas Gallo", 5, "FIFA") #LLAMADA DE LA FUNCION
print("EL NUEVO ARBITRO ES", arbitros)  #MUESTRA EN PANTALLA EL NUEVO ARBITRO

# FUNCION 2 ASIGNAR ARBITRO 
def asignar_arbitro(id_partido: str, id_arbitro: str) -> tuple:
    # FECHA PARA ASIGNAR EL ARBITRO AL PARTIDO
    fecha_asignacion = "2024-10-25"  
    asignacion = (id_partido, id_arbitro, fecha_asignacion)  # TUPLA PARA ASIGNAR AL ARBITRO POSICION POR POCISION 
    return asignacion  # Retornar la tupla

# EJEMPLO DE USO
asignacion_arbitro = asignar_arbitro("PAR001", "ARB001")
print("EL PARTIDO AL QUE SE LE ASIGNO EL ARBITRO ES:", asignacion_arbitro)

#FUNCION 3 REPORTE DE ARBITROS 
# Lista de arbitros
arbitros = [
    {
        "id_arbitro": "ARB001",
        "nombre": "Carlos Rodriguez",
        "experiencia": 5,
        "categoria": "FIFA",
        "partidos_dirigidos": 14
    },
    {
        "id_arbitro": "ARB002",
        "nombre": "Wiliam Roldan",
        "experiencia": 15,
        "categoria": "FIFA",
        "partidos_dirigidos": 20
    },
    {
        "id_arbitro": "ARB003",
        "nombre": "Carlos Ortega",
        "experiencia": 10,
        "categoria": "FIFA",
        "partidos_dirigidos": 18
    }
]

# Funcion muy simple para generar el reporte
def generar_reporte_arbitros():
    """
    Genera un reporte de todos los arbitros ordenado por el numero de partidos dirigidos.
    """
    # Vamos a usar un enfoque de intercambio (Bubble Sort) para ordenar la lista
    for i in range(len(arbitros)):
        for j in range(i + 1, len(arbitros)):
            if arbitros[i]["partidos_dirigidos"] < arbitros[j]["partidos_dirigidos"]:
                # Intercambiar los arbitros si el de la posicion i tiene menos partidos dirigidos
                arbitros[i], arbitros[j] = arbitros[j], arbitros[i]
    
    return arbitros

# Llamar a la funcion y mostrar el reporte
reporte = generar_reporte_arbitros()
for arbitro in reporte:
    print(f"ID: {arbitro['id_arbitro']}, Nombre: {arbitro['nombre']}, "
          f"Experiencia: {arbitro['experiencia']} anos, Categoria: {arbitro['categoria']}, "
          f"Partidos dirigidos: {arbitro['partidos_dirigidos']}")






