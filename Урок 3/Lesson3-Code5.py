k = int(input('Enter amount of companies: '))

enterprises = {}

for i in range(1, k + 1):
    name = input("Enter company's name: ")
    enterprises[name] = [float(input('Planing income: ')), float(input('Fact income: '))]
    enterprises[name].append(enterprises[name][1] / enterprises[name][0])
    # print(enterprises)

print('Фактическая прибыль больше 10, но план не выполнен (меньше 100%  )')

for key, value in enterprises.items:
    if value[1] > 10 and value[2] < 1:
        print(f'Компания {name} заработала {value[1]}, что составило {value[2] * 100:.2f}%')
