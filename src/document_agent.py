# Defines the DocumentAgent class.
class DocumentAgent:
    def __init__(self, document, agent_info):
        self.document = document
        self.agent = agent_info['agent']
        self.summary = agent_info['summary']

    def answer_query(self, query):
        # Implement a method to use the embedded agent for answering questions specific to this document
        response = self.agent.answer_query(query)
        return response
