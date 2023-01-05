import requests

cookies = {
    '_ga_34B604LFFQ': 'GS1.1.1664968148.1.1.1664968212.59.0.0',
    '_ga': 'GA1.2.921267162.1664968147',
    'session': '53616c7465645f5f253ba63c2ccf70156550fcb1edf304e2e1442d100d8669cbe14f703f5294ebf7b8edb5a0ff4c0a9ae036849ad56de11ec8c0dbe471c344dc',
}

headers = {
    'Content-Type': '',
    'authority': 'adventofcode.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
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
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://adventofcode.com/2022/day/2/input', cookies=cookies, headers=headers)
#result = response.text.strip().split('\n')
result = [
    'A Y',
    'B X',
    'C Z',
]
total = 0
dictionary = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
for x in result:
    a = x.strip().split(' ')
    if dictionary[a[0]] == dictionary[a[1]]:
        total += (3 + int(dictionary[a[1]]))
    elif (dictionary[a[1]] < dictionary[a[0]] and dictionary[a[0]] - dictionary[a[1]] != 2) or dictionary[a[1]] - dictionary[a[0]] == 2:
        total += int(dictionary[a[1]])
    else:
        total += (int(dictionary[a[1]]) + 6)
print(total)