import pytest
import my_rsa


def setup_module(module):
    #init_something()
    pass


def teardown_module(module):
    #teardown_something()
    pass


def test_generate_keys():
    n = 1024
    public, private = my_rsa.generate_keys(n).values()
    assert public[1] != 0
    assert private[1] != 0
