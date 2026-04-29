import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="The Journey of the Be Like Brit Kids – built by Gesner Deslandes",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS (BLUE THEME) ----------
st.markdown("""
<style>
    /* Main background and text */
    .stApp {
        background: linear-gradient(135deg, #e6f0ff 0%, #cce4ff 100%);
    }
    .main-header {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .lesson-card {
        background-color: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s;
        border-left: 5px solid #2a5298;
    }
    .lesson-card:hover { transform: translateY(-5px); }
    .story-text {
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #1e2a3e;
        text-align: justify;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: #d4e4ff;
        border-radius: 20px;
        color: #1e3c72;
    }
    .sidebar-logo {
        text-align: center;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .sidebar-content {
        background-color: #e8f0fe;
        padding: 1rem;
        border-radius: 15px;
    }
    .pulse-dot {
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #ff4444;
        border-radius: 50%;
        animation: pulse 1.2s infinite;
        margin-right: 8px;
        vertical-align: middle;
    }
    @keyframes pulse {
        0% { transform: scale(0.8); opacity: 0.5; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(0.8); opacity: 0.5; }
    }
    .reading-indicator {
        display: inline-flex;
        align-items: center;
        background: #f0f0f0;
        padding: 5px 12px;
        border-radius: 30px;
        font-size: 0.8rem;
        margin-top: 10px;
    }
    h1, h2, h3 {
        color: #1e3c72;
    }
    .stButton button {
        background-color: #2a5298;
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #1e3c72;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div class="sidebar-logo">📘</div>', unsafe_allow_html=True)
    st.markdown("## 🌐 GlobalInternet.py")
    st.markdown("**👨‍💻 Gesner Deslandes** – Storyteller & Python Builder")
    st.markdown("📞 (509) 4738-5663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("---")
    st.markdown("🌍 [Visit our website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 📖 The Journey of the Be Like Brit Kids")
    st.markdown("*Inspiring stories of hope, resilience, and love from Haiti*")
    st.markdown("---")
    st.caption("Built by Gesner Deslandes – GlobalInternet.py")

# ---------- STORIES DATA (10 chapters) ----------
chapters = [
    {
        "title": "Chapter 1: A New Beginning",
        "image": "https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?w=600&auto=format",
        "text": "The sun rose over the mountains of Grand‑Goâve, painting the sky in shades of orange and pink. Marie, a seven‑year‑old girl with bright eyes and braided hair, stood at the gate of Be Like Brit. She had arrived just the day before, scared and silent. Her parents had passed away, and she had no one left. But when she stepped inside, she was greeted by the warmest smiles. Mama Nerlande took her hand and said, 'You are home now, little one.' Marie looked around at the other children playing football and laughing. For the first time in weeks, she felt a tiny spark of hope. That night, she ate a hot meal and slept in a soft bed. In the morning, she woke to the sound of children singing. Marie smiled. Her new journey had begun.",
        "caption": "A child looking hopefully toward the future"
    },
    {
        "title": "Chapter 2: The First Day of School",
        "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=600&auto=format",
        "text": "The bell rang at 7:30 AM. Jean‑Pierre, age nine, had never been to school before. He held his new backpack tightly, a gift from the house parents. The classroom was simple – wooden desks, a chalkboard, and a map of Haiti on the wall. His teacher, Madame Claire, smiled at him. 'Bonjour, Jean‑Pierre. Today, you will learn to write your name.' He was nervous, but the other children shared their crayons with him. By the end of the day, he could write 'Jean‑Pierre' in big blue letters. He ran to show the other kids. 'Look what I did!' he shouted. That night, he vowed to become an engineer one day. He wanted to build schools for other children like him. His journey had started with a single letter.",
        "caption": "Children learning in a bright classroom"
    },
    {
        "title": "Chapter 3: The Garden of Hope",
        "image": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?w=600&auto=format",
        "text": "Behind the orphanage, there was a small garden. It was overgrown with weeds, but the children saw potential. Led by their mentor, Jonas, they decided to turn it into a vegetable garden. 'We will grow our own food,' he said. Every afternoon, they dug the soil, planted seeds, and watered the young plants. The first week was hard; their hands got dirty and their backs ached. But they worked together. Rose, a twelve‑year‑old girl, loved watching the tiny sprouts appear. 'They look like little soldiers fighting their way to the sun,' she said. Two months later, they harvested tomatoes, carrots, and beans. The cook used them to make a delicious stew. Everyone ate together, proud of what they had grown. The garden became a symbol of their strength: even in hard soil, beautiful things can bloom.",
        "caption": "Children working together in a garden"
    },
    {
        "title": "Chapter 4: A Letter from Afar",
        "image": "https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?w=600&auto=format",
        "text": "One day, a letter arrived at the orphanage. It was from a college student in Boston who had heard about Be Like Brit. Her name was Sarah, and she wanted to become a pen pal to one of the kids. The director chose Elie, a quiet 14‑year‑old boy who loved drawing. Elie wrote his first letter in careful French: 'My name is Elie. I like to draw birds. What is your favourite animal?' Weeks passed, and a reply came. Sarah sent pictures of the Boston skyline and a drawing of a parrot. Elie was overjoyed. He started drawing every day, planning to become an artist. Their letters went back and forth for years. Elie’s art improved, and he learned English from Sarah’s notes. One day, he said, 'A friend across the ocean believed in me. Now I believe in myself.'",
        "caption": "A child writing a letter by lamplight"
    },
    {
        "title": "Chapter 5: The Big Match",
        "image": "https://images.unsplash.com/photo-1552667466-07770ae110d0?w=600&auto=format",
        "text": "Soccer was the heartbeat of the orphanage. Every Saturday, the older kids challenged the younger ones to a friendly match. This time, the prize was a shiny new trophy donated by a visitor. The older team was confident – they had height and experience. But the younger team had speed and hunger. The match was intense. With five minutes left, the score was 2–2. Little Joseph, only ten years old, received a pass near the goal. He closed his eyes and kicked. The ball flew straight into the net. The younger team erupted in cheers. Joseph was carried on their shoulders. That night, the trophy was placed in the common room. Joseph said, 'We proved that size doesn’t matter. What matters is the size of your heart.' The older team shook hands and smiled. Everyone was a winner that day.",
        "caption": "Children playing soccer in a field"
    },
    {
        "title": "Chapter 6: The Art of Giving",
        "image": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=600&auto=format",
        "text": "Christmas was approaching, and the children were excited. But instead of asking for gifts, they decided to give. They made handmade cards and bracelets. They practiced songs in the church choir. On Christmas Eve, they visited a nearby nursing home. The elderly residents had no families left. The children sang carols, handed out their crafts, and sat with the old people. An old man named Pierre cried tears of joy. 'I have not been visited in years,' he said. 'You are angels.' The children returned home with full hearts. That year, they learned that giving is a gift in itself. One child, Mirlande, said, 'We have so little, but we can still share. That is the true magic of Christmas.'",
        "caption": "Children sharing gifts with elderly people"
    },
    {
        "title": "Chapter 7: The Storm",
        "image": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=600&auto=format",
        "text": "A hurricane was approaching. The sky turned dark, and the wind howled. The children were scared. The house parents gathered them in the main hall. They lit candles and told stories to keep everyone calm. For two days, the rain poured, and the wind shook the walls. But the building held strong, thanks to the engineers who had built it. When the storm passed, the children saw that the garden was destroyed and some trees had fallen. But they were all alive. They worked together to clean up. They planted new seeds in the garden. 'Storms will come,' said Jonas, 'but we are stronger than any storm.' The children understood that home is not just walls; it is the people inside them.",
        "caption": "A hurricane seen through a window"
    },
    {
        "title": "Chapter 8: The Visitor",
        "image": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?w=600&auto=format",
        "text": "One afternoon, a car pulled up to the gate. A tall man in a suit stepped out. He was a filmmaker from the United States. He had heard about Be Like Brit and wanted to make a documentary. The children were shy at first, but soon they opened up. They showed him their art, their soccer field, their garden. He filmed them laughing, studying, and helping each other. When the documentary was released, people around the world saw the children's courage. Donations poured in. A new dormitory was built. The children learned that their story had power. 'We are not just victims,' said one of the older boys, 'we are heroes of our own lives.' The filmmaker stayed in touch and visited every year.",
        "caption": "A filmmaker interviewing a child"
    },
    {
        "title": "Chapter 9: Graduation Day",
        "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600&auto=format",
        "text": "Marie, now 18, had finished school. She stood on a small stage in the courtyard, wearing a white dress. All the children, staff, and some neighbours had gathered. The house mother handed her a certificate. Marie gave a speech. 'When I came here, I could not even speak. I was afraid of everything. But you gave me a family. You gave me an education. You gave me hope.' She planned to study nursing at a university. She would be the first in her cohort to go to college. The younger children cheered for her. They saw that one day, they too could walk across that stage. Marie hugged each of them. 'I will come back,' she promised. 'I will help those who come after me.' Her journey was just beginning, but she had already travelled so far.",
        "caption": "A proud graduate holding a certificate"
    },
    {
        "title": "Chapter 10: A Bright Future",
        "image": "https://images.unsplash.com/photo-1509099836639-18b84c05e2cb?w=600&auto=format",
        "text": "Today, the children of Be Like Brit are doctors, nurses, teachers, artists, and engineers. They live in Haiti and abroad, but they never forget where they came from. Every year, on the anniversary of the orphanage, many return. They play soccer with the new kids, share meals, and tell stories of their own journeys. The garden still grows vegetables. The classroom still resounds with lessons. The walls still stand strong, like the love that built them. The journey of the Be Like Brit kids is not just about survival. It is about thriving. It is about taking a small seed of hope and nurturing it until it becomes a tree that shades many. And the story continues, with every new child who walks through the gate.",
        "caption": "Children raising their hands in hope"
    }
]

# ---------- MAIN PAGE ----------
def main():
    st.markdown(
        '<div class="main-header"><h1>📘 The Journey of the Be Like Brit Kids</h1><p>Inspiring stories of hope, resilience, and love from Haiti – built by Gesner Deslandes</p></div>',
        unsafe_allow_html=True
    )
    
    # Chapter selector in sidebar
    chapter_titles = [f"{i+1}. {ch['title']}" for i, ch in enumerate(chapters)]
    selected_idx = st.sidebar.selectbox("📖 Select Chapter", range(len(chapters)), format_func=lambda i: chapter_titles[i])
    
    chapter = chapters[selected_idx]
    
    # Display the chapter card
    with st.container():
        st.markdown(f'<div class="lesson-card">', unsafe_allow_html=True)
        col_img, col_text = st.columns([1, 2])
        with col_img:
            st.image(chapter['image'], caption=chapter.get('caption', 'Illustration'), use_container_width=True)
        with col_text:
            st.markdown(f"## {chapter['title']}")
            st.markdown(f'<div class="story-text">{chapter["text"]}</div>', unsafe_allow_html=True)
            
            # Read Aloud button with visual indicator
            read_btn = st.button(f"🔊 Read Aloud (Chapter {selected_idx+1})", key=f"read_{selected_idx}")
            if read_btn:
                indicator = st.empty()
                indicator.markdown(
                    '<div class="reading-indicator"><span class="pulse-dot"></span> 🔊 Now reading... (audio playing)</div>',
                    unsafe_allow_html=True
                )
                text_to_speak = chapter["text"].replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
                js_code = f"""
                <script>
                    var utterance = new SpeechSynthesisUtterance("{text_to_speak}");
                    utterance.lang = "en-US";
                    utterance.onend = function() {{
                        var event = new CustomEvent('streamlit:setComponentValue', {{detail: {{value: "done"}}}});
                        window.dispatchEvent(event);
                    }};
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(utterance);
                </script>
                """
                components.html(js_code, height=0)
                st.success("🔊 Now reading aloud... (make sure your device volume is on)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div class="footer">
        <p>© {datetime.now().year} GlobalInternet.py – Storytelling by Gesner Deslandes</p>
        <p>📖 "The Journey of the Be Like Brit Kids" – A book of hope from Haiti</p>
        <p>🌐 Built with Streamlit | Hosted on GitHub + Streamlit Cloud</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- PAGE ROUTING ----------
if __name__ == "__main__":
    main()
