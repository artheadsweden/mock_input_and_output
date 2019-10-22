def get_input_stacks():
    n = int(input())
    stacks = []
    for _ in range(n):
        str_stack = input().split()
        end_pos = int(str_stack[0])
        str_stack = str_stack[1:end_pos+1]
        stack = [int(s) for s in str_stack]
        stacks.append(stack)
    return stacks


def print_greeting(name):
    print("Hi", name)


def main():
    pass


if __name__ == '__main__':
    main()
