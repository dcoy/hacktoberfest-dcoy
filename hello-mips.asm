# Hello, reader!
# @author Clotifoth

.data
	hello_world_string: .asciiz "Hello, world!\n"

.text
	main: 
	li $v0, 4 # print_str
	la $a0, hello_world_string
	syscall

	# I guess that's all we really need to do.
	# Certainly not going to recreate asmttpd here or something

	li $v0, 10
	syscall
