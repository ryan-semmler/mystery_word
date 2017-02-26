import mystery_word

def test_valid():
    assert mystery_word.valid_test('ab') == "too long"
    assert mystery_word.valid_test('5') == 'not letter'
    assert mystery_word.valid_test('X') == True
    assert mystery_word.valid_test('x') == True
