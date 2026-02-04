from sys import argv,path

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


    print('命令行参数')
    for arg in argv:
        print(arg)
    print('/n python路径为:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

