import argparse
import sys

from AbstractSerializer.abstract_serializer import GeneralSerializer


def func_pars(file_from, file_to, format_from, format_to):
    ser_from = GeneralSerializer.parser(format_from)
    ser_to = GeneralSerializer.parser(format_to)

    res = ser_from.load(f'/home/user/PycharmProjects/lr3_IGI/{file_from}')
    print(res)

    ser_to.dump(res, file_to)


def main():
    parser = argparse.ArgumentParser(prog='my_prog', description='ConcreteSerializer')
    parser.add_argument('file_from', type=str, help='from file')
    parser.add_argument('file_to', type=str, help='to file')
    parser.add_argument('format_from', type=str, help='from format type')
    parser.add_argument('format_to', type=str, help='to format type')

    args = parser.parse_args()

    file_from = args.file_from
    file_to = args.file_to
    format_from = args.format_from
    format_to = args.format_to

    if file_from == '' or file_to == '' or format_from == '' or format_to == '':
        print('Error, args is missing!')
        sys.exit()
    else:
        func_pars(file_from, file_to, format_from, format_to)


if __name__ == '__main__':
    main()
