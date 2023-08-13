from circuitMaker import CircuitMaker
from logicBlock import LogicBlock
from logicSimUnit import LogicSimUnit
from operatorblock import inBlock
from smlFileReader import SmlFileReader
from blockList import blockList


unit = LogicSimUnit()

connectionData = SmlFileReader.readSmlFile()
blocks, blockNames = CircuitMaker.makeCircuit(connectionData, blockList)
for block in zip(blocks, blockNames):
    unit.addBlock(block[1], block[0])

unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()