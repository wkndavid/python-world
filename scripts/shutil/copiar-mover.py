import shutil

# Copiando arquivos

shutil.copy2('teste_copiar1.txt', 'pasta_copiar/teste_copiar1.txt') # Copiando arquivo com mesmo nome.
shutil.copy2('teste_copiar2.txt', 'pasta_copiar') # Copiando arquivo somente para destino.
shutil.copy2('teste_copiar3.txt', 'pasta_copiar/teste_copiar4') # Copiando arquivo alterando nome.

# Movendo

shutil.move('teste_mover1.txt', 'pasta_mover/teste_mover1.txt') # Movendo arquivo com mesmo nome.
shutil.move('teste_mover2.txt', 'pasta_mover/') # Somente movendo para destino.
shutil.move('teste_mover3.txt', 'pasta_mover/teste_mover4.txt') # Movendo arquivo alterando nome.