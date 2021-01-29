# MIPS-Assembler-Project
A simple assembler using a high-level programming language such as Python to convert any MIPS assembly program containing some of the main MIPS instructions to hexadecimal machine language or object code. A list of the instructions that are required to work with assembler can be found in "instructions.src". Assume the first line of the swap code is stored at MIPS memory location 0x80001000, and sort code is stored immediately after. The solution should support an interactive mode and a batch mode. The interactive mode reads an instruction from command line, assembles it to hexadecimal (converting from pseudo-instruction as necessary), and outputs the result to the screen. The batch mode reads a source file with extension .src, assembles to hexadecimal, and outputs the result to an object code file with extension .obj. 
# Built With
Python - 3.7.4.
#Instructions
swap:sll $t1,$a1,2 
add $t1,$a0,$t1 
lw $t0,0($t1) 
lw $t2,4($t1) 
sw $t2,0($t1) 
sw $t0,4($t1) 
jr $ra
sort:addi $sp,$sp,-20
sw $ra,16($sp)
sw $s3,12($sp)
sw $s2,8($sp)
sw $s1,4($sp)
sw $s0,0($sp)
move $s2,$a0
move $s3,$a1
for1tst:slt $t0,$s0,$s3
move $s0,$zero
beq $t0,$zero,exit1
addi $s1,$s0,-1
for2tst:slti $t0,$s1,0
bne $t0,$zero,exit2
sll $t1,$s1,2
add $t2,$s2,$t1
lw $t3,0($t2)
lw $t4,4($t2)
slt $t0,$t4,$t3
beq $t0,$zero,exit2
move $a0,$s2
move $a1,$s1
addi $s1,$s1,-1
j for2tst
exit2:addi $s0,$s0,1
j for1tst
exit1:lw $s0,0($sp)
lw $s1,4($sp)
lw $s2,8($sp)
lw $s3,12($sp)
lw $ra,16($sp)
addi $sp,$sp,20
jr $ra
