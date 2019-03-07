class Namespace:
    name = ''
    vars = ''
    parent = None

    def add(self, var_name):
        self.vars += var_name

    def get_name(self):
        return self.name

    def get(self, var_name):
        if var_name in self.vars:
            return self.name
        elif self.parent is None:
            return 'None'
        else:
            return self.parent.get(var_name)

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


def read_lines(n):
    namespaces = dict()
    namespaces['global'] = Namespace('global', None)
    for line in range(n):
        cmd, namesp, arg = input().split()
        if cmd == 'create':
            namespaces[namesp] = Namespace(namesp, namespaces[arg])
            print('adding namespace to parent:', namespaces[namesp].parent.get_name())
        elif cmd == 'add':
            namespaces[namesp].add(arg)
        elif cmd == 'get':
            print(namespaces[namesp].get(arg))


n = int(input())
read_lines(n)


