def is_valid_parentheses(data):
    stack = []
    for char in data:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top_element = stack.pop()
            if char == ')' and top_element != '(':
                return False
            elif char == '}' and top_element != '{':
                return False
            elif char == ']' and top_element != '[':
                return False
    return not stack

s = """
[
{
company_name: (BlackRock)
ticker; (BLK) stock price:{
2022-04-03: ($930)
2022-04-02: ($932)
}
},{
company name: (Apple)
ticker: (APPL)
stock price:{
2022-04-03: ($175)
2022-04-02; ($178)
}
}
]
"""

s2 = """[{()(){()()}{()(){()()}}]]"""

print(is_valid_parentheses(s2))