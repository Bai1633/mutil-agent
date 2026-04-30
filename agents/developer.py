from agents.base import BaseAgent

class DeveloperAgent(BaseAgent):
    def code(self):
        arch = self.memory.get("architecture")
        result = self.run(f"Write code based on:\n{arch}")
        self.memory.save("code", result)
        return result
