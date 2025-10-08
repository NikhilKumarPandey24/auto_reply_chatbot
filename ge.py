import google.generativeai as genai

# ============================================
# 🔑 SETUP
# ============================================
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.0-flash")

# ============================================
# 📚 YAHAN APNI CONVERSATIONS PASTE KARO
# ============================================
# Format: "Person: message\nYou: reply\n\n" 
# Jitni zyada examples doge, utna better!

MY_CONVERSATIONS = """
[13:22, 19/7/2025] Sanjeev (Ptu): Tumhra kitna h?
[13:24, 19/7/2025] Nikhil Kumar Pandey: Tumse bahut kam hai
[13:34, 19/7/2025] Sanjeev (Ptu): Mere se km tumhra aa he nhi skta
[13:34, 19/7/2025] Sanjeev (Ptu): It's universal truth😀
[14:58, 19/7/2025] Nikhil Kumar Pandey: This universal truth is no more truth 🥲
[10:29, 3/10/2025] Nikhil Kumar Pandey: Brown Munde
[10:30, 3/10/2025] Nikhil Kumar Pandey: Yeh niraj ka logic hai
"""

# ============================================
# 🤖 MAIN FUNCTION - STYLE LEARNING
# ============================================

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

# ============================================
# 🎮 MAIN PROGRAM
# ============================================

def main():
    print("="*70)
    print("🤖 GEMINI STYLE LEARNING BOT - Teri Style Me Replies!")
    print("="*70)
    print("\n📚 Training data loaded! Teri style seekh li maine.")
    print("💬 Ab koi bhi message de, main teri style me reply karunga!\n")
    
    while True:
        print("-"*70)
        message = input("📩 Message (ya 'quit' to exit): ").strip()
        
        if message.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Bye bhai! Baad me milte hain!")
            break
        
        if not message:
            print("⚠️ Koi message toh type kar bhai!")
            continue
        
        print("\n🤔 Soch raha hun...\n")
        
        try:
            reply = generate_reply(message)
            print("="*70)
            print("🎯 TERA REPLY:")
            print("="*70)
            print(reply)
            print("="*70)
            print()
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Phir se try kar bhai!\n")

# ============================================
# 🚀 RUN KARO!
# ============================================

if __name__ == "__main__":
    main()
