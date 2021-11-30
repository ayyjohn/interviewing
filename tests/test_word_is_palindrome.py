from interviewing.questions import word_is_palindrome
import string


def test_empty_string():
    word = ""
    assert word_is_palindrome(word) is True


def test_all_single_character_words():
    for word in string.ascii_letters:
        assert word_is_palindrome(word) is True


def test_case_doesnt_matter():
    word = "Bib"
    assert word_is_palindrome(word) is True


def test_odd_number_of_letters():
    word = "lol"
    assert word_is_palindrome(word) is True


def test_even_number_of_letters():
    word = "peep"
    assert word_is_palindrome(word) is True


def test_failure_case():
    word = "notapalindrome"
    assert word_is_palindrome(word) is False
