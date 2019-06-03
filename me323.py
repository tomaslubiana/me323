import random
import matplotlib.pyplot as plt
import os as s

def func_testes(num,vet):
	vet_probabilidade = []
	for j in range(2000):	#número de testes do problema
		for i in range(num):#gera números aleatórios
			aleatorio = random.sample(range(0,amostra),num)
			p.append(vet[aleatorio[i]])
		flag=0
		for k in range(len(p)):
			if p[k] == 1:
				flag+=1
		prob_p = flag/len(p)
		vet_probabilidade.append(round(prob_p,3))
	return vet_probabilidade

global total
global amostra
total = 2000
amostra = 500
N = []
p = []
probabilidade1 = []
probabilidade2 = []
tentativas = []

for i in range(total):
	tentativas.append(i+1)

for i in range(amostra):	#inicializando N
	if i<(0.3*amostra):
		N.append(1);
	else:
		N.append(0);

probabilidade1 = func_testes(10,N)
probabilidade2 = func_testes(200,N)
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (11,7)
plt.plot(tentativas, probabilidade1, color = 'green', label = 'Escolhendo 10')
plt.plot(tentativas, probabilidade2, color = 'red', label = 'Escolhendo 200')
plt.legend()
plt.title('Candidatos A e B')
plt.xlabel('Tentativas(N)')
plt.ylabel('Probabilidade(P)')
plt.show()
