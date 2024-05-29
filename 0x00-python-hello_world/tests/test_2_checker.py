import unittest
import subprocess

class TestTask2(unittest.TestCase):

    def test_script_exists(self):
        try:
            subprocess.check_output(["./2-print.py"])
            self.assertTrue(True)
        except FileNotFoundError:
            self.fail("Script './2-print.py' not found")

    def test_script_output(self):
        try:
            output = subprocess.check_output(["./2-print.py"]).decode().strip()
            expected_output = '"Programming is like building a multilingual puzzle'  # Updated
            self.assertEqual(output, expected_output)
        except subprocess.CalledProcessError:
            self.fail("Error occurred while executing script")

    def test_shebang_exists(self):
        try:
            with open("2-print.py", "r") as file:
                first_line = file.readline().strip()
                self.assertTrue(first_line.startswith("#!/usr/bin/python3"),
                                msg="First line does not contain correct shebang")
        except FileNotFoundError:
            self.fail("Script file '2-print.py' not found")

    def test_pep8_validation(self):
        try:
            subprocess.check_output(["pycodestyle", "2-print.py"])
            self.assertTrue(True)
        except subprocess.CalledProcessError:
            self.fail("PEP8 validation failed")

if __name__ == '__main__':
    unittest.main()
