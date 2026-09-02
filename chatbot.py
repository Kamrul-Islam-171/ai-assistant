from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompts import (
    programming_prompt,
    math_prompt,
    general_prompt,
    category_prompt,
    summary_prompt,
    structured_prompt
)

from langchain_core.runnables import (
    RunnableBranch,
    RunnableParallel,
)

from langchain_core.output_parsers import StrOutputParser

from schemas import ChatResponse

load_dotenv()



model = ChatGroq(model="openai/gpt-oss-120b")
structured_model = model.with_structured_output(ChatResponse)

parser = StrOutputParser()

category_chain = category_prompt | model | parser
programming_chain = programming_prompt | model
math_chain = math_prompt | model
general_chain = general_prompt | model
summary_chain = summary_prompt | model
structured_chain = structured_prompt | structured_model


branch = RunnableBranch(
    (
        lambda x : x['category'] == 'programming',
        programming_chain
    ),
    (
        lambda x : x['category'] == 'mathematics',
        math_chain   
    ),
    general_chain
)

parallel_chain = RunnableParallel(
    answer = branch,
    summary = summary_chain
)




# start the function from here

def get_response(question) :

    # question = "How to do service worker in react.js?"

    category = category_chain.invoke({
        "question" : question
    })

    parallel_res = parallel_chain.invoke({
        "question" : question,
        "category" : category
    })


    ans = parallel_res['answer'].content
    sum = parallel_res['summary'].content

    result = structured_chain.invoke(
        {
                "question": question,
                "category": category,
                "answer": ans,
                "summary": sum,
        }
    )
    
    # print("ai ans = \n", result)

    return result