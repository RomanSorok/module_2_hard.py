3result = []

n = int(input("ввести число в первой ячейке: "))
for i in range(1, n):
    if i > n / 2:
        break
    for j in range(i + 1, n):
        if j == i:
            continue
        else:
            if n % (i + j) == 0:
                result.append(f'{i}{j}')

print(result)

result_string = str(result).translate({ord(i): None for i in ", '[]"})
print(result_string)