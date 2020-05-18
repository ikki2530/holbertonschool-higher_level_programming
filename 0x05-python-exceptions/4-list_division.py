#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            val = my_list_1[i] / my_list_2[i]
            new.append(val)
        except TypeError:
            new.append(0)
            print("{}".format("wrong dasdastype"))
        except ZeroDivisionError:
            new.append(0)
            print("{}".format("division by 0"))
        except IndexError:
            new.append(0)
            print("{}".format("out of range"))
        finally:
            pass
    return new
