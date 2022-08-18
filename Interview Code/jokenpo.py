# @author   Lucas Cardoso de Medeiros
# @since    03/06/2022
# @version  1.0

# JOKENPÔ

# Regras:
# Pedra   (0) ganha de: Tesoura (2) e (3) Lagarto
# Papel   (1) ganha de: Pedra   (0) e (4) Spock
# Tesoura (2) ganha de: Papel   (1) e (3) Lagarto
# Lagarto (3) ganha de: Spock   (4) e (1) Papel
# Spock   (4) ganha de: Tesoura (2) e (0) Pedra

# 0 - Pedra
# 1 - Papel
# 2 - Tesoura
# 3 - Lagarto
# 4 - Spock

jogadas = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']
vitoria = [
            [2, 3],
            [0, 4],
            [1, 3],
            [1, 4],
            [0, 2]
        ]

print('''Opções:
        0 - Pedra
        1 - Papel
        2 - Tesoura
        3 - Lagarto
        4 - Spock''')
print()
p1 = int(input('Jogador 1: '))
p2 = int(input('Jogador 2: '))

if p1 < 0 or p2 < 0 or p1 >= len(jogadas) or p2 >= len(jogadas):
    print('Jogada inválida')
    exit(-1)

print(f'P1: {jogadas[p1]}')
print(f'P2: {jogadas[p2]}')
print()

if p1 == p2:
    print('EMPATE')
else:
    for i in vitoria[p1]:
        if i == p2:
            print('Jogador 1 venceu!')
            exit(1)
    print('Jogador 2 venceu!')
    exit(2)


