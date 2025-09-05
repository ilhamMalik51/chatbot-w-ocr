# chatbot-w-ocr
This repo is for hiring process purposes from Shopee

* Name : Muhammad Ilham Malik
* Email : muh.ilham.malik@gmail.com


1 - **Question:** Describe differences between REST API and MCP in the context of AI.

**Answer:** REST (Representational State Transfer) API is a general purpose application interface. meaning that:
* It's designed for application to application communication.
* It has different endpoint format, authorization, and parameters or body request structure.

On the other hand, MCP (Model Context Protocol) is a specific purpose application interface for foundational LLM (Large Language Model). This means:

* It has context that LLM can work with.
* It has dynamic self discovery. This gives the LLM of all information on what the MCP is capable of.
* It also a standardized interface. Each MCP server (regardless of services) has the same protocol.

2 - **Question:** How REST API, MCP, can improve the AI use case.

**Answers:** REST API and MCP can improve the AI use case by integrating them into an AI Application that is AI Agents.
* MCP can wrap REST API to improve AI application use case so that it can answer real-time data.
* They also can improve AI application to process transactional flow such as creating a complaint ticket, creating an email, and book a flight.
* They also can improve AI application to help analyze data from the database or data warehouse. Giving visualization and insight regarding the data in the database.

3 - **Question:** How do you ensure that your AI agent answers correctly.

**Answers:** There are several ways to make sure AI Agent can answer correctly.
* Define or use appropriate persona (system message). In my experience, defining a clear rules on what, who, and how an AI Agent answer can directly affect the answer generation of AI Agent.
* Prompt engineering (prompt message). After defining appropriate persona, we also need to define a clear instruction on what we want achieve. For example, "Summarize the following paragraph into 3 sentences."
* Few-shot Example. We can also gives the LLM a few example on how to answer the user question in the prompt.
* Retrieval Augmented Generation. RAG is a process where we retrieve a relevant or factual context to help LLM answer user's question. It has been proven that by providing relevant context in the prompt can help LLM answer more accurately.
* Tools Calling. Tools calling is a process where an LLM recommend the the best possible tool to use based on user question. This can help AI agent answer question about real-time data.
* Implement Agent Flow such as ReAct or Self-ask. These two method is an iterative method to help LLM answer correctly. This method works by refining the answer at each step until the LLM stops at give the full answer.

4 - **Question:** Describe what you can do with Docker / Containerize environment in the context of AI.
Docker or containerization can do the following:
* Help developers run AI applications smoothly in different operating system.
* Help AI applications to run consistently in different machine.
* In production settings, it can help to scale up smoothly by rolling out different container. Also, rolling back to the old image if there is an error in the current image.

5 - **Question:** How do you finetune the LLM model from raw.


Video Link: 