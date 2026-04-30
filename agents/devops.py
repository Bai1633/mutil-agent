from agents.base import BaseAgent

class DevOpsAgent(BaseAgent):
    def deploy(self):
        arch = self.memory.get("architecture")
        return self.run(f"Deployment strategy:\n{arch}")
