import pytest
import chain

def test_it_works():
    assert chain.chain("tip", "top") == ["tip", "top"]

def test_same_word():
    assert chain.chain("top", "top") == ["top"]

@pytest.mark.parametrize("start, target, exception", (
    ("awef", "loop", "awef"),
    ("loop", "qwer", "qwer"),
    ("awef", "qwer", "awef"),
))
def test_non_english_words(start, target, exception):
    with pytest.raises(chain.InvalidWord, match=exception):
        chain.chain(start, target)

def test_next_words_no_options():
    assert chain.next_words("tip", {"cat"}) == set()

def test_next_words_one_option():
    assert chain.next_words("tip", {"top", "cat"}) == {"top"}

def test_next_words_different_lengths():
    assert chain.next_words("tip", {"sips"}) == set()

def test_it_works_short_chain():
    assert chain.chain("cat", "cog") == ["cat", "cot", "cog"]