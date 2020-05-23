import time


if __name__ == "__main__":
    # declare our two strings.
    the_first_string = "hello"
    the_second_string = "world"
    LOOP_COUNT = 300000

    first_test_start_time = time.time()
    for i in range(LOOP_COUNT):
        # The easy way
        combined_string = the_first_string + " " + the_second_string
    first_test_end_time = time.time()
    print("first test")
    print(first_test_end_time-first_test_start_time)

    second_test_start_time = time.time()
    for i in range(LOOP_COUNT):
        # with the % operator
        combined_string = "%s %s" % (the_first_string, the_second_string)
        # I personally like this way. It is easy to use and for me I immediately know what is happening.
    second_test_end_time = time.time()
    print("second test")
    print(second_test_end_time-second_test_start_time)

    third_test_start_time = time.time()
    for i in range(LOOP_COUNT):
        # with .format()
        combined_string = "{} {}".format(the_first_string, the_second_string)
    third_test_end_time = time.time()
    print("third test")
    print(third_test_end_time-third_test_start_time)

    fourth_test_start_time = time.time()
    for i in range(LOOP_COUNT):
        # with the .join method
        combined_string = "".join([the_first_string, ' ', the_second_string])
        # I find this the least readable format. I do not recommend this.
        # Unless dumping a list to string, this could be useful.
    fourth_test_end_time = time.time()
    print("fourth test")
    print(fourth_test_end_time-fourth_test_start_time)

    fifth_test_start_time = time.time()
    for i in range(LOOP_COUNT):
        # with f"{variable}"
        combined_string = f'{the_first_string} {the_second_string}'
        # I actually came across this while making this script and I also like this.
    fifth_test_end_time = time.time()
    print("fifth test")
    print(fifth_test_end_time-fifth_test_start_time)