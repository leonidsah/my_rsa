import pytest
import prime_generator


def setup_module(module):
    #init_something()
    pass


def teardown_module(module):
    #teardown_something()
    pass


def test_get_probably_prime():
    assert prime_generator.get_probably_prime(1024) != 0
