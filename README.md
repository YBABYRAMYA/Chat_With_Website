---

# 🌐 Chat with Website Using RAG Pipeline

Leverage the power of AI to extract, filter, and query content from web pages! **Chat with Websites** is a simple yet robust tool designed to make web content interaction intuitive and insightful.

---

## ✨ Key Features ✨
- 🔗 **Fetch Website Content**: Input multiple URLs to extract relevant web content.
- 🔍 **Keyword-Based Filtering**: Filter text using predefined keywords like "research," "innovation," and more.
- ✂️ **Content Chunking**: Automatically splits content into manageable pieces for better querying.
- 💬 **AI Query Response**: Get context-rich answers to your questions.
- ⚡ **Efficient Processing**: Fast, scalable, and accurate content handling.

---

## 📂 Project Structure 📂
```plaintext
Chat_With_Website/
├── templates/
│   └── index.html           # HTML template for the web interface
├── fetcher.py               # Core functionality for fetching and processing web content
├── app.py                   # Flask backend application
```

---

## 🚀 Getting Started 🚀

### 1️⃣ Prerequisites
- Python 3.8+
- `pip` (Python package manager)

### 2️⃣ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Chat-With-Website.git
   cd Chat-With-Website
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🖼️ Visual Demo 🖼️

### Home Page
📂 **Enter URLs and Queries**  
![Screenshot (1525)](https://github.com/user-attachments/assets/c46220b3-00ef-4611-9a2f-d98909f97df8)


---

## 🛠️ Tech Stack 🛠️
- **Backend**: Flask
- **Web Scraping**: Custom functions in `fetcher.py`
- **Frontend**: HTML5, CSS3 (from `templates/index.html`)
- **Text Processing**: Keyword filtering and chunking for semantic queries
- **AI Responses**: Generate query-based responses from filtered content

---

## 💡 How It Works 💡

1. **🌐 Input URLs**: Enter one or more URLs in the web interface.
2. **🔎 Extract Content**: Fetch and process text data from the URLs.
3. **📖 Keyword Filtering**: Keep only the most relevant parts of the content.
4. **✂️ Chunking**: Split the filtered text into smaller, manageable pieces.
5. **🤔 Query**: Ask your question, and the system responds with contextually accurate answers.

---

## 🚧 Roadmap 🚧
- 🌟 **Multi-language Support**: Enable querying for non-English content.
- 🌐 **Cloud Deployment**: Deploy on platforms like AWS, GCP, or Heroku.
- 🔒 **User Authentication**: Add personalized features for registered users.
- 📘 **Additional File Formats**: Support DOCX and TXT files alongside URLs.

---

## 🤝 Contribute 🤝
We welcome contributions to make this project better! Here's how you can help:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

## 📈 Use Cases 📈
- 📚 **Academic Research**: Quickly extract and query information from research papers or university websites.
- 🧑‍💻 **Developer Tools**: Analyze content from developer documentation or blogs.
- 📰 **Media Analysis**: Summarize and query articles from news websites.

---

## 👤 Author
- **Your Name** : Yalagandula Baby Ramya
---
