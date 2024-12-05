import regex as re
import sys

import argparse

def report_is_safe(report, debug=False):
    """
    report: list with levels 
    debug: bool whether you want debug prints or not
    return: bool indicating if safe (i.e. not 'unsafe')
    """

    level_prev = report[0]
    level = report[1]


    decreasing = False
    increasing = False

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
        return False

    if decreasing:
        for i in range(2, len(report)):
            level = report[i]
            level_prev = report[i - 1]

            if report[i] not in range(level_prev - 3, level_prev):
                return False
        # if we go through the loop whitout breaking, it means it was all decreasing in a safe amount
        return True

    if increasing:
        for i in range(2, len(report)):
            level = report[i]
            level_prev = report[i - 1]

            if report[i] not in range(level_prev + 1, level_prev + 3 + 1):
                return False

        # if we go through the loop whitout breaking, it means it was all decreasing in a safe amount
        return True
    raise Exception("This code should never be reached")


def report_is_safe_with_Dampener(report):
    # Dampener
    for i in range(0, len(report)):
        # remove one level from report, if this subreport is safe, the whole report is safe
        subreport = [x for j, x in enumerate(report) if j != i]
        safe = report_is_safe(subreport, debug=False)
        if safe:
            return True # no more subreports needed for this line
    return False

    # safe_lines = 0
    # for line in input.split("\n"):
    #     if not line:  # or if line == ''
    #         continue
    #     if args.debug:
    #         print(line)
    #     # check if decresing or increasing
    #     report = [int(level) for level in line.split(" ")]
    #     level_prev = report[0]
    #     level = report[1]

    #     unsafe = False # we start assuming the report is safe, as soon as we find unsafe transition, we continue with the next report OR we break out of the loop going through values and then continue woth the next report

    #     decreasing = False
    #     increasing = False

    #     # def iter

    #     # note: range is right exclusive!
    #     if level in range(
    #         level_prev - 3, level_prev
    #     ):  # e.g. "7,6" then 6 is in range(7-3, 7) -> yes so decreasing
    #         decreasing = True
    #     elif level in range(
    #         level_prev + 1, level_prev + 3 + 1
    #     ):  # e.g. "6,7" then 7 is in range(6+1, 6+4) -> yes so increasing
    #         increasing = True
    #     else:
    #         if args.debug:
    #             print("unsafe")
    #         continue

    #     if decreasing:
    #         for i in range(2, len(report)):
    #             level = report[i]
    #             level_prev = report[i - 1]

    #             if report[i] not in range(level_prev - 3, level_prev):
    #                 if args.debug:
    #                     print("unsafe")
    #                 unsafe = True
    #                 break
    #         # if we go through the loop whitout breaking, it means it was all decreasing in a safe amount
    #         if not unsafe:
    #             if args.debug:
    #                 print("safe")
    #             safe_lines += 1

    #     if increasing:
    #         for i in range(2, len(report)):
    #             level = report[i]
    #             level_prev = report[i - 1]

    #             if report[i] not in range(level_prev + 1, level_prev + 3 + 1):
    #                 if args.debug:
    #                     print("unsafe")
    #                 unsafe = True
    #                 break

    #         # if we go through the loop whitout breaking, it means it was all decreasing in a safe amount
    #         if not unsafe:
    #             if args.debug:
    #                 print("safe")
    #             safe_lines += 1

    # print("Part1")
    # print(safe_lines)

    #########


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
    # input: str with several lines (= reports) each representing a sequence of levels
    for line in input.split("\n"):

            if not line:  # or if line == ''
                continue
            if args.debug:
                print(line)
            # check if decresing or increasing

            report = [int(level) for level in line.split(" ")] # a report is a list of levels representing one line in input

            safe = report_is_safe(report, debug=args.debug)
            if safe:
                safe_lines += 1
            if args.debug:
                if safe:  
                    print("safe")
                else:
                    print("unsafe")

    print()
    print("Part1")
    print(safe_lines)
    print()


    ########################## PART 2 ###################################

    safe_lines = 0
    for line in input.split("\n"):
        if not line:  # or if line == ''
            continue
        if args.debug:
            print(line)
        # check if decresing or increasing

        report = [int(level) for level in line.split(" ")] # a report is a list of levels representing one line in input
        if report_is_safe_with_Dampener(report):
            safe_lines += 1
            if args.debug:
                print("safe")
        else:
            if args.debug:
                print("unsafe")

    print()
    print("Part2")
    print(safe_lines)

if __name__ == "__main__":
    main()
