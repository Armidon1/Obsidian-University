#easypeasy

def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])

with open('flag.enc', 'r') as f:
    lines = f.readlines()
    line1 = bytes.fromhex(lines[0].split()[-1])
    line2 = bytes.fromhex(lines[-1].split()[-1])
   # print(line2)
    key=xor(line2,b"ccit{")
    key = xor(bytes.fromhex(lines[4]), b"Insieme")
    key = xor(bytes.fromhex(lines[6]), b"sognando")
    key = xor(bytes.fromhex(lines[3]), b"e il nostro")
    key = xor(bytes.fromhex(lines[0]), b"Se nel mondo")
    key = xor(bytes.fromhex(lines[1]), b"e ognuno guarda")
    key = xor(bytes.fromhex(lines[2]), b"si alleggerirebbe")
    key = xor(bytes.fromhex(lines[1]), b"e ognuno guardasse")
    key = xor(bytes.fromhex(lines[7]), b"dove il bene comune")
    key = xor(bytes.fromhex(lines[4]), b"Insieme costruiremmo")
    key = xor(bytes.fromhex(lines[0]), b"Se nel mondo regnasse")
    key = xor(bytes.fromhex(lines[3]), b"e il nostro mondo risplenderebbe")
    key = xor(bytes.fromhex(lines[0]), b"Se nel mondo regnasse un briciolo")
    key = xor(bytes.fromhex(lines[8]), b"ccit{G4br13l3_gull4_pr0f_di_4n4l1s1")
    key = xor(bytes.fromhex(lines[6]), b"sognando un futuro di pace e fraternit")
    key = xor(bytes.fromhex(lines[5]), b'abbattendo muri di indifferenza e orgogl')
    key = xor(bytes.fromhex(lines[4]), b'Insieme costruiremmo ponti di solidariet\xc3\xa0')
    key = xor(bytes.fromhex(lines[3]), b'e il nostro mondo risplenderebbe di un amore')
    key = xor(bytes.fromhex(lines[1]), b'e ognuno guardasse al suo prossimo come fratello')


    i=0
    while i<len(lines): 
        lines[i] = xor(bytes.fromhex(lines[i]),key)
        print(lines[i])
        i+=1

    


    #plain_line1_xor_line2 = xor(line1,line2)
   

