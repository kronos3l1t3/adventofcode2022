import sys

import requests


class Tree:
    """
            Tree class solution.
            """

    def __init__(self, name='/', parent='/', data=0):
        self.data = data
        self.name = name
        self.parent = parent
        self.children = []
        self.files = {}

    def add_child(self, obj):
        self.children.append(obj)

    def add_data(self, number):
        self.data += int(number)

    def add_file(self, file, size):
        self.files[file] = int(size)

    def look_node(self, name, children=None):
        if self.name == name:
            return self

        if children is None:
            children = self.children

        for node in children:
            if node.name == name:
                return node
            elif len(node.children) > 0:
                node = node.look_node(name, node.children)
                if node is not None:
                    return node

    def recalc_totals(self, children=None):
        if children is None:
            children = self.children

        for node in children:
            if len(node.children) > 0:
                self.data += node.recalc_totals(node.children)
            else:
                self.data += node.data
        return self.data

    def calc_total(self, children=None):
        total = 0
        if self.data < 100001:
            total = self.data

        if children is None:
            children = self.children

        for node in children:
            if len(node.children) > 0:
                total += node.calc_total(node.children)
            else:
                if node.data <= 100000:
                    total += node.data
        return total

    def __str__(self):
        return self.name


class Exercise7:
    """
        Solution to day 7 of advent of code 2022 with good practice. standard SOLID and some techniques like recursive.
        """

    @staticmethod
    def extract_data():
        cookies = {
            '_ga_34B604LFFQ': 'GS1.1.1664968148.1.1.1664968212.59.0.0',
            '_ga': 'GA1.2.921267162.1664968147',
            'session': '53616c7465645f5f253ba63c2ccf70156550fcb1edf304e2e1442d100d8669cb'
                       'e14f703f5294ebf7b8edb5a0ff4c0a9ae036849ad56de11ec8c0dbe471c344dc',
        }

        headers = {
            'Content-Type': '',
            'authority': 'adventofcode.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
                      'avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'es-ES,es;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }

        # return requests.get('https://adventofcode.com/2022/day/7/input', cookies=cookies, headers=headers).text.strip().split('\n')
        return open('data.txt', 'r').readlines()

    def seek_file_system(self):
        try:
            tree = Tree()
            flag = ''
            for item in self.extract_data():
                if '$' in item:
                    if 'cd' in item:
                        simbol, command, directory = item.split(' ')
                        if '..' in directory:
                            node_obj = tree.look_node(flag)
                            flag = node_obj.parent
                        else:
                            if '/' not in str(directory).strip():
                                flag = flag + str(directory).strip() + '/'
                            else:
                                flag = str(directory).strip()


                elif 'dir' in item:
                    command, node_name = item.split(' ')
                    node = Tree(str(flag+node_name+'/').replace('\n', '').strip(), flag)
                    node_obj = tree.look_node(flag)
                    node_obj.children.append(node)

                else:
                    number, file = item.split(' ')
                    if str(number).strip().isnumeric():
                        node_obj = tree.look_node(flag)
                        node_obj.add_data(str(number).strip())
                        node_obj.add_file(file, str(number).strip())

            tree.recalc_totals()
            print(tree.calc_total())
        except Exception as error:
            print(error)
        except:
            print("Error:", sys.exc_info()[0])


exercise7 = Exercise7()
exercise7.seek_file_system()
