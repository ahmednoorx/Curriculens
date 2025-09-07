# 📚 Curriculens – AI Assistant for Curriculum Design

Curriculens is an AI-powered education assistant that helps teachers and curriculum designers summarize lesson content and generate clear learning objectives. Built using **Streamlit**, it supports **PDF and DOCX document parsing**, **text generation using LLMs**, **taxonomy tagging**, **chatbot assistance**, and **exporting results**.

This project was originally created during the PEC-GENAI Hackathon 2025.

---

## ✨ Key Features

- 🧠 **AI-Powered Content Generation**: Uses advanced LLM through Groq API for creating lesson plans, summaries, and assessments
- 📄 **Smart Document Processing**: Upload and extract text from PDF and DOCX files with automatic chapter detection
- 🎯 **Educational Content Creation**: Generate lesson plans, MCQs, short questions, and summaries instantly
- 💬 **Interactive AI Assistant**: Built-in chatbot (Curriculens) for Q&A about your uploaded content
- 📤 **Flexible Export Options**: Download generated content as PDF or DOCX for easy sharing
- 🔍 **Keyword Extraction**: Automatically identify key terms and concepts from educational materials
- ⚡ **User-Friendly Interface**: Simple, responsive Streamlit-based web application

## 🎯 What Can Curriculens Do for You?

### **For Educators & Teachers**
- ⏰ **Save Time**: Transform hours of lesson planning into minutes of guided content creation
- 📚 **Enhance Quality**: Generate professionally structured lesson plans with clear objectives and procedures
- 🧪 **Create Assessments**: Instantly produce diverse MCQs and short-answer questions for any topic
- 💡 **Get Teaching Ideas**: Use the AI chatbot to brainstorm activities and teaching strategies
- 📊 **Maintain Consistency**: Ensure all your materials follow educational best practices

### **For Students & Learners**
- 📖 **Study Assistance**: Get instant summaries and key points from textbooks and materials
- ❓ **Q&A Support**: Ask questions about specific chapters or concepts and get immediate answers
- 📝 **Practice Materials**: Generate practice questions to test your understanding
- 🎯 **Focused Learning**: Extract specific chapters or sections for targeted study sessions

### **For Educational Institutions**
- 🏗️ **Curriculum Development**: Rapidly create standardized course materials and assessments
- 👥 **Teacher Training**: Help educators learn content creation best practices
- 📈 **Quality Assurance**: Ensure consistent, high-quality educational materials across courses
- 🔄 **Resource Optimization**: Transform existing documents into comprehensive teaching resources

### **Key Benefits**
- ✅ **Instant Results**: Generate educational content in seconds, not hours
- ✅ **Professional Quality**: AI-generated materials follow educational standards and best practices
- ✅ **Customizable**: Review and edit generated content to match your specific needs
- ✅ **Versatile**: Works with any subject matter - from elementary to university level
- ✅ **Accessible**: No technical expertise required - just upload and generate
- ✅ **Cost-Effective**: Free alternative to expensive curriculum development services

> **💡 Quick Example**: Upload a 50-page textbook chapter, and Curriculens will automatically detect sections, generate a complete lesson plan with objectives and activities, create 20 MCQs for assessment, provide a comprehensive summary, and answer any questions you have about the content - all in under 5 minutes!

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

## 📋 Complete Capabilities Guide

For a detailed breakdown of all features, use cases, and benefits, see our comprehensive **[Capabilities Documentation](CAPABILITIES.md)** which covers:

- 🎯 **Detailed Feature Breakdown**: In-depth explanation of each AI capability
- 👩‍🏫 **Educator Benefits**: How teachers can maximize their productivity and quality
- 👩‍🎓 **Student Advantages**: Ways learners can enhance their study experience
- 🏫 **Institutional Value**: Benefits for schools, universities, and training organizations
- 💡 **Best Practices**: Tips for getting the most out of Curriculens
- 🔧 **Technical Details**: Under-the-hood technology and performance features

**📖 [User Guide](USER_GUIDE.md)** - Step-by-step instructions, practical examples, and pro tips for maximizing your experience with Curriculens.

**❓ [FAQ](FAQ.md)** - Answers to frequently asked questions about features, usage, and troubleshooting.

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

