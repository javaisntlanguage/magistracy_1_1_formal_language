from Machine import Machine


class BracketsChecker(Machine):
    # конструктор
    def __init__(self, alphabet=[], initStateId=0, successState=0, failState=0, states=dict()):
        super().__init__(alphabet, initStateId, states)
        self.currentStateId = initStateId
        self.successState = successState
        self.failState = failState
        self.magazine = []

    #
    # Установить начальное состояние
    #
    def setInitStateId(self, initStateId=0):
        super().setInitStateId(initStateId)
        self.currentStateId = initStateId

    # Запустить автомат
    # true, если очередность ремонта правильная
    def run(self, actions=[]):
        self.magazine.clear()
        self.currentStateId = self.initStateId
        isCorrectActions = self.checkActions(actions)
        if isCorrectActions:
            actionsLen = len(actions)
            for counter, i in enumerate(actions):
                self.currentStateId = self.states[self.currentStateId].rule(i, self.magazine, actionsLen - counter)
                if self.currentStateId == self.failState:
                    return False
            return True if self.currentStateId == self.successState else False
        else:
            raise ValueError("Элемент отсутствует в алфавите")
