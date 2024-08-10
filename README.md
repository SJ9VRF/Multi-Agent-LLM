# Multi-Agent LLM

![Screenshot_2024-08-10_at_11 24 29_AM-removebg-preview](https://github.com/user-attachments/assets/d00da3cb-aed8-4071-9bd9-7ef5e263ade2)


## Project Overview
This project implements a multi-document agent using the LlamaIndex framework. It is designed to manage document-specific agents that can perform QA and summarization tasks within individual documents, as well as a top-level agent that orchestrates queries across these document agents.

## Features
- **Document-Specific Query Handling:** Each document has a dedicated agent capable of answering queries specific to its content.
- **Top-Level Query Orchestration:** A top agent manages interactions across multiple document agents.
- **Reranking and Query Planning:** Utilizes advanced features like reranking during document retrieval and dynamic query planning for efficient information retrieval.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llamaindex-multi-document-agent.git
   cd llamaindex-multi-document-agent
   ```

2. Install dependencies::
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the agent, navigate to the project directory and execute:
   ```bash
 python main.py
   ```

## Configuration
Modify the src/config.py to set the necessary API keys and parameters.
