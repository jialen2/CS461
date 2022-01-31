.global _main
.section .text

_main:

push    %ebp
mov     %esp,%ebp

# Your code here
movl $11, %eax
sub $8, %esp
movl $0x0068732F, 4(%esp)
movl $0x6E69622F, (%esp)
movl %esp, %ebx
movl $0, %ecx
movl $0, %edx
int $0x80 

leave
ret
