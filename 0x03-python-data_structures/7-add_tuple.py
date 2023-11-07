#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    f_a = tuple_a[0] if len(tuple_a) > 0 else 0
    s_a = tuple_a[1] if len(tuple_a) > 1 else 0
    f_b = tuple_b[0] if len(tuple_b) > 0 else 0
    s_b = tuple_b[1] if len(tuple_b) > 1 else 0
    f_n = f_a + f_b
    s_n = s_a + s_b
    new_tuple = (f_n, s_n)
    return new_tuple
