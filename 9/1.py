import numpy as np

import requests

import time


class Exercise9:
    """
        Solution to day 8 of advent of code 2022 with good practice. standard SOLID.
        """
    data = []

    def __init__(self):
        self.step_list = ["0:0"]
        self.last_postition = [0, 0]
        self.tail = [0, 0]
        self.head = [0, 0]
        self.count = 0
        self.extract_data()

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

        self.data = requests.get(
            'https://adventofcode.com/2022/day/9/input', cookies=cookies, headers=headers
        ).text.strip().split('\n')
        # self.data = open('data.txt', 'r').readlines()

    def actualize_tail(self) -> None:
        x_axis = int(self.head[0]) - int(self.tail[0])
        y_axis = int(self.head[1]) - int(self.tail[1])
        if x_axis > 1 or x_axis < -1 or y_axis > 1 or y_axis < -1:
            self.tail = self.last_postition.copy()
            new_pos = str(self.tail[0]) + ":" + str(self.tail[1])
            if new_pos not in self.step_list:
                self.count += 1
                self.step_list.append(new_pos)
        self.last_postition = self.head.copy()

    def move_steps_direction(self, steps, element, decrease=False):
        for x in range(0, steps):
            if not decrease:
                self.head[element] += 1
            else:
                self.head[element] -= 1
            self.actualize_tail()

    def move_positions(self) -> None:
        for x in self.data:
            if x is not None:
                command, steps = x.strip().split(' ')
                if 'R' in str(command).upper():
                    self.move_steps_direction(int(steps), 0)
                elif 'L' in str(command).upper():
                    self.move_steps_direction(int(steps), 0, True)
                elif 'U' in str(command).upper():
                    self.move_steps_direction(int(steps), 1)
                else:
                    self.move_steps_direction(int(steps), 1, True)
        print(self.count)

Exercise9 = Exercise9()

start = time.time_ns()
Exercise9.move_positions()
end = time.time_ns()
tiempo_de_ejecucion = end - start
print(tiempo_de_ejecucion, "ns")
