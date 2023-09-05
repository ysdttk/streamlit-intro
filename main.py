import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration =st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

    
left_column,right_column = st.columns(2)

button= left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander =st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')   
# text = st.text_input('あなたの趣味を教えてください')

# 'あなたの好きな趣味は、', text,'です'

# condition = st.slider('あなたの今の調子は？',0, 100, 50)
# 'コンディション' ,condition
# if st.checkbox('Show Image'):
#    img=Image.open('sample.jpg')
#    st.image(img,caption='otoware', use_column_width = True)


#st.table(df.style.highlight_max(axis=0))
#st.map(df)
