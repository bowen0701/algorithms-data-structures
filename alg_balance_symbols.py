from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def balance_parentheses(a_str):
    """Balance parentheses in a string."""
    stack = []
    balanced = True
    pos = 0
    while pos < len(a_str) and balanced:
        symbol = a_str[pos]
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            if not stack:
                balanced = False
                break
            else:
                stack.pop()
        else:
            pass
        pos += 1

    if balanced and not stack:
        return True
    else:
        return False


def _match_symbols(opener, closer):
    openers = '([{'
    closers = ')]}'
    match_bool = openers.index(opener) == closers.index(closer)
    return match_bool


def balance_symbols(a_str):
    """Balance "arbitrary" symbols in a string.
    The symbols here are '()', '[]' and '{}'. 
    """
    stack = []
    balanced = True
    pos = 0
    while pos < len(a_str) and balanced:
        symbol = a_str[pos]
        if symbol in '([{':
            stack.append(symbol)
        elif symbol in ')]}':
            if not stack:
                balanced = False
                break
            else:
                open_symbol = stack.pop()
                if not _match_symbols(open_symbol, symbol):
                    balanced = False
                    break
        else:
            pass
        pos += 1

    if balanced and not stack:
        return True
    else:
        return False


def main():
    import time

    text_match = '(abcd)'

    start_time = time.time()
    print('By balance_parentheses(): {}'
          .format(balance_parentheses(text_match)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By balance_symbols(): {}'
          .format(balance_symbols(text_match)))
    print('Time: {}'.format(time.time() - start_time))

    text_match2 = '([abcd]efg)'

    start_time = time.time()
    print('By balance_symbols(): {}'
          .format(balance_symbols(text_match2)))
    print('Time: {}'.format(time.time() - start_time))

    text_unmatch = '(abcd]'

    start_time = time.time()
    print('By balance_parentheses(): {}'
          .format(balance_parentheses(text_unmatch)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By balance_symbols(): {}'
          .format(balance_symbols(text_unmatch)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()