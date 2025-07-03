# exemplos das lib nativa do python
# dir(lib) para verificar oque existe dentro das libs
# https://docs.python.org/3/library/index.html

import math
import datetime as timer
import random
import os
import time as t

inicio = t.time()

print(math.pi)
print(timer.datetime.now)
print(timer.datetime(2000, 1, 1))

for _ in range(5):
    n = random.randint(1, 10)
    t.sleep(1) # famoso sleep
    print(n)

print(os.getcwd())


fim = t.time()
print(f'tempo total do script em segundos: {fim - inicio}')