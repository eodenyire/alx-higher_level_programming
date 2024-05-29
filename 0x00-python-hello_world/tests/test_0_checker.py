import unittest
import subprocess

class TestTask0(unittest.TestCase):

    def test_shell_script_exists(self):
        try:
            subprocess.check_output(["./0-run"])
            self.assertTrue(True)
        except FileNotFoundError:
            self.fail("Shell script './0-run' not found")

    def test_shell_script_execution(self):
        try:
            output = subprocess.check_output(["./0-run"]).decode().strip()
            self.assertEqual(output, "Best School")
        except subprocess.CalledProcessError:
            self.fail("Error occurred while executing shell script")

    def test_readme_exists_and_not_empty(self):
        try:
            with open("README.md", "r") as file:
                content = file.read().strip()
                self.assertTrue(len(content) > 0, msg="README.md is empty")
        except FileNotFoundError:
            self.fail("README.md file not found")

    def test_script_has_correct_shebang(self):
        try:
            with open("0-run", "r") as file:
                first_line = file.readline().strip()
                self.assertTrue(first_line.startswith("#!/bin/bash"),
                                msg="First line does not contain correct shebang")
        except FileNotFoundError:
            self.fail("Script file '0-run' not found")

    def test_script_is_two_lines_long(self):
        try:
            with open("0-run", "r") as file:
                lines = file.readlines()
                self.assertEqual(len(lines), 2, msg="Script does not have exactly 2 lines")
        except FileNotFoundError:
            self.fail("Script file '0-run' not found")

if __name__ == '__main__':
    unittest.main()
