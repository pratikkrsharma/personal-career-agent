import app
import gradio as gr
# from vectordb import create_vector_db

if __name__ == "__main__":
    # create_vector_db()
    me = app.Me()
    gr.ChatInterface(me.chat, type="messages").launch()
