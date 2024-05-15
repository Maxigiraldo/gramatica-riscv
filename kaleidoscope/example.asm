_LAB00_1:
    # x0 = 0
    addi x1, x0, 0 ; x1 = 0
    addi x2, x0, 3940
    add x2, x5, x7
    xori x4, x0, 34
    jal x6, 10(x7)

vfsofvihsofhv:
    add x3, x3, x4
    lw x4, 0(x2)
    slli x4, x4, 2
    sw x3, 0(x4)
    beq x2, x4, 23(x4)
    lui x7, 323