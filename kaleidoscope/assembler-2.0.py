import plyplus
import sys

regNames = {
  'zero': 0,
  'ra': 1,
  'x0': 0, 
  'x1': 1,
  'x2': 2,
  'x2': 2,
  'x3': 3,
  'x4': 4,
  'x5': 5,
  'x6': 6,
  'x7': 7,
  'x8': 8,
  'x9': 9,
  'x10': 10, 
  'x11': 11,
  'x12': 12,
  'x12': 12,
  'x13': 13,
  'x14': 14,
  'x15': 15,
  'x16': 16,
  'x17': 17,
  'x18': 18,
  'x19': 19,
  'x20': 20, 
  'x21': 21,
  'x22': 22,
  'x22': 22,
  'x23': 23,
  'x24': 24,
  'x25': 25,
  'x26': 26,
  'x27': 27,
  'x28': 28,
  'x29': 29,
  'x30': 30,
  'x31': 31,
  'zero': 0,
  'ra': 1,
  'sp': 2,
  'gp': 3,
  'tp': 4,
  't0': 5,
  't1': 6,
  't2': 7,
  's0': 8,
  'fp': 8,
  's1': 9,
  'a0': 10,
  'a1': 11,
  'a2': 12,
  'a3': 13,
  'a4': 14,
  'a5': 15,
  'a6': 16,
  'a7': 17,
  's2': 18,
  's3': 19,
  's4': 20,
  's5': 21,
  's6': 22,
  's7': 23,
  's8': 24,
  's9': 25,
  's10': 26,
  's11': 27,
  't3': 28,
  't4': 29,
  't5': 30,
  't6': 31
}

instInfo = {
  'add': {
    'opcode': '0110011',
    'f3': '000',
    'f7': '0000000'
  },
  'sub': {
    'opcode': '0110011',
    'f3': '000',
    'f7': '0100000'
  },
  'xor': {
    'opcode': '0110011',
    'f3': '100',
    'f7': '0000000'
  },
  'or': {
    'opcode': '0110011',
    'f3': '110',
    'f7': '0000000'
  },
  'and': {
    'opcode': '0110011',
    'f3': '111',
    'f7': '0000000'
  },
  'sll': {
    'opcode': '0110011',
    'f3': '001',
    'f7': '0000000'
  },
  'srl': {
    'opcode': '0110011',
    'f3': '101',
    'f7': '0000000'
  },
  'sra': {
    'opcode': '0110011',
    'f3': '101',
    'f7': '0100000'
  },
  'slt': {
    'opcode': '0110011',
    'f3': '010',
    'f7': '0000000'
  },
  'sltu': {
    'opcode': '0110011',
    'f3': '011',
    'f7': '0000000'
  },
  'mul': {
    'opcode': '0110011',
    'f3': '000',
    'f7': '0000001'
  },
  'mulh': {
    'opcode': '0110011',
    'f3': '001',
    'f7': '0000001'
  },
  'mulsu': {
    'opcode': '0110011',
    'f3': '010',
    'f7': '0000001'
  },
  'mulu': {
    'opcode': '0110011',
    'f3': '011',
    'f7': '0000001'
  },  
  'div': {
    'opcode': '0110011',
    'f3': '100',
    'f7': '0000001'
  },
  'divu': {
    'opcode': '0110011',
    'f3': '101',
    'f7': '0000001'
  },
  'rem': {
    'opcode': '0110011',
    'f3': '110',
    'f7': '0000001'
  },
  'remu': {
    'opcode': '0110011',
    'f3': '111',
    'f7': '0000001'
  },
  'addi': {
    'opcode': '0010011',
    'f3': '000'
  },
  'xori': {
    'opcode': '0010011',
    'f3': '100'
  },
  'ori': {
    'opcode': '0010011',
    'f3': '110'
  },
  'andi': {
    'opcode': '0010011',
    'f3': '111'
  },
  'slti': {
    'opcode': '0010011',
    'f3': '010'
  },
  'sltiu': {
    'opcode': '0010011',
    'f3': '011'
  },
  'slli': {
    'opcode': '0010011',
    'f3': '001'
  },
  'srli': {
    'opcode': '0010011',
    'f3': '101'
  },
  'srai': {
    'opcode': '0010011',
    'f3': '101'
  },
  
}

class HVisitor(plyplus.STransformer):
  def __init__(self):
    super().__init__()
    self.instructionCounter = 0
    self.labels = {}

  def label(self, expr):
    self.labels[expr.tail[0]] = self.instructionCounter + 4

  def program(self, expr):
    print("Nodo programa")
    print(self.instructionCounter)
    print(expr)
    
  def regname(self, expr):
    val = expr.tail[0]
    regNum = regNames[val]
    regBin = format(int(regNum),'05b')
    return {'encode':regBin, 'name':val}
  
  def instr(self, expr):
    # Instruction name
    inst =  expr.tail[0]
  
    return {
      'type': 'R',
      'name': expr.tail[0],
      'opcode': instInfo[inst]['opcode'],
      'f3': instInfo[inst]['f3'],
      'f7': instInfo[inst]['f7']
    }
    
  def insti(self, expr):
    inst =  expr.tail[0]
    return {
      'type': 'I',
      'name': expr.tail[0],
      'opcode': instInfo[inst]['opcode'],
      'f3': instInfo[inst]['f3']
    }
    
  def imm(self, expr):
    val = expr.tail[0]
    regNum = int(val)
    regBin = format(regNum,'012b')
    return {'encode':regBin, 'name':val}
    
  def imm12(self, expr):
    val = expr.tail[0]
    print("imm12(" + val +")", end='')

  def inst(self, expr):
    print("Expresion en inst", expr)
    instInfo = expr.tail[0]
    name = instInfo['name']
    typ = instInfo['type']
    opcode = instInfo['opcode']
    funct3 = instInfo['f3']
    if(typ == "R"):
      funct7 = instInfo['f7']
    rd = expr.tail[1]['encode']
    rs1 = expr.tail[2]['encode']
    rs2 = expr.tail[3]['encode']


    #print("-{}--".format(self.instructionCounter))
    self.instructionCounter = self.instructionCounter + 4
    if(typ == "R"):
        print("EncodeR", name, opcode, rd, rs1, rs2, funct3, funct7)
    elif(typ == "I"):
        print("EncodeI", name, opcode, rd, rs1, rs2, funct3)
    #print("opcode({})-rd({})-f3({})-rs1({})-rs2({})-f7({})".format(expr.tail[0]['opcode'], expr.tail[1],expr.tail[0]['f3'] ,expr.tail[2],expr.tail[3],expr.tail[0]['f7']))
    #print("-xxx-")
    

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("Example call: {} input.asm output.asm".format(sys.argv[0]))
  else:
    sourceFile = sys.argv[1]
    targetFile = sys.argv[2]
    with open('riscv.g', 'r') as grm:
      with open(sourceFile, 'r') as scode:
        parser = plyplus.Grammar(grm)
        source = scode.read();
        t = parser.parse(source)
        #t.to_png_with_pydot(r"tree.png")
        v = HVisitor()
        v.transform(t)
        print(v.labels)