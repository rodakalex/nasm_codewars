global get_age

section .text

; <--- unsigned int get_age(const char *inp) --->
get_age:
    xor rax, rax
    mov al, [rdi]
    sub al, 48
    ret
; ---------> endof get_age <---------