from db import create_db,insert_data,select_data,update_data,delete_data
import streamlit as st
tab1,tab2,tab3,tab4 = st.tabs(
    ["Add Contact","Show Data","Delete data","Update data"]
)
with tab1:
    name = st.text_input("Enter your  name, type here:")
    phone_number = st.text_input(
        label="Phone Number",
        max_chars=15,
        placeholder="+1 (555) 000-0000",
        help="Enter your full phone number including country code.")
    email =st.text_input("Enter the email, type here")
    if st.button("Submit"):
        if name and name.strip():
            create_db()
            st.success(f"Database initialized and Welcome {name}!")
            insert_data((name,phone_number,email))
        else:
            st.warning("Please enter a name before submitting")

with tab2:
    if st.button("Show data"):
        columns=['ID','Name','Phone','Email']
        df= select_data()

        st.dataframe(df,column_config={
            "0":"ID",
            "1":"Name",
            "2":"Phone",
            "3":"Email"},use_container_width=True)
    



with tab3:
    del_data=st.text_input("Enter your id:")
    if st.button("Delete"): 
        delete_data(del_data)

with tab4:
    upd_data= st.text_input("Enter your id:",key="my_custom_id_box")
    name1 = st.text_input("Enter your  name, type here:",key = "farid")
    phone_number1 = st.text_input(
            label="Phone Number",
            max_chars=15,
            placeholder="+1 (555) 000-0000",
            help="Enter your full phone number including country code.",
            key = "FARID@")
    email1 =st.text_input("Enter the email, type here",key="MUHAMMED FARID")
    if st.button("Update"):
   
        update_data(upd_data,name=name1,phone=phone_number1,email_address=email1)
        