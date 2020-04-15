def add_all(cargo1, cargo2, cargo3, double=True):
    """
    Takes three arguments, sums them up, adds 2 and returns the result.

    If double is True, the result is doubled.
    """
    res = cargo1 + cargo2 + cargo3 # sum() could be faster

    if double is True:
        res = res * 2

    else:
        res = res + 2  # TODO: Maybe use elif and check explicitely

    return res


if __name__ == '__main__':
    # Define some data
    bananas, apples, milk = 4, 6, 12

    # Test if the function terminates
    add_all(bananas, apples, milk, double=False)

    # Look at the cargo and evaluate the function
    print(bananas, apples, milk)

    res = add_all(bananas, apples, milk, double=False)
    print(res)
