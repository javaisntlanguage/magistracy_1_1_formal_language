from RepairChecker import RepairChecker
from Struct import Struct

alphabet = ['замена пола', 'ремонт стен', 'ремонт потолка']
machine = RepairChecker(alphabet)

machine.setInitStateId(0)  # добавлям идентификатор начального состояния
machine.setEndStateId(3)  # добавлям идентификатор конечного состояния

# добавляем состояния ремонта
machine.addState(0,Struct(rule=lambda x: 1 if x == alphabet[0] else 0))
machine.addState(1,Struct(rule=lambda x: 2 if x == alphabet[1] else 1))
machine.addState(2,Struct(rule=lambda x: 3 if x == alphabet[2] else 2))
machine.addState(3,Struct(rule=lambda x: 3))

# моделируем очередность ремонта
print(machine.run(['замена пола', 'ремонт стен', 'ремонт потолка']))  # True
print(machine.run(['ремонт стен', 'замена пола', 'ремонт потолка']))  # False
print(machine.run(['ремонт стен']))  # False
