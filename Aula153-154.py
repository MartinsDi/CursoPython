# Módulos padrão do Python (import, from, as e *)
#import Aula133_lambda

import sys

print(sys.platform)


print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')