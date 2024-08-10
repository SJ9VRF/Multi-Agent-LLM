# Defines the TopLevelAgent class.
class TopLevelAgent:
    def __init__(self, document_agents):
        self.document_agents = document_agents

    def answer_query(self, query):
        # A method to manage queries across multiple document agents
        print(f"Query: {query}")
        for agent in self.document_agents:
            response = agent.answer_query(query)
            print(f"Document: {agent.document.metadata['path']} Response: {response}")
