from block import Block
from copy import copy


class Operatorblock(Block):
    def __init__(self) -> None:
        super().__init__()
        self.connectionsIn: list[Operatorblock] = []
        self.connectionsOut: list[Operatorblock] = []
        self.inputData: dict[Operatorblock, any] = {}
        self.usedData: dict[Operatorblock, any] = {}
        self.name: str

    def getOutConnections(self):
        return self.connectionsOut

    def addOutConnection(self, connection):
        if connection not in self.connectionsOut:
            self.connectionsOut.append(connection)
            connection.addInConnection(self)

    def removeOutConnection(self, connection):
        if connection in self.connectionsOut:
            self.connectionsOut.remove(connection)
            connection.removeInConnection(self)

    def clearOutputs(self):
        for connection in self.connectionsOut:
            self.removeOutConnection(connection)

    def getInConnections(self):
        return self.connectionsIn

    def addInConnection(self, connection):
        if connection not in self.connectionsIn:
            self.connectionsIn.append(connection)
            connection.addOutConnection(self)

    def removeInConnection(self, connection):
        if connection in self.connectionsIn:
            self.connectionsIn.remove(connection)
            connection.removeOutConnection(self)

    def clearInputs(self):
        for connection in self.connectionsIn:
            self.removeInConnection(connection)

    def clearConnections(self):
        self.clearInputs()
        self.clearOutputs()

    def giveData(self, data, giver):
        self.inputData[giver] = data

    def updateDataUsed(self):
        self.usedData = copy(self.inputData)

    def run(self):
        if len(self.usedData) == 0:
            outData = False
        else:
            outData = list(self.usedData.values())[0]
        self.outputData(outData)

    def outputData(self, data):
        for out in self.connectionsOut:
            out.giveData(data, self)


class inBlock(Operatorblock):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.output = False

    def setData(self, data):
        self.output = data

    def run(self):
        self.outputData(self.output)
