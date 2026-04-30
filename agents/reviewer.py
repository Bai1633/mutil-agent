from agents.base import BaseAgent

class ReviewerAgent(BaseAgent):
    def review(self):
        code = self.memory.get("code")
        tests = self.memory.get("tests")

        return self.run(f"""
Review code quality and test coverage.

Code:
{code}

Tests:
{tests}

Return PASS or FAIL with reason.
""")
