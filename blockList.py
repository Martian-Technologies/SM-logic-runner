from logicBlock import LogicBlock

def andBlock():
    return LogicBlock(0)

def orBlock():
    return LogicBlock(1)

def xorBlock():
    return LogicBlock(2)

def nandBlock():
    return LogicBlock(3)

def norBlock():
    return LogicBlock(4)

def xnorBlock():
    return LogicBlock(5)


blockList = {
    'and': andBlock,
    'or': orBlock,
    'xor': xorBlock,
    'nand': nandBlock,
    'nor': norBlock,
    'xnor': xnorBlock,
    }