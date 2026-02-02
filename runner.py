def run(memory):
    counter = 0
    acc = 0
    currentInstruction = None
    index = 0
    while counter <= 99:
        #print(memory[counter])
        currentInstruction = str(memory[counter])
        skipAdd = False
        command = int(currentInstruction[0])
        operand = int(currentInstruction[-1])
        match command:

            #(currentInstruction[0])
            case 0:
                if currentInstruction == "000":
                    counter = 99999
                    continue
                else:
                    pass
            case 1: # add
                
                acc += int(memory[int(currentInstruction[1:])])
            case 2: # sub
                acc -= int(memory[int(currentInstruction[1:])])
            case 3:
                index = int(currentInstruction[1:])
                memory[index] = acc
            case 4:
                print(chr(acc))
            case 5: # LDA
                data = memory[int(currentInstruction[1:])]
                acc = int(data)
            case 6: # BRA
                counter = int(currentInstruction[1:])
                skipAdd = True
            case 7:# BRZ
                if acc == 0:
                    counter = int(currentInstruction[1:])
                    
                    skipAdd = True
                    
            case 8: # BRP
                if acc > 0:
                    counter = int(currentInstruction[1:])
                    skipAdd = True
            case 9: # handles the input and output
                if operand == 1:
                    acc = int(input(">> "))
                elif operand == 2:
                    print(acc)
        if not skipAdd:
            counter +=1
    #print(acc)

if __name__ == "__main__":
    run([510, 313, 513, 400, 111, 313, 212, 709, 602, '000', '032', '01', '0127', '00', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
