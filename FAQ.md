# 🙋‍♀️ Curriculens FAQ - Frequently Asked Questions

## General Questions

### What is Curriculens?
Curriculens is an AI-powered educational assistant that helps teachers, students, and curriculum designers create high-quality educational materials from PDF and DOCX documents. It can automatically generate lesson plans, assessments, summaries, and provide interactive Q&A support.

### Who can benefit from using Curriculens?
- **Teachers** (K-12, university, corporate training)
- **Students** (for study guides and comprehension)
- **Curriculum designers** and educational consultants
- **Educational institutions** seeking to standardize content
- **Homeschool educators** and tutors
- **Training professionals** in corporate environments

### Is Curriculens free to use?
The application is open-source and available for free. However, it requires an API key for the AI service (Groq), which may have usage costs depending on volume.

## Technical Questions

### What file formats are supported?
Currently, Curriculens supports:
- **PDF files** (with selectable text)
- **DOCX files** (Microsoft Word documents)

### How large can my uploaded documents be?
For optimal performance, the application processes the first 12,000 characters of your document. For larger documents, consider breaking them into smaller sections or focusing on specific chapters.

### What AI technology powers Curriculens?
Curriculens uses advanced Large Language Models (LLMs) through the Groq API, combined with Natural Language Processing (NLTK) for text analysis and keyword extraction.

### Do I need to install anything?
If running locally, you need Python and the dependencies listed in `requirements.txt`. Alternatively, you can use the online version on Hugging Face Spaces.

## Usage Questions

### How do I get the best results from content generation?
- Use well-structured documents with clear headings
- Ensure content is educational and focused
- Try generating content multiple times for variety
- Review and customize AI-generated content to match your needs
- Use specific chapter selections for targeted content

### Can I edit the generated content?
Yes! All generated content can be exported as Word documents for full editability. You can customize, add to, or modify any generated materials to suit your specific requirements.

### How accurate is the AI-generated content?
While Curriculens produces high-quality educational content, it's designed to augment, not replace, your professional expertise. Always review and validate generated content for accuracy and appropriateness for your specific context.

### Can I use this for any subject area?
Yes, Curriculens works across all subject areas including:
- STEM subjects (Math, Science, Engineering)
- Humanities (Literature, History, Philosophy)
- Languages and Linguistics
- Business and Economics
- Arts and Creative subjects
- Professional training materials

## Features and Capabilities

### What types of content can Curriculens generate?
- **Lesson Plans**: Complete structured plans with objectives, materials, and procedures
- **Multiple Choice Questions (MCQs)**: Diverse assessment questions
- **Short Answer Questions**: Open-ended questions for deeper thinking
- **Summaries**: Concise overviews of complex content
- **Keywords**: Important terms and concepts extraction

### How does the chatbot feature work?
The Curriculens chatbot can answer questions about your uploaded content. You can:
- Ask for clarification on concepts
- Request teaching strategies and ideas
- Get additional examples or explanations
- Focus discussions on specific chapters
- Export chat conversations for future reference

### Can I export my generated content?
Yes! You can export content in two formats:
- **PDF**: For sharing and printing (read-only)
- **Word (DOCX)**: For editing and customization
- **Chat History**: Save your Q&A sessions as text or Word files

## Best Practices

### How should I prepare my documents for upload?
- Ensure PDFs have selectable text (not just scanned images)
- Use documents with clear structure and headings
- Focus on educational content rather than administrative text
- Consider breaking very long documents into chapters or sections

### What's the difference between "Book" and "Syllabus" content types?
- **Book**: Best for textbooks, manuals, or materials with multiple chapters
- **Syllabus**: Ideal for course outlines, single-topic documents, or curriculum guides

### How can I get the most value from Curriculens?
1. Start with high-quality source materials
2. Experiment with different content generation types
3. Use the chatbot for creative teaching ideas
4. Build a library of exported materials
5. Combine AI assistance with your professional expertise
6. Share successful approaches with colleagues

## Troubleshooting

### My PDF isn't being processed correctly. What should I do?
- Ensure the PDF contains selectable text, not just images
- Try extracting a specific chapter or section
- Check that the document is not password-protected
- Consider converting the PDF to a Word document first

### The generated content seems off-topic. How can I fix this?
- Try uploading a more focused section of your document
- Use the chapter selection feature for books
- Ensure your source material is clearly educational
- Try generating content multiple times for different results

### I'm not getting the chapter detection I expected. What can I do?
- Check that your document uses clear chapter headings
- Try manually selecting "All" if chapters aren't detected
- Consider the document structure - clear formatting helps
- Focus on one chapter at a time for better results

### The application seems slow. How can I improve performance?
- Use smaller document sections
- Ensure stable internet connection
- Try generating content for specific chapters rather than entire documents
- Consider the current server load if using the online version

## Educational Effectiveness

### How can I ensure the content meets educational standards?
- Review all generated content for accuracy and appropriateness
- Align generated materials with your curriculum standards
- Use generated content as a starting point for customization
- Combine AI assistance with your pedagogical expertise

### Can Curriculens help with differentiated instruction?
Yes! You can:
- Generate content at different complexity levels
- Create varied assessment types for different learning styles
- Use the chatbot to brainstorm accommodation strategies
- Export materials in formats suitable for different needs

### How does this support evidence-based teaching practices?
Curriculens promotes evidence-based practices by:
- Generating structured lesson plans with clear objectives
- Creating diverse assessment options
- Encouraging the use of quality educational materials
- Supporting reflective practice through the Q&A feature

## Getting Help

### Where can I find more detailed instructions?
- **[User Guide](USER_GUIDE.md)**: Comprehensive step-by-step instructions
- **[Capabilities Documentation](CAPABILITIES.md)**: Detailed feature breakdown
- **Application Interface**: Built-in help in the sidebar

### How can I report bugs or suggest features?
Please visit the [GitHub repository](https://github.com/ahmednoorx/Curriculens) to:
- Report issues
- Suggest new features
- Contribute to development
- Access the latest updates

### Is training available for teams or institutions?
While formal training isn't currently offered, the comprehensive documentation and user guide provide everything needed to get started. For institutional implementations, consider:
- Sharing the user guide with your team
- Conducting internal workshops using the documentation
- Starting with pilot programs before full deployment

---

*Don't see your question here? Check the [User Guide](USER_GUIDE.md) for detailed instructions or visit our [GitHub repository](https://github.com/ahmednoorx/Curriculens) for additional support.*