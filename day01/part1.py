from __future__ import annotations

import argparse
import os.path

import pytest

# from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    for n in numbers:
        pass

    count = 0
    last = 0
    lines = s.splitlines()
    for sline in lines:
        line = int(sline)
        if last != 0 and last < line:
            count = count+1
        last = line
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
         print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
