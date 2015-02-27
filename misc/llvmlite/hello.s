	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 14, 0
	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:                                ## %.1
	pushq	%rax
Ltmp0:
	.cfi_def_cfa_offset 16
	leaq	_.str4(%rip), %rdi
	callq	_puts
	xorl	%eax, %eax
	popq	%rdx
	retq
	.cfi_endproc

	.section	__DATA,__data
	.globl	_.str4                  ## @.str4
_.str4:
	.ascii	"hello, world!"


.subsections_via_symbols
