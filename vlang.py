import enum
import sys
import os
import re
import itertools


Keywords = enum.Enum('Keywords',
                     """number 
                     venumAdd 
                     venumMin
                     venumDiv
                     venumMul
                     venumPrintln
                     venumPrint
                     venumEq
                     venumNotEq
                     venumGt
                     venumMod
                     venumLs
                     venumGte
                     venumLte
                     venumIf
                     venumEnd
                     venumString
                     venumMem
                     venumIdf
                     venumPop
                     venumIncVar
                     venumDo
                     venumEndLoop
                     sus
                     venumInclude
                     venumHalt
                     venumContinue
                     venumInput
                     """)

multi_vars_list = ["+=", "=", "/=", "*="]

def cross_reference(start, stop, content, index, reverse=False): 
    ifs_between = 0
    multi_vars = 0
    checker = 1 if reverse else -1

    loop_range = None
    if reverse:
        loop_range = range(index - 1, 0, -1)
    else:
        loop_range = range(index, len(content))
    for i in loop_range:
        if content[i + checker] in multi_vars_list:
            print(content[i + 1])
            multi_vars += 1
        if content[i] == start and i != index:
            ifs_between += 1
        elif content[i] == stop and ifs_between != 0:
            ifs_between -= 1
        elif content[i] == stop and ifs_between == 0:
            return i - multi_vars

def pre_process(content):
    for index, line in enumerate(content):
        if line == "include":
            path = content[index + 1]
            if path.startswith("\"") and path.endswith("\"") and os.path.isfile(path[1:-1]):
                path = path[1:-1]
            else:
                raise Exception("Include path invalid: %s" % path)
            del content[index: index + 2]
            contents = parse_to_individual(path)
            content[index: index] = contents
    return content

def parse_to_individual(filename):
    lines = open(filename).readlines()
    lines = [line.strip().split("//")[0] for line in lines]
    content = [re.findall(r'"[^"]*"|[^ ]+', line) for line in lines]
    parsed_content = list(itertools.chain.from_iterable(content))
    parsed_content = pre_process(parsed_content)
    return parsed_content
        

def make_tokens(content):
    toks = []
    vars = []
    for index, line in enumerate(content):
        
        if line.startswith("\"") and line.endswith("\""):
            toks.append((line[1:-1], Keywords.venumString))
        elif line.isnumeric():
            toks.append((int(line), Keywords.number))
        elif line == "+":
            toks.append((None, Keywords.venumAdd))
        elif line == "-":
            toks.append((None, Keywords.venumMin))
        elif line == "/":
            toks.append((None, Keywords.venumDiv))
        elif line == "*":
            toks.append((None, Keywords.venumMul))
        elif line == "%":
            toks.append((None, Keywords.venumMod))
        elif line == "print":
            toks.append((None, Keywords.venumPrint))
        elif line == "println":
            toks.append((None, Keywords.venumPrintln))
        elif line == "==":
            toks.append((None, Keywords.venumEq))
        elif line == "!=":
            toks.append((None, Keywords.venumNotEq))
        elif line == ">":
            toks.append((None, Keywords.venumGt))
        elif line == "<":
            toks.append((None, Keywords.venumLs))
        elif line == ">=":
            toks.append((None, Keywords.venumGte))
        elif line == u"à¶ž":
            toks.append((None, Keywords.sus))
        elif line == "<=":
            toks.append((None, Keywords.venumLte))
        elif line == "if":
            toks.append((None, Keywords.venumIf, cross_reference("if", "end", content, index)))
        elif line == "end":
            toks.append((None, Keywords.venumEnd))
        elif line == "do":
            toks.append((None, Keywords.venumDo, cross_reference("do", "endloop", content, index)))
        elif line == "halt":
            toks.append((None, Keywords.venumHalt))
        elif line == "endloop" or line == "continue":
            toks.append((cross_reference("endloop", "do", content, index, True), Keywords.venumEndLoop))
        elif index < len(content) and content[index + 1] == "+=":
            toks.append((content[index], Keywords.venumIncVar, int(content[index + 2])))
            del content[index: index + 2]
        elif index < len(content) and  content[index + 1 ] == "=":
            vars.append(line)
            val = content[index + 2]
            if val.isnumeric():
                val = int(val)
            # who needs real expressions lol
            elif val.startswith("\"") and val.endswith("\""):
                val = str(val).replace("\"", "")
            elif val == "pop":
                val = Keywords.venumPop
            elif val == "input":
                val = Keywords.venumInput
            else:
                raise Exception("Assigment value not allowed: %s" % val)
            toks.append((content[index], Keywords.venumMem, val))
            del content[index: index + 2]
        elif line in vars:
            toks.append((line, Keywords.venumIdf))
        else:
            raise Exception("Unknow operation %s" % line)
    return toks

