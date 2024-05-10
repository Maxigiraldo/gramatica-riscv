start: program;

program:
  (label inst*)*;

label: '[a-zA-Z_][\w_]*:';

inst: 
    instr regname ',' regname ',' regname // R instruction
  | insti regname ',' regname ',' imm     // I instruction
  | instil regname ',' offset // IL instruction
  | insts regname ',' offset ',' regname // S instruction
  | instb regname ',' regname ',' imm // B instruction
  | instj imm // J instruction
  | instu regname ',' imm // U instruction
  ;

offset: imm '\(' regname '\)';

instname: instr | insti | instil | insts | instb | instj | instu;

instr: 'add' | 'sub' | 'xor' | 'or' | 'and' | 'sll' | 'srl' | 'sra' | 'slt' | 'sltu' | 'mul' | 'mulh' | 'mulsu' | 'mulu' | 'div' | 'divu' | 'rem' | 'remu';
insti: 'addi' | 'xori' | 'ori' | 'andi' | 'slli' | 'srli' | 'srai' | 'slti' | 'sltiu' | 'jalr' | 'ecall' | 'ebreak';
instil: 'lw' | 'lh' | 'lb' | 'lbu' | 'lhu';
insts: 'sw' | 'sh' | 'sb';
instb: 'beq' | 'bne' | 'blt' | 'bge' | 'bltu' | 'bgeu';
instj: 'jal';
instu: 'lui' | 'auipc';

imm : VAL;

VAL: '[0]|(\-|\+)?[1-9][0-9]*';

regname: 
   'x0' | 
  | 'x1' | 'ra'
  | 'x2' | 'sp'
  | 'x3' | 'gp'
  | 'x4' | 'tp'
  | 'x5' | 't0' 
  | 'x6' | 't1'
  | 'x7' | 't2'
  | 'x8' | 's0' | 'fp'
  | 'x9' | 's1'
  | 'x10' | 'a0' 
  | 'x11' | 'a1'
  | 'x12' | 'a2' 
  | 'x13' | 'a3' 
  | 'x14' | 'a4' 
  | 'x15' | 'a5' 
  | 'x16' | 'a6' 
  | 'x17' | 'a7'
  | 'x18' | 's2' 
  | 'x19' | 's3' 
  | 'x20' | 's4' 
  | 'x21' | 's5' 
  | 'x22' | 's6' 
  | 'x23' | 's7' 
  | 'x24' | 's8' 
  | 'x25' | 's9' 
  | 'x26' | 's10' 
  | 'x27' | 's11'
  | 'x28' | 't3' 
  | 'x29' | 't4' 
  | 'x30' | 't5' 
  | 'x31' | 't6'
;

COMMENT: '[;#][^\n\r]*' (%ignore);
WS: '[ \t\r\n]+' (%ignore);