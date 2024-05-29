import unittest
import subprocess

class TestTask7(unittest.TestCase):
    
    def test_script_output(self):
        # Run the script and capture its output
        process = subprocess.Popen(["./7-edges.py"], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.decode().strip()

        # Define the expected output
        expected_output = """First 3 letters: Hol
Last 2 letters: on
Middle word: olberto"""

        # Assert that the output matches the expected output
        self.assertEqual(output, expected_output)

    def test_first_line_contains_shebang(self):
        with open("7-edges.py", "r") as file:
            first_line = file.readline().strip()
            self.assertTrue(first_line.startswith("#!/usr/bin/python3"))

    def test_no_loops_or_conditionals_used(self):
        with open("7-edges.py", "r") as file:
            script_content = file.read()
            self.assertFalse("for" in script_content or "while" in script_content)
            self.assertFalse("if" in script_content or "else" in script_content)

    def test_script_has_correct_number_of_lines(self):
        with open("7-edges.py", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 8)

    def test_pycodestyle_validation(self):
        import pycodestyle
        style = pycodestyle.StyleGuide()
        result = style.check_files(["7-edges.py"])
        self.assertEqual(result.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
