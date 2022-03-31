import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import plotly.express as px

df = pd.read_csv("C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Resturantdata.csv")



data_select = st.sidebar.selectbox("Select the data you want to see", ("Home", "Restaurants", "Hotels", "Pubs"))


if data_select == "Home":

    st.title("Welcome")
    st.header('Team member')
    st.markdown('* *Andrea*')
    st.markdown('* *Eunice*')


#   Restaurants

elif data_select == "Restaurants":

    st.title("Restaurant insights")


    #   First graph

    # st.subheader('Graph Title - to do')       --> Made a better version with plotly

    # fig1 = df['Neighbourhoods'].value_counts()
    # plt.xlabel('Locations')
    # plt.ylabel('Counts')

    # st.bar_chart(fig1)

    

    # st.subheader('Graph Title - to do')
    # df_neigh = df["Neighbourhoods"].value_counts()
    # go = px.bar(df_neigh, x='Neighbourhoods')
    # st.write(go)
    # st.text('Little description here')
    
    st.subheader('Graph Title - to do')
    fig=px.bar(df['Neighbourhoods'].value_counts(), height=600, width=800, labels={
        "value": "Number of restaurants per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)
    
    st.text('Little description here')
    
    
    #   Second graph
    
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


    #   Third graph
    st.subheader('Need to do it faincier')
    df[['Type_of_resturant','Ratings']].groupby('Type_of_resturant').value_counts().nlargest(10). plot(kind='barh')

    plt.xlabel('Counts')
    plt.title('Most prefered type of restaurant by rating')
    st.pyplot()




    # Graph
    st.text('Little description here')



    fig = px.bar(df['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
            "value": "Number of Restaurants with respective price range",
            "index": "Price range (in euros)"
    },
    title='Price range of restaurants in Berlin')
    st.write(fig)



    st.subheader('Graph Title - to do')
    df_type = px.bar(df["Type_of_resturant"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of restaurants",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')






    # fig2 = df[['Neighbourhoods','Ratings']].groupby('Ratings').value_counts()
    # go = px.bar(fig2, x='Neighbourhoods', y='Ratings')
    # st.write(fig2)





    # fig2 = df[['Neighbourhoods','Ratings']].groupby('Ratings').value_counts()
    # plt.xlabel
    # plt.ylabel


    # st.bar_chart(fig2)






    # Need to fix it
    # fig = px.scatter(data_frame=df, x = 'Number_of_reviews', y = 'Ratings', color = 'Index', template = 'seaborn',
    #     title = 'Test' )


#   Hotels

elif data_select == "Hotels":

    st.title("Hotels insights")










#       '''first way'''

# sidebar = st.sidebar
# header = st.container()

# with sidebar:
#     st.header('Team member')
#     st.markdown('* **Andrea**')
#     st.markdown('* **Eunice**')


#     st.header('Data analyze')
#     st.markdown('* **1:** Yelp web scraping.')



#       '''second way'''

# st.title("Welcome to Yelp web scraping challenge")
# st.subheader("Let's have a look")


# headers = ['Home', 'Restaurants', 'Hotels', 'Pubs']
# df = pd.read_csv(r'C:/Users/andre/Documents/Strive_repository/1st-Build-Week/Data/Resturantdata.csv', header=0)

# if st.button('Show data'):
#     st.dataframe(df)


# book_input = st.text_input('Names')
# df1 = df.loc[df['Names'].str.contains(book_input, flags=re.IGNORECASE)]
# if len(book_input) > 0:
#     st.dataframe(df1)