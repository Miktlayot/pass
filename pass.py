result = []
n = int(input('Ключ: '))
for i in range(1, n):
        a = 0
        for j in range(a, n):
            a += 1
            if i > a:
                continue
            if n % (i + a) == 0 and i != a:
                result.append(i)
                result.append(a)
        a += 1
print('Пароль: ', *result)
