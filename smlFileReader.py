from pathlib import Path
from random import Random as rng
path = Path('test.sml')
relitave = True

rng = rng()

class SmlFileReader:
    blockNameIncrement = 0
    
    @staticmethod
    def readSmlFile(path:Path=path, blockTypes:list[str] = ['and', 'or', 'xor', 'nand', 'nor', 'xnor']):
        fileText = open(path).read()
        fileText = SmlFileReader.removeComments(fileText)
        data, blocksNames = SmlFileReader.getConnections(fileText, blockTypes)
        for name in blocksNames:
            if name not in data.keys():
                data[name] = []
        return data
    
    @staticmethod
    def removeComments(fileText:str):
        doDel = False
        i = 0
        while i < len(fileText):
            if fileText[i] == '#':
                fileText = SmlFileReader.removeCharFromStr(i, fileText)
                doDel = True
                continue
            elif fileText[i] == '\n':
                doDel = False
            elif doDel:
                fileText = SmlFileReader.removeCharFromStr(i, fileText)
                continue
            i+=1
        return fileText
    
    @staticmethod
    def removeCharFromStr(index:int, string:str):
        return string[:index] + string[index + 1:]
    
    @staticmethod
    def getConnections(fileText:str, blockTypes:list[str]):
        blockInputs:dict[str, list[str]] = {}
        string = ''
        buffer = None
        operator = None
        blocksNames = []
        for char in fileText:
            if char == ' ':
                continue
            
            if char in ['<', '>']:
                if buffer != None:
                    blockInputs, buffer, string = SmlFileReader.addBlockToBlockInputs(blockInputs, blockTypes, operator, buffer, string)
                    blocksNames.append(string)
                    blocksNames.append(buffer)
                buffer = string
                string = ''
                operator = char
            elif char == '\n':
                if buffer != None:
                    blockInputs, buffer, string = SmlFileReader.addBlockToBlockInputs(blockInputs, blockTypes, operator, buffer, string)
                    blocksNames.append(string)
                    blocksNames.append(buffer)
                buffer = None
                string = ''
                operator = None
            else:
                string += char
        if buffer != None:
            blockInputs, buffer, string = SmlFileReader.addBlockToBlockInputs(blockInputs, blockTypes, operator, buffer, string)
            blocksNames.append(string)
            blocksNames.append(buffer)
        return blockInputs, blocksNames
                
    def addBlockToBlockInputs(blockInputs:dict[str, list[str]], blockTypes, operator, buffer, string):
        if buffer in blockTypes:
            buffer = buffer + str(SmlFileReader.blockNameIncrement) + 'r' + str(rng.randint(0, 99999))
            SmlFileReader.blockNameIncrement += 1
        if string in blockTypes:
            string = string + str(SmlFileReader.blockNameIncrement) + 'r' + str(rng.randint(0, 99999))
            SmlFileReader.blockNameIncrement += 1
        
        if operator == '<':
            if buffer in blockInputs.keys():
                blockInputs[buffer].append(string)
            else:
                blockInputs[buffer] = [string]
        else:
            if string in blockInputs.keys():
                blockInputs[string].append(buffer)
            else:
                blockInputs[string] = [buffer]
        return blockInputs, buffer, string