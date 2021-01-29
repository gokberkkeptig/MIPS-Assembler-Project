#GB-Assembler
#Yusuf Gokberk Keptig - 2079366
#Mehmet Bengican Altunsu - 2329126

import re, os
#pre-defined list in order to reduce writing same fixed values over and over again
#instruction name list
namelist = [
 'add',     #check
 'sll',     #check
 'slt',     #check
 'jr',      #Check
 'addi',    #check
 'lw',      #check
 'sw',      #check
 'beq',     #Check
 'bne',     #Check
 'slti',    #Check
 'j',       #Check
 'jal',     #Check
 'move']    #Check
#op code list according to operations
oplist = ['000000',
 '000000',
 '000000',
 '000000',
 '001000',
 '100011',
 '101011',
 '000100',
 '000101',
 '001010',
 '000010',
 '000011',
 '000000']
#function code list according to operations
funclist = [
 '100000',
 '000000',
 '101010',
 '001000',
 'NA',
 'NA',
 'NA',
 'NA',
 'NA',
 'NA',
 'NA',
 'NA',
 '100000']
#instruction type list according to operations
formatlist = [
 'R',
 'R',
 'R',
 'R',
 'I',
 'I',
 'I',
 'I',
 'I',
 'I',
 'J',
 'J',
 'R']
#register list
registerlist = ['$zero',
 '$at',
 '$v0', '$v1',
 '$a0', '$a1', '$a2', '$a3',
 '$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7',
 '$s0', '$s1', '$s2', '$s3', '$s4', '$s5', '$s6', '$s7',
 '$t8', '$t9',
 '$k0', '$k1',
 '$gp',
 '$sp',
 '$fp',
 '$ra']
#register list in binary according to register list
registerBinAdd = ['00000',
 '00001',
 '00010', '00011',
 '00100', '00101', '00110', '00111',
 '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111',
 '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111',
 '11000', '11001',
 '11010', '11011',
 '11100',
 '11101',
 '11110',
 '11111']

#if address could not be found this method will print a message related with
def errorAddr():
    print('Specified address does not exist!')

#ones complement
def flip(c):
    if c == '0':
        return '1'
    return '0'

#twos complement
def twoscomp(bin):
    fig = len(bin)
    ones = ''
    twos = ''
    for t in range(fig):
        ones += flip(bin[t])

    ones = list(ones.strip(''))
    twos = list(ones)
    twostr = ''
    for t in range(fig - 1, -1, -1):
        if ones[t] == '1':
            twos[t] = '0'
        else:
            twos[t] = '1'
            break

    if t == -1:
        twos.insert(0, '1')
    for i in twos:
        twostr = twostr + i

    return twostr

#initilize instruction type list with related bits

instructionR = ['000000', '00000', '00000', '00000', '00000', '000000']
instructionI = ['000000', '00000', '00000', '0000000000000000']
instructionJ = ['000000', '00000000000000000000000000']

#this method converts register name into binary and returns it
def registerBin(r):
    for i in range(32):
        if registerlist[i] == r:
            break
        if i == 31:
            if registerlist[i] != r:
                errorAddr()

    rs = registerBinAdd[i]
    return rs

#gets menu method
def menu():
    inp = input('\n------------------------\n1.Interactive Mode \n2.Batch Mode\n3.Exit\n------------------------\nChoose Mode: ')
    return inp

#this method takes result value and returns it as a string
def resultStr(s):
    string = ''
    return string.join(s)

