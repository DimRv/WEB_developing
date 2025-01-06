from django.shortcuts import render
import keyword


def index(request):
    builtins_functions_list = [i for i in __builtins__ if i[0] in [chr(j) for j in range(97, 123)]]
    builtins_functions_list.sort()
    builtins_functions_dict = {}
    for builtin_function in builtins_functions_list:
        if builtin_function[0] in builtins_functions_dict:
            builtins_functions_dict[builtin_function[0]].append(builtin_function)
        else:
            builtins_functions_dict[builtin_function[0]] = [builtin_function]

    content = {
        "title": "Встроенные функции",
        "builtin_functions": builtins_functions_dict,
    }

    return render(request, "builtin_functions/index.html", content)


def details(request, func_name):
    content = {
        "title": f"Встроенная функция {func_name}",
    }
    return render(request, f"builtin_functions/{func_name}.html", content)
