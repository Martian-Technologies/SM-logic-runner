from logicSimUnit import LogicSimUnit, LogicSimInBlock, LogicSimOutBlock
from operatorblock import Operatorblock
from block import Block


class LogicSimBlock(Block):
    def __init__(self) -> None:
        super().__init__()
        self.simUnit = LogicSimUnit()

    def clearBlocks(self):
        self.simUnit.clearBlocks()

    def setBlocks(
        self,
        blocks: list[tuple[str, Operatorblock]],
        inBlocks: list[tuple[str, LogicSimInBlock]],
        outBlocks: list[tuple[str, LogicSimOutBlock]],
    ):
        self.clearBlocks()
        for block in blocks:
            self.simUnit.addBlock(block[0], block[1])
        for block in inBlocks:
            self.simUnit.addInput(block[0], block[1])
        for block in outBlocks:
            self.simUnit.addOutput(block[0], block[1])

    def run(self):
        self.simUnit.run()

    def updateDataUsed(self):
        self.simUnit.updateDataUsed()
