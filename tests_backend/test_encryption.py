def test_random_string_generation_length():
    from backend import helpers
    testing_len = 1000000
    r = helpers.generate_cryptographically_random_string(testing_len)
    assert len(r) == testing_len