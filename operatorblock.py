from block import Block


class Operatorblock(Block):
    def __init__(self) -> None:
        super().__init__()
        self.connectionsIn: list[Operatorblock] = []
        self.connectionsOut: list[Operatorblock] = []
        self.inputData: dict[Operatorblock, any] = {}

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

    def giveData(self, data, giver):
        self.inputData[giver] = data

    def run(self):
        if len(self.inputData) == 0:
            outData = False
        else:
            outData = list(self.inputData.values())[0]
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