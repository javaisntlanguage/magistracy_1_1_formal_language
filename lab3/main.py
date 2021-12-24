from dataclasses import dataclass


class DFA:
    def __init__(self):
        self.States = list()
        self.Symbols = list()
        self.endStates = list()
        self.transitions = list()
        self.startState = ' '

    def addState(self, addState):
        if addState not in self.States:
            self.States.append(addState)

    def delState(self, delState):
        if delState in self.States:
            self.States.remove(delState)

    def addSymbol(self, addSymbol):
        if addSymbol not in self.Symbols:
            self.Symbols.append(addSymbol)

    def delSymbol(self, delSymbol):
        if delSymbol in self.Symbols:
            self.Symbols.remove(delSymbol)

    def setStartState(self, _startState):
        if _startState in self.States:
            self.startState = _startState

    def addEndState(self, addEndStates):
        if addEndStates in self.States:
            self.endStates.append(addEndStates)

    def delEndState(self, delEndState):
        if delEndState in self.States:
            self.endStates.remove(delEndState)

    def addTransistion(self, addTransition):
        if not any(x.currState == addTransition.currState and
                   x.Symbol == addTransition.Symbol and
                   x.nextState == addTransition.nextState
                   for x in self.transitions):
            self.transitions.append(addTransition)

    def InitWork(self, bufString):
        currState = self.startState
        for i in range(len(bufString)):
            currState = self.getNextState(currState, bufString[i])
            if currState == ' ':
                return False

        if self.isEndStates(currState):
            return True
        else:
            return False

    def getNextState(self, currState, curSymbol):
        newState = ' '
        for t in self.transitions:
            if t.currState == currState and t.Symbol == curSymbol:
                newState = t.nextState
                break

        return newState

    def isEndStates(self, currState):
        for endState in self.endStates:
            if endState == currState:
                return True
        return False


@dataclass
class Transition:
    currState: chr
    Symbol: chr
    nextState: chr


def initDfa():
    @dataclass
    class Transition:
        currState: chr
        Symbol: chr
        nextState: chr

    bufDfa = DFA()
    startState = '0'
    endStates = ['2']
    States = ['0', '1', '2']
    EngSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    NumSymbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    Transitions = list()

    for i in range(len(EngSymbols)):
        Transition1 = Transition('0', EngSymbols[i], '1')
        Transitions.append(Transition1)

    for i in range(len(NumSymbols)):
        Transition1 = Transition('1', NumSymbols[i], '2')
        Transitions.append(Transition1)
        Transition2 = Transition('2', NumSymbols[i], '2')
        Transitions.append(Transition2)

    for State in States:
        bufDfa.addState(State)

    for EngSymbol in EngSymbols:
        bufDfa.addSymbol(EngSymbol)

    for NumSymbol in NumSymbols:
        bufDfa.addSymbol(NumSymbol)

    bufDfa.setStartState(startState)

    for endState in endStates:
        bufDfa.addEndState(endState)

    for Transition in Transitions:
        bufDfa.addTransistion(Transition)

    return bufDfa


oneDfa = initDfa()
chechAutomat = "a11232523213"
print("Входная строка для ДКА:")
print(chechAutomat)

print()

print("Результат работы автомата:")
if oneDfa.InitWork(chechAutomat):
    print("Данная последовательность принадлежит языку автомата")
else:
    print("Данная последовательность не принадлежит языку автомата")
print()

chechAutomat = "aaaaa"
print("Входная строка для ДКА:")
print(chechAutomat)

print()

print("Результат работы автомата:")
if oneDfa.InitWork(chechAutomat):
    print("Данная последовательность принадлежит языку автомата")
else:
    print("Данная последовательность не принадлежит языку автомата")
