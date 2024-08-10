class Stack():
    def __init__(self, stack):
        self.stack = stack

    # проверка стека на пустоту. Метод возвращает True или False
    def is_empty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

    # Добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, item):
        self.stack.append(item)

    # Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    # Возвращает верхний элемент стека, но не удаляет его. Стек не меняется
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    # Возвращает количество элементов в стеке
    def size(self):
        lenght = len(self.stack)
        return lenght


def is_balanced(self):
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    bracket_stack = []
    is_good = True
    for bracket in self.stack:
        if bracket in opening_brackets:
            bracket_stack.append(bracket)
        elif bracket in closing_brackets:
            if len(bracket_stack) == 0:
                is_good = False
                break
            open_bracket = bracket_stack.pop()
            if open_bracket == '(' and bracket == ')':
                continue
            if open_bracket == '{' and bracket == '}':
                continue
            if open_bracket == '[' and bracket == ']':
                continue
            is_good = False
    if is_good and len(bracket_stack) == 0:
        return f'{self.stack} - Cбалансированно'
    else:
        return f'{self.stack} - Несбалансированно'


def test():
    stack = Stack('(((([{}]))))')
    assert is_balanced(stack)
    stack2 = Stack('[([])((([[[]]])))]{()}')
    assert is_balanced(stack2)
    stack3 = Stack('{{[()]}}')
    assert is_balanced(stack3)
    stack4 = Stack('}{}')
    assert is_balanced(stack4)
    stack5 = Stack('{{[(])]}}')
    assert is_balanced(stack5)
    stack6 = Stack('{{[(])]}}')
    assert is_balanced(stack6)
    stack7 = Stack('[[{())}]')
    assert is_balanced(stack7)
    print('Все тесты прошли успешно!')


if __name__ == '__main__':
    
    test()
