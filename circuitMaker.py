from operatorblock import Operatorblock


class CircuitMaker:
    @staticmethod
    def makeCircuit(data:dict[str, list[str]], blockClasses:dict[str, type[Operatorblock]]):
        print(data)
        blockList = CircuitMaker.createAllBLockClasses(data, blockClasses)
        return CircuitMaker.connectBlocks(data, blockList), list(data.keys())
    
    @staticmethod
    def createAllBLockClasses(data:dict[str, list[str]], blockClasses:dict[str, type[Operatorblock]]):
        blockList:dict[str, Operatorblock] = {}
        for block in data.keys():
            blockList[block] = CircuitMaker.getBlockType(block, blockClasses)()
        return blockList
        
    @staticmethod
    def getBlockType(name:str, blockClasses:dict[str, type[Operatorblock]]):
        bestGuess:str = None
        for blockClassName in blockClasses.keys():
            if name.startswith(blockClassName) and (bestGuess == None or len(bestGuess) < len(blockClassName)):
                bestGuess = blockClassName
        if bestGuess == None:
            raise Exception(f"Could not find class name in block {name}")
        return blockClasses[bestGuess]

    @staticmethod
    def connectBlocks(data:dict[str, list[str]], blockList:dict[str, Operatorblock]):
        blocks = []
        for blockName in data.keys():
            for connectToBlockName in data[blockName]:
                blockList[blockName].addInConnection(blockList[connectToBlockName])
            blocks.append(blockList[blockName])
        return blocks
