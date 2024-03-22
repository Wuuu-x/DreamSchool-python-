def check_parentheses(s):
    stack = []
    output = ''

    for i, char in enumerate(s):
        if char == '(':
            stack.append((char, i))
        elif char == ')':
            if stack:
                stack.pop()
            else:
                output += '?'

    while stack:
        _, index = stack.pop()
        output = output[:index] + 'x' + output[index:]

    return output


if __name__ == "__main__":
    test_str = input("请输入字符串：\n")
    result = check_parentheses(test_str)
    print(result)
