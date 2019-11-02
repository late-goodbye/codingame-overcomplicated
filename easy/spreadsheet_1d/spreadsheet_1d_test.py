import unittest
from easy.spreadsheet_1d.spreadsheet_1d import Spreadsheet


class TestSpreadsheet(unittest.TestCase):
    def test_simple_dependency(self):

        input_data = '''
            2
            VALUE 3 _
            ADD $0 4
        '''
        expected_output = '''
            3
            7
        '''
        expected_output = [
            int(x) for x in map(str.strip, expected_output.split('\n')) if x]

        spreadsheet = Spreadsheet(input_data)
        for cell_value, expected_value in zip(spreadsheet, expected_output):
            self.assertEqual(cell_value, expected_value)


if __name__ == '__main__':
    unittest.main()
