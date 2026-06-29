# GitHub Models Setup Guide

# QA Jira MCP Agent Framework

## Purpose

This document explains how to configure and use **GitHub Models** with the QA Jira MCP Agent Framework.

By the end of this guide, you will be able to:

* Understand what GitHub Models are
* Generate a Personal Access Token (PAT)
* Configure the project
* Connect to GPT-4.1 using GitHub Models
* Test the connection
* Troubleshoot common issues

# What are GitHub Models?

GitHub Models is a cloud-based AI inference service provided by GitHub.

Instead of calling the OpenAI API directly, developers can access multiple AI models through a single endpoint.

Supported models include:

* GPT-4.1
* GPT-4o
* GPT-4o-mini
* o1
* o3
* Phi
* Mistral
* Llama
* DeepSeek (availability may vary)

This project uses **GPT-4.1** because it provides reliable structured JSON generation for QA artifacts such as test cases and workbooks.

# Why GitHub Models?

This project uses GitHub Models because it offers several advantages for learning and enterprise development.

### Single API Endpoint

A single endpoint provides access to multiple models.

### Familiar Authentication

Authentication is performed using a GitHub Personal Access Token (PAT), eliminating the need to manage separate API keys.

### Structured Output

GitHub Models supports JSON mode, which is ideal for generating:

* Test Cases
* QA Workbooks
* Requirement Summaries
* Traceability Matrices
* Automation Scripts

### Rapid Experimentation

Switching models requires only changing the model name in code.

Example:

```python
model="gpt-4.1"
```

can be changed to:

```python
model="gpt-4o"
```

without changing the rest of the application.



# Architecture

```
Application

↓

GitHub Models Client

↓

Azure AI Inference Endpoint

↓

GPT-4.1

↓

JSON Response

↓

Excel Workbook
```



# Prerequisites

Before starting, ensure you have:

* GitHub account
* Python 3.11 or later
* Git installed
* Internet connectivity



# Step 1 – Create a GitHub Account

If you do not already have one:

1. Go to GitHub.
2. Create an account.
3. Verify your email address.



# Step 2 – Generate a Personal Access Token

1. Open GitHub.
2. Click your profile picture.
3. Go to **Settings**.
4. Select **Developer Settings**.
5. Choose **Personal Access Tokens**.
6. Click **Generate New Token**.
7. Select the required permissions.
8. Generate the token.
9. Copy the token immediately.

> Store the token securely. GitHub will not display it again.



# Step 3 – Create the Environment File

Create a file named:

```text
.env
```

Place it in the project root directory.

Example:

```env
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Do not:

* Add quotation marks
* Add extra spaces
* Commit this file to Git



# Step 4 – Install Dependencies

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```



# Step 5 – Configure the Client

The project uses the OpenAI SDK configured for GitHub Models.

Example:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN
)
```



# Step 6 – Verify the Connection

Run a simple test prompt.

Example:

```python
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Return JSON only."
        }
    ]
)

print(response.choices[0].message.content)
```

Expected output:

```json
{
  "status": "success"
}
```



# JSON Mode

This project uses JSON mode to ensure the model returns structured data.

Example:

```python
response_format={
    "type": "json_object"
}
```

Benefits:

* Easier parsing
* Predictable output
* Reduced formatting errors
* Simplified Excel generation



# Cleaning the Response

Sometimes the model returns Markdown code fences.

Example:

````text
```json
{
}
```
````

The helper function removes these wrappers before parsing the response.



# Supported Models

Current examples include:

```python
model="gpt-4.1"
```

Other supported models may include:

```python
model="gpt-4o"
model="gpt-4o-mini"
model="o1"
model="o3"
```

Refer to the latest GitHub Models documentation for model availability.



# Temperature

Recommended settings:

| Use Case             | Temperature |
| -- | -: |
| Test Case Generation |         0.2 |
| Requirement Analysis |         0.2 |
| Sprint Workbook      |         0.3 |
| Creative Writing     |         0.8 |

Lower values produce more deterministic outputs.



# Prompt Best Practices

Always provide:

* Role
* Context
* Input
* Output format
* Constraints

Example:

```text
You are a Senior QA Architect.

Generate comprehensive manual test cases.

Return ONLY valid JSON.
```



# Security Best Practices

Never:

* Hardcode tokens
* Commit `.env`
* Share API keys publicly

Always add `.env` to `.gitignore`.

Rotate tokens periodically.



# Common Errors

## Missing Token

Error:

```text
GITHUB_TOKEN is missing
```

Solution:

Verify the `.env` file exists and contains a valid token.



## Invalid Token

Error:

```text
401 Unauthorized
```

Solution:

Generate a new Personal Access Token.



## Connection Timeout

Possible causes:

* No internet connection
* GitHub service unavailable
* Firewall restrictions



## JSON Parsing Error

Possible cause:

The model returned Markdown instead of raw JSON.

Solution:

Use the `clean_json_response()` helper before parsing.



## Rate Limits

If you receive rate limit errors:

* Wait before retrying
* Reduce request frequency
* Avoid unnecessary API calls



# Recommended Folder Structure

```
shared/
│
├── github_models_client.py
├── prompts.py
└── utils.py
```

The client should only be responsible for communicating with GitHub Models.

Business logic belongs elsewhere.

# Summary

GitHub Models provides a convenient, unified interface for accessing powerful AI models while keeping authentication and configuration simple.

Within this project, GitHub Models is used to:

* Analyze Jira requirements
* Generate structured JSON
* Produce QA test cases
* Build Sprint QA Workbooks
* Support future AI-powered QA agents

Using a centralized client and well-structured prompts ensures that every version of the framework remains modular, maintainable, and easy to extend.
