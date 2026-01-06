# 📊 Data Quality Checker using LLM

A Gen AI-powered tool that analyzes CSV files and generates natural language reports about data quality issues using Large Language Models.

## 🎯 Problem Statement

Build a Gen AI agent that can analyze a CSV file and generate a natural language report about the file's data quality issues — like missing values, duplicate rows, outliers, wrong datatypes, etc.

## 💡 Why It Matters

In real-world projects, bad data = bad analytics. Data engineers usually write manual scripts to check quality. With this project, an LLM automates the boring initial analysis.

## 🏗️ Architecture

```
User Uploads CSV
      ↓
Python (Streamlit Backend) Reads File
      ↓
Summarizes data stats (missing %, duplicates, data types) using Pandas
      ↓
LLM (DeepSeek R1 via OpenRouter) Generates a human-readable Data Quality Report
      ↓
Returns the Report to User
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python + Streamlit |
| Data Processing | Pandas |
| LLM | DeepSeek R1 (via OpenRouter API) |
| Frontend | Streamlit |

## 📁 Project Structure

```
Data-Quality-Checker/
├── .devcontainer/          # DevContainer config for GitHub Codespaces
│   └── devcontainer.json
├── .env                    # Environment variables (gitignored)
├── .gitignore              # Git ignore rules
├── streamlit_app.py        # Main application (single-file)
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── LICENSE                 # License file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- OpenRouter API key ([Get one free here](https://openrouter.ai))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Data-Quality-Checker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Streamlit server**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - Or manually navigate to the URL shown in the terminal

3. **Use the application**
   - Enter your OpenRouter API key in the input field
   - Upload a CSV file
   - View automatic data quality metrics
   - Click "🧠 Summarize with LLM" for AI-generated insights

### Development Mode (with CORS disabled)

```bash
streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
```

## 📊 Features

### Automated Data Quality Metrics
- **Total rows and columns** count
- **Duplicate row detection**
- **Missing value percentage** per column
- **Data type analysis** for each column

### AI-Powered Insights
- Natural language summary of data quality issues
- Highlighting of key problems
- Suggestions for fixes and improvements

### Interactive UI
- Drag-and-drop CSV upload
- Real-time data preview
- Expandable detailed reports
- Clean, modern interface

## 🔑 API Key Management

The application uses **manual API key input** for security and flexibility:
- Enter your OpenRouter API key directly in the UI
- Key is not stored permanently (re-enter each session)
- Prevents accidental exposure of credentials

## 🐳 DevContainer Support

This project includes DevContainer configuration for:
- **GitHub Codespaces** - Cloud-based development
- **VS Code Dev Containers** - Local containerized development

Features:
- Auto-installs Python 3.11 and all dependencies
- Automatically starts Streamlit server on port 8501
- Includes Python and Pylance extensions

## 📝 Dependencies

```
streamlit       # Web framework
pandas          # Data analysis
requests        # HTTP requests to OpenRouter API
python-dotenv   # Environment variable management
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

See [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [OpenRouter API Documentation](https://openrouter.ai/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
