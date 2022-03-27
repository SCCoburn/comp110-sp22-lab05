"""
Module: comp110_lab05

Exercises from lab 05, dealing with strings and file reading.
"""

"from fcntl import F_GETLEASE"


def max_wind_speed(hurricane_filename):
    """
    Finds the maximum wind speed for the hurricane.

    Parameters:
    1. hurricane_filename (type: string) - Name of the file containing the data

    Returns:
    (type: int) The maximum wind speed of the hurricane.
    """
    max_speed = 0
    my_file = open(hurricane_filename, 'r')
    for line in my_file:
        vals = line.split(',')
        if int(vals[4]) > max_speed:
            max_speed = int(vals[4])
    my_file.close()
    return max_speed
    

        

def contains_word(word, review):
    """
    Determines whether the review contains the given word. 

    Note that should ignore the "casing" of letters. For example "ok" is
    considered to be contained in the review "It was an OK movie."

    Parameters:
    1. word (type: string): The word to search for.
    2. review (type: string): The review in which to search.

    Returns:
    (type: boolean) True if word is contained in the review, and false
    otherwise.
    """

    pass # replace this line with your implementation of this function


def test_max_wind_speed():
    """ Function that tests the max_wind_speed function. """

    print("Starting test of max_wind_speed")
    max_wind_speed("dorian.csv")
    if max_wind_speed ("dorian.csv") == 185 :
        print("max_wind_speed(dorian.csv) PASSED")
    else:
        print("max_wind_speed(dorian.csv) FAILED")
    max_wind_speed("florence.csv")
    if max_wind_speed("florence.csv") == 140 :
        print("max_wind_speed(florence.csv) PASSED")
    else:
        print("max_wind_speed(florence.csv) FAILED")
    max_wind_speed("irma.csv")
    if max_wind_speed("irma.csv") == 185:
        print("max_wind_speed(irma.csv) PASSED")
    else:
        print("max_wind_speed(irma.csv) FAILED")
    

    # To Do: Call your max_wind_speed function on the irma.csv file, using an if
    # statement to indicate whether the result was correct or not.
    # Then repeat the process for the florence.csv and dorian.csv files to check
    # whether your function works for those files.

   

    print("Done testing max_wind_speed")


def test_contains_word():
    """ Function that tests the contains_word function. """

    print("\nStarting test of contains word")

    if contains_word('ok', 'ok') != True:
        print("FAILED: contains_word('ok', 'ok')")
    elif contains_word('ok', 'OK') != True:
        print("FAILED: contains_word('ok', 'OK')")
    elif contains_word('ok', 'bad') != False:
        print("FAILED: contains_word('ok', 'bad')")
    elif contains_word('ok', 'movie ok') != True:
        print("FAILED: contains_word('ok', 'movie ok')")
    # To Do: update the chained conditional to test all of your new test cases.
    else:
        print("All contains_word test cases passed!")


    print("Done testing contains word")


def main():
    """ Calls the tester functions in the code. """
    test_max_wind_speed()
    test_contains_word()

# Do not modify anything after this point.
if __name__ == "__main__":
    main()