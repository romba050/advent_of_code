import regex as re
import sys

import argparse


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

    with open(f"inputs/02.{args.input_suffix}", "r") as file:
        input = file.read()

    if args.debug:
        print(input)

    safe_lines = 0
    unsafe_found = False
    for line in input.split("\n"):
        if not line:  # or if line == ''
            continue
        if args.debug:
            print(line)
        # check if decresing or increasing
        level_list = [int(level) for level in line.split(" ")]
        level_prev = level_list[0]
        level = level_list[1]

        unsafe = False

        decreasing = False
        increasing = False

        # def iter

        # note: range is right exclusive!
        if level in range(
            level_prev - 3, level_prev
        ):  # e.g. "7,6" then 6 is in range(7-3, 7) -> yes so decreasing
            decreasing = True
        elif level in range(
            level_prev + 1, level_prev + 3 + 1
        ):  # e.g. "6,7" then 7 is in range(6+1, 6+4) -> yes so increasing
            increasing = True
        else:
            if args.debug:
                print("unsafe")
            continue

        if decreasing:
            for i in range(2, len(level_list)):
                level = level_list[i]
                level_prev = level_list[i - 1]

                if level_list[i] not in range(level_prev - 3, level_prev):
                    if args.debug:
                        print("unsafe")
                    unsafe = True
                    break
            # if we go through the loop whitout breaking, it means it was all decreasing in a safe amount
            if not unsafe:
                if args.debug:
                    print("safe")
                safe_lines += 1

        if increasing:
            for i in range(2, len(level_list)):
                level = level_list[i]
                level_prev = level_list[i - 1]

                if level_list[i] not in range(level_prev + 1, level_prev + 3 + 1):
                    if args.debug:
                        print("unsafe")
                    unsafe = True
                    break

            # if unsafe_found: # guarantees a double break, so we go to
            #     break

            # if we go through the loop whitout breaking, it means it was all decreasing in a safe amount
            if not unsafe:
                if args.debug:
                    print("safe")
                safe_lines += 1

    print(safe_lines)


if __name__ == "__main__":
    main()
