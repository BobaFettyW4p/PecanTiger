import sys
sys.path.insert(0,'./app/')

import string, pytest, gutenbergpy.textget, GetNovelText


@pytest.fixture
def sample_text():
    book = gutenbergpy.textget.get_text_by_id(890)
    return book

@pytest.fixture
def sample_dictionary():
    book = GetNovelText.get_book(890)
    final_book = GetNovelText.clean_book(book)
    return final_book

def test_get_book(sample_text):
    assert type(GetNovelText.get_book(890)) is bytes

def test_clean_book_type(sample_text):
    assert type(GetNovelText.clean_book(sample_text)) is list

def test_clean_book_word_length(sample_text):
    book = GetNovelText.clean_book(sample_text)
    valid = True
    for page in book:
        if len(page) < 4:
            valid = False
            break
    assert valid == True

def test_capitalizaton_clean_book(sample_text):
    book = GetNovelText.clean_book(sample_text)
    valid = True
    for page in book:
        if page[0] in string.ascii_lowercase:
            valid = False
            break
    assert valid

def test_clean_book_word_length(sample_text):
    book = GetNovelText.clean_book(sample_text)
    valid = True
    for word in book:
        if len(word) <= 3:
            valid = False
            break
    assert valid

def test_clean_book_uniqueness(sample_text):
    book = GetNovelText.clean_book(sample_text)
    valid = True
    for word in book:
        if book.count(word) != 1:
            valid = False
            break
    assert valid

def test_generate_password_candidates(sample_dictionary):
    PASSWORD_LENGTH = 20
    candidates = GetNovelText.generate_password(sample_dictionary,PASSWORD_LENGTH)
    assert len(candidates) == 5
