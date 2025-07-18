# Detailed Blog Writer

A Streamlit web app that generates detailed blog content using Google's Gemini language model via LangChain. Enter a topic, and the app will suggest five ideas and expand on one to create a detailed blog section.

## Features

- Enter any blog topic and get five related ideas.
- Automatically expands on one idea to generate detailed blog content.
- Simple, interactive Streamlit interface.
- Powered by Google's Gemini model via LangChain.
- **LangSmith Traceability:** All LLM calls are tracked using LangSmith, enabling advanced debugging, analytics, and traceability of model interactions.

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd Detailed-Blog-Writer
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

Install the required packages:

```
streamlit
python-dotenv
langchain
langchain-google-genai
langsmith
```

Or use the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

A `.env.template` file is provided in the project root. Copy it to `.env` and fill in your API keys:

```bash
cp .env.template .env  # On Windows, use: copy .env.template .env
```

Edit the `.env` file to add your keys:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
```

- `GEMINI_API_KEY`: Your Google Gemini API key (required for LLM access)
- `LANGCHAIN_API_KEY`: Your LangSmith API key (required for traceability)

### 5. Run the app

```bash
streamlit run streamlit_script.py
```

## Usage

1. Enter a blog topic in the input box.
2. Click "Generate Blog Content".
3. Wait for the ideas and detailed blog content to appear.

## LangSmith Traceability

This app integrates with [LangSmith](https://smith.langchain.com/) to provide traceability for all LLM calls. This enables:
- Debugging and inspection of LLM chains
- Analytics on model usage and performance
- Audit trails for generated content

To use this feature, ensure you have a valid LangSmith API key and set `LANGCHAIN_API_KEY` in your `.env` file.

## Notes

- You need access to the Gemini API and a valid API key.
- You need a LangSmith account and API key for traceability features.
- The app uses the `gemini-2.0-flash` model by default.

## License

MIT License 