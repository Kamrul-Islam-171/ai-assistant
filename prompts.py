from langchain_core.prompts import PromptTemplate


programming_prompt = PromptTemplate.from_template(
    """
You are an expert programming assistant.

The user asked a programming-related question.

Explain the concept clearly and provide examples when useful.

User Question:
{question}

Return a helpful and technically accurate response.
"""
)


math_prompt = PromptTemplate.from_template(
    """
You are an expert mathematics tutor.

The user asked a mathematics-related question.

Solve the problem step by step and explain the reasoning clearly.

User Question:
{question}

Return a helpful and mathematically accurate response.
"""
)


general_prompt = PromptTemplate.from_template(
    """
You are a helpful general-purpose AI assistant.

Answer the user's question clearly and concisely.

User Question:
{question}

Return a helpful response that is easy to understand.
"""
)

category_prompt = PromptTemplate.from_template(
    """
    Classify the following user question into exactly one of these categories:
    programming, mathematics, or general.

    User Question:
    {question}

    Return only the category name.
    """
)


summary_prompt = PromptTemplate.from_template(
    """
Summarize the following user question in one or two sentences.

User Question:
{question}

Return only the summary.
"""
)


structured_prompt = PromptTemplate.from_template(
    """
Create the final response using the information provided below.

User Question:
{question}

Category:
{category}

Answer:
{answer}

Summary:
{summary}

Return the response according to the required schema.

Make sure:
- answer contains the complete answer
- summary contains a short summary
- category is one of: programming, mathematics, general
- confidence is between 0 and 1
- keywords contains important keywords
"""
)