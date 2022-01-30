.global your_asm_fn
.section .text

your_asm_fn:

push    %ebp
mov     %esp,%ebp

# Your code here
push $0xc001f00d
push %esp
sub $8, %esp
movl $0xc105ed, 4(%esp)
movl $0xacce55ed, (%esp)
call practice

leave
ret
