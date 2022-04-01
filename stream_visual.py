import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import plotly.express as px
from PIL import Image

df = pd.read_csv("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Resturantdata.csv")
df_pub = pd.read_csv("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Pubdata.csv")
df_hotel = pd.read_csv("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Hoteldata.csv")


plt.rcdefaults()
plt.rcParams.update({'axes.facecolor':'black'})
plt.figure(facecolor='black')

# df_test = pd.read_csv("C:/Users/andre/Desktop/Resturantdata.csv")



data_select = st.sidebar.selectbox("Select the data you want to see", ("Home", "Restaurants", "Hotels", "Pubs"))

#   Homepage
if data_select == "Home":

    image_1 = Image.open("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/img1.jpg")
    image_2 = Image.open("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/img2.png")

    st.title('Accommodation, Restaurants & Drink Services in Berlin')
    st.image(image_1)
    st.header('Why accommodation, food, and drink services industry?')
    st.markdown("""The accommodation industry and the food and drink services industry have faced unprecedented change due to the coronavirus (COVID-19) pandemic.
    Up until this moment, the accommodation, food, and drink services industry have been seeing consistent year-over-year growth in all its sectors.
    Yet, while the pandemic has proved to be a difficult time for these industries, it is still predicted to see growth (Statista, n.d.).""")

    st.header('Why Berlin?')
    st.markdown("""Investing in Berlin is an interesting opportunity from an economic point of view, demographic and geographic. 
    The city of Berlin offers more and more settlement opportunities to international companies.
    Every year, the population of Berlin increases, and the growth potential is still very strong due to the space available.
    The capital of an economically strong country is now the geographical centre of the European Union (AB Real Estate GmbH, n.d.).""")

    st.header('Goals and data source')
    st.markdown("""In this analysis, it has been studied the dynamics of the main accommodation activities, restaurants, and pubs in the city of Berlin.
    The main goal of our project is to provide our investors some suggestions about the characteristics of reliable activities to invest in.
    This analysis was conducted collecting data from Yelp about hotels, restaurants, and pubs in Berlin. Therefore, the data from these three categories and the rate has been compared to provide some recommendation.""")


    st.header('Team members')
    st.image(image_2)

    st.header('Sources')
    st.markdown("""AB Real Estate GmbH. (n.d.). Invest in Berlin estate. Retrieved March 31, 2022, from Invest-AB: https://www.invest-ab.com/invest-in-berlin/""")
    st.markdown("""Statista. (n.d.). Food & Drink Services. Retrieved March 31, 2022, from Statista: https://www.statista.com/markets/420/topic/494/food-drink-services/#overview""")

    # px.set_mapbox_access_token(open(".mapbox_token").read())
    # fig = px.scatter_mapbox(df_test, lat="Latitude", lon="Longitude",zoom=12, size = 'reviews', color='rating', 
    # width=900, height=600, opacity=1, template="plotly_dark")
    # st.plotly_chart(fig) 

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

    st.subheader('Need to do it faincier')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    new = df[df['Number_of_reviews']>280]
    new = new.sort_values('Number_of_reviews',ascending=False)
    new.plot(x='Type_of_resturant',y='Number_of_reviews',kind='bar')
    st.pyplot()





    #   Graph n.3

    fig = px.bar(df['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
            "value": "Number of Restaurants with respective price range",
            "index": "Price range (in euros)"
    },
    title='Price range of restaurants in Berlin')
    st.write(fig)    
    
    #   Graph n.4

    st.subheader('Graph Title - to do')
    df_type = px.bar(df["Type_of_resturant"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of restaurants",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')

    #   Graph n.4 
    
    # Test

    # st.subheader('Average rating compared to price range')
    # fig = px.bar(x = df.groupby('Prices')['Ratings'].agg('mean').sort_values().values, 
    # y = df.groupby('Prices')['Ratings'].agg('mean').sort_values().index,
    # height=600, width=800, 
    # labels={
    #         "x": "Average rating",
    #         "y": "Price range"
    # })
    # st.plotly_chart(fig)



    # st.subheader('Average rating compared to price range')
    # fig = px.bar(x = df.groupby('Number_of_reviews')['Ratings'].agg('mean').sort_values().values, 
    # y = df.groupby('Number_of_reviews')['Ratings'].agg('mean').sort_values().index,
    # height=600, width=800, 
    # labels={
    #         "x": "Average rating",
    #         "y": "Price range"
    # })
    # st.plotly_chart(fig)

    #   finished test

    #   Graph n.5
    st.subheader('Need to do it faincier')

    st.set_option('deprecation.showPyplotGlobalUse', False)
    df[['Ratings','Prices']].groupby(['Prices']).value_counts().plot(kind='bar')
    plt.ylabel('Counts')
    plt.title('Most prefered price range')
    st.pyplot()
    st.text('Little description here')
    #   Graph n.5

    # st.subheader('Need to do it faincier')
    # df[['Type_of_resturant','Ratings']].groupby('Type_of_resturant').value_counts().nlargest(10). plot(kind='barh')

    # plt.xlabel('Counts')
    # plt.title('Most prefered type of restaurant by rating')
    # st.pyplot()
    



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
    plt.figure(facecolor='white')

    df_hotel['Neighbourhoods'].value_counts().nlargest(10).plot(kind = 'pie',figsize=(8,8), autopct = '%1.1f%%')
    
    plt.title('Cluster location of hotels')
    st.pyplot()


#   Graph n.3

    st.subheader('Graph Title - to do')
    fig = px.bar(df_hotel['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
        "value": "Number of hotels with respective price range",
        "index": "Price range (in euros)"
    },
    title='Price range of hotels in Berlin')
    st.write(fig)   

    st.text('Little description here')


#   Graph n.4

    st.subheader('Graph Title - to do')
    df_hotel[['Ratings','Prices']].groupby(['Prices']).value_counts().plot(kind='bar')
    plt.ylabel('Counts')
    plt.title('Most prefered price range')
    st.pyplot()
    st.text('Little description here')


#   Graph n.5
    st.subheader('Graph Title - to do')
    df_hotel[['Prices','Number_of_reviews']].groupby(['Prices']).sum().plot(kind='bar')
    plt.ylabel('Counts')
    plt.title('Most prefered price range')
    st.pyplot()
    st.text('Little description here')



#   Graph n.5

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
    fig=px.bar(df_pub['Neighbourhoods'].value_counts(), orientation='h', height=750, width=850, labels={
        "value": "Number of pubs per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)

    st.text('Little description here')

#   Graph n.2

    plt.figure(facecolor='white')

    df_pub['Neighbourhoods'].value_counts().nlargest(10).plot(kind = 'pie',figsize=(8,8), autopct = '%1.1f%%')
    
    plt.title('Cluster location of hotels')
    st.pyplot()


#   Graph n.3

    fig = px.bar(df_pub['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
        "value": "Number of pubs with respective price range",
        "index": "Price range (in euros)"
    },
    title='Price range of pubs in Berlin')
    st.write(fig)   

    st.text('Little description here')



    df_pub[['Ratings','Prices']].groupby(['Prices']).value_counts().plot(kind='bar')
    plt.ylabel('Counts')
    plt.title('Most prefered price range')
    st.pyplot()
    st.text('Little description here')

#   Graph n.3

    st.subheader('Graph Title - to do')
    df_type = px.bar(df_pub["Type_of_pubs"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of pubs",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')













