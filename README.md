# 📚 Curriculens – AI Assistant for Curriculum Design

Curriculens is an AI-powered education assistant that helps teachers and curriculum designers summarize lesson content and generate clear learning objectives. Built using **Streamlit**, it supports **PDF and DOCX document parsing**, **text generation using LLMs**, **taxonomy tagging**, **chatbot assistance**, and **exporting results**.

This project was originally created during the PEC-GENAI Hackathon 2025.

---

## ✨ Features

- 🧠 **Text Generation**: Uses open-source Falcon LLM through Groq for generating summaries and learning outcomes.
- 🏷️ **Bloom/SOLO Taxonomy Tagging**: Select desired taxonomy level and get outcomes aligned with it.
- 📄 **PDF & DOCX Parsing**: Upload and extract text directly from Microsoft Word or PDF lesson plans.
- 📤 **Export Options**: Download generated content as PDF or DOCX for easy sharing or record keeping.
- 💬 **Built-in Chatbot**: Ask questions or get additional suggestions related to your content.
- ⚡ **Streamlit Frontend**: Simple, responsive interface that runs locally or on Hugging Face Spaces.

---

## 🗂️ Project Structure

```

Curriculens/
├── src/
│   ├── app.py               # Main Streamlit app
│   ├── models/
│   │   └── text\_generation.py     # LLM integration (Groq/Hugging Face)
│   ├── parsers/
│   │   ├── pdf\_parser.py     # For PDF text extraction
│   │   └── docx\_parser.py    # For DOCX text extraction
│   ├── exporters/
│   │   ├── export\_pdf.py     # Export to PDF
│   │   └── export\_docx.py    # Export to DOCX
│   └── utils/
│       └── helpers.py        # Utility/helper functions
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
└── .gitignore                # Ignored files during git commits

````

---

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/ahmednoorx/Curriculens.git
cd Curriculens
````

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the app locally using Streamlit:

```bash
streamlit run src/app.py
```

Then open the URL shown in the terminal to access the web interface.

---

## 🧭 Roadmap (Ideas for Future)

* Multi-language support for text generation
* Automatic learning outcome classification
* Connect to LMS (like Moodle, Google Classroom)

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more info.

---

## 🙋‍♂️ Author

Made with ❤️ by [Ahmed Noor](https://www.linkedin.com/in/ahmednoorx) and Team memebers Fahad Ullah Jan, Khushbakht and Muhammad Usman during the PEC-GENAI Hackathon.
Check it out live on [Hugging Face Spaces](https://huggingface.co/spaces/ahmednoorx/curriculens)

