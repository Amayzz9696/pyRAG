#判断标识符是否合法
def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False


if __name__ == '__main__':
    # print('hello world')
    # print(2**32)
    print(is_valid_identifier("2var"))
    print(is_valid_identifier("var2"))

