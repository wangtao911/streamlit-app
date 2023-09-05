# streamlit_app.py
import streamlit as st
import datetime
import pandas as pd
import numpy as np
import graphviz
st.set_page_config(
    page_title="源目绘图 v1",
    page_icon='❇️',
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# 源头与目的绘图，类似物流订单. \n # This is an *Simple* app! \n by WangTao"
    }
)

with st.sidebar:
    cols = st.columns([1,2])
    shapes = ['box', 'egg', 'star', 'house', 'note']
    with cols[0]:
        shape = st.selectbox("节点外形:", shapes)
    with cols[1]:
        dpi = st.slider("清晰度:", 10, 600, 200, 10)

    col1, col2,col3 = st.columns([2,2,2])
    with col1:
        start_loc_df = pd.DataFrame(
            [
                {'提货地址':'A地址'},
                {'提货地址':'B地址'},
            ]
        )
        start_loc_edited_df = st.data_editor(start_loc_df,key="star",
            num_rows="dynamic")
    with col2:
        end_loc_df = pd.DataFrame(
            [
                {'目的地址':'B地址'},
                {'目的地址':'A地址'},
            ]
        )
        end_loc_df_edited_df = st.data_editor(end_loc_df,key="end",
            num_rows="dynamic")
    with col3:
        comm_df = pd.DataFrame(
            [
                {'备注':'原因aaa'},
                {'备注':'原因bbb'},
            ]
        )
        comm_edited_df = st.data_editor(comm_df,key="comm",
            num_rows="dynamic")

wuliu_df = pd.DataFrame()
wuliu_df['start'] = start_loc_edited_df['提货地址']
wuliu_df['end']   = end_loc_df_edited_df['目的地址']
wuliu_df['comm']  = comm_edited_df['备注']
#wuliu_df['flow'] = wuliu_df['start']+"->"+wuliu_df['end']
#st.dataframe(wuliu_df)

s_list=[]
e_list=[]
c_list=[]
for s in wuliu_df['start']:
    s_list.append(s)
for e in wuliu_df['end']:
    e_list.append(e)
for c in wuliu_df['comm']:
    c_list.append(c)

#graphviz.set_default_engine()
graph = graphviz.Digraph()
graph.node_attr['shape'] = shape
for i in range(len(s_list)):
    graph.edge(s_list[i],e_list[i],label=c_list[i], shape='box')

st.graphviz_chart(graph)
