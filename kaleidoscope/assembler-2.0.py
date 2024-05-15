import plyplus
import sys

regNames = {
  'x0': 0, 
  'x1': 1,
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
    'f3': '101',
    'f7': '0100000'
  },
  'lw': {
    'opcode': '0000011',
    'f3': '010'
  },
  'lh': {
    'opcode': '0000011',
    'f3': '001'
  },
  'lb': {
    'opcode': '0000011',
    'f3': '000'
  },
  'lbu': {
    'opcode': '0000011',
    'f3': '100'
  },
  'lhu': {
    'opcode': '0000011',
    'f3': '101'
  },
  'sw': {
    'opcode': '0100011',
    'f3': '010'
  },
  'sh': {
    'opcode': '0100011',
    'f3': '001'
  },
  'sb': {
    'opcode': '0100011',
    'f3': '000'
  },
  'beq': {
    'opcode': '1100011',
    'f3': '000'
  },
  'bne': {
    'opcode': '1100011',
    'f3': '001'
  },
  'blt': {
    'opcode': '1100011',
    'f3': '100'
  },
  'bge': {
    'opcode': '1100011',
    'f3': '101'
  },
  'bltu': {
    'opcode': '1100011',
    'f3': '110'
  },
  'bgeu': {
    'opcode': '1100011',
    'f3': '111'
  },
  'jal': {
    'opcode': '1101111',
  },
  'jalr': {
    'opcode': '1100111',
    'f3': '000'
  },
  'lui': {
    'opcode': '0110111',
  },
  'auipc': {
    'opcode': '0010111',
  },
  'ecall': {
    'opcode': '1110011',
    'f3': '000',
  },
  'ebreak': {
    'opcode': '1110011',
    'f3': '000',
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
    
  def instil(self, expr):
        inst = expr.tail[0]
        return {
            'type': 'IL',
            'name': expr.tail[0],
            'opcode': instInfo[inst]['opcode'],
            'f3': instInfo[inst]['f3']
        }
    
  def instis(self, expr):
        inst = expr.tail[0]
        return {
            'type': 'IS',
            'name': expr.tail[0],
            'opcode': instInfo[inst]['opcode'],
            'f3': instInfo[inst]['f3'],
            'f7': instInfo[inst].get('f7', '0000000')
        }
    
  def insts(self, expr):
    inst =  expr.tail[0]
    return {
      'type': 'S',
      'name': expr.tail[0],
      'opcode': instInfo[inst]['opcode'],
      'f3': instInfo[inst]['f3']
    }
  
  def instb(self, expr):
    inst =  expr.tail[0]
    return {
      'type': 'B',
      'name': expr.tail[0],
      'opcode': instInfo[inst]['opcode'],
      'f3': instInfo[inst]['f3']
    }
    
  def instu(self, expr):
    inst =  expr.tail[0]
    return {
      'type': 'U',
      'name': expr.tail[0],
      'opcode': instInfo[inst]['opcode']
    }
  
  def instj(self, expr):
    inst =  expr.tail[0]
    return {
      'type': 'J',
      'name': expr.tail[0],
      'opcode': instInfo[inst]['opcode']
    }
    
    
  def imm(self, expr):
    val = expr.tail[0]
    if val.startswith("0x"):  # Handle hex immediates
        val = int(val, 16)
    elif val.startswith("0b"):  # Handle binary immediates
        val = int(val, 2)
    else:  # Handle decimal immediates
        val = int(val)
    return {'value': val}
      
  def offset(self, expr):
    imm = expr.tail[0]['value']
    reg = expr.tail[1]['encode']
    immBin = format(imm, '012b')  # Immediate in 12-bit binary format
    return {'encode': immBin, 'reg': reg}

  def inst(self, expr):
    print("Expresion en inst", expr)
    instInfo = expr.tail[0]
    name = instInfo['name']
    typ = instInfo['type']
    opcode = instInfo['opcode']
    if typ == "R":
      funct3 = instInfo['f3']
      funct7 = instInfo['f7']
      rd = expr.tail[1]['encode']
      rs1 = expr.tail[2]['encode']
      rs2 = expr.tail[3]['encode']
      self.instructionCounter += 4
      print("EncodeR", name, opcode, rd, rs1, rs2, funct3, funct7)
    elif typ == "I":
      funct3 = instInfo['f3']
      rd = expr.tail[1]['encode']
      rs1 = expr.tail[2]['encode']
      imm = format(expr.tail[3]['value'], '012b')
      self.instructionCounter += 4
      print("EncodeI", name, opcode, rd, rs1, imm, funct3)
    elif typ == "IL":
      funct3 = instInfo['f3']
      rd = expr.tail[1]['encode']
      offset = expr.tail[2]
      imm = offset['encode']
      rs1 = offset['reg']
      self.instructionCounter += 4
      print("EncodeIL", name, opcode, rd, rs1, imm, funct3)
    elif typ == "IS":
      funct3 = instInfo['f3']
      funct7 = instInfo['f7']
      rd = expr.tail[1]['encode']
      rs1 = expr.tail[2]['encode']
      imm = format(expr.tail[3]['value'], '012b')
      self.instructionCounter += 4
      print("EncodeIS", name, opcode, rd, rs1, imm, funct3, funct7)
    elif typ == "S":
      rs2 = expr.tail[1]['encode']
      offset = expr.tail[2]
      imm = offset['encode']
      rs1 = offset['reg']
      funct3 = instInfo['f3']
      self.instructionCounter += 4
      print("EncodeS", name, opcode, rs1, rs2, imm, funct3)
    elif typ == "B":
      offset = expr.tail[3]
      imm = offset['encode']
      funct3 = instInfo['f3']
      rs1 = expr.tail[1]['encode']
      rs2 = expr.tail[2]['encode']
      self.instructionCounter += 4
      print("EncodeB", name, opcode, rs1, rs2, imm, funct3)
    elif typ == "U":
      rd = expr.tail[1]['encode']
      imm = format(expr.tail[2]['value'], '020b')
      self.instructionCounter += 4
      print("EncodeU", name, opcode, rd, imm)
    elif typ == "J":
      rd = expr.tail[1]['encode']
      offset = expr.tail[2]
      imm = offset['encode']
      self.instructionCounter += 4
      print("EncodeJ", name, opcode, rd, imm)
    #print("-{}--".format(self.instructionCounter))
        
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