from gendiff.generate_diff import generate_diff


test_data = [('tests/test_data/file1.json', 'tests/test_data/file2.json'), ('tests/test_data/file1.yaml', 'tests/test_data/file2.yml')]


def test_generate_diff():
    for f in test_data:
        file1, file2 = f
        with open('tests/test_data/result_flat.txt', 'r') as f:
            result = f.read().strip()
        assert generate_diff(file1, file2) == result
        
        
test_data2 = [('tests/test_data/file1_rec.json', 'tests/test_data/file2_rec.json'), ('tests/test_data/file1_rec.yaml', 'tests/test_data/file2_rec.yml')]


def test_generate_diff2():
    for f in test_data2:
        file1, file2 = f
        with open('tests/test_data/result_rec.txt', 'r') as f:
            result = f.read().strip()
        assert generate_diff(file1, file2) == result
