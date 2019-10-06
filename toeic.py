import random
import argparse
from time import sleep

WORDS_LIST = './words_list/'

def train(args):
    sleep(2)
    list = WORDS_LIST + args.level + '.txt'
    with open(list, 'r', encoding='UTF-8') as f:
        lines = []
        for line_orig in f:
            lines.append(line_orig)
        random.shuffle(lines)
        for line_random in lines:
            elements = line_random.split(',')
            for element in elements:
                print(element)
                sleep(args.time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='level_selection')
    parser.add_argument('--level', nargs='?', type=str, default=None,
                        help='Select level [\'GOLD, extra, 600, 600_2, 700, 800\']')
    parser.add_argument('--time', nargs='?', type=float, default=2,
                        help='Interval[second]')
    args = parser.parse_args()
    train(args)
