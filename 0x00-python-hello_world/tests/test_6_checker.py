import unittest
import subprocess

class TestScript(unittest.TestCase):
    
    def test_script_output(self):
        process = subprocess.Popen(["./6-concat.py"], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.decode().strip()
        expected_output = "Welcome to Holberton School!"
        self.assertEqual(output, expected_output)

    def test_first_line_contains_shebang(self):
        with open("6-concat.py", "r") as file:
            first_line = file.readline().strip()
            self.assertTrue(first_line.startswith("#!/usr/bin/python3"))

    def test_no_loops_or_conditionals_used(self):
        with open("6-concat.py", "r") as file:
            script_content = file.read()
            self.assertFalse("for" in script_content or "while" in script_content)
            self.assertFalse("if" in script_content or "else" in script_content)

    def test_script_has_correct_number_of_lines(self):
        with open("6-concat.py", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 5)

    def test_str1_and_str2_used(self):
        with open("6-concat.py", "r") as file:
            script_content = file.read()
            self.assertTrue("str1" in script_content)
            self.assertTrue("str2" in script_content)

    def test_pycodestyle_validation(self):
        import pycodestyle
        style = pycodestyle.StyleGuide()
        result = style.check_files(["6-concat.py"])
        self.assertEqual(result.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
