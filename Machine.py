class Machine:
    # конструктор
    def __init__(self, alphabet=[], initStateId=0,states=dict()):
        self.alphabet = alphabet
        self.initStateId = initStateId
        self.states = states

    # Добавить состояние
    def addState(self,key, state=[]):
        self.states[key] = state

    # Удалить состояние
    def removeState(self, key):
        self.states.pop(key)

    # Установить начальное состояние
    def setInitStateId(self, initStateId=0):
        self.initStateId = initStateId

    # Проверить валидность событий
    def checkActions(self, actions=''):
        for i in actions:
            if i not in self.alphabet:
                return False
        return True