from logicBlock import LogicBlock
from logicSimUnit import LogicSimUnit
from operatorblock import inBlock


unit = LogicSimUnit()

input1:inBlock = unit.addInput('1', LogicBlock(0))
input2:inBlock = unit.addBlock(inBlock('2'))

output1 = unit.addOutput('1')
output1.doPrint = True

andGate = unit.addBlock(LogicBlock(2))

#input1.setData(True)
input2.setData(True)

input1.addOutConnection(andGate)
input2.addOutConnection(andGate)
output1.addInConnection(andGate)
output1.addOutConnection(input1)

unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()
unit.stepSim()