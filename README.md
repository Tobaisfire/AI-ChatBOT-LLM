
# Project Description: LLM Chatbot with Cohere Embedding and Langchain Framework

This repository contains a comprehensive implementation of an advanced chatbot using the LLM (Large Language Model) OpenAI, Cohere embedding, and the Langchain framework. The project focuses on vector embedding of Wikipedia articles in English, leveraging Cohere to perform efficient embedding. Additionally, it utilizes Langchain to establish connections between Cohere and Wevaite vector database, enabling seamless integration and retrieval of Wiki embeddings.

## Features:
- **Vector Embedding**: The project employs Cohere embedding to generate vector representations of Wikipedia articles in English. This enables efficient storage and retrieval of semantic information.
- **Langchain Integration**: Langchain framework is utilized to connect Cohere and Wevaite vector database. This integration streamlines the process of pushing and pulling Wiki embeddings, ensuring optimal performance and retrieval efficiency.
- **Semantic Search and QA Retrieval**: By leveraging Langchain and Wevaite, the chatbot performs semantic search and question-answering retrieval. It retrieves relevant information based on user queries and provides contextually appropriate responses.
- **LLM GPT 3.5 Turbo**: The chatbot utilizes the powerful LLM GPT 3.5 Turbo from OpenAI to enhance the conversational experience. It takes context from semantic search results and generates responses based on the retrieved information.
- **Chat History With MONGO DB**: he chatbot utilizes MongoDb to Stored up converstion flow.
## Repository Structure:
The repository is organized as follows:
- `langchain`: Implements the Langchain framework for converting questions to embeddings using Cohere.
- `Wevaite`: Handles the integration with Wevaite Vector Database for storing and retrieving embeddings.
- `semantic_search`: Implements semantic search and QA retrieval using Langchain and Wevaite.
- `llm_gpt_3_5_turbo`: Utilizes the OpenAI Large Language Model (LLM) GPT-3.5 Turbo to generate context-based answers.
- `requirements.txt`: Lists the necessary dependencies and packages required to run the project.
- `LICENSE`: Specifies the license information for the project.
- `README.md`: Provides essential information about the project, including setup instructions, usage guidelines, and additional resources.
## Preview:

![image](https://github.com/Tobaisfire/vercel-repo/assets/67000746/18c9fae9-338e-4f28-9d43-1e82b790df64)


## Link to Model:

[https://chat-with-tobis.vercel.app/]

## Getting Started:
To get started with the project, please follow the instructions provided in the `README.md` file. It includes detailed steps for installation, setup, and usage of the chatbot. Make sure to review the documentation and example code snippets in the `docs/` and `examples/` directories, respectively, to gain a better understanding of the project's capabilities and usage scenarios.

## Contributions and Feedback:
Contributions and feedback are welcome! If you encounter any issues, have ideas for improvements, or would like to contribute to the project, please feel free to submit a pull request or open an issue. Your contributions will be greatly appreciated and will help enhance the functionality and usability of the chatbot.

## License:
This project is licensed under the [MIT License](LICENSE).