#this is main method where all calculations are done
def fun(code, labeladds):
    #instruction fetch and gets values accordingly
    a = code.split(':', 2)
    if len(a) == 2:
        # if there is a label discard the label
        b = re.split(' |,', a[1])
        # then fetch instructions based on their length
        if len(b) == 4:
            op = b[0]
            rd = b[1]
            rs = b[2]
            rt = b[3]
        elif len(b) == 3:
            op = b[0]
            rs = b[1]
            rd = b[2]
            rt = b[2]
        elif len(b) == 2:
            op = b[0]

    #if there is no label in the instruction
    else:
        b = re.split(' |,', a[0])
        # then fetch instructions based on their length
        if len(b) == 4: #Instructions with 4 fields(beq,add etc.)
            op = b[0]
            rd = b[1]
            rs = b[2]
            rt = b[3]
        elif len(b) == 3: #Instructions with 3 fields (lw,sw etc.)
            op = b[0]
            rs = b[1]
            rd = b[2]
            rt = b[2]
        elif len(b) == 2: #Instructions with 2 fields (j,jr etc.)
            op = b[0]
            rs = b[1]
    # get the index according to opcode
    for k in range(13):
        if namelist[k] == op:
            break

    # add or slt conversion
    if k == 0 or (k == 2):
        instructionR[0] = oplist[k]
        instructionR[1] = registerBin(rs)
        instructionR[2] = registerBin(rt)
        instructionR[3] = registerBin(rd)
        instructionR[4] = '00000'
        instructionR[5] = funclist[k]
        result = resultStr(instructionR)
        result = hex(int(result, 2))
        result = str(result)
        result = result[:2] + "0" + result[2:]

        return result
    # sll conversion
    if k == 1:
        instructionR[0] = oplist[k]
        instructionR[1] = '00000'
        instructionR[2] = registerBin(rs)
        instructionR[3] = registerBin(rd)
        rt = int(rt)
        rt = format(rt, '#05b')
        rt = str(rt).replace('0b', '00')
        instructionR[4] = rt
        instructionR[5] = funclist[k]
        result = resultStr(instructionR)
        result = hex(int(result, 2))
        result = str(result)
        result = result[:2] + "00" + result[2:]
        return result

    # move conversion
    if k == 12:
        instructionR[0] = oplist[k]
        instructionR[1] = registerBin(rd)
        instructionR[2] = registerBin('$zero')
        instructionR[3] = registerBin(rs)
        instructionR[4] = '00000'
        instructionR[5] = funclist[k]
        result = resultStr(instructionR)
        result = hex(int(result, 2))
        result = str(result)
        result = result[:2] + "0" + result[2:]
        return result

    # jr conversion
    if k == 3:
        instructionR[0] = oplist[k]
        instructionR[1] = registerBin(rs)
        instructionR[2] = '00000'
        instructionR[3] = '00000'
        instructionR[4] = '00000'
        instructionR[5] = '001000'
        result = resultStr(instructionR)
        result = hex(int(result, 2))
        result = result[:2] + "0" + result[2:]
        return result

    # addi or slti conversion
    if k == 4 or (k == 9):
        instructionI[0] = oplist[k]
        instructionI[1] = registerBin(rs)
        instructionI[2] = registerBin(rd)
        rt = int(rt)
        if rt < 0:
            comp = 1
        else:
            comp = 0
        rt = format(rt, '#016b')
        rt = str(rt).replace('0b', '00')
        if comp == 1:
            rt = str(rt).replace('-', '0')
            rt = twoscomp(rt)
        instructionI[3] = rt
        result = resultStr(instructionI)
        result = hex(int(result, 2))
        return result

    # beq or bne conversion
    if k == 7 or (k == 8):
        target = labeladds.get(rt, 0)
        target = target[18:]
        instructionI[0] = oplist[k]
        instructionI[1] = registerBin(rd)
        instructionI[2] = registerBin(rs)
        instructionI[3] = target
        result = resultStr(instructionI)
        result = hex(int(result, 2))
        return result

    # lw or sw conversion
    if k == 5 or (k == 6):
        instructionI[0] = oplist[k]
        instructionI[2] = registerBin(rs)
        part = re.split('\\(|\\)', rt)
        rs2 = part[1]
        rsIm = part[0]
        instructionI[1] = registerBin(rs2)
        rsIm = int(rsIm)
        rsIm = format(rsIm, '#016b')
        rsIm = str(rsIm).replace('0b', '00')
        instructionI[3] = rsIm
        result = resultStr(instructionI)
        result = hex(int(result, 2))
        return result

    # j or jal conversion
    if k == 10 or (k == 11):
        target = labeladds[rs]
        target = target[8:]
        instructionJ[0] = oplist[k]
        instructionJ[1] = target
        result = resultStr(instructionJ)
        result = hex(int(result, 2))
        result = str(result)
        result = result[:2] + "0" + result[2:]
        return result

#mode = -5 is to enter first while loop to start program
mode = -5
while mode != 3:
    mode = menu()
    #mode 1 interactive mode
    if mode == '1':
        print('-----------------------Interactive Mode-------------------------\n')
        try:
            code = input('Please write the instruction in (instruction $rs,$rt...) format: ')
            result = fun(code, 0)
            print("Hex Instruction: ", result)
        except:
            print("Please follow the instruction format as (addi $s1,$s1,-17)!")
        continue
    # mode 2 batch mode
    elif mode == '2':
        #reads from file instructions.src
        filepath = 'instructions.src'
        with open(filepath) as f:
            #starts pc from 0x80001000
            PC = 2147487744
            #reads label accordingly and change pc value relatively
            labeladds = {}
            code = f.readline().rstrip('\n')
            a = code.split(':', 2)
            if len(a) == 2:
                label = a[0]
                temp = PC
                temp = format(temp, '#016b')
                temp = str(temp).replace('0b', '00')
                labeladds[label] = temp
            # inc Pc by 4 to read next adress
            PC = PC + 4
            while code:
                code = f.readline().rstrip('\n')
                a = code.split(':', 2)
                if len(a) == 2:
                    label = a[0]
                    temp = PC
                    temp = format(temp, '#016b')
                    temp = str(str(temp).replace('0b', '00'))
                    labeladds[label] = temp
                #inc Pc by 4 to read next adress
                PC = PC + 4
            f.seek(0)
            code = f.readline().rstrip('\n')
            #creates result.obj file and writes the output in it
            with open('result.obj', 'w') as the_file:
                # starts pc from 0x80001000
                PC = 2147487744
                result = fun(code, labeladds)
                the_file.write(hex(PC) + ' ' + result + os.linesep)
                PC = PC + 4
                while code:
                    code = f.readline().rstrip('\n')
                    if code == '':
                        break
                    else:
                        result = fun(code, labeladds)
                        the_file.write(hex(PC) + ' ' + result + os.linesep)
                        PC = PC + 4
                    continue
                print("Hex file 'result.obj' is created successfully!")
    #mode 3 exit
    if mode == '3':
        break
exit()