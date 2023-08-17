from operatorblock import Operatorblock


class LogicBlock(Operatorblock):
    def __init__(self, type: int = None) -> None:
        """
        0: 'and'\n
        1: 'or'\n
        2: 'xor'\n
        3: 'nand'\n
        4: 'nor'\n
        5: 'xnor'
        """
        super().__init__()
        if type == None:
            type = 0
        self.type = None
        self.setType(type)

    def setType(self, type):
        if self.type != type:
            self.type = type
            if self.type in [0, "and"]:

                def operation(data: list):
                    for value in data:
                        if not value:
                            return False
                    return True

            elif self.type in [1, "or"]:

                def operation(data: list):
                    for value in data:
                        if value:
                            return True
                    return False

            elif self.type in [2, "xor"]:

                def operation(data: list):
                    on = 0
                    for value in data:
                        if value:
                            on += 1
                    if on % 2 == 0:
                        return False
                    return True

            elif self.type in [3, "nand"]:

                def operation(data: list):
                    for value in data:
                        if not value:
                            return True
                    return False

            elif self.type in [4, "nor"]:

                def operation(data: list):
                    for value in data:
                        if value:
                            return False
                    return True

            elif self.type in [5, "xnor"]:

                def operation(data: list):
                    on = 0
                    for value in data:
                        if value:
                            on += 1
                    if on % 2 == 0:
                        return True
                    return False

            self.runOperation = operation

    def run(self):
        if len(self.usedData) == 0:
            outData = False
        else:
            outData = self.runOperation(list(self.usedData.values()))
        print(self.name, " " * (20 - len(self.name)), outData)
        self.outputData(outData)
