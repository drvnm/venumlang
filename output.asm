global _start
section .text
_start: 
  ; push 3 on top of the stack
  push 3
  ; push 4 on top of the stack
  push 4
  ; pop 2 elements of stack, add them and push back 
  pop eax 
  pop ebx 
  add eax, ebx 
  push eax 
  ; call print (not implemented) 
  ; push 4 on top of the stack
  push 4
  ; push 5 on top of the stack
  push 5
  ; pop 2 elements of stack, multiply them and push back 
  pop eax 
  pop ebx 
  mul eax, ebx 
  push eax 
  ; call print (not implemented) 
  ; push 10 on top of the stack
  push 10
  ; push 4 on top of the stack
  push 4
  ; pop 2 elements of stack, substract them and push back 
  pop ebx 
  pop eax 
  sub eax, ebx 
  push eax 
  ; call print (not implemented) 
  ; push 6 on top of the stack
  push 6
  ; pop 2 elements of stack, compare them and push back 
  ; implement comparison (not implemented) 
  ; implement if (not implemented) 
  ; push 10000 on top of the stack
  push 10000
  ; call print (not implemented) 
  ; push 3333 on top of the stack
  push 3333
  ; call print (not implemented) 
  ; push 6920 on top of the stack
  push 6920
  ; call print (not implemented) 
  ; push 3333 on top of the stack
  push 3333
  ; call print (not implemented) 
