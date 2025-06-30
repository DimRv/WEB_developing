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

    keywords_list = list(keyword.kwlist) + list(keyword.softkwlist)
    keywords_list.sort()
    builtins_instructions_dict = {}
    instructions_list = [i for i in keywords_list if i[0] in [chr(j) for j in range(97, 123)]]
    for builtin_instruction in instructions_list:
        if builtin_instruction[0] in builtins_instructions_dict:
            builtins_instructions_dict[builtin_instruction[0]].append(builtin_instruction)
        else:
            builtins_instructions_dict[builtin_instruction[0]] = [builtin_instruction]

    content = {
        "title": "PyPro",
        "builtin_functions": builtins_functions_dict,
        "builtin_instructions": builtins_instructions_dict,
    }
    return render(request, "base/index.html", content)
