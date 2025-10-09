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

testu_originala = """
ABCD
"""

def decrypter(testu_originala, mapeaketa):
    alfabetoa = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    testu_deszifratua = ""
    
    for char in testu_originala:
        testu_deszifratua += mapeaketa.get(char,char)
    
    print(testu_deszifratua)
    return testu_deszifratua

def karak_kont_ordenatuta(testua):
    alfabetoa = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    kont = {letra: 0 for letra in alfabetoa}
    
    for char in testua:
        if char in kont:
            kont[char] += 1
    
    # Hiztegia ordenatu handienetik txikienera
    kontagailu_ordenatua = dict(sorted(kont.items(), key=lambda item: item[1], reverse=True))
    
    for letra, frek in kontagailu_ordenatua.items():
        if frek > 0:
            print(f"{letra}: {frek}")
    
    return kontagailu_ordenatua

if __name__ == "__main__":
   karak_kont_ordenatuta(testu_originala)
   print("Testu zifratua: \n")
   print(testu_originala)
   print("\nTestu deszifratua: \n")
   decrypter(testu_originala, mapeaketa)

