# 🛡️ Insurance Policy Assistant Chatbot

This is a Python-based chatbot powered by Google's **Gemini API** and **LangChain**, designed to answer customer queries related to insurance policy details from a CSV file. It applies **guardrails** to ensure security, scope control, and data privacy.

---

## 📂 Project Structure

```
.
├── main.py               # Main application script
├── insurance_policies.csv # CSV file containing policy data
└── README.md             # Project documentation
```

---

## 📌 Features

* ✅ Answer questions about:

  * Premium amount
  * Policy type
  * Coverage amount
  * Renewal date
* 🚫 Guardrails:

  * No personal info revealed (e.g., names, contact details)
  * Rejects out-of-scope questions (e.g., cancellation, claim filing)
  * Validates policy IDs
  * Handles ambiguous queries by requesting clarification
* 🧠 Powered by **Gemini Pro (Google Generative AI)** via LangChain
* 🗃️ Data source: `insurance_policies.csv`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/insurance-chatbot.git
cd insurance-chatbot
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Dependencies** include:

* `pandas`
* `langchain`
* `langchain-google-genai`
* `google-generativeai`

You can manually install with:

```bash
pip install pandas langchain langchain-google-genai google-generativeai
```

### 3. Prepare the CSV

Make sure your `insurance_policies.csv` file looks like this:

```csv
policy_id,customer_name,policy_type,coverage_amount,premium,renewal_date
POL001,John Doe,Health Insurance,500000,12000,2025-12-31
POL002,Jane Smith,Life Insurance,1000000,18000,2026-03-15
...
```

Ensure the file is placed in the root directory of the project.

### 4. Set Your API Key

Replace the placeholder API key in `main.py` with your own [Google Gemini API key](https://makersuite.google.com/app/apikey):

```python
GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY"
```

---

## 🚀 Running the Chatbot

```bash
python main.py
```

Example usage (inside the script or via a UI integration):

```python
chat_with_bot("POL001", "What is my premium?")
```

---

## ✅ Example Output

**Input:**

```text
chat_with_bot("POL001", "What is my premium?")
```

**Output:**

```text
Your premium amount is ₹12000.
Please consult an insurance advisor for detailed guidance.
```

---

## ⚠️ Guardrail Responses

* **Invalid Policy ID:**

  ```
  Policy not found. Please verify your ID.
  Please consult an insurance advisor for detailed guidance.
  ```

* **Out of Scope:**

  ```
  Sorry, I can’t help with that. Please contact support.
  Please consult an insurance advisor for detailed guidance.
  ```

* **Ambiguous Question:**

  ```
  Could you please clarify your question?
  Please consult an insurance advisor for detailed guidance.
  ```

---

## 🔒 Disclaimer

This chatbot is for informational purposes only and does not replace professional insurance advice. For detailed assistance, always consult a licensed insurance advisor.

---

## 📬 Contact

Built by **Prajwal**
📧 Email: prajwal4102@gmail.com
🌐 LinkedIn: https://www.linkedin.com/in/prajwal-a-c/
📦 GitHub: https://github.com/prajwal4102
