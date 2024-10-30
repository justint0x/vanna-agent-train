
# Quickstart App with Streamlit and LangChain

## Overview

This project is a simple Streamlit application that leverages the LangChain library to interact with OpenAI's chat models. The app allows users to ask questions related to healthcare automation agents provided by Thoughtful AI.

## Features

- User-friendly interface for entering queries.
- Real-time responses from an AI model.
- Integration with OpenAI's API for generating responses.

## Requirements

- Python 3.10 or higher
- Streamlit
- LangChain
- OpenAI Python client

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/justint0x/vanna-agent-train
   cd vanna-agent-train
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable or enter it in the app.

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your OpenAI API key in the sidebar and type your question in the text area.

4. Click "Submit" to get a response from the AI model.

## Code Explanation

The main components of the application are:

- **Imports**: The necessary libraries are imported at the beginning.
- **Title**: The title of the app is set using `st.title()`.
- **API Key Input**: A sidebar input for the OpenAI API key is created.
- **Response Generation**: The `generate_response()` function handles the interaction with the LangChain model.
- **Form Submission**: A form is created for user input, which triggers response generation upon submission.

## Example Questions

- What does the eligibility verification agent (EVA) do?
- What does the claims processing agent (CAM) do?
- How does the payment posting agent (PHIL) work?
- What are the benefits of using Thoughtful AI's agents?

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.readthedocs.io/)
- [OpenAI](https://openai.com/)
