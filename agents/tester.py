from agents.base import BaseAgent

class TesterAgent(BaseAgent):
    def test(self):
        code = self.memory.get("code")
        result = self.run(f"Generate test cases:\n{code}")
        self.memory.save("tests", result)
        return result
