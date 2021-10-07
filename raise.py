#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program tells you if you are eligible for a raise


def main():
    # this function is the program

    # input
    number_of_years_as_string = input(
        "How many years have you been an employee at your company : "
    )

    # process & output
    try:
        number_of_years = int(number_of_years_as_string)
        if number_of_years >= 5:
            salary_as_string = input("Please enter your yearly salary (CAD $) : ")
            salary = int(salary_as_string)
            increase = 0.05 * salary
            print(
                "Congratulations, you are eligible for a ${0} raise!".format(increase)
            )
        else:
            remainder = 5 - number_of_years
            print(
                "Sorry, in {0} years you will be able to receive a 5% raise.".format(
                    remainder
                )
            )
    except Exception:
        print("Invalid number entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
