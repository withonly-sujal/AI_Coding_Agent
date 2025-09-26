# 🤖AI Coding Agent:

**An intelligent command-line utility for developers that enables seamless Python code creation, editing, execution, and file management using natural language, powered by the Gemini API's advanced function calling.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![LLM](https://img.shields.io/badge/LLM%20Engine-Gemini%20API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemini-api/docs)
[![Tools Framework](https://img.shields.io/badge/Tools%20Framework-Core%20Python-000000?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Current Support](https://img.shields.io/badge/Language%20Support-Python%20Only-FFD43B?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

---

## ✨ Core Features & Technical Highlights

This agent uses a **function-calling architecture** to translate natural language commands into specific file system and execution operations, acting as a powerful developer utility.

| Feature | Description | Technical Implementation |
| :--- | :--- | :--- |
| **📝 Create File** | Generates a new Python script with code content specified via natural language. | Utilizes the **Gemini API** for reliable code generation, ensuring proper syntax before writing to disk. |
| **📖 Read File** | Displays the contents of an existing file back to the user for review. | A dedicated system tool that reads the file and returns its content as observation. |
| **✏️ Overwrite/Edit** | Modifies the content of an existing file based on instructions like "fix bug" or "add function." | The agent sends the existing file content + the user's instruction to the LLM to output the complete, revised code. |
| **▶️ Run File** | Executes the specified Python file safely within a controlled subprocess environment. | Employs Python's built-in `subprocess` module (`subprocess.run()`) to capture and return the `stdout` (output) and `stderr` (errors). |
| **⚡ Python-Only Focus** | The agent's prompt is heavily engineered to constrain its outputs strictly to valid Python 3.x logic, maximizing reliability. | A strong system instruction is used to enforce the agent's persona, its available tools, and the single-language scope. |

---

## 🛠️ Project Architecture

The application is structured into key components that manage the interaction loop between the user, the Gemini LLM, and the local file system tools.

| File / Component | Purpose | Functionality |
| :--- | :--- | :--- |
| `agent.py` | **Core Execution Loop** | Initializes the Gemini model, manages the chat history, and orchestrates the **tool-calling** workflow. |
| `tools.py` | **Agent Tools Library** | Contains the actual Python functions (`create_file`, `read_file`, `overwrite_file`, `run_file`) that define the agent's capabilities. |
| `requirements.txt` | **Dependencies** | Lists all required Python libraries, primarily `google-genai` and related utilities. |
| `.env` | **Configuration** | Stores the required `GEMINI_API_KEY` for secure access to the LLM. |

---

## ⚙️ Setup and Installation

### Prerequisites

1.  **Python 3.8+**
2.  **Gemini API Key:** Obtain a key from Google AI Studio.
3.  **Google-genai:** To use function calling and Gemini API

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [YOUR-REPO-URL]
    cd gemini-ai-coding-agent
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate # Windows
    # source venv/bin/activate # macOS/Linux
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables (`.env` file):**
    Create a file named **`.env`** in the root directory and add your API key:
    ```
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

---

## 🚀 How to Run the Application

The agent operates as a persistent, interactive chat session in your terminal, allowing for rapid iteration on code.

### Start the Agent

Run this command in your terminal:

```bash
py agent.py
