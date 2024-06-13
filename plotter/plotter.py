import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableMap,RunnableLambda, RunnablePassthrough,RunnableParallel
from langchain.output_parsers import PydanticOutputParser,OutputFixingParser
from langchain.pydantic_v1 import BaseModel, Field
from typing import List
from .prompts import prompt_template

llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192"
)

class PO( BaseModel):
    x_axis: List[str]= Field(description="coordinates of the X-axis of the graph")
    x_axis_name:str=Field(description="name of the x axis")
    y_axis: List[int]= Field(description="coordinates of the Y-axis of the graph")
    y_axis_name:str=Field(description="name of the y axis")
    graph_type: str= Field(description="the type of graph")
    explanation:str=Field(description="brief explanation of the graph")
    graph_name: str=Field(description="name of the graph")

parser=PydanticOutputParser(pydantic_object=PO)

fix_parser = OutputFixingParser.from_llm(parser=parser, llm=llm)

prompt = PromptTemplate(template=prompt_template,
                        input_variables=['qns'],
                        partial_variables={"format_instructions": fix_parser.get_format_instructions()},
                        template_format="jinja2"
                        )
graph_chain = RunnableParallel({
    "qns":RunnablePassthrough()
}) | prompt | llm | fix_parser

