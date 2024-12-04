import regex as re
import sys

import argparse


def mul(X, Y):
    return X * Y


def main():
    # Initialize parser
    parser = argparse.ArgumentParser(
        description="Process input file type and debug flag"
    )

    # Add arguments
    parser.add_argument(
        "input_suffix",  # choices=['in', 'example'],
        help="Suffix of input file to process",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")

    # Parse arguments
    try:
        args = parser.parse_args()
    except SystemExit:
        # Handle the case where argparse displays help or errors
        sys.exit(1)

    # with open('inputs/03.in', 'r') as file:
    # with open('inputs/03.example', 'r') as file:
    with open(f"inputs/03.{args.input_suffix}", "r") as file:
        input = file.read()

    if args.debug:
        print(input)

    match_list = re.findall(
        pattern=r"mul\([0-9]?[0-9]?[0-9]\,[0-9]?[0-9]?[0-9]\)", string=input
    )

    if args.debug:
        print(match_list)

    result = 0
    for item in match_list:
        result += eval(item)
        if args.debug:
            print(item)
            print(eval(item))

    print("Part 1")
    print(result)

    # ?: at the beginning of paranthesis is defining a non-capturing group. This means that you have a group that needs to be matched as a whole and can be modified (by '?' at the end) but it doesn't need to
    match_list = re.findall(
        pattern=r"mul\([0-9]?[0-9]?[0-9]\,[0-9]?[0-9]?[0-9]\)|do(?:n't)?\(\)",
        string=input,
    )
    # match_list = re.findall(pattern=r"mul\([0-9]?[0-9]?[0-9]\,[0-9]?[0-9]?[0-9]\)", string=input)

    if args.debug:
        print(match_list)

    result = 0
    do = True
    for item in match_list:
        if item == "do()":
            do = True
            if args.debug:
                print(item)
        elif item == "don't()":
            do = False
            if args.debug:
                print(item)
        elif do:
            result += eval(item)
            if args.debug:
                print(item)
                print(eval(item))

    print("Part 2")
    print(result)


if __name__ == "__main__":
    main()
