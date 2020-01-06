from codonPython.sqlFileToDf import openSqlFile
import pytest

@pytest.mark.parametrize("path, expected_string", [
    ('test_utf8.sql',  'test'),
])
def test_open_sql_file(path, expected_string):
    output_string = openSqlFile(path)
    assert expected_string == output_string