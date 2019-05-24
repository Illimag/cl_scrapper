with open("../test_run/duplicates_test.txt", "r") as f:

    a=list(set(f))

    for val in a:
        test = val.rstrip('\r\n')
        print test