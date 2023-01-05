import requests

cookies = {
    '_ga_34B604LFFQ': 'GS1.1.1664968148.1.1.1664968212.59.0.0',
    '_ga': 'GA1.2.921267162.1664968147',
    'session': '53616c7465645f5f253ba63c2ccf70156550fcb1edf304e2e1442d100'
               'd8669cbe14f703f5294ebf7b8edb5a0ff4c0a9ae036849ad56de11ec8c0dbe471c344dc',
}

headers = {
    'Content-Type': '',
    'authority': 'adventofcode.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/'
              'webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
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
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://adventofcode.com/2022/day/4/input', cookies=cookies, headers=headers)
result = response.text.strip().split('\n')

cont = 0
for x in result:
    part1, part2 = x.split(',')
    part11, part12 = part1.split('-')
    part21, part22 = part2.split('-')
    if (int(part11) <= int(part21) <= int(part12)) or (int(part21) <= int(part11) <= int(part22)):
        print(x)
        cont += 1

print(cont)
