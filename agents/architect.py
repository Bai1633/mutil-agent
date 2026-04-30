from agents.base import BaseAgent

class ArchitectAgent(BaseAgent):
    def design(self):
        tasks = self.memory.get("tasks")
        result = self.run(f"Design architecture based on:\n{tasks}")
        self.memory.save("architecture", result)
        return result
