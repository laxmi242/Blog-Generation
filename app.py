import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers
from langchain_community.llms import CTransformers

## function to get response from llama2 model

def getLlamaresponse(input_text,no_words,blog_style):
    llm = ctransformers(model='Users\Laxmi\Documents\codes\langChain\Blog_Generation_model\llama-2-7b-chat.ggmlv3.q8_0.bin', 
                        model_type='llama',
                        lib='avx',
                        config={'max_new_token':256, 'temperature':0.01})
    
    ##PromptTemplate
    
    template="""
        Write a blog for {blog_style} job profile for the topic {input_text} write 
        within {no_words} words.
            """
    promt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                     template=template)

    ##generate the response from the llama 2 model
    response=llm(promt.format(style=blog_style,text=input_text,n_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                   page_icon='🎍',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🎍")

input_text = st.text_input("Enter the Title of Blog")

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of words')
with col2:
    blog_style=st.selectbox('writing the blog for',('Data Science','Astrologist','Researcher','General Person'),index=0)

submit=st.button('Generate')

##
if submit:
    st.write(getLlamaresponse(input_text,no_words,blog_style))

