"""Написать программу, которая считает
сумму всех чисел от 1 до 50. И выводит
ее через print()"""
summary = 0
for i in range(1, 51):
    summary += i

print(summary)

# есть решение проще:
print(sum(range(1, 51)))

