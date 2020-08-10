import streamlit as st
from src import strs as s
from src import back as b

def main():
    st.markdown(
        s.title,
        unsafe_allow_html=True,
    )
    st.text("""""")
    
    st.markdown(
    s.about, unsafe_allow_html=True
    )
    st.markdown(s.hr, unsafe_allow_html=True)
    st.markdown(
    s.about_1,
    unsafe_allow_html=True,
    )
    st.markdown(
        s.about_2,
        unsafe_allow_html=True,
    )
    st.text("""""")
    
    st.markdown(
    s.howToUseIt, unsafe_allow_html=True
    )
    st.markdown(s.hr, unsafe_allow_html=True)
    st.write(s.howToUseIt_1)
    st.text("""""")

    st.markdown(
    s.disclaimer, unsafe_allow_html=True
    )
    st.markdown(s.hr, unsafe_allow_html=True)
    st.write(s.disclaimer_1)
    st.text("""""")

    st.markdown(
    s.use_it, unsafe_allow_html=True
    )
    st.markdown(s.hr, unsafe_allow_html=True)
    url = st.text_input(s.use_it_11, s.use_it_12)
    user_price = st.text_input(s.use_it_21, s.use_it_22)
    user_mail_id = st.text_input(s.use_it_31, s.use_it_32)
    st.text("""""")
    st.text("""""")
    send_notification = st.button(s.button_name)
    st.text("""""")
    if send_notification:
        try:
            user_price_float = float(user_price)
            if 'amazon.in' in url:
                b.main(url, user_price_float, user_mail_id)
            else:
                st.markdown(s.not_amazon_in, unsafe_allow_html=True)
        except:
            st.write(s.not_number_warning)
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.text("""""")
    st.write(s.copy_right)

    st.sidebar.markdown(s.sidebar, unsafe_allow_html=True)