from gendiff.generate_diff import generate_list, generate_diff, parse

def test_generate_list():
    file1 = parse('tests/test_data/file1.json')
    file2 = parse('tests/test_data/file2.json')
    file3 = generate_diff(file1, file2)
    with open('tests/test_data/result_json.txt', 'r') as f:
        result = f.read().strip()
    assert generate_list(file3) == result
