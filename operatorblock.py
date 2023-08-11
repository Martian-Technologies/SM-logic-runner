from block import Block


class Operatorblock(Block):
    def __init__(self) -> None:
        super().__init__()
        self.connectionsIn:list[Operatorblock] = []
        self.connectionsOut:list[Operatorblock] = []
    
    def getOutConnections(self):
        return self.connectionsOut

    def addOutConnections(self, connection):
        self.connectionsOut.append(connection)

    def removeOutConnections(self, connection):
        self.connectionsOut.remove(connection)

    def getInConnections(self):
        return self.connectionsIn

    def addInConnections(self, connection):
        self.connectionsIn.append(connection)

    def removeInConnections(self, connection):
        self.connectionsIn.remove(connection)

    def giveData():
        pass
    
    def run(self, data):
        for out in self.connectionsOut:
            out.run(data)