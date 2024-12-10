import regex as re
import sys

import argparse
import numpy as np

import operator



def string_to_char_matrix(text):
    """
    Convert a multiline string into a NumPy array of characters.
    
    Parameters:
    text (str): Input string with newlines
    
    Returns:
    numpy.ndarray: 2D array of characters
    """
    # Split the string into lines and remove empty lines (since line.strip("") returns False)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Verify all lines have the same length
    if not all(len(line) == len(lines[0]) for line in lines):
        raise ValueError("All lines must have the same length")
    
    # Convert to array of characters
    char_array = np.array([list(line) for line in lines])
    
    return char_array

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
    with open(f"inputs/04.{args.input_suffix}", "r") as file:

        input = file.read()
        if args.debug:
            print(input)

        print("Part1")
        solution_example = """
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""
        print(f"solution_example: \n{solution_example}")

        input_matrix = string_to_char_matrix(input)

        # pattern = list("XMAS")
        # reverse_pattern = pattern[::-1]
        # pl = len(pattern)

        # print(pattern)
        # print(reverse_pattern)


        print(input_matrix)
        nrows = input_matrix.shape[0]
        ncols = input_matrix.shape[1]

        match_list = []

        # print(dim(input_matrix))
        def count_matches_horizontal(pattern_str):
            pl = len(pattern_str)
            match_count = 0
            for i in range(0, nrows): 
                # stop short pl letters before the end
                for j in range(0, ncols-pl+1): # +1 because range(x) is x-exclusive in python. e.g. if ncols=10, pl=4 we want to go up to 7, not just 6
                    # .all() because we have an array of element wise comparison results
                    if pattern_str == ''.join(input_matrix[i, j: j+pl]):
                        match_count += 1
                        if args.debug:
                            print(f'horizontal match of {pattern_str} at {(i, j)}')
                            match_list.append((i, j, pattern_str, 'horizontal'))
            return match_count

        def count_matches_vertical(pattern_str):
            pl = len(pattern_str)
            match_count = 0
            for i in range(0, nrows-pl+1): # +1 because range(x) is x-exclusive in python. e.g. if nrows=10, pl=4 we want to go up to 7, not just 6
                for j in range(0, ncols):
                    # .all() because we have an array of element wise comparison results
                    if pattern_str == ''.join(input_matrix[i: i+pl, j]):
                        match_count += 1
                        if args.debug:
                            print(f'vertical match of {pattern_str} at {(i, j)}')
                            match_list.append((i, j, pattern_str, 'vertical'))
            return match_count

        def count_matches_major_diagonal(pattern_str, part2 = False):
            # the major diagonal is the one from the top left ot the bottom right
            pl = len(pattern_str)
            match_count = 0
            for i in range(0, nrows-pl+1):
                for j in range(0, ncols-pl+1):
                    # .join() to convert back ot str
                    diagonal_window = ''.join([input_matrix[i+k, j+k] for k in range(0, pl)])
                    if (pattern_str == diagonal_window):
                        match_count += 1
                        if part2:
                            match_list.append((i+1, j+1, pattern_str, 'major_diagonal'))
                            if args.debug:
                                print(f'major diagonal match of {pattern_str} at {(i+1, j+1)}')
                        else:
                            match_list.append((i, j, pattern_str, 'major_diagonal'))
                            if args.debug:
                                print(f'major diagonal match of {pattern_str} at {(i, j)}')
                            
            return match_count

        def count_matches_minor_diagonal(pattern_str, part2 = False):
            # if part2, we save the coordinates of the central 'A', if Part1, we save the coordinate of the first letter of the pattern
            # the minor diagonal is the one from the top right ot the bottom left
            pl = len(pattern_str)
            match_count = 0
            for i in range(0, nrows-pl+1):
                for j in range(pl-1, ncols):
                    # .join() to convert back ot str
                    diagonal_window = ''.join([input_matrix[i+k, j-k] for k in range(0, pl)])
                    if (pattern_str == diagonal_window):
                        match_count += 1
                        if part2:
                            match_list.append((i+1, j-1, pattern_str, 'minor_diagonal'))
                            if args.debug:
                                print(f'minor diagonal match of {pattern_str} at {(i+1, j-1)}')
                        else:
                            match_list.append((i, j, pattern_str, 'minor_diagonal'))
                            if args.debug:
                                print(f'minor diagonal match of {pattern_str} at {(i, j)}')

            return match_count

        cmhf = count_matches_horizontal("XMAS")
        cmhb = count_matches_horizontal("SAMX")
        cmvf = count_matches_vertical("XMAS")
        cmvb = count_matches_vertical("SAMX")
        cmmadf = count_matches_major_diagonal("XMAS")
        cmmadb = count_matches_major_diagonal("SAMX")
        cmmidf = count_matches_minor_diagonal("XMAS")
        cmmidb = count_matches_minor_diagonal("SAMX")

        print(f"cmhf: {cmhf}")
        print(f"cmhb: {cmhb}")
        print(f"cmvf: {cmvf}")
        print(f"cmvb: {cmvb}")
        print(f"cmmadf: {cmmadf}")
        print(f"cmmadb: {cmmadb}")
        print(f"cmmidf: {cmmidf}")
        print(f"cmmidb: {cmmidb}")

        total_matches = cmhf + cmhb + cmvf + cmvb + cmmadf + cmmadb + cmmidf + cmmidb

        print("Part1")
        print(total_matches)

        def draw_solution(nrows, ncols, match_list=[], part2 = False):
            # if part2 =True, we assume the provided matchlist contains coordinates of central 'A', otherwise matchlist contains coordinates of first letter of pattern
            # create grid of dots
            solution_grid = '\n'.join('.' * ncols for _ in range(nrows)) # compact form
            # print(solution_grid)
            solution_grid = np.array([np.array(list(row)) for row in solution_grid.split()]) # transform into arrays because strings are immutable and we need to overwrite

            print(solution_grid.shape)

            # overwrite grid with matches
            for match in match_list:
                i, j, pattern_str, direction = match
                pl = len(pattern_str)

                if part2: # since we save the central A in part2, we need to readjust the coordinate so that the drawing works
                    if direction == 'major_diagonal':
                        i, j = i-1, j-1
                    elif direction == 'minor_diagonal':
                        i, j = i-1, j+1
                    else:
                        raise Exception(f'Illegal direction: {direction}')

                if direction == 'horizontal':
                    for k in range(0, pl):
                        solution_grid[i, j+k] = pattern_str[k]
                elif direction == 'vertical':
                    for k in range(0, pl):
                        solution_grid[i+k, j] = pattern_str[k]
                elif direction == 'major_diagonal':
                    for k in range(0, pl):
                        solution_grid[i+k, j+k] = pattern_str[k]
                    # ''.join(solution_grid[i+k, j+k] for k in range(0, pl))
                elif direction == 'minor_diagonal':
                    for k in range(0, pl):
                        solution_grid[i+k, j-k] = pattern_str[k]
                    # ''.join(solution_grid[i-k, j-k] for k in range(0, pl))
                else:
                    raise Exception(f'Illegal direction: {direction}')

            solution_grid = '\n'.join(''.join(row) for row in solution_grid) # compact form - inner join connects elements of a 'row-list' by connecting with empty space (makes strings), outer row connects rows with newline
            return solution_grid

        if args.debug:
            print()
            print(draw_solution(nrows=nrows, ncols=ncols, match_list=match_list))


    print("Part2")
    # Idea: use Part 1 solution but change pattern to "MAS"
    # only major diagonal and moinor diagonal search is needed
    # save the coordinates of the central point A instead of the starting point: for major diagonal this means i+1, j+1
    # for minor diagonal i-1, j-1
    # in the match list, we need can only ever find diagonal matches, and a maximum of 2 diagonal matches with the same central coordinate (it doesn't matter if they are forward or backwards matches)
    # search match list for 2 matches that both have the same coordinate and where one is major and the other is minor diagonal
    # since there can be only one major and one minor diagonal passing through the central A coordinate, we don't need to check that one diagonal is major and one is minor, any two coordinates with the same diagonal will work
    # we can find recurring diagonal coordinates with a hashmap

    match_list = []

    cmmadf = count_matches_major_diagonal("MAS", part2=True)
    cmmadb = count_matches_major_diagonal("SAM", part2=True)
    cmmidf = count_matches_minor_diagonal("MAS", part2=True)
    cmmidb = count_matches_minor_diagonal("SAM", part2=True)

    # print(f"cmmadf: {cmmadf}")
    # print(f"cmmadb: {cmmadb}")
    # print(f"cmmidf: {cmmidf}")
    # print(f"cmmidb: {cmmidb}")

    if args.debug:
        print(match_list)

    hash_map_A_coordinates = {}
    for match in match_list:
        i, j, pattern_str, direction = match
        if (i, j) not in hash_map_A_coordinates: # new entry
            hash_map_A_coordinates[(i, j)] = 1
        else:
            hash_map_A_coordinates[(i, j)] += 1

    if args.debug:
        print()
        print(draw_solution(nrows=nrows, ncols=ncols, match_list=match_list, part2=True))
    
    print()    
    print("Part2")
    print(hash_map_A_coordinates.values())
    print(operator.countOf(hash_map_A_coordinates.values(), 2)) # count how often the dictionary has value 2: those are the central A,s that have MAS through it twice


if __name__ == "__main__":
    main()
