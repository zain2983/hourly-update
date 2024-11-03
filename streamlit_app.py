# import streamlit as st

# st.title("🎈 Zain Ki Test App")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )




import streamlit as st

def embed_youtube_video(video_url):
    """
    Embeds a YouTube video in a Streamlit app
    Args:
        video_url (str): Full YouTube video URL or video ID
    """
    # Extract video ID if full URL is provided
    if "youtube.com" in video_url:
        video_id = video_url.split("v=")[1].split("&")[0]
    elif "youtu.be" in video_url:
        video_id = video_url.split("/")[-1]
    else:
        video_id = video_url  # Assume the provided string is already a video ID

    # Create YouTube embed HTML
    youtube_html = f"""
        <iframe
            width="100%"
            height="400"
            src="https://www.youtube.com/embed/{video_id}"
            frameborder="0"
            allowfullscreen
        ></iframe>
    """
    
    # Display the video using streamlit's html component
    st.markdown(youtube_html, unsafe_allow_html=True)

# Example usage
def main():
    st.title("Get rick rolled Son")
    
    # # Input field for YouTube URL
    # video_url = st.text_input("Enter YouTube Video URL or ID")
    
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    if video_url:
        embed_youtube_video(video_url)

if __name__ == "__main__":
    main()