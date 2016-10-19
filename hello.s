.data
	msg: .string "Hello world!\n"
	tam: .quad . - msg

.text
	.global _start

_start:
	mov $1, %rax
	mov $1, %rdi
	mov $msg, %rsi
	mov tam, %rdx
	syscall

	mov $60, %rax
	syscall
  
  #build with: gcc -nostdlib hello.s
