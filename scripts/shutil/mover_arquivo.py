import shutil

shutil.copy2('teste_copiar1.txt', 'pasta_copiar/teste_copiar1.txt') # Copiando arquivo com mesmo nome.
shutil.copy2('teste_copiar2.txt', 'pasta_copiar') # Copiando arquivo somente para repositório de destino.
shutil.copy2('teste_copiar3.txt', 'pasta_copiar/teste_copiar4') # Copiando arquivo alterando nome.