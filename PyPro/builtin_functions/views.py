from django.shortcuts import render
from . import code
import os


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
    builtins_functions_list = [i for i in __builtins__ if i[0] in [chr(j) for j in range(97, 123)]]
    builtins_functions_list.sort()
    builtins_functions_dict = {}
    for builtin_function in builtins_functions_list:
        if builtin_function[0] in builtins_functions_dict:
            builtins_functions_dict[builtin_function[0]].append(builtin_function)
        else:
            builtins_functions_dict[builtin_function[0]] = [builtin_function]
    content = {
        "title": f"Встроенная функция {func_name}",
        "builtin_functions": builtins_functions_dict,
    }
    path = f'{os.getcwd()}\\builtin_functions\\static\\builtin_functions\\'
    examples = []
    for address, dirs, files in os.walk(f'{path}\\{func_name}'):

        if dirs:
            for dir_name in dirs:
                files = os.listdir(f'{path}\\{func_name}\\{dir_name}')
                for file in files:
                    ex_code = []
                    with open(f'{path}\\{func_name}\\{dir_name}\\{file}', 'r', encoding='utf-8') as opened:
                        new_code = code.color_code4(opened.read())
                        # ex_code.append(code.color_code3(opened.readline()))
                    examples.append(new_code)
    content["examples"] = examples

    return render(request, f"builtin_functions/{func_name}.html", content)
