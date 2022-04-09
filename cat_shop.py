# Cats Mini Project

#In this part of the activity you will import the functions from your wallet.py file and create an interface using streamlit

#In this portion of the activity we will create an interface and check our balance in ether to determine if we are able to purchase a cat.

# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from PIL import Image



# @TODO: # From crypto_wallet.py import w3, generate_account, get_balance
from crypto_wallet import w3, generate_account, get_balance

################################################################################
# Cat Information

# Database of cats including their name, digital address, rating and in Ether.
# A single Ether is currently valued at $3,900

cat_database = {
    "Jennifurr": ["Jennifurr", 22],
    "Cheddar": ["Cheddar", 151],
    "Meowise": ["Meowise", 31],
}

# Create a list of the the cats by first names
kitties = ["Jennifurr", "Cheddar", "Meowise"]

# Create a get_cats function to display the purchase information from the cats
def get_cats():
    """Display the database of cats to purchase information."""
    db_list = list(cat_database.values())
# Create a for loop through the cat_database use `db_list to produce the results`
    for number in range(len(kitties)):

  # @TODO Use `st.write` to add the objects from the object to the code (hint price and name)
      st.write('Name: ', db_list[number][0])
      st.write('Price in Ether: ', db_list[number][1],'eth')
      st.text(" \n")
################################################################################
# Streamlit Code

# @TODO Create Streamlit application headings using `st.markdown` to explain this app is for buying kitties
st.markdown('# Kitties')
st.markdown('## Buy a Kitty!')
st.text(" \n")

# @TODO: Call the `generate_account` function and save it as a variable  called `account`.
account = generate_account()
# @TODO: Call the `get_balance` function and save it as the variable `ether`
ether = get_balance(account.address)
# Disply the balance of ether in the account
st.sidebar.markdown("## Your Balance of Ether")
st.sidebar.markdown(ether)
st.sidebar.markdown("---------")

col1 = st.sidebar
col2, col3 = st.columns((1, 1))


# @TODO: Create a select box to chose a Cat using `st.sidebar.selectbox`
cat = st.sidebar.selectbox('Select a cat', kitties)
width = 100
with col1:
  if cat == "Jennifurr":
    image = Image.open('cat1.jpg')
    st.image(image)
  elif cat == "Cheddar":
    image = Image.open('cat2.jpg')
    st.image(image)
  elif cat == "Meowise":
    image = Image.open('cat3.jpg')
    st.image(image)
# @TODO: Create a header using ` st.sidebar.markdown()` to display cat name and price.
col1.markdown('## Cat Name and Price')
# Identify the cat for purchase by name
width = 100
with col2:
  if cat == "Jennifurr":
    image = Image.open('cat1.jpg')
    st.image(image)
  elif cat == "Cheddar":
    image = Image.open('cat2.jpg')
    st.image(image)
  elif cat == "Meowise":
    image = Image.open('cat3.jpg')
    st.image(image)
cat = cat_database[cat][0]

#@TODO: Create a variable called cat_price to retrive the cat price
cat_price = cat_database[cat][1]
#@TODO: create an if else statement to check if the selected cat can be purchased
if cat_price <= ether:
  new_balance = float(ether) - float(cat_price) 
# Write the cats name to the sidebar
  st.sidebar.write("If you buy", cat, "for", cat_price, "eth, your account balance will be", new_balance, ".")
  get_cats()
else:
  st.sidebar.write("With a balance of", ether, "ether, you can't buy", cat, "for", cat_price, "eth." )
  get_cats()

with col3:
  vid_file = open("example.mp4", "rb").read()
  st.video(vid_file,format="video/mp4")

  
