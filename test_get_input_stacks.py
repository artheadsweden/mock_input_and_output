from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from Stacks import get_input_stacks, print_greeting


class TestGetInputStacks(TestCase):
    def test_get_input_stacks1(self):
        user_input = [
            '3',
            '4 1 2 3 2',
            '1 2',
            '0',
        ]

        expected_stacks = [
            [1, 2, 3, 2],
            [2],
            [],
        ]

        with patch('builtins.input', side_effect=user_input):
            stacks = get_input_stacks()
        self.assertEqual(stacks, expected_stacks)


    def test_get_input_stacks2(self):
        user_input = [
            '3',
            '4 1 2 3 2 6',
            '1 2',
            '0',
        ]

        expected_stacks = [
            [1, 2, 3, 2],
            [2],
            [],
        ]

        with patch('builtins.input', side_effect=user_input):
            stacks = get_input_stacks()
        self.assertEqual(stacks, expected_stacks)

    def test_get_multiple_input_stacks1(self):
        user_inputs = [
            [
                '4',
                '2 1 2',
                '7 1 2 3 4 5 6 7 8',
                '3 1 3 5',
                '1 6'
            ],
            [
                '1',
                '6 6 5 4 3 2 1',
            ]
        ]

        expected_stacks = [
            [
                [1, 2],
                [1, 2, 3, 4, 5, 6, 7],
                [1, 3, 5],
                [6],
            ],
            [
                [6, 5, 4, 3, 2, 1]
            ]
        ]
        test_no = 0
        for user_input in user_inputs:
            with patch('builtins.input', side_effect=user_input):
                stacks = get_input_stacks()
            self.assertEqual(stacks, expected_stacks[test_no])
            test_no += 1

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_greeting(self, mock_stdout):
        print_greeting("Billy Bob")
        self.assertEqual("Hi Billy Bob\n", mock_stdout.getvalue())