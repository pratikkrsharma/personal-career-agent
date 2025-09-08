from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import ssl
import smtplib
from email.mime.text import MIMEText
import gradio as gr
# from vectordb import load_vector_db

load_dotenv(override=True)


def notification(message):
    try:
        message = json.loads(message)
        subject = message["subject"]
        body = message["body"]
        receiver_address = os.environ.get("RECEIVER_MAIL_ADDRESS")
        sender_address = os.environ.get("SENDER_MAIL_ADDRESS")
        sender_password = os.environ.get("MAIL_PASSWORD")
        if not receiver_address or not sender_address or not sender_password:
            raise ValueError("RECEIVER_MAIL_ADDRESS or MAIL_ADDRESS or MAIL_PASSWORD environment variables must be set.")

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(sender_address, sender_password)

            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = sender_address
            msg["To"] = receiver_address
            server.sendmail(sender_address, receiver_address, msg.as_string())
            # print("📧 Notification email sent.")
    except Exception as e:
        print(f"❌ Failed to send notification: {e}")


class Me:
    def __init__(self):
        self.name = "Pratik Sharma"
        # self.vector_db = load_vector_db()
        self.openai = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

    def system_prompt(self):
        return f"""You are acting as {self.name}. You are answering questions on {self.name}'s website, \
        particularly questions related to {self.name}'s career, background, skills, and experience. \
        Start the conversation by asking their name. Once user reply with name, then ask them how I can you help with details related of {self.name}. \
        Be helpful, professional, and engaging like you're speaking to a potential client or employer. \
        If you think the user wants to get in touch with {self.name} or want to contact {self.name}, Share them Pratik's email and phone number. \
        Also at same time ask them their email or phone number and also ask if any messsage that they want to convey to Pratik ? \
        Once user has responded with their details and message to Pratik, then respond in this **strict format**: \
        'send notification to {self.name} that this person with <user email id> or <user phone number> wants to get in touch with you'"""

    def chat(self, message, history):
        # docs = self.vector_db.similarity_search(message, k=5)
        # context = "\n\n".join([doc.page_content for doc in docs])
        with open("me/Profile.txt", "r", encoding="utf-8") as f:
            profile_details = f.read()
        messages = [{"role": "system", "content": self.system_prompt() + "\n\n## .Profile Details:\n" + profile_details + f" \n Each section in Profile details starts with ##. With this context, please chat with the user, always staying in character as {self.name}."}]
        messages += history + [{"role": "user", "content": message}]

        response = self.openai.chat.completions.create(
            model="tngtech/deepseek-r1t2-chimera:free",  # Or any model that fits
            messages=messages,
        )
        # Safely extract the reply content, handling possible None values
        reply_content = getattr(response.choices[0].message, "content", None)
        reply = reply_content.strip() if reply_content else ""

        # Detect intent to notify
        if "send notification to pratik sharma" in reply.lower():

            # Construct message
            message_payload = {
                "subject": "New Contact Request from Personal Career Agent",
                "body": f"A visitor wants to get in touch.\n\n Message:\n '{message}'\n\n LLM Response:\n{reply}"
            }

            notification(json.dumps(message_payload))

            # Replace user response with pre-written contact info
            return f"Thank you! Your messsage has been sent to Pratik. Is there anything else I can helo you with ?\n \
                    You can also directly email **pratikkrsharma@gmail.com** or call **+91-8217824920** for quicker assistance."

        return reply


if __name__ == "__main__":
    me = Me()
    gr.ChatInterface(me.chat, type="messages").launch()
