from django.shortcuts import render

def gugu(req, num):
    return render(req, 'toy/gugu.html', 
            {'mul_table': [f"{num} * {i} = {num * i}" for i in range(1, 10)]})