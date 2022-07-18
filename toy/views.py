from django.shortcuts import render

def gugu(req, num):

    # classical
    mul_table = []
    for i in range(1, 10):
        mul_text = f"{num} * {i} = {num * i}"
        mul_table.append(mul_text)
    print(1, mul_table)

    # list comprehension
    mul_table = [f"{num} * {i} = {num * i}" for i in range(1, 10)]
    print(2, mul_table)

    # map + functinal
    mul_table = list(map(lambda i: f"{num} * {i} = {num * i}", range(1, 10)))
    print(3, mul_table)

    return render(req, 'toy/gugu.html', {'mul_table': mul_table})