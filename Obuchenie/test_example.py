class TestExample:
    def test_check_math(self):
        a = 10
        b = 15
        expected_sum = 25
        assert a+b == expected_sum, f"Sum of variables a and b not equal to {expected_sum}"

    def test_check_math2(self):
        a = 1
        b = 15
        expected_sum = 25
        assert a+b == expected_sum, f"Sum of variables a and b not equal to {expected_sum}"