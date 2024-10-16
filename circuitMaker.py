from operatorblock import Operatorblock


class CircuitMaker:
    @staticmethod
    def makeCircuit(data: list[tuple[list[str]]], blockClasses: dict[str, type[Operatorblock]]):
        print(data)
        blockList = CircuitMaker.createAllBLockClasses(data, blockClasses)
        CircuitMaker.connectBlocks(data, blockList), list(data.keys())
        return blockList.values()

    @staticmethod
    def createAllBLockClasses(
        data: list[tuple[list[str]]], blockClasses: dict[str, type[Operatorblock]]
    ):
        blockList: dict[str, Operatorblock] = {}
        for blocksPair in data:
            for blocks in blocksPair:
                for block in blocks:
                    if block not in blockList.keys():
                        blockList[block] = CircuitMaker.getBlockType(block, blockClasses)()
                        blockList[block].name = block
        return blockList

    @staticmethod
    def getBlockType(name: str, blockClasses: dict[str, type[Operatorblock]]):
        bestGuess: str = None
        for blockClassName in blockClasses.keys():
            if name.startswith(blockClassName) and (
                bestGuess == None or len(bestGuess) < len(blockClassName)
            ):
                bestGuess = blockClassName
        if bestGuess == None:
            raise Exception(f"Could not find class name in block {name}")
        return blockClasses[bestGuess]

    @staticmethod
    def connectBlocks(data: list[tuple[list[str]]], blockList: dict[str, Operatorblock]):
        for blocksPair in data:
            if len(blocksPair[0]) == 1:
                for connectToBlockName in blocksPair[1]:
                    blockList[blocksPair[0]].addInConnection(blockList[connectToBlockName])
            elif len(blocksPair[1]) == 1:
                for blockName in blocksPair[1]:
                    blockList[blockName].addInConnection(blockList[blocksPair[1]])
            elif len(blocksPair[0]) == len(blocksPair[1]):
                for i in range(len(blocksPair[0])):
                    blockList[blocksPair[0][i]].addInConnection(blockList[blocksPair[1][i]])
