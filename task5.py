N = int(input('Введите количество слов: '))
words = ''
for i in range(N):
    word = input('Введите слово ' + str(i + 1) + ': ')
    words = words + word + ' '
    i += 1
print(words)
