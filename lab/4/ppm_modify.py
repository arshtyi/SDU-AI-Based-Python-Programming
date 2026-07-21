from math import sqrt


def decode(in_filename, out_filename):
    """Decode the body of a PPM image into a new PPM file.

    Args:
        in_filename (str): The name of the encoded input PPM file.
        out_filename (str): The name of the decoded output PPM file.

    Returns:
        None: The decoded image is written to ``out_filename``.
    """
    with open(in_filename, "r") as input_file, open(out_filename, "w") as output_file:
        # A PPM header consists of its encoding, dimensions, and maximum value.
        for _ in range(3):
            output_file.write(input_file.readline())

        # Decode each remaining value according to its remainder modulo three.
        decoded_values = ("0", "153", "255")
        for line in input_file:
            numbers = line.split()
            decoded_line = []
            for number in numbers:
                decoded_line.append(decoded_values[int(number) % 3])
            output_file.write(" ".join(decoded_line) + "\n")


def main_part1():
    """Decode the Part 1 image and save it in the files subdirectory.

    Returns:
        None: ``files/part1_out.ppm`` is created by calling ``decode``.
    """
    decode("files/part1.ppm", "files/part1_out.ppm")


def negate(line):
    """Negate every color component in one line of PPM image data.

    Args:
        line (str): Integers from 0 through 255 separated by whitespace.

    Returns:
        str: The same number of components, each replaced by 255 minus its
        original value and separated by single spaces.
    """
    numbers = line.split()
    negated_numbers = []

    for number in numbers:
        negated_numbers.append(str(255 - int(number)))

    return " ".join(negated_numbers)


def grey_scale(line):
    """Convert every RGB pixel in one line of PPM data to grey scale.

    Args:
        line (str): Groups of three RGB integers from 0 through 255,
        separated by whitespace.

    Returns:
        str: The grey-scaled RGB components separated by single spaces. Each
        pixel's three components equal the truncated RGB magnitude, capped at
        255.
    """
    numbers = line.split()
    grey_numbers = []

    for index in range(0, len(numbers), 3):
        red = int(numbers[index])
        green = int(numbers[index + 1])
        blue = int(numbers[index + 2])
        grey = int(sqrt(red**2 + green**2 + blue**2))
        grey = min(grey, 255)
        grey_numbers.extend([str(grey), str(grey), str(grey)])

    return " ".join(grey_numbers)


def remove_color(line, color):
    """Remove one color channel from every pixel in a line of PPM data.

    Args:
        line (str): Groups of three RGB integers from 0 through 255,
        separated by whitespace.
        color (str): The channel to remove: ``"red"``, ``"green"``, or
        ``"blue"``.

    Returns:
        str: The RGB components separated by single spaces, with every value
        in the selected channel replaced by zero.
    """
    numbers = line.split()
    color_positions = {"red": 0, "green": 1, "blue": 2}
    position_to_remove = color_positions[color]

    for index in range(position_to_remove, len(numbers), 3):
        numbers[index] = "0"

    return " ".join(numbers)


def main():
    """Prompt for a PPM file and write the requested modified image.

    The user selects negation, grey scale, or removal of one RGB channel.
    Invalid modification choices are rejected until a valid number is given.

    Returns:
        None: The modified PPM image is written to the requested output file.
    """
    input_filename = input("input file name:\n")
    output_filename = input("output file name:\n")

    print("modifications are:")
    print("  1. negate")
    print("  2. greyscale")
    print("  3. remove red")
    print("  4. remove green")
    print("  5. remove blue")

    choice = input("enter the number of the desired modification\n")
    while choice not in ("1", "2", "3", "4", "5"):
        print("please enter a valid number")
        choice = input("enter the number of the desired modification\n")

    with (
        open(input_filename, "r") as input_file,
        open(output_filename, "w") as output_file,
    ):
        # Copy the PPM header without changing it.
        for _ in range(3):
            output_file.write(input_file.readline())

        for line in input_file:
            if choice == "1":
                modified_line = negate(line)
            elif choice == "2":
                modified_line = grey_scale(line)
            else:
                colors = {"3": "red", "4": "green", "5": "blue"}
                modified_line = remove_color(line, colors[choice])

            output_file.write(modified_line + "\n")

    print("done")


if __name__ == "__main__":
    main()
