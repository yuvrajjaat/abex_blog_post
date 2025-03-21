# Multi-Agent SEO Blog Generator

## Overview
This project is a Python-based multi-agent system that generates a high-quality, SEO-optimized blog post (~2000 words) on trending HR topics. The system is designed with modular agents that simulate different aspects of content creation:
- **Research Agent:** Fetches trending HR topics and related information from the web (using NewsAPI).
- **Content Planning Agent:** Creates a structured outline based on research.
- **Content Generation Agent:** Writes a comprehensive blog post using the outline and research data.
- **SEO Optimization Agent:** Enhances the content with SEO best practices such as keyword integration and proper formatting.
- **Review Agent:** Proofreads and refines the final content.

## System Architecture and Agent Workflow
1. **Research Agent:**  
   - Searches and collects trending HR news via NewsAPI.
2. **Content Planning Agent:**  
   - Analyzes the research and produces an outline that organizes content into sections with appropriate headings and subheadings.
3. **Content Generation Agent:**  
   - Uses the outline and research data to generate a detailed blog post.
4. **SEO Optimization Agent:**  
   - Optimizes the content by integrating target keywords, meta descriptions, and proper formatting to boost SEO.
5. **Review Agent:**  
   - Reviews the final draft to correct errors and improve overall quality.

  The agents are implemented in a modular fashion within `agents.py` and orchestrated via `main.py`.

---
## Screenshot
![Screenshot 2025-03-22 032300](https://github.com/user-attachments/assets/db0eff4e-ea9e-472c-9d69-3a6b7b5a6ff2)

## Tools and Frameworks Used
- **Python 3**: Core programming language.
- **Requests**: For calling the NewsAPI.
- **Built-in libraries**: For text manipulation and file I/O.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yuvrajjaat/abex_blog_post.git
   cd abex_blog_post
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python main.py
   ```
4. **Output:**
   The final blog post is saved as output_blog.txt.

## Explanation of Implementation Choices
- **Modular Agent Design:** Each agent is encapsulated in its own class within agents.py for clarity and modularity.
- **Sequential Workflow:** The agents interact sequentially, where the output of one serves as the input for the next, simulating a production pipeline.
- **Simplicity and Extensibility:** The code is written to be clear and easily extendable. For more complex implementations, each agent could interface with APIs or machine learning models.

---

### requirements.txt
```txt
# For this simple implementation, no external libraries are required.
# If you wish to use an LLM or frameworks like LangChain, add the necessary packages here.
```

---
## Contact
For any questions or feedback, feel free to reach out to [yuvrajsogarwal@gmail.com].

