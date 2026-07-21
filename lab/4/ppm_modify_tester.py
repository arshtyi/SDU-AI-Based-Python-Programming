"""Test cases for the PPM image modification functions."""

from ppm_modify import grey_scale, negate, remove_color


def main():
    """Run thorough assertion-based tests for the three line modifiers."""
    print("*** testing negate ***")
    assert negate("1 2 3 200 100 150") == "254 253 252 55 155 105"
    assert negate("0 0 0 255 255 255") == "255 255 255 0 0 0"
    assert negate("10\t20  30\n40 50 60") == "245 235 225 215 205 195"
    assert negate("") == ""
    print("negate passed")

    print("*** testing grey_scale ***")
    assert grey_scale("1 2 3 200 100 150") == "3 3 3 255 255 255"
    assert grey_scale("0 0 0 3 4 0") == "0 0 0 5 5 5"
    assert grey_scale("255\t255\t255") == "255 255 255"
    assert grey_scale("2 2 1 1 1 1") == "3 3 3 1 1 1"
    assert grey_scale("") == ""
    print("grey_scale passed")

    print("*** testing remove_color ***")
    sample = "1 2 3 200 100 150"
    assert remove_color(sample, "red") == "0 2 3 0 100 150"
    assert remove_color(sample, "green") == "1 0 3 200 0 150"
    assert remove_color(sample, "blue") == "1 2 0 200 100 0"
    assert remove_color("0\t255  86 47 55 255", "green") == (
        "0 0 86 47 0 255"
    )
    assert remove_color("", "red") == ""
    print("remove_color passed")


if __name__ == "__main__":
    main()
