from StateMachine import StateMachine


class RepairChecker(StateMachine):
    # конструктор
    def __init__(self, alphabet=[], initStateId=0, endStateId=0, states=dict()):
        super().__init__(alphabet, initStateId, endStateId, states)
        self.currentStateId = initStateId

    #
    # Установить начальное состояние
    #
    def setInitStateId(self, initStateId=0):
        super().setInitStateId(initStateId)
        self.currentStateId = initStateId

    # Запустить автомат
    # true, если очередность ремонта правильная
    def run(self, actions=[]):
        self.currentStateId = self.initStateId
        isCorrectActions = self.checkActions(actions)
        if isCorrectActions:
            for i in actions:
                self.currentStateId = self.states[self.currentStateId].rule(i)
            return True if self.currentStateId == self.endStateId else False
        else:
            raise ValueError("Элемент отсутствует в алфавите")
