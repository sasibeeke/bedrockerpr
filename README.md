# 🚀 AI-Powered PR Reviewer (AWS Bedrock + Lambda + GitHub)

## 📌 Overview

This project demonstrates how to build an **AI-powered Pull Request (PR) reviewer** using AWS serverless services and generative AI.

Whenever a PR is opened or updated, the system:

1. Fetches the PR diff
2. Sends it to an AI model (Amazon Bedrock)
3. Generates a structured code review
4. Posts the review as a comment on the PR

---

## 🧠 Architecture

```
GitHub PR Event
      ↓
Webhook → API Gateway → Lambda → Bedrock (Nova AI)
                                      ↓
                              GitHub PR Comment
```

---

## ⚙️ Tech Stack

* AWS Lambda (Python 3.12)
* Amazon Bedrock (amazon.nova-lite-v1:0)
* Amazon API Gateway
* GitHub Webhooks
* Python (boto3, urllib)

---

## ✨ Features

* ✅ Automated PR code review
* ✅ AI-generated feedback (summary, issues, suggestions)
* ✅ Serverless architecture
* ✅ Real-time GitHub integration
* ✅ Lightweight and cost-efficient

---

## 📂 Project Structure

```
.
├── lambda_function.py
├── README.md
```

---

## 🔐 Prerequisites

* AWS Account (Billing enabled)
* GitHub Repository
* Python 3.9+
* GitHub Personal Access Token

---

## 🚀 Setup Guide

### 1️⃣ Create IAM Role

Attach policies:

* AWSLambdaBasicExecutionRole
* AmazonBedrockFullAccess

---

### 2️⃣ Create Lambda Function

* Runtime: Python 3.12
* Add environment variable:

```
GITHUB_TOKEN=your_token_here
```

---

### 3️⃣ Add Lambda Code

Paste your `lambda_function.py` code.

---

### 4️⃣ Configure API Gateway

* Create REST API
* Resource: `/review`
* Method: POST
* Integration: Lambda Proxy

Deploy API and copy endpoint URL.

---

### 5️⃣ Configure GitHub Webhook

Go to:
GitHub Repo → Settings → Webhooks

Add:

* Payload URL → API Gateway URL
* Content Type → application/json
* Event → Pull Requests

---

## 🧪 Testing

1. Create a new branch
2. Make a code change
3. Open a Pull Request

👉 Within seconds, AI will post a review comment.

---

## 📸 Example Output

```
🤖 AI Code Review

Summary: Added validation logic
Issues: Missing null check
Security: Input not sanitized
Suggestions: Add unit tests
```

---

## ⚠️ Common Issues & Fixes

### ❌ Bedrock Access Error

* Ensure billing is enabled

### ❌ Model Not Found

* Use latest model: `amazon.nova-lite-v1:0`

### ❌ GitHub Token Error

* Ensure token has repo permissions

### ❌ No PR Comment

* Check Lambda logs in CloudWatch

---

## 💡 Future Improvements

* Inline code comments
* Multi-language support
* Slack/Teams notifications
* CI/CD integration

---

## 📈 Learning Outcomes

* Serverless architecture
* Event-driven systems
* AI integration in DevOps
* AWS services (Lambda, API Gateway, Bedrock)

---

## 🤝 Contributing

Feel free to fork and improve this project.

---

## 📬 Connect

If you found this useful, connect with me on LinkedIn!

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

