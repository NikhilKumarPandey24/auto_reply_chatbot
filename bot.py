import pyautogui
import time
import pyperclip
import google.generativeai as genai

from ge import MY_CONVERSATIONS

# Gemini API setup
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.0-flash")

pyautogui.FAILSAFE = False  # disable fail-safe

def learn_my_style():
    """
    Yeh function tumhari conversation style seekhta hai
    """
    system_prompt = f"""
Tu ek AI assistant hai jo MERE jaisa reply karta hai.

MERI PREVIOUS CONVERSATIONS:
{MY_CONVERSATIONS}

INSTRUCTIONS - CAREFULLY FOLLOW KARO:
1. **Language**: Hinglish mix - Hindi aur English dono naturally use karo
2. **Tone**: Casual, friendly, bro-type vibes
3. **Emojis**: Occasionally use karo jab natural lage (😎🔥💪✨)
4. **Short Forms**: Use karo - hai, hoga, kya, bhai, yaar, arre
5. **Sentence Structure**: Short, crisp sentences. Paragraphs me mat likhna
6. **Energy**: Enthusiastic but not over the top
7. **Technical Terms**: English me but explain Hinglish me
8. **Personality**: Helpful, chill, supportive friend

IMPORTANT: Sirf reply do, koi extra explanation nahi!
"""
    return system_prompt

def generate_reply(message):
    """
    Kisi bhi naye message ka reply generate karta hai
    """
    style_prompt = learn_my_style()
    
    full_prompt = f"""
{style_prompt}

NAYA MESSAGE:
"{message}"

Ab iska reply de MERE style me. Direct reply, no explanations:
"""
    
    response = model.generate_content(full_prompt)
    return response.text.strip()

# Step 1: Pehle click karo jaha message hai
pyautogui.click(864, 749)
time.sleep(1)

# Step 2: Text select karo - drag karke
pyautogui.moveTo(479, 148)  # starting point
pyautogui.dragTo(1344, 670, duration=1, button='left')  # ending point
time.sleep(0.5)

# Step 3: Selected text ko copy karo
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.click(479, 148)  # selection hatao

# Step 4: Clipboard se text retrieve karo
chat_history = pyperclip.paste()
print("Copied text:", chat_history)

# Step 5: Gemini se reply generate karo
print("Generating reply...")
response = generate_reply(chat_history)
print("Generated reply:", response)

# Step 6: Reply ko clipboard me copy karo
pyperclip.copy(response)

# Step 7: Reply box pe click karo
pyautogui.click(628, 688)
time.sleep(1)

# Step 8: Reply paste karo aur send karo
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')

print("Message sent! ✅")
