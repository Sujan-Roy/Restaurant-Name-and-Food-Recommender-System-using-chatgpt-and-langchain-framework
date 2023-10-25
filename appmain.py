import streamlit as st
import langchainhelper as lch
st.title("Restaurant Name and Food Recommender System")

name=st.sidebar.selectbox("Select a country",["Bangladesh","India","Japan","USA","Russia", "Thailand"])



if name:
    response= lch.generate_restaurant_name_and_foodItems(name)

    st.header(response['restaurant_name'].strip())
    food_items= response['food_item'].strip().split(",")
    st.write("**Food Items**")
    for food_item in food_items:
        st.write(food_item)
 