"""Работа с python примерами"""
import re
import keyword


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
