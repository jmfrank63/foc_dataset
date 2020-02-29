import pytest
from create_dataset import *

CONTENT = """TEXT This is the header
1 This is the first line
2 This is the second line
3 This is the third line
4 This is his(her) text of crappy words
5 Here are 10000 words
6 Should and Shouldn't care"""


@pytest.fixture
def text_dict(tmp_path):
    directory = tmp_path / "sub"
    directory.mkdir()
    filename = 'text.txt'
    file_path = directory / filename
    file_path.write_text(CONTENT)
    text_dict = read_to_dict(file_path)
    return text_dict


def test_create_file(tmp_path):
    directory = tmp_path / "sub"
    directory.mkdir()
    filename = 'text.txt'
    file_path = directory / filename
    file_path.write_text(CONTENT)
    text_dict = read_to_dict(file_path)
    assert file_path.read_text() == CONTENT
    assert len(text_dict) == len(CONTENT.split('\n'))
    assert text_dict[3] == tuple('This is the third line'.split(' '))


def test_encode_letter():
    assert encode_letter('a') == 1
    assert encode_letter('Z') == 26


def test_encode_name():
    assert encode_name('A') == 1
    assert encode_name('abcdefgh') == 36
    assert encode_name('abcd efgh') == 36


def test_get_position_and_line_number():
    assert get_position_and_line_number(59) == (0, 60)
    assert get_position_and_line_number(99) == (0, 100)
    assert get_position_and_line_number(100) == (4, 1)
    assert get_position_and_line_number(136) == (4, 37)
    assert get_position_and_line_number(800) == (9, 1)
    assert get_position_and_line_number(999) == (9, 100)


def test_make_data_set(text_dict):
    assert make_data_set(0, 1, text_dict,
                         4) == ['this', 'firs', 'line', 'seco']
    assert make_data_set(4, 1, text_dict,
                         4) == ['line', 'this', 'seco', 'thir']
    assert make_data_set(0, 2, text_dict,
                         4) == ['this', 'seco', 'line', 'thir']
    assert make_data_set(9, 2, text_dict,
                         5) == ['this', 'thir', 'line', 'text', 'crap']
    assert make_data_set(0, 5, text_dict, 2) == ['here', 'word']
    assert make_data_set(0, 6, text_dict, 2) == ['shou', 'care']
