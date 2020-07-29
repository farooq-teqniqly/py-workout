from typing import List


def average(values: List[float], decimal_places=2) -> float:
    if not values:
        raise ValueError("average() needs at least one value")

    return round(sum(values) / len(values), decimal_places)


def main():
    input_str = None
    values: List[float] = []

    while input_str != "":
        input_str = input("Enter 10km run time in seconds: ")

        if input_str == "":
            break

        try:
            values.append(float(input_str))
        except ValueError:
            print("Enter a number!")
            continue

    if not values:
        print("Goodbye!")
    else:
        print(f"Average of {average(values)} over {len(values)} runs.")


if __name__ == "__main__":
    main()
