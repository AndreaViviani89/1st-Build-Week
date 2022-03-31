import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import plotly.express as px
from PIL import Image

df = pd.read_csv("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Resturantdata.csv")
df_pub = pd.read_csv("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Pubdata.csv")
df_hotel = pd.read_csv("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Hoteldata.csv")



data_select = st.sidebar.selectbox("Select the data you want to see", ("Home", "Restaurants", "Hotels", "Pubs"))

#   Homepage
if data_select == "Home":


    st.title("Welcome")
    st.header('Team member')
    st.markdown('* *Andrea*')
    st.markdown('* *Eunice*')

    st.title('Accommodation, Restaurants & Drink Services in Berlin')
    st.header('Why accommodation, food, and drink services industry?')
    st.markdown("""The accommodation industry and the food and drink services industry have faced unprecedented change due to the coronavirus (COVID-19) pandemic.
    Up until this moment, the accommodation, food, and drink services industry have been seeing consistent year-over-year growth in all its sectors.
    Yet, while the pandemic has proved to be a difficult time for these industries, it is still predicted to see growth.""")

#   Restaurants
elif data_select == "Restaurants":

    st.title("Restaurant insights")
    
    #   Graph n.1

    st.subheader('Graph Title - to do')
    fig=px.bar(df['Neighbourhoods'].value_counts(), height=600, width=800, labels={
        "value": "Number of restaurants per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)
    
    st.text('Little description here')

    #   Graph n.2

    fig = px.bar(df['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
            "value": "Number of Restaurants with respective price range",
            "index": "Price range (in euros)"
    },
    title='Price range of restaurants in Berlin')
    st.write(fig)    
    
    #   Graph n.3

    st.subheader('Graph Title - to do')
    df_type = px.bar(df["Type_of_resturant"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of restaurants",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')

    #   Graph n.4 
    
    st.subheader('Need to do it faincier')

    st.set_option('deprecation.showPyplotGlobalUse', False)
    df[['Ratings','Prices']].groupby(['Prices']).value_counts().plot(kind='bar')
    plt.ylabel('Counts')
    plt.title('Most prefered price range')
    st.pyplot()

    #   Fancier but..
    df_prices = df[['Ratings','Prices']].groupby(['Prices']).value_counts()
    test = px.bar(df_prices, x=df_prices.index.get_level_values(1),y=0)
    st.write(test)
    st.text('Little description here')

    #   Graph n.5

    st.subheader('Need to do it faincier')
    df[['Type_of_resturant','Ratings']].groupby('Type_of_resturant').value_counts().nlargest(10). plot(kind='barh')

    plt.xlabel('Counts')
    plt.title('Most prefered type of restaurant by rating')
    st.pyplot()
    st.text('Little description here')



#   Hotels

elif data_select == "Hotels":

    st.title("Hotels insights")


#   Graph n.1

    st.subheader('Graph Title - to do')
    fig=px.bar(df_hotel['Neighbourhoods'].value_counts(), orientation='h', height=700, width=850, labels={
        "value": "Number of hotels per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)

    st.text('Little description here')


#   Graph n.2

    fig = px.bar(df_hotel['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
        "value": "Number of hotels with respective price range",
        "index": "Price range (in euros)"
    },
    title='Price range of hotels in Berlin')
    st.write(fig)   

    st.text('Little description here')


#   Graph n.3

    st.subheader('Graph Title - to do')
    df_type = px.bar(df_hotel["Type_of_hotels"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of hotels",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')




#   Pubs

elif data_select == "Pubs":

    st.title("Pubs insights")


#   Graph n.1

    st.subheader('Graph Title - to do')
    fig=px.bar(df_pub['Neighbourhoods'].value_counts(), orientation='h', height=700, width=850, labels={
        "value": "Number of pubs per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)

    st.text('Little description here')


#   Graph n.2

    fig = px.bar(df_pub['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
        "value": "Number of pubs with respective price range",
        "index": "Price range (in euros)"
    },
    title='Price range of pubs in Berlin')
    st.write(fig)   

    st.text('Little description here')


#   Graph n.3

    st.subheader('Graph Title - to do')
    df_type = px.bar(df_pub["Type_of_pubs"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of pubs",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')













