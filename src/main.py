# Entry point to setup and run the agents.
from src.document_agent import DocumentAgent
from src.top_level_agent import TopLevelAgent
from src.data_loader import DataLoader

def main():
    data_loader = DataLoader()
    documents, agents_info = data_loader.load_and_process_docs()

    agents = [DocumentAgent(doc, info) for doc, info in zip(documents, agents_info)]
    top_agent = TopLevelAgent(agents)
    top_agent.answer_query("What types of agents are available in LlamaIndex?")

if __name__ == "__main__":
    main()
