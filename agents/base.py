from llm.client import call_llm

class BaseAgent:
    def __init__(self, role, memory):
        self.role = role
        self.memory = memory

    def run(self, task):
        context = str(self.memory.all())

        prompt = f"""
Context:
{context}

Task:
{task}
"""
        return call_llm(self.role, prompt)
