#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Cifrado/Descifrado por Sustitución de Letras
======================================================

Este programa permite cifrar y descifrar texto usando un abecedario de sustitución personalizable.
Puedes modificar fácilmente el mapeo de letras cambiando las variables ABECEDARIO_ORIGINAL y ABECEDARIO_SUSTITUCION.

Autor: Tu Nombre
Fecha: 4 de octubre de 2025
"""

# ====================================================
# CONFIGURACIÓN DEL ABECEDARIO (MODIFICABLE)
# ====================================================

# Abecedario original (español estándar)
ABECEDARIO_ORIGINAL = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Abecedario de sustitución (modifica este para cambiar el cifrado)
# Cada letra del abecedario original se sustituye por la letra en la misma posición aquí
ABECEDARIO_SUSTITUCION = "ZYXWVUTSRQPOÑMLKJIHGFEDCBA"

# ====================================================
# EJEMPLOS DE OTROS ABECEDARIOS DE SUSTITUCIÓN
# ====================================================

# Ejemplo 1: Desplazamiento César (shift +3)
# ABECEDARIO_SUSTITUCION = "DEFGHIJKLMNÑOPQRSTUVWXYZABC"

# Ejemplo 2: Abecedario aleatorio
# ABECEDARIO_SUSTITUCION = "QWERTYUIOPÑLKJHGFDSAZXCVBNM"

# Ejemplo 3: Intercambio de vocales y consonantes
# ABECEDARIO_SUSTITUCION = "EBCDIFJHIKLMNÑOQURSTUVAXYZU"

# Ejemplo 4: Abecedario invertido (actual)
# ABECEDARIO_SUSTITUCION = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

def crear_mapeo_sustitucion():
    """
    Crea el diccionario de mapeo de sustitución basado en los abecedarios configurados.
    
    Returns:
        dict: Diccionario con el mapeo de cada letra original a su sustitución
    """
    if len(ABECEDARIO_ORIGINAL) != len(ABECEDARIO_SUSTITUCION):
        raise ValueError("Los abecedarios deben tener la misma longitud")
    
    # Crear mapeo para mayúsculas
    mapeo = {}
    for i, letra_original in enumerate(ABECEDARIO_ORIGINAL):
        mapeo[letra_original] = ABECEDARIO_SUSTITUCION[i]
    
    # Crear mapeo para minúsculas
    for i, letra_original in enumerate(ABECEDARIO_ORIGINAL.lower()):
        mapeo[letra_original] = ABECEDARIO_SUSTITUCION[i].lower()
    
    return mapeo

def crear_mapeo_inverso():
    """
    Crea el diccionario de mapeo inverso para descifrar.
    
    Returns:
        dict: Diccionario con el mapeo inverso (de sustitución a original)
    """
    if len(ABECEDARIO_ORIGINAL) != len(ABECEDARIO_SUSTITUCION):
        raise ValueError("Los abecedarios deben tener la misma longitud")
    
    # Crear mapeo inverso para mayúsculas
    mapeo_inverso = {}
    for i, letra_sustitucion in enumerate(ABECEDARIO_SUSTITUCION):
        mapeo_inverso[letra_sustitucion] = ABECEDARIO_ORIGINAL[i]
    
    # Crear mapeo inverso para minúsculas
    for i, letra_sustitucion in enumerate(ABECEDARIO_SUSTITUCION.lower()):
        mapeo_inverso[letra_sustitucion] = ABECEDARIO_ORIGINAL[i].lower()
    
    return mapeo_inverso

def cifrar_texto(texto):
    """
    Cifra un texto usando el abecedario de sustitución configurado.
    
    Args:
        texto (str): Texto a cifrar
        
    Returns:
        str: Texto cifrado
    """
    mapeo = crear_mapeo_sustitucion()
    texto_cifrado = ""
    
    for caracter in texto:
        if caracter in mapeo:
            texto_cifrado += mapeo[caracter]
        else:
            # Mantener espacios, números, puntuación, etc.
            texto_cifrado += caracter
    
    return texto_cifrado

def descifrar_texto(texto_cifrado):
    """
    Descifra un texto usando el mapeo inverso del abecedario de sustitución.
    
    Args:
        texto_cifrado (str): Texto cifrado a descifrar
        
    Returns:
        str: Texto descifrado (original)
    """
    mapeo_inverso = crear_mapeo_inverso()
    texto_descifrado = ""
    
    for caracter in texto_cifrado:
        if caracter in mapeo_inverso:
            texto_descifrado += mapeo_inverso[caracter]
        else:
            # Mantener espacios, números, puntuación, etc.
            texto_descifrado += caracter
    
    return texto_descifrado

def mostrar_mapeo():
    """
    Muestra el mapeo de sustitución actual de forma visual.
    """
    print("=" * 50)
    print("MAPEO DE SUSTITUCIÓN ACTUAL")
    print("=" * 50)
    print(f"Original:    {ABECEDARIO_ORIGINAL}")
    print(f"Sustitución: {ABECEDARIO_SUSTITUCION}")
    print("=" * 50)
    
    print("\nMapeo detallado:")
    for i, (original, sustitucion) in enumerate(zip(ABECEDARIO_ORIGINAL, ABECEDARIO_SUSTITUCION)):
        print(f"  {original} -> {sustitucion}    {original.lower()} -> {sustitucion.lower()}")
        if (i + 1) % 5 == 0:  # Salto de línea cada 5 elementos
            print()

def menu_interactivo():
    """
    Menú interactivo para usar el sistema de cifrado/descifrado.
    """
    while True:
        print("\n" + "=" * 60)
        print("   SISTEMA DE CIFRADO POR SUSTITUCIÓN DE LETRAS")
        print("=" * 60)
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Mostrar mapeo actual")
        print("4. Ejemplo de uso")
        print("5. Salir")
        print("-" * 60)
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            texto = input("\nIngresa el texto a cifrar: ")
            resultado = cifrar_texto(texto)
            print(f"\n✅ Texto cifrado: {resultado}")
            
        elif opcion == "2":
            texto = input("\nIngresa el texto a descifrar: ")
            resultado = descifrar_texto(texto)
            print(f"\n✅ Texto descifrado: {resultado}")
            
        elif opcion == "3":
            mostrar_mapeo()
            
        elif opcion == "4":
            mostrar_ejemplo()
            
        elif opcion == "5":
            print("\n👋 ¡Hasta luego!")
            break
            
        else:
            print("\n❌ Opción no válida. Por favor, selecciona 1-5.")

def mostrar_ejemplo():
    """
    Muestra un ejemplo completo de cifrado y descifrado.
    """
    print("\n" + "=" * 50)
    print("EJEMPLO DE USO")
    print("=" * 50)
    
    texto_original = "Hola Mundo! ¿Cómo estás? 123"
    
    print(f"Texto original: {texto_original}")
    
    # Cifrar
    texto_cifrado = cifrar_texto(texto_original)
    print(f"Texto cifrado:  {texto_cifrado}")
    
    # Descifrar
    texto_descifrado = descifrar_texto(texto_cifrado)
    print(f"Texto descifrado: {texto_descifrado}")
    
    # Verificar que el descifrado es correcto
    if texto_original == texto_descifrado:
        print("\n✅ ¡El cifrado y descifrado funcionan correctamente!")
    else:
        print("\n❌ Error en el proceso de cifrado/descifrado")

def cambiar_abecedario_sustitucion(nuevo_abecedario):
    """
    Función para cambiar el abecedario de sustitución programáticamente.
    
    Args:
        nuevo_abecedario (str): Nuevo abecedario de sustitución
    """
    global ABECEDARIO_SUSTITUCION
    
    if len(nuevo_abecedario) != len(ABECEDARIO_ORIGINAL):
        raise ValueError(f"El nuevo abecedario debe tener {len(ABECEDARIO_ORIGINAL)} caracteres")
    
    ABECEDARIO_SUSTITUCION = nuevo_abecedario.upper()
    print(f"✅ Abecedario de sustitución actualizado: {ABECEDARIO_SUSTITUCION}")

# ====================================================
# FUNCIÓN PRINCIPAL
# ====================================================

def main():
    """
    Función principal del programa.
    """
    print("🔐 Sistema de Cifrado por Sustitución de Letras")
    print("📝 Para modificar el abecedario, edita las variables al inicio del archivo")
    
    # Mostrar configuración actual
    mostrar_mapeo()
    
    # Mostrar ejemplo automático
    mostrar_ejemplo()
    
    # Iniciar menú interactivo
    menu_interactivo()

# ====================================================
# EJECUCIÓN DEL PROGRAMA
# ====================================================

if __name__ == "__main__":
    main()

# ====================================================
# EJEMPLOS DE USO PROGRAMÁTICO
# ====================================================

"""
# Ejemplo 1: Uso básico
texto = "Hola mundo"
cifrado = cifrar_texto(texto)
descifrado = descifrar_texto(cifrado)

# Ejemplo 2: Cambiar abecedario dinámicamente
cambiar_abecedario_sustitucion("QWERTYUIOPÑLKJHGFDSAZXCVBNM")
nuevo_cifrado = cifrar_texto("Hola mundo")

# Ejemplo 3: Cifrar un párrafo completo
parrafo = '''
Este es un párrafo de ejemplo que contiene múltiples líneas,
números como 123 y 456, signos de puntuación como ¡¿?!,
y caracteres especiales como @#$%.
'''
parrafo_cifrado = cifrar_texto(parrafo)
"""
