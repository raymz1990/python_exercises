## EXERCISE #001
#(by pythonparadados on Instagram)

#### STATISTICS WITH PYTHON (by pythonparadados on Instagram)

# Importando bibliotecas
import pandas as pd

# Gerando os dados
notas_e_nomes = {'João':    [7.5, 6.5, 9.0, 4.2],
                 'Maria':   [8.0, 8.5, 9.5, 10],
                 'José':    [5.0, 5.0, 7.0, 5.0],
                 'Pedro':   [8.0, 10, 9.0, 9.0]}

bimestres = ['1 Bimestre', '2 Bimestre',
             '3 Bimestre', '4 Bimestre']

# Construindo o dataframe
boletim = pd.DataFrame(notas_e_nomes, index = bimestres)

# Calculando e imprimindo as médias
print(' -- Média dos Alunos --')
print()
print(f'João obteve média   {boletim["João"].mean()}')
print(f'Maria obteve média  {boletim["Maria"].mean()}')
print(f'José obteve média   {boletim["José"].mean()}')
print(f'Pedro obteve média  {boletim["Pedro"].mean()}')

# Calculando e imprimindo as medianas
print(' -- Mediana dos Alunos --')
print()
print(f'João obteve mediana   {boletim["João"].median()}')
print(f'Maria obteve mediana  {boletim["Maria"].median()}')
print(f'José obteve mediana   {boletim["José"].median()}')
print(f'Pedro obteve mediana  {boletim["Pedro"].median()}')

# Calculando a Variância
print(' -- Variância --')
print()
print(f'João variou   {round(boletim["João"].var(),2)} pontos.')
print(f'Maria variou  {round(boletim["Maria"].var(),2)} pontos.')
print(f'José variou   {round(boletim["José"].var(),2)} pontos.')
print(f'Pedro variou  {round(boletim["Pedro"].var(),2)} pontos.')

# Desvio Padrão
print(' -- Desvio Padrão das notas --')
print()
print(f'João obteu um desvio de:   {round(boletim["João"].std(),1)}')
print(f'Maria obteu um desvio de:  {round(boletim["Maria"].std(),1)}')
print(f'José obteu um desvio de:   {round(boletim["José"].std(),1)}')
print(f'Pedro obteu um desvio de:  {round(boletim["Pedro"].std(),1)}')
