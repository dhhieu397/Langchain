import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexico", "American", "Japanese"))



if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    # print(menu_items)
    st.write("**Menu Items**\n")

    for item in menu_items:
        st.write("-", item)



 





#  python3 -m streamlit run main.py