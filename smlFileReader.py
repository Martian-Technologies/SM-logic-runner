from pathlib import Path
from random import Random as rng

path = Path("test.sml")
relitave = True

rng = rng()


class SmlFileReader:
    blockNameIncrement = 0

    @staticmethod
    def readSmlFile(
        path: Path = path, blockTypes: list[str] = ["and", "or", "xor", "nand", "nor", "xnor"]
    ):
        fileText = open(path).read()
        fileText = SmlFileReader.removeComments(fileText)
        data, blocksNames = SmlFileReader.getConnections(fileText, blockTypes)
        return data, blocksNames

    @staticmethod
    def removeComments(fileText: str):
        doDel = False
        i = 0
        while i < len(fileText):
            if fileText[i] == "#":
                fileText = SmlFileReader.removeCharFromStr(i, fileText)
                doDel = True
                continue
            elif fileText[i] == "\n":
                doDel = False
            elif doDel:
                fileText = SmlFileReader.removeCharFromStr(i, fileText)
                continue
            i += 1
        return fileText

    @staticmethod
    def removeCharFromStr(index: int, string: str):
        return string[:index] + string[index + 1 :]

    @staticmethod
    def getConnections(fileText: str, blockTypes: list[str]):
        blockInputs: list[tuple[list[str]]] = []
        string = ""
        buffer = None
        operator = None
        blocksNames = []
        for char in fileText:
            if char == " ":
                continue

            if char in ["<", ">"]:
                if buffer != None:
                    blockInputs, buffer, string = SmlFileReader.addBlockToBlockInputs(
                        blockInputs, blockTypes, operator, buffer, string
                    )
                    if type(string) == list:
                        blocksNames.extend(string)
                    else:
                        blocksNames.append(string)
                    if type(buffer) == list:
                        blocksNames.extend(buffer)
                    else:
                        blocksNames.append(buffer)
                buffer = string
                string = ""
                operator = char
            elif char == ",":
                if string == "":
                    raise Exception("can not start a list of blocks with ''")

                if type(string) == list:
                    string.append(string)
                else:
                    string = [string, char]
            elif char == "\n":
                if buffer != None:
                    blockInputs, buffer, string = SmlFileReader.addBlockToBlockInputs(
                        blockInputs, blockTypes, operator, buffer, string
                    )
                    blocksNames.extend(string)
                    blocksNames.extend(buffer)
                buffer = None
                string = ""
                operator = None
            else:
                if type(string) == list:
                    string[-1] += char
                else:
                    string += char
        if buffer != None:
            blockInputs, buffer, string = SmlFileReader.addBlockToBlockInputs(
                blockInputs, blockTypes, operator, buffer, string
            )
            blocksNames.extend(string)
            blocksNames.extend(buffer)
        return blockInputs, blocksNames

    @staticmethod
    def addBlockToBlockInputs(
        blockInputs: list[tuple[list[str], list[str]]],
        blockTypes: list[str],
        operator: str,
        buffer: str | list[str],
        string: str | list[str],
    ):
        if type(buffer) == list:
            for i in range(len(buffer)):
                if buffer[i] in blockTypes:
                    buffer[i] = SmlFileReader.makeRandName(buffer[i])
        elif buffer in blockTypes:
            buffer = SmlFileReader.makeRandName(buffer)

        if type(string) == list:
            for i in range(len(string)):
                if string[i] in blockTypes:
                    string[i] = SmlFileReader.makeRandName(string[i])
        elif string in blockTypes:
            string = SmlFileReader.makeRandName(string)

        if type(buffer) == str:
            buffer = [buffer]
        if type(string) == str:
            string = [string]

        if operator != "<":
            valueIn = buffer
            valueOut = string
        else:
            valueIn = string
            valueOut = buffer
        blockInputs.append((valueIn, valueOut))
        return blockInputs, buffer, string

    @staticmethod
    def makeRandName(string: str):
        string = string + str(SmlFileReader.blockNameIncrement) + "r" + str(rng.randint(0, 99999))
        SmlFileReader.blockNameIncrement += 1
        return string
