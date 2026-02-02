from assembler import assemble
def run(memory):
    counter = 0
    acc = 0
    currentInstruction = None
    index = 0
    while counter < 99:
        #print(memory[counter])
        #print(counter)
        currentInstruction = str(memory[counter])
        skipAdd = False
        command = int(currentInstruction[0])
        operand = int(currentInstruction[-1])
        debug = False
        match command:

            #(currentInstruction[0])
            case 0:
                if currentInstruction == "000":
                    counter = 99999
                    continue
                else:
                    print("pass")
            case 1: # add
                address = int(currentInstruction[1:])
                acc += int(memory[address])
                if debug:
                    print(f"add {address}")
            case 2: # sub
                if debug:
                    print("sub")
                acc -= int(memory[int(currentInstruction[1:])])
            case 3: # STA / STO
                if debug:
                    print("store")
                index = int(currentInstruction[1:])
                memory[index] = "0"+str(acc)
            case 4:
                if debug:
                    print("OTC")
                print(chr(acc))
            case 5: # LDA
                if debug:
                    print("load")
                data = memory[int(currentInstruction[1:])]
                acc = int(data)
            case 6: # BRA
                if debug:
                    print("branch always")
                counter = int(currentInstruction[1:])
                skipAdd = True
            case 7:# BRZ
                
                if acc == 0:
                    counter = int(currentInstruction[1:])
                    skipAdd = True
                    if debug:
                        print("branch if 0")
                    
            case 8: # BRP
                
                if acc > 0:
                    counter = int(currentInstruction[1:])
                    skipAdd = True
                    if debug:
                        print("branch if positive")
            case 9: # handles the input and output
                
                if operand == 1:
                    if debug:
                        print("input")
                    acc = int(input(">> "))
                elif operand == 2:
                    print(f"{acc}")

        if not skipAdd:
            counter +=1
    #print(acc)

if __name__ == "__main__":
    memory = assemble("code.txt")
    run(memory)
