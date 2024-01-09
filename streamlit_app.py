import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
# don't run anything past here while we troubleshoot 
streamlit.title ('My parents new healthy Diner')
streamlit.header ( 'Breakfast Menu') 
streamlit.text ('🥣 Omega 3 and Bluebury OatMeal')  
streamlit.text ('🥗 Kale, Spinach and Rocket Smoothie') 
streamlit.text ( '🐔 Hard Boiled Free Range Eggs') 
streamlit.text ( '🥑🍞 Avacado Toast')    
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruit_to_shows= my_fruit_list.loc [fruits_selected]
# Display the table on the page.
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruit_to_shows)
# new section to display response from fruityvise respnse
streamlit.header("Fruityvice Fruit Advice!")
# create a funciton 
def get_fruityvice_data (this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
      return fruityvice_normalized
try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data (fruit_choice)
    streamlit.dataframe (back_from_function)
   #  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   #  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   #  streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error ()
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

streamlit.header("Food load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
 With my_cnx.cursor() as my_cur:
      my_cur.execute(“Select * from fruit_load_list”)
Return my_cur.fetchall()

# Add a button to load the fruit
If streamlit.button(‘Get Fruit Load list’):
my_cnx=snowflake.connector.connect (**streamlist.secrets[“snowflake”])
my_data_rows=get_fruit_load_list()
streamlit.dataframe(my_data_rows)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("Select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
# my_data_row = my_cur.fetchone()
my_data_rows=my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
#streamlit.header("Food load list contains:")
# streamlit.dataframe(my_data_row) # Fetch one row
#streamlit.dataframe(my_data_rows) # Fetch all rows
#streamlit.stop()
# allow end user to add fruit in the list 
fruit_choice_inserted = streamlit.text_input('What fruit would you like to add ?')
streamlit.write('The user inserted ', fruit_choice_inserted)
my_cur.execute ( "insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")

