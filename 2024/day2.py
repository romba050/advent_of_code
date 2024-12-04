import regex as re
import sys

import argparse

def mul(X,Y):
  return X*Y

def main():
    # Initialize parser
    parser = argparse.ArgumentParser(description='Process input file type and debug flag')
    
    # Add arguments
    parser.add_argument('input_suffix', #choices=['in', 'example'],
                      help='Suffix of input file to process')
    parser.add_argument('--debug', action='store_true',
                      help='Enable debug mode')

    # Parse arguments
    try:
        args = parser.parse_args()
    except SystemExit:
        # Handle the case where argparse displays help or errors
        sys.exit(1)

    with open(f'inputs/02.{args.input_suffix}', 'r') as file:
      input = file.read()

    if args.debug:
      print(input)


if __name__ == "__main__":
    main()