def simulate(tokens):
    mem = {}
    pc = 0
    stack = []
    
    while pc < len(tokens):
        token = tokens[pc]
        operation = token[1]
        if operation == Keywords.number:
            stack.insert(0, token[0])
        elif operation == Keywords.venumString:
            stack.insert(0, token[0])
        elif operation == Keywords.venumAdd:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            stack.insert(0, operand1 + operand2)
        elif operation == Keywords.venumMin:
            operand2 = stack.pop(0)
            operand1 = stack.pop(0)
            stack.insert(0, operand1 - operand2)
        elif operation == Keywords.venumDiv:
            operand2 = stack.pop(0)
            operand1 = stack.pop(0)
            stack.insert(0, operand1 / operand2)
        elif operation == Keywords.venumMul:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            stack.insert(0, operand1 * operand2)
        elif operation == Keywords.venumMod:
            # print(stack)
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            stack.insert(0, operand2 % operand1)
        elif operation == Keywords.venumPrint:
            print(stack.pop(0), end="")
        elif operation == Keywords.venumPrintln:
            print()
            print(stack.pop(0))
        elif operation == Keywords.venumEq:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            result = operand1 == operand2
            stack.insert(0, result)
        elif operation == Keywords.venumNotEq:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            result = operand1 != operand2
            stack.insert(0, result)
        elif operation == Keywords.venumGt:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            result = operand1 > operand2
            stack.insert(0, result)
        elif operation == Keywords.venumLs:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            result = operand1 < operand2
            stack.insert(0, result)
        elif operation == Keywords.venumGte:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            result = operand1 >= operand2
            stack.insert(0, result)
        elif operation == Keywords.venumLte:
            operand1 = stack.pop(0)
            operand2 = stack.pop(0)
            result = operand1 <= operand2
            stack.insert(0, result)
        elif operation == Keywords.venumHalt:
            continue
        elif operation == Keywords.venumDo:
            stack_top = stack.pop(0)
            # print(stack_top)
            if stack_top:
                pc += 1
                continue
            else:
                pc = token[2] 
                continue
        elif operation == Keywords.venumEndLoop:
            pc = token[0] - 3
            continue
        elif operation == Keywords.sus:
            stack.insert(0, u"sussy mogus ඞ")
        elif operation == Keywords.venumIf:
            do_jmp = stack.pop(0)
            if do_jmp:
                pc += 1
                continue
            else: 
                pc = token[2]
                continue
        elif operation == Keywords.venumEnd:
            pc += 1
            continue 
        elif operation == Keywords.venumMem:
            val = token[2]
            if val == Keywords.venumPop:
                val = stack.pop(0)
            elif val == Keywords.venumInput:
                val = input()
                if val.isnumeric():
                    val = int(val)
            mem[token[0]] = val
        elif operation == Keywords.venumIdf:
            stack.insert(0, mem[token[0]])
        elif operation == Keywords.venumIncVar:
            mem[token[0]] += token[2]
            # print(mem[token[0]])
            pc += 1
            continue
        pc += 1
         
        
def compile(tokens):
    raise Exception("Not all features are in compilation mode")
    f = open("output.asm", "w")
    
    f.write("global _start\n")
    f.write("section .text\n")
    f.write("_start: \n")
    
    pc = 0
    stack = []
    while pc < len(tokens):
        token = tokens[pc]
        operation = token[1]
        if operation == Keywords.number:
            f.write(f"  ; push {token[0]} on top of the stack\n")
            f.write(f"  push {token[0]}\n")
        elif operation == Keywords.venumAdd:
            f.write(f"  ; pop 2 elements of stack, add them and push back \n")
            f.write(f"  pop eax \n")
            f.write(f"  pop ebx \n")
            f.write(f"  add eax, ebx \n")
            f.write(f"  push eax \n")
        elif operation == Keywords.venumMin:
            f.write(f"  ; pop 2 elements of stack, substract them and push back \n")
            f.write(f"  pop ebx \n")
            f.write(f"  pop eax \n")
            f.write(f"  sub eax, ebx \n")
            f.write(f"  push eax \n")
        elif operation == Keywords.venumDiv:
           f.write(f"  ; pop 2 elements of stack, div them and push back \n")
           f.write(f"  pop ebx \n")
           f.write(f"  pop eax \n")
           f.write(f"  div eax, ebx \n")
           f.write(f"  push eax \n")
        elif operation == Keywords.venumMul:
            f.write(f"  ; pop 2 elements of stack, multiply them and push back \n")
            f.write(f"  pop eax \n")
            f.write(f"  pop ebx \n")
            f.write(f"  mul eax, ebx \n")
            f.write(f"  push eax \n")
        elif operation == Keywords.venumPrint:
            f.write(f"  ; call print (not implemented) \n")
        elif operation == Keywords.venumEq:
            f.write(f"  ; pop 2 elements of stack, compare them and push back \n")
            f.write(f"  ; implement comparison (not implemented) \n")
        elif operation == Keywords.venumIf:
            f.write(f"  ; implement if (not implemented) \n")
        elif operation == Keywords.venumEnd:
            pc += 1
            continue
        pc += 1
        

        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: vlang.py <filename> <mode>")
        sys.exit(1)
        
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("File does not exist")
        sys.exit(1)
        
    parsed_content = parse_to_individual(filename)
    toks = make_tokens(parsed_content)
    if len(sys.argv) == 3 and sys.argv[2] == "-simulate" or sys.argv[2] == "-sim":
        simulate(toks)
        
    if len(sys.argv) == 3 and sys.argv[2] == "-compile" or sys.argv[2] == "-com":
        compile(toks)


