.global your_asm_fn
.section .text

your_asm_fn:

push    %ebp
mov     %esp,%ebp

# Your code here
push $0x0
push $0x646f6f66
push $0x6c6f6f63
movl %esp, %edx
push $0xc105ed
movl %esp, %ebx
push %edx
push %ebx
sub $4, %esp
movl $0xacce55ed, (%esp)
call practice

leave
ret
