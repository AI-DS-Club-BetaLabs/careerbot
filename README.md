# Career Counselling Chatbot with RAG and State-of-the-Art LLMs

This project is a career counselling chatbot designed to provide personalized advice and guidance to users regarding their career paths. The chatbot utilizes advanced language models (LLMs) and the Retrieval-Augmented Generation (RAG) framework to offer tailored recommendations and responses. 

## Technologies Used:

- **LLamaindex**: An indexing system for large language models to efficiently retrieve relevant information.
- **Langchain**: A library for managing and processing conversational data in a structured manner.
- **RAG (Retrieval-Augmented Generation)**: A framework for leveraging retrievers and generative language models together for improved performance in tasks like question answering and dialogue generation.
- **Hugging Face Transformers**: A library providing pre-trained models for Natural Language Processing (NLP) tasks.

## Project Structure:

```
career-counselling-chatbot/
│
├── Research/
│   ├── scraper.ipynb
│   └── model.ipynb
│
├── config/
│   ├── config.yaml
│   └── param.yaml
│
├── src/
│   ├── careerbot/
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   ├── llm.py
│   │   │   └── scraper.py
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── configuration.py
│   │   ├── constants/
│   │   │   └── __init__.py
│   │   ├── entity/
│   │   │   └── __init__.py
│   │   ├── pipeline/
│   │   │   ├── __init__.py
│   │   │   └── chat.py
│   │   └── __init__.py
│   ├── logger/
│   │   └── __init__.py
│   └── utility.
│       ├── __init__.py
│       └── common.py
│
├── README.md
├── app.py
├── requirements.txt
├── setup.py
└── template.py
```

## Setup:

1. Create environment:

   ```
   conda create -n venv python=3.10
   conda activate venv
   ```

2. Clone the repository:

   ```
   git clone https://github.com/AI-DS-Club-BetaLabs/careerbot.git
   cd careerbot
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```
   python app.py
   ```

5. Access the chatbot through CLI

## Usage:

Once the application is running, users can interact with the chatbot through the command line interface. They can input their queries or requests related to career counselling, and the chatbot will respond with personalized advice and guidance.

## Contributors:

- [Subodh Uniyal](https://github.com/Subodh7976)

## License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.