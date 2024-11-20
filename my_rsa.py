from prime_generator import generate_primes


def generate_closed_exponent(euler):
    return 0
def generate_open_exponent(euler):
    return 0

# Returns dict {public: public_key, private: private_key}
def generate_keys():
    p, q = generate_primes()
    n = p * q
    euler = (p - 1) * (q - 1)
    e = generate_open_exponent(euler)
    d = generate_closed_exponent(euler)
    keys = {"public": (e, n), "private": (d, n)}
    return keys


if __name__ == "__main__":
    public, private = generate_keys().values()
    print(public)
    print(private)