# Sources:
# https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python

if __name__ == "__main__":
    # declare our two strings.
    the_first_string = "hello"
    the_second_string = "world"

    # The easy way
    combined_string = the_first_string + " " + the_second_string
    print(combined_string)

    # with the % operator
    combined_string = "%s %s" % (the_first_string, the_second_string)
    print(combined_string)
    # I personally like this way. It is easy to use and for me I immediately know what is happening.

    # with .format()
    combined_string = "{} {}".format(the_first_string, the_second_string)
    print(combined_string)




