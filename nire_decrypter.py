mapeaketa = {
    'A': 'D',
    'B': 'Ñ',
    'C': 'I',
    'D': 'P',
    'E': 'A',
    'F': 'X',
    'G': 'J',
    'H': 'T',
    'I': 'O',
    'J': 'N',
    'K': 'R',
    'L': 'Z',
    'M': 'H',
    'N': 'S',
    'Ñ': 'Z',
    'O': 'F',
    'P': 'M',
    'Q': 'B',
    'R': 'C',
    'S': 'Q',
    'T': 'L',
    'U': 'G',
    'V': 'Y',
    'W': 'X',
    'X': 'E',
    'Y': 'K',
    'Z': 'U'
}

texto_original = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"

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
   print("TEXTO ORIGINAL: \n")
   print(texto_original)
   print("\nTEXTO DESCIFRADO: \n")
   decrypter(texto_original, mapeaketa)

