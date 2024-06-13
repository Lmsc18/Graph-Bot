import os
from dotenv import load_dotenv
load_dotenv()
from plotter.plotter import graph_chain
import streamlit as st
from plotter.graph_gen import line_plot,bar_plot
import pandas as pd

def generate_graph(question):
    out=graph_chain.invoke(question).dict()
    return out

st.title("Graph Plotting App")

input_text = st.text_input("Enter some text:")


if st.button("Generate Graph"):
    # Call the process_text function with the input text
    output_text = generate_graph(input_text)
    data={output_text['x_axis_name']:output_text['x_axis'],output_text['y_axis_name']:output_text["y_axis"]}
    df=pd.DataFrame(data)
    df.set_index(output_text['x_axis_name'], inplace=True)
    if output_text['graph_type']=="line":
        st.write("**Question:** ",input_text)
        st.write("**Description of the Graph:** ",output_text['explanation'])
        st.line_chart(df)
    else:
        st.write("**Question:** ",input_text)
        st.write("**Description of the Graph:** ",output_text['explanation'])
        st.bar_chart(df)




