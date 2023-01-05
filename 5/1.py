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

response = requests.get('https://adventofcode.com/2022/day/5/input', cookies=cookies, headers=headers)
result = response.text.strip().split('\n')
superArray = []

def fixingArray(simpleArray):
    flag = 0
    newArray = []
    for y in simpleArray:
        if y != '' or flag:
            flag = 1
            newArray.append(y)
    secondArray = []
    flag = 0
    for x in newArray:
        if x != '':
            secondArray.append(x)
            flag = 0
        else:
            if flag == 3:
                secondArray.append(x)
                flag = 0
            else:
                flag+=1

    return [*[""]*(9-len(secondArray)), *secondArray]

def createMixArray(multiArray):
    fixedArray = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    for x in multiArray:
        for y in range(0, 9):
            fixedArray[y+1].append([x[y]]) if x[y] != '' else 1
    return fixedArray

def createCargo(result):
    multiArray = []
    complete = 1
    flag = 0
    for x in result:
        if 'move' in x:
            if flag == 0:
                multiArray = createMixArray(multiArray)
                flag = 1
            part1, part2 = x.split('from')
            part1 = int(part1.replace('move', "").strip())
            part_from, part_to = part2.split('to')
            part_from = int(part_from.strip())
            part_to = int(part_to.strip())
            multiArray[part_to] = [*[*multiArray[part_from][part1-1::-1]][::-1], *multiArray[part_to]]
            del multiArray[part_from][part1 - 1::-1]

        else:
            if len(x.strip()) > 0:
                simpleArray = x.split(' ')
                elseArray = x.strip().split(' ')
                try:
                    int(elseArray[0])
                    print("That s an int!", x)
                except ValueError:
                    multiArray.append(fixingArray(simpleArray))
                    complete+=1
    str = ""
    for x in range(0, 9):
        str += ''.join(e for e in multiArray[x + 1][0].__str__() if e.isalnum())
    return str

# requests.post('https://adventofcode.com/2022/day/5/answer', data={'level': 1, 'answer': createCargo(result)}, cookies=cookies, headers=headers)
print(createCargo(result))




