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
        #dpi = st.slider("清晰度:", 10, 600, 200, 10)

    col1, col2,col3 = st.columns([2,2,2])
    with col1:
        start_loc_df = pd.DataFrame(
            [
                {'起点':'A site'},
                {'起点':'B site'},
            ]
        )
        start_loc_edited_df = st.data_editor(start_loc_df,key="star",
            num_rows="dynamic")
    with col2:
        end_loc_df = pd.DataFrame(
            [
                {'终点':'B site'},
                {'终点':'C site'},
            ]
        )
        end_loc_df_edited_df = st.data_editor(end_loc_df,key="end",
            num_rows="dynamic")
    with col3:
        comm_df = pd.DataFrame(
            [
                {'备注':'aaa'},
                {'备注':'4456'},
            ]
        )
        comm_edited_df = st.data_editor(comm_df,key="comm",
            num_rows="dynamic")

wuliu_df = pd.DataFrame()
wuliu_df['start'] = start_loc_edited_df['起点']
wuliu_df['end']   = end_loc_df_edited_df['终点']
wuliu_df['comm']  = comm_edited_df['备注']
#wuliu_df['flow'] = wuliu_df['start']+"->"+wuliu_df['end']
#st.dataframe(wuliu_df)

s_list=[]
e_list=[]
c_list=[]
for s in wuliu_df['start']:
    s_list.append(str(s))
for e in wuliu_df['end']:
    e_list.append(str(e))
for c in wuliu_df['comm']:
    c_list.append(str(c))

max = (max(len(start_loc_edited_df),len(end_loc_df_edited_df),len(comm_edited_df)))
if len(s_list) < max :
    i = max - len(s_list)
    for n in range(i):
        s_list.append('空-起始')

if len(e_list) < max :
    i = max - len(e_list)
    for n in range(i):
        e_list.append('空-目的')

if len(c_list) < max :
    i = max - len(c_list)
    for n in range(i):
        c_list.append('')

#graphviz.set_default_engine()
graph = graphviz.Digraph()
graph.node_attr['shape'] = shape
for i in range(len(s_list)):
    graph.edge(s_list[i],e_list[i],label=c_list[i], shape='box')

st.graphviz_chart(graph)
