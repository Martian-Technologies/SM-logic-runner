from operatorblock import Operatorblock


class LogicSimUnit:
    def __init__(self) -> None:
        self.operatorblocks: list[Operatorblock] = []
        self.inBlocks: list[LogicSimInBlock] = []
        self.outBlocks: list[LogicSimOutBlock] = []

    def addBlock(self, name, block: Operatorblock):
        block.name = name
        self.operatorblocks.append(block)
        return block

    def clearBlocks(self):
        for block in self.operatorblocks:
            block.clearConnections()
        self.operatorblocks = []
        self.inBlocks = []
        self.outBlocks = []

    def addInput(self, name, typeOverride: Operatorblock = None):
        if typeOverride == None:
            block: LogicSimInBlock = self.addBlock(LogicSimInBlock(name))
        else:
            block: Operatorblock = self.addBlock(typeOverride)
            block.name = name
        self.inBlocks.append(block)
        return block

    def addOutput(self, name, typeOverride: Operatorblock = None):
        if typeOverride == None:
            block: LogicSimOutBlock = self.addBlock(LogicSimOutBlock(name))
        else:
            block: Operatorblock = self.addBlock(typeOverride)
            block.name = name
        self.outBlocks.append(block)
        return block

    def getInputBlock(self, name):
        for block in self.inBlocks:
            if block.name == name:
                return block

    def getOutputBlock(self, name):
        for block in self.outBlocks:
            if block.name == name:
                return block

    def run(self):
        for block in self.operatorblocks:
            block.run()

    def updateDataUsed(self):
        for block in self.operatorblocks:
            block.updateDataUsed()


class LogicSimInBlock(Operatorblock):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name


class LogicSimOutBlock(Operatorblock):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
