from Machine import Machine

class StateMachine(Machine):
    # конструктор
    def __init__(self, alphabet=[], initStateId=0, endStateId=0, states=dict()):
        super().__init__(alphabet, initStateId, states)
        self.endStateId = endStateId

    # Установить конечное состояние
    def setEndStateId(self, endStateId=0):
        self.endStateId = endStateId

