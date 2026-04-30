from agents.base import BaseAgent

class PMAgent(BaseAgent):
    def analyze(self, req):
        result = self.run(f"Break requirement into tasks:\n{req}")
        self.memory.save("tasks", result)
        return result
