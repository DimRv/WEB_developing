from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def form(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    n1 = int(request.POST.get('a'))
    n2 = int(request.POST.get('b'))
    method = request.POST.get('method')
    result = 0
    match method:
        case "+":
            result = n1 + n2
        case "-":
            result = n1 - n2
        case "*":
            result = n1 * n2
        case "/":
            if n2 == 0:
                result = "Ошибка!"
            result = n1 + n2

    return HttpResponse(f"{n1} {method} {n2} = {result}")

