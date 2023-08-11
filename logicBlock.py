from operatorblock import Operatorblock


class LogicBlock(Operatorblock):
    def __init__(self, type:int) -> None:
        super().__init__()
        self.type:int = type
        
    def setType(self, type):
        if self.type != type:
            self.type == type

            if self.type == 1:
                pass
            
    def run(self, data:bool):
        pass