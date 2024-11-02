import speech_recognition as sr
import pywhatkit
import time

# Function to capture voice input and convert to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized command: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Network error.")
    return None

# Function to process commands based on recognized text
def process_command(command):
    if 'send message' in command:
        send_whatsapp_message(command)
    elif 'send file' in command:
        # Trigger file sending function (implement separately)
        print("File sending feature is coming soon.")
    elif 'contact' in command:
        # Trigger contact sharing function (implement separately)
        print("Contact sharing feature is coming soon.")
    else:
        print("Command not recognized.")

# Function to send a WhatsApp message
def send_whatsapp_message(command):
    try:
        # Extract recipient's number and message
        print("Extracting recipient details and message...")
        # For demonstration, we're using hardcoded values
        phone_number = "+1234567890"  # Replace with actual number or extract from command
        message = command.replace('send message', '').strip()
        
        print(f"Sending message to {phone_number}: {message}")
        # Use pywhatkit to send message
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        print("Message sent successfully.")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Main function to run the assistant
def run_assistant():
    while True:
        command = recognize_speech()
        if command:
            process_command(command)
        time.sleep(1)

# Run the assistant
if __name__ == "__main__":
    run_assistant()
