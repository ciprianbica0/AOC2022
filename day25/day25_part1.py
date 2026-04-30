import datetime
import random

start = datetime.datetime.now()
file = open('day25\\day25_input.txt', 'r')

numbas = []
for line in file:
    numbas.append(line)

print(numbas)


translation_map = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

normal_numbers = []


def to_base10(translation_map, snafu_number):
    normal = 0
    for i in range(len(snafu_number)):
        power = len(snafu_number)-1-i
        normal += translation_map[snafu_number[i]]*(5**power)
    return normal


for snafu in numbas:
    snafu = snafu.replace("\n", "")
    normal = to_base10(translation_map, snafu)
    normal_numbers.append(normal)

print(normal_numbers)
final_sum = sum(normal_numbers)
print(final_sum)


def to_snafu(x):
    remainder = x
    result = ""
    trans_map = {
        0: '0',
        1: '1',
        2: '2',
        3: '=',
        4: '-',
    }
    while remainder > 0:
        rem,remainder = remainder % 5, round(remainder/5)
        result += trans_map[rem] 
    return result[::-1]


print(to_snafu(final_sum))
end = datetime.datetime.now()
print("ended in", end-start)
