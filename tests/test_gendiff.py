from gendiff.gendiff import generate_diff

def test_gendiff():
    assert generate_diff('file1.json', 'file2.json') == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff('file1.json', 'file1.json') == '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
