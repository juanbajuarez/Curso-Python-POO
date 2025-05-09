# Autor: Juan Bautista Juárez
# Fecha: Abril de 2025
# Descripción: Your task is to create userlinks for the url,
# you will be given a username and must return a valid link.

import urllib.parse
# Este módulo define una interfaz estándar para dividir cadenas de
# Localizador Uniforme de Recursos (URL) en componentes (esquema de
# direccionamiento, ubicación de red, ruta, etc.), para combinar los
# componentes nuevamente en una cadena de URL y para convertir una "URL
# relativa" en una URL absoluta dada una "URL base".
def generate_link(username)->str:
    """
    Funcón que genera un link utilizando encoded recomendado por codewars.
    :param username: Nombre del usuario
    :return: Link utilizando el nombre del usuario
    """
    encoded = urllib.parse.quote(username)
    return f"http://www.codewars.com/users/{encoded}"


#Código a nivel de módulo.
if __name__ == '__main__':
    #Mi código para hacer pruebas.

    print(generate_link('matt c'))
    print(generate_link('g964'))
    print(generate_link('Juan Bautista Juáez')) #link de mi perfil de codewars
