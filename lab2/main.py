from EndingWordChecker import EndingWordChecker
from Struct import Struct

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
machine = EndingWordChecker(alphabet)

machine.setInitStateId(999)  # добавлям идентификатор начального состояния
machine.setEndStateId(99)  # добавлям идентификатор конечного состояния

# добавляем состояния
machine.addState(99, Struct(rule=lambda x: []))
machine.addState(999, Struct(rule=lambda: [0, 3, 5]))  # эпсилон-переход

machine.addState(0, Struct(rule=lambda x: [1] if x == 'о' else []))
machine.addState(1, Struct(rule=lambda x: [99] if x == 'е' else []))

machine.addState(3, Struct(rule=lambda x: [4] if x == 'а' else []))
machine.addState(4, Struct(rule=lambda x: [99] if x == 'я' else []))

machine.addState(5, Struct(rule=lambda x: [6] if x == 'и' else []))
machine.addState(6, Struct(rule=lambda x: [99] if x == 'е' else []))

print(machine.run('большоо'))  # False
print(machine.run('большоее'))  # False
print(machine.run('большое'))  # True
print(machine.run('большая'))  # True
print(machine.run('большие'))  # True
print(machine.run('питон'))  # False

