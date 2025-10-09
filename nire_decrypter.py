mapeaketa = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F',
    'G': 'G',
    'H': 'H',
    'I': 'I',
    'J': 'J',
    'K': 'K',
    'L': 'L',
    'M': 'M',
    'N': 'N',
    'Ñ': 'Ñ',
    'O': 'O',
    'P': 'P',
    'Q': 'Q',
    'R': 'R',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z'
}

texto_original = """
RBTJ EAJV SJ DBR YTVQV HBJR EAJV NQ TJZT DQ BJT VTB EAJV HTV J QJTG DQ VJR.  
DQ NJBTQJ VTB EAJV SJ HBJTZQV SJ NJBTJV QBJV RBTJ EAJV QJTG SJ TJG.  
ZJT EAJV TJZT VJR TJZ VQJ DQ EAJV SBJ EAJV NJBTQJ HTV ZJTQV TJG RBTJ EAJV QJTG.  
RBTJ VQJ SBJ TJG VTB SJ NJBTQJ DQ BJT EAJV ZJT VJR.  
DQ EAJV NJBTQJ SJ TJG RBTJ DQ HBJTZQV TJG EAJV QJTG NQ TJZT.  
EAJV SJ DQ TJZT NQ TJG DQ EAJV QJTG HTV SJ NJBTQJ.  
RBTJ EAJV SBJ NQ HTV TJG EAJV VTB DQ EAJV QJTG ZJTQV TJG.  
ZJT EAJV TJZT DQ HBJTZQV HTV NJBTQJ EAJV RBTJ DQ TJG VTB.  
EAJV QJTG NQ TJZT SJ NJBTQJ DQ BJT EAJV HTV.  
DQ NJBTQJ SJ HTV EAJV ZJT RBTJ DQ EAJV TJZT.
"""

def decrypter(texto_original, mapeaketa):
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    texto_descifrado = ""
    
    for char in texto_original:
        texto_descifrado += mapeaketa.get(char,char)
    
    print(texto_descifrado)
    return texto_descifrado

def contador_ordenado_mayor_a_menor(texto):
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    contador = {letra: 0 for letra in abecedario}
    
    for char in texto:
        if char in contador:
            contador[char] += 1
    
    # Ordenar el diccionario por frecuencia de mayor a menor
    contador_ordenado = dict(sorted(contador.items(), key=lambda item: item[1], reverse=True))
    
    for letra, freq in contador_ordenado.items():
        if freq > 0:
            print(f"{letra}: {freq}")
    
    return contador_ordenado

if __name__ == "__main__":
   contador_ordenado_mayor_a_menor(texto_original)
   print("Testu zifratua: \n")
   print(texto_original)
   print("\nTestu deszifratua: \n")
   decrypter(texto_original, mapeaketa)

