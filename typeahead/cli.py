import argparse

def parse():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('port', metavar='port', type=int, help='an integer for the accumulator')
    parser.add_argument('data_path', metavar='data_path', type=str, help='an integer for the accumulator')
    return parser.parse_args()