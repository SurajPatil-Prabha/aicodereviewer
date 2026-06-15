import subprocess
import ast


class CodeReviewer:

    def syntax_check(self, filename):
        try:
            with open(filename, "r") as file:
                ast.parse(file.read())

            return "✅ No Syntax Errors Found"

        except Exception as error:
            return f"❌ Syntax Error: {error}"

    def review(self, filename):

        result = subprocess.run(
            ["pylint", filename],
            capture_output=True,
            text=True
        )

        return result.stdout

    def metrics(self, filename):

        with open(filename, "r") as file:
            lines = file.readlines()

        return len(lines)