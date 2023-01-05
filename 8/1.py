import numpy as np

import requests

import time


class Exercise8:
    """
        Solution to day 8 of advent of code 2022 with good practice. standard SOLID.
        """
    data = []

    def __init__(self):
        self.count = 0
        self.extract_data()
        self.matrix = np.zeros((len(self.data), len(self.data[0].strip())))
        self.matrix_copy = np.array([list(item.strip()) for item in self.data])

    def extract_data(self) -> None:
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

        # self.data = requests.get(
        #     'https://adventofcode.com/2022/day/8/input', cookies=cookies, headers=headers
        # ).text.strip().split('\n')
        self.data = open('data.txt', 'r').readlines()

    def counter(self, len_matrix: int, line: int = 0) -> None:
        if line == 0 or line == len(self.matrix):
            for item in range(0, len_matrix+1):
                if self.matrix[line][item] != 1:
                    self.count += 1
                self.matrix[line][item] = 1
        else:
            if self.matrix[line][0] != 1:
                self.count += 1
            if self.matrix[line][len_matrix] != 1:
                self.count += 1
            self.matrix[line][0] = 1
            self.matrix[line][len_matrix] = 1
            for item in range(1, len_matrix):
                if max(self.matrix_copy[line][0:item]) < self.matrix_copy[line][item] \
                        or max(self.matrix_copy[line][item + 1: len_matrix + 1]) < self.matrix_copy[line][item]:
                    if self.matrix[line][item] != 1:
                        self.count += 1
                    self.matrix[line][item] = 1

    def counter_matrix(self) -> None:
        line = 0
        len_matrix = len(self.matrix_copy[line]) - 1
        for _ in self.matrix_copy:
            self.counter(len_matrix, line)
            line += 1
        self.matrix = self.matrix.T
        self.matrix_copy = self.matrix_copy.T

    def print_len_matrix(self) -> None:
        print(self.count)

    def seek_amount_trees(self) -> None:
        try:
            self.counter_matrix()
            self.counter_matrix()
            self.print_len_matrix()
        except Exception as error:
            print(error)


exercise8 = Exercise8()

start = time.time_ns()
exercise8.seek_amount_trees()
end = time.time_ns()
tiempo_de_ejecucion = end - start
print(tiempo_de_ejecucion, "ns")
