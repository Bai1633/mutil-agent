from core.memory import Memory
from agents.pm import PMAgent
from agents.architect import ArchitectAgent
from agents.developer import DeveloperAgent
from agents.tester import TesterAgent
from agents.reviewer import ReviewerAgent
from agents.devops import DevOpsAgent
from config import MAX_RETRY

class Orchestrator:

    def __init__(self):
        self.memory = Memory()
        self.pm = PMAgent("Product Manager", self.memory)
        self.arch = ArchitectAgent("Architect", self.memory)
        self.dev = DeveloperAgent("Developer", self.memory)
        self.test = TesterAgent("Tester", self.memory)
        self.rev = ReviewerAgent("Reviewer", self.memory)
        self.ops = DevOpsAgent("DevOps", self.memory)

    def run(self, requirement):

        self.pm.analyze(requirement)
        self.arch.design()

        for _ in range(MAX_RETRY):
            self.dev.code()
            self.test.test()
            review = self.rev.review()

            if "PASS" in review:
                break
            else:
                self.memory.save("feedback", review)

        deployment = self.ops.deploy()

        return {
            "memory": self.memory.all(),
            "deployment": deployment
        }
