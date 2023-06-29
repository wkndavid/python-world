# Exercício de medidas
dt = float(input('Digite um comprimento em metros: '))
km = dt * 0.001
hm = dt * 0.01
dam = dt * 0.1
dm = dt * 10
cm = dt * 100
mm = dt * 1000

print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}dm, {}cm e {}mm.'.format(dt, (km), hm, dam, dm, cm, mm))