class Parse:

    def __init__(self, tokens):
        self.tokens = tokens
        self.AST = []

    def add_node(self, parent, node):
        for a in self.AST:
            if parent in a:
                a[parent].append(node)

    def build_AST(self):
        saved = {}
        parent = {}
        collect = False

        for token in self.tokens:
            if token['id'] == 'label':
                t = {token['value']: []}

                if parent != t:
                    parent = token['value']
                    self.AST.append(t)

            elif token['id'] == 'keyword':
                if token['value'] == 'stop':
                    t = {token['value']: 0}
                    self.add_node(parent, t)
                else:
                    if collect == False:
                        saved = token
                        collect = True
                    else:
                        t = {saved['value']: token['value']}
                        self.add_node(parent, t)
                        collect = False

            elif token['id'] == 'char' or token['id'] == 'atom':
                if collect == False:
                    saved = token
                    collect = True
                else:
                    t = {saved['value']: token['value']}
                    self.add_node(parent, t)
                    collect = False 

            elif token['id'] == 'int':
                if collect == False:
                    saved = token
                    collect = True
                else:
                    if "+" in token['value']:
                        x = token['value'].split('+')
                        i = float(x[0]) + float(x[1])

                    elif "-" in token['value']:
                        x = token['value'].split('-')
                        i = float(x[0]) - float(x[1])
                    
                    elif "/" in token['value']:
                        x = token['value'].split('/')
                        i = float(x[0]) * float(x[1])

                    elif "*" in token['value']:
                        x = token['value'].split('*')
                        i = float(x[0]) * float(x[1])

                    t = {saved['value']: i}
                    self.add_node(parent, t)
                    collect = False              