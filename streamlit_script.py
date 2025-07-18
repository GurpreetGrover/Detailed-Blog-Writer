import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] =os.getenv('GEMINI_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    max_retries=2
)



from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain



user_prompt = PromptTemplate(input_variables=['topic'] ,
                         template="List five ideas about {topic}.")

idea_formation = LLMChain(llm=llm, prompt = user_prompt)

detailed_prompt = PromptTemplate(input_variables=['idea'] ,
                      template="Expand on this idea: {idea}.")

Blog_content = LLMChain(llm=llm, prompt = detailed_prompt)

# Combine them into a sequential chain
sequential_chain = SimpleSequentialChain(chains=[idea_formation, Blog_content])

# Run the chain
# response = sequential_chain.run(input={"topic": "Sustainable Living"})

st.title("Blog Generator")

# Add a text input for the user to enter the blog topic
topic_input = st.text_input("Enter the blog topic:")

# Add a button to generate the blog content
if st.button("Generate Blog Content"):
    if topic_input:
        # Generate the blog content using the sequential chain
        with st.spinner("Generating blog content..."):
            response = sequential_chain.run(topic_input)
        st.write("### Generated Blog Content:")
        st.write(response)
    else:
        st.warning("Please enter a blog topic.")