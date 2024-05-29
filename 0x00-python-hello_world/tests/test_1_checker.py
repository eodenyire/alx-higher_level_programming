import unittest
import subprocess
import os

class TestTask1(unittest.TestCase):

    def test_shell_script_exists(self):
        try:
            subprocess.check_output(["./1-run_inline"])
            self.assertTrue(True)
        except FileNotFoundError:
            self.fail("Shell script './1-run_inline' not found")

    def test_shell_script_execution(self):
        try:
            output = subprocess.check_output(["./1-run_inline"]).decode().strip()
            self.assertEqual(output, "Best School: 98")
        except subprocess.CalledProcessError:
            self.fail("Error occurred while executing shell script")

    def test_script_has_correct_shebang(self):
        try:
            with open("1-run_inline", "r") as file:
                first_line = file.readline().strip()
                self.assertTrue(first_line.startswith("#!/bin/bash"),
                                msg="First line does not contain correct shebang")
        except FileNotFoundError:
            self.fail("Script file '1-run_inline' not found")

    def test_script_is_two_lines_long(self):
        try:
            with open("1-run_inline", "r") as file:
                lines = file.readlines()
                self.assertEqual(len(lines), 2, msg="Script does not have exactly 2 lines")
        except FileNotFoundError:
            self.fail("Script file '1-run_inline' not found")

    def test_python_code_execution(self):
        try:
            pycode = 'print(f"Best School: {88+10}")'
            output = subprocess.check_output(["bash", "-c", f"export PYCODE='{pycode}' && ./1-run_inline"]).decode().strip()
            self.assertEqual(output, "Best School: 98")
        except subprocess.CalledProcessError:
            self.fail("Error occurred while executing Python code")

if __name__ == '__main__':
    unittest.main()
