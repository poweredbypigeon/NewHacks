# app.py
import os
from dotenv import load_dotenv
import streamlit as st
from auth0.v3.authentication import GetToken
from jose import jwt

# Load environment variables
load_dotenv()

AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")

# Auth0 authentication functions
def get_auth0_token():
    domain = f"https://{AUTH0_DOMAIN}/"
    client_id = AUTH0_CLIENT_ID
    client_secret = AUTH0_CLIENT_SECRET
    audience = "https://your-api-audience"

    get_token = GetToken(domain)
    return get_token.client_credentials(client_id, client_secret, audience)

def decode_jwt(token):
    return jwt.decode(token, algorithms=["RS256"], audience="your-api-audience", issuer=f"https://{AUTH0_DOMAIN}/")

def secure_app():
    st.title("Secure Streamlit App")
    st.write("Welcome to the secure section of the app!")

def main():
    st.title("Streamlit App with Auth0")

    if st.button("Login"):
        token = get_auth0_token()["access_token"]
        decoded_token = decode_jwt(token)

        if "sub" in decoded_token:
            st.success(f"Successfully logged in as {decoded_token['sub']}")
            secure_app()
        else:
            st.error("Authentication failed. Please check your credentials.")

if __name__ == "__main__":
    main()
