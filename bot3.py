import pyautogui
import time
import pyperclip
import google.generativeai as genai

from ge import MY_CONVERSATIONS

# Gemini API setup
genai.configure(api_key="AIzaSyAu5pmzYn7J3aYvksp2cGmxZn5Z6zJWC3g")
model = genai.GenerativeModel("gemini-2.0-flash")

pyautogui.FAILSAFE = False

# ------------------ STYLE LEARNING ------------------
MY_STYLE_EXAMPLES = """
Friend: Kya kar raha hai?
Nikhil Kumar Pandey: kuch nahi yaar, tu bata 
Friend: Kal milna hai?
Nikhil Kumar Pandey: dekhte hai agar free raha to milte hai 
Friend: Paper kaisa gaya?
Nikhil Kumar Pandey: thik hi tha yaar 
Friend: Movie dekhni hai?
Nikhil Kumar Pandey: kaun si movie hai?
friend: Chal cricket khelte hai
Nikhil Kumar Pandey: bro, aaj thak gaya hu, kal khelte hai
Friend: kaisa hai?
Nikhil Kumar Pandey: thik hi hu yaar, tu bata
friend: Kaunsa game khelna hai?
Nikhil Kumar Pandey: yaar mai waise koi game khelta to nahi hu 
friend: Chal bahar chalte hai
Nikhil Kumar Pandey: aaj thak gaya hu yaar, kal chale kya 
friend: Kya kar raha hai?
Nikhil Kumar Pandey: kuch nahi yaar bas baitha tha 
friend: Movie dekhni hai?
Nikhil Kumar Pandey: man to hai par thak gaya hu yaar abhi if you don,t mind kal dekh lete hai
friend: Kal milna hai?
Nikhil Kumar Pandey: dekhte hai yaar, kal free raha to milte hai
friend: Paper kaisa gaya?
Nikhil Kumar Pandey: thik hi tha yaar, tere kaisa gaya tha 

"""

def generate_reply(message):
    style_prompt = f"""
Tere ko ek role mila hai:
Tu EXACTLY "Nikhil Kumar Pandey" ke style me reply karega.

STYLE RULES:
1. Hinglish mix (thoda Hindi, thoda English)
2. Short aur crisp replies
3. bhai yaar jaise short forms use karna
5. Bilkul normal insaan ki tarah, koi AI jaisa formal tone nahi hona chahiye 

EXAMPLES:
{MY_STYLE_EXAMPLES}

NAYA MESSAGE:
"{message}"

Ab iska reply de jaise Nikhil Kumar Pandey khud deta. Sirf reply do, explanation nahi don,t add masala 
on you own just reply the way Nikhil Kumar Pandey do .
"""

    response = model.generate_content(style_prompt)
    return response.text.strip()


# ------------------ MESSAGE HANDLING ------------------
my_name = "Nikhil Kumar Pandey"   # apna naam
last_processed_message = None
last_bot_reply = None

def get_last_message(chat_history):
    """
    Format: [11:49, 7/10/2025] Sender Name: Message
    """
    lines = [line.strip() for line in chat_history.splitlines() if line.strip()]
    if not lines:
        return None, None

    last_line = lines[-1]

    # Remove [time,date]
    if "]" in last_line:
        after_bracket = last_line.split("]", 1)[1].strip()  # Sender: Message
    else:
        after_bracket = last_line

    if ":" in after_bracket:
        sender, message = after_bracket.split(":", 1)
        return sender.strip(), message.strip()
    return None, after_bracket.strip()

# ------------------ MAIN LOOP ------------------
print("🤖 Bot started...")
pyautogui.click(864, 749)
time.sleep(1)
while True:
    try:
        # Step 1: Copy chat
        pyautogui.moveTo(501, 166)
        pyautogui.dragTo(591, 690, duration=1, button='left')
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.click(501, 166)

        chat_history = pyperclip.paste()
        sender, message = get_last_message(chat_history)

        if not message:
            time.sleep(2)
            continue

        print(f"📩 Last message detected: {sender}: {message}")

        # Skip agar mera hi naam hai
        if sender and sender.lower() == my_name.lower():
            print("⏭ My own message, skipping...")
            last_processed_message = message
            time.sleep(2)
            continue

        # Skip agar bot ka apna reply hi hai
        if last_bot_reply and message == last_bot_reply:
            print("⏭ My last reply, skipping...")
            last_processed_message = message
            time.sleep(2)
            continue

        # Skip agar already processed hai
        if message == last_processed_message:
            print("⏭ Already processed, skipping...")
            time.sleep(2)
            continue

        # Dusre ka naya message hai → reply
        if sender and sender.lower() != my_name.lower():
            print(f"⚡ Generating reply to {sender}: {message}")
            response = generate_reply(message)
            print("✅ Generated reply:", response)

            pyperclip.copy(response)
            pyautogui.click(628, 688)
            time.sleep(1)

            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')

            print("📤 Message sent!")

            last_processed_message = message
            last_bot_reply = response

        time.sleep(3)

    except Exception as e:
        print("❌ Error:", e)
        time.sleep(5)
