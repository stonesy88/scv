import streamlit as st

# Layout for the title and the logo
col1, col2 = st.columns([3, 1])
with col1:
    st.title('Single Customer View')
with col2:
    # Direct link to the image
    st.image('https://upload.wikimedia.org/wikipedia/commons/0/01/New-betfred-logo.png')

# Rest of your Streamlit code
# ...

# Tab for the SCV Graph Analysis - Replace with the correct direct URL to the image
with tab1:
    # Placeholder image URL
    placeholder_image_url = 'https://pyvis.readthedocs.io/en/latest/_images/net.png'  # Replace with the direct URL to the image
    st.image(placeholder_image_url, caption='Network Graph Placeholder')

# ...
