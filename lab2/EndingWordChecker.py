from StateMachine import StateMachine


class EndingWordChecker(StateMachine):
    # конструктор
    def __init__(self, alphabet=[], initStateId=0, endStateId=0, states=dict()):
        super().__init__(alphabet, initStateId, endStateId, states)

    # Запустить автомат
    # true, если очередность ремонта правильная
    def run(self, actions=''):
        if self.checkActions(actions):
            currentStates = self.getInitStateRule()
            for i in actions:
                currentStatesLen = len(currentStates)
                for j in set(currentStates):
                    currentStates.update(set(self.states[j].rule(i)))
                if len(currentStates) == currentStatesLen:
                    currentStates = self.getInitStateRule()
            return True if self.endStateId in currentStates else False
        else:
            raise ValueError("Элемент отсутствует в алфавите")

    # Проверить валидность событий
    def checkActions(self, actions=''):
        for i in actions:
            if str.lower(i) not in self.alphabet:
                return False
        return True

    # ПолучитьПравило начального состояния
    def getInitStateRule(self):
        return set(self.states[self.initStateId].rule())
