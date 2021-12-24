from BracketsChecker import BracketsChecker
from Struct import Struct

alphabet = '()'

machine = BracketsChecker(alphabet, failState=-1, successState=1)
machine.setInitStateId(0)  # добавлям идентификатор начального состояния


def state0(x, magazine, remains):
    if x == alphabet[0]:
        magazine.append('A')
    elif x == alphabet[1]:
        try:
            magazine.pop()
            if remains == 1 and len(magazine) == 0:
                return 1
        except:
            return -1
    return 0


# добавляем состояния
machine.addState(0, Struct(rule=lambda x, magazine, remains: state0(x, magazine, remains)))
machine.addState(-1, Struct(rule=lambda x, magazine, remains: -1))
machine.addState(1, Struct(rule=lambda x, magazine, remains: 1))

print(machine.run('(()()(()(())(((())))())())'))  # True
print(machine.run('()'))  # True
print(machine.run('('))  # False
print(machine.run(')'))  # False
print(machine.run('(()'))  # False
print(machine.run('())'))  # False
