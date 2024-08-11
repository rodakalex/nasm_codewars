extern malloc


section .text
global dna_strand


dna_strand:
  mov rsi, rdi
  push rsi
  mov rdi, 1024
  call malloc
  pop rsi
  mov rdi, rax
  mov rcx, rax
loop:
  lodsb
  test al, 2 ; is G or C
  jz notgc
  xor al, 4 ; G <-> C
  stosb
  jmp loop
notgc:
  test al, al
  jz done
  xor al, 21 ; A <-> T
  stosb
  jmp loop
done:
  stosb
  mov rax, rcx
  ret