from extract_data import extract_data


# result of the test
data1 = [
    1301,
    # 1604850,
    # 3885894,
    # 2
]
data2 = [
    1345,
    # 1685186100,
    # 4375225,
    # 1
]

# Initialising variables
index = 0
var1 = None
var2 = None

# Initialising testing variables
dataTest = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1 " \
           "" \
           "22 13 17 11  0 " \
           "8  2 23  4 24" \
           "21  9 14 16  7" \
           "6 10  3 18  5" \
           "1 12 20 15 19" \
           "" \
           "3 15  0  2 22" \
           "9 18 13 17  5" \
           "19  8  7 25 23" \
           "20 11 10 24  4" \
           "14 21 16 12  6" \
           "" \
           "14 21 17 24  4" \
           "10 16 15  9 19" \
           "18  8 23 26 20" \
           "22 11 13  6  5" \
           "2  0 12  3  7"


def general_testing():
    if index == 3:
        exec(f'from day{index} import exercise{index}1, exercise{index}2')
        exec(f'assert (exercise{index}1.execute({dataTest}) == {var1})')
        exec(f'assert (exercise{index}2.execute({dataTest}) == {var2})')
    else:
        exec(f'from day{index} import exercise{index}1, exercise{index}2')
        exec(f'assert (exercise{index}1.execute(extract_data({index})) == {var1})')
        exec(f'assert (exercise{index}2.execute(extract_data({index})) == {var2})')


for item in range(0, len(data1)):
    var1 = data1[item]
    var2 = data2[item]
    index = item + 1
    assert type(extract_data(item)) is list
    exec(f'test{item} = lambda: general_testing()')
