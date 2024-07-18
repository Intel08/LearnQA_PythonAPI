class TestEx10:
    def test_check_len(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) <15, f"Допустимое количство символов превышено"



