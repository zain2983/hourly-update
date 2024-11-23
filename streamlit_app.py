
from __future__ import print_function
import time
import datetime
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint




from datetime import datetime
# Get the current time
def get_time():
  current_time = datetime.now()
  # Format the time as HH:MM:SS
  tame = current_time.strftime("%Y-%m-%d %H:%M:%S")
  return tame
  
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))





import streamlit as st

# Initialize session state for recipients
if "recipients" not in st.session_state:
    st.session_state.recipients = []

# Function to add a recipient (new entries at the top)
def add_recipient(email):
    if email and email not in st.session_state.recipients:
        st.session_state.recipients.insert(0, email)  # Add to the beginning of the list

# Function to remove a recipient
def remove_recipient(email):
    st.session_state.recipients.remove(email)

# App Layout
st.title("Email Sending App")

# Message Input
message = st.text_area("Enter your message", height=150)

# Add Recipient Input
with st.form(key="add_recipient_form"):
    email_input = st.text_input("Enter recipient email")
    add_button = st.form_submit_button("Add Recipient")
    if add_button:
        add_recipient(email_input)

# Display Recipients in a Streamlit container
st.write("### Recipients:")
recipient_container = st.container(height=250)

if st.session_state.recipients:
    with recipient_container:
        for email in st.session_state.recipients:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(email)
            with col2:
                if st.button("❌", key=email):
                    remove_recipient(email)
else:
    with recipient_container:
        st.info("No recipients added yet.")



# Send Email Button
if st.button("Send Email"):
    if not message.strip():
        st.error("Please enter a message.")
    elif not st.session_state.recipients:
        st.error("Please add at least one recipient.")
    else:
        # Send email using Brevo (formerly Sendinblue) API
        # api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient())
        email_content = f"""
        <html>
        <body>
            <p>{message}</p>
        </body>
        </html>
        """
        
        email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": recipient} for recipient in st.session_state.recipients],
            sender={"email": "jfhdk99879@gmail.com", "name": "Younus Marketing"},  # Replace with your email and name
            subject="Hi, How are you doing?",
            html_content=email_content
        )

        try:
            # Send the email
            response = api_instance.send_transac_email(email)
            st.success(f"Email sent successfully! Response: {response}")
        except ApiException as e:
            st.error(f"Exception when sending email: {e}")


# # Email details
# email = sib_api_v3_sdk.SendSmtpEmail(
#     to=[{"email": "zainijaz2983@gmail.com", "name": "Recipient Name"}],  # Replace with recipient's email and name
#     sender={"email": "jfhdk99879@gmail.com", "name": "Younus Marketing"},   # Replace with your email and name
#     subject="Hi, How are you doing ?",
#     html_content=email_content
# )

# try:
#     # Send the email
#     response = api_instance.send_transac_email(email)
#     print("Email sent successfully! Response:", response)
# except ApiException as e:
#     print("Exception when sending email:", e)
