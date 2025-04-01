"""Работа с python примерами"""


import re
import keyword
import struct


def color_code(code: str) -> str:
    res = []
    for code_str in code.split("\n"):
        keywords_list = list(keyword.kwlist) + list(keyword.softkwlist)
        keywords_list.remove("type")
        matches = re.findall(r"\b\w+\b", code_str)
        for word in matches:
            if word in keywords_list:
                code_str = re.sub(r"\b(" + word + r")\b", r'<code class="code-python-keyword">\1</code>', code_str)
        code_str = re.sub(r'("""[^"]*""")', r'<code class="code-python-comment">\1</code>', code_str)
        code_str = re.sub(r"\b(\w{3,})\(", r'<code class="code-python-func">\1</code>(', code_str)
        code_str = re.sub(r"(self)", r'<code class="code-python-s">\1</code>', code_str)
        code_str = re.sub(r"(#.+)", r'<code class="code-python-com">\1</code>', code_str)
        res.append(code_str)
    res = "\n".join(res)
    return res


def color_code2(code: str, long_string: str = '') -> str:
    new_strings = []
    string_symbols = ('"""', "'''", "'", '"')
    for code_str in code.split('\n'):
        if not long_string:
            for symbol in string_symbols:
                if symbol in code_str:
                    parts = code_str.split(symbol)
                    for i, part in enumerate(parts):
                        if i % 2 == 0:
                            if i == len(part) - 1:
                                part = color_code2(part, long_string=symbol)
                            else:
                                part = color_code2(part)
                        else:
                            part = f"<code class='code-python-comment'>{part}</code>"
                        parts[i] = part
                    new_strings.append(symbol.join(parts))
            if "#" in code_str:
                parts = code_str.split("#")
                code_str = color_code2(parts[0]) + "<code class='code-python-com'>#" + parts[1] + "</code>"
                new_strings.append(code_str)
                continue

    return "\n".join(new_strings)


def color_code3(code: str) -> str:
    changes = {}
    keywords_list = list(keyword.kwlist) + list(keyword.softkwlist)
    keywords_list.remove("type")

    pattern = r"#.+"
    finds = re.findall(pattern, code)
    for f in finds:
        k = "__str" + str(len(changes) + 1)
        changes[k] = f"<code class='code-python-com'>{f}</code>"
        f = re.sub(r"\\", r"\\\\", f)
        f = re.sub(r"\[", r"\\[", f)
        f = re.sub(r"\?", r"\\?", f)
        code = re.sub(f, k, code)

    pattern = r'"""[^"]*?"""'
    finds = re.findall(pattern, code)
    for f in finds:
        k = "__str" + str(len(changes) + 1)
        changes[k] = f"<code class='code-python-comment'>{f}</code>"
        code = re.sub(f, k, code)

    pattern = r'"[^"]*?"'
    finds = re.findall(pattern, code)
    for f in finds:
        k = "__str" + str(len(changes) + 1)
        changes[k] = f"<code class='code-python-string'>{f}</code>"
        code = re.sub(f, k, code)

    pattern = r"'[^']*?'"
    finds = re.findall(pattern, code)
    for f in finds:
        k = "__str" + str(len(changes) + 1)
        changes[k] = f"<code class='code-python-string'>{f}</code>"
        code = re.sub(f, k, code)

    pattern = r'self'
    finds = re.findall(pattern, code)
    for f in finds:
        k = "__str" + str(len(changes) + 1)
        changes[k] = f"<code class='code-python-self'>{f}</code>"
        code = re.sub(f, k, code)

    pattern = r"\b\w+\b"
    finds = re.findall(pattern, code)
    for f in finds:
        if f in keywords_list:
            k = "__str" + str(len(changes) + 1)
            changes[k] = f"<code class='code-python-keyword'>{f}</code>"
            code = re.sub(f, k, code)

    code = re.sub(r"\b(\w{3,})\(", r'<code class="code-python-func">\1</code>(', code)

    def changer(match):
        return changes[match[0]]

    new_code = re.sub(r"__str\d+", changer, code)
    return new_code


def color_code4(code: str) -> str:
    changes = {}
    n = 0
    keywords_list = list(keyword.kwlist) + list(keyword.softkwlist)
    keywords_list.remove("type")

    patterns = ((r"#.+", "<code class='code-python-com'>"),
                (r'"""[^"]*?"""', "<code class='code-python-comment'>"),
                (r'"[^"]*?"', "<code class='code-python-string'>"),
                (r"'[^']*?'", "<code class='code-python-string'>"),
                (r'self', '<code class="code-python-self">'),
                (r"@.+", '<code class="code-python-decorator">'),
                (r"\b\w+\b", '<code class="code-python-keyword">'),
                )

    def change_code(match, n_code) -> str:
        if n_code == '<code class="code-python-keyword">':
            if match[0] not in keywords_list:
                return match[0]
        nonlocal changes
        nonlocal n
        kw = f"__chg{n}"
        n += 1
        changes[kw] = f"{n_code}{match[0]}</code>"
        return kw

    for pattern, change in patterns:
        code = re.sub(pattern, lambda m: change_code(m, change), code)

    code = re.sub(r"\b(\w{3,})\(", r'<code class="code-python-func">\1</code>(', code)

    def changer(match):
        nonlocal changes
        return changes[match[0]]

    new_code = re.sub(r"__chg\d+", changer, code)
    return new_code


