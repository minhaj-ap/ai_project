# 🎬 AI Movie Review Tools API

An open-source Flask-based API that brings AI-powered tools to your movie review application — and to the public! This API provides intelligent text analysis for movie reviews, including:

- ⭐ Extracting a rating from a review paragraph
- 🏷️ Generating relevant tags from a review
- ✂️ Summarizing review or movie overview paragraphs

Anyone is welcome to use and contribute to this API — it's built with openness and collaboration in mind!

---

## 🌐 Live Demo

Hosted on Render (free tier):  
🔗 **[https://ai-project-qhew.onrender.com](https://ai-project-qhew.onrender.com)**

---

## 🚀 Endpoints

All endpoints use the **GET** method and expect plain text in the **body** (not as a JSON object). The response type depends on the task.

| Endpoint      | Function                       | Request Body           | Response Type      |
|---------------|--------------------------------|------------------------|--------------------|
| `/rate`       | Extracts rating from paragraph | Paragraph text         | `String` (e.g., "4.5/5") |
| `/tags`       | Generates relevant tags        | Paragraph text         | `Array` of strings |
| `/summary`    | Summarizes the paragraph       | Paragraph text         | `String` summary   |

---

## 📦 Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/minhaj-ap/ai_project.git
cd ai-project

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
flask run
````

---

## 🧠 Technologies & NLP Models used so far

* **Flask** for API creation


---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## ⚠️ Notes

* Hosted on **Render (free tier)** — cold starts may delay responses slightly.
* A ping service is set up to minimize cold start delays.
* This is an early-stage project; model performance and accuracy may improve over time.

---

## 👨‍💻 Author

**Minhaj AP**
[GitHub Profile](https://github.com/minhaj-ap)

---

## 🤝 Contributors

[Click here to see all contributors](https://github.com/minhaj-ap/ai_project/graphs/contributors)

> Want to contribute? Check out [issues](https://github.com/minhaj-ap/ai_project/issues) or submit a PR!


> Want to contribute? start with an issue or PR!

---
