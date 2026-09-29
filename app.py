"""
================================================================================
ROMANTIC INTERACTIVE BIRTHDAY WEBSITE FOR MY WIFE
A handmade scrapbook-style digital birthday experience built with Python & Streamlit.

Dedicated with love to: Sona, Mona, Baby, Amar Paakhi 🐦❤️
================================================================================
"""

import streamlit as st
import base64
import os
import re
from pathlib import Path
from PIL import Image

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & STREAMLIT UI SETUP
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Happy Birthday Sona ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).parent.resolve()
ASSETS_DIR = BASE_DIR / "assets"
PHOTOS_DIR = ASSETS_DIR / "photos"
MUSIC_DIR = ASSETS_DIR / "music"
IMAGES_DIR = ASSETS_DIR / "images"

# Ensure all asset directories exist safely
PHOTOS_DIR.mkdir(parents=True, exist_ok=True)
MUSIC_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------------------------------------------------------
# 2. BULLETPROOF HTML/SVG RENDERER (NO RAW CODE BLOCKS!)
# -----------------------------------------------------------------------------
def render_html(html_str: str):
    """
    Safely renders custom HTML/SVG without Markdown converting indented lines
    into unwanted <pre><code> code blocks.
    Removes HTML comments and strips leading whitespace from every line so
    CommonMark never triggers indented code block formatting.
    """
    if not html_str:
        return
    # Remove HTML comments to eliminate any markdown comment parsing glitches
    no_comments = re.sub(r'<!--.*?-->', '', html_str, flags=re.DOTALL)
    # Strip leading spaces from each line so no line starts with 4+ spaces
    cleaned = "\n".join(line.lstrip() for line in no_comments.strip().splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
def initialize_state():
    """Initializes all state variables required for the romantic experience."""
    defaults = {
        "stage": 0,                     # 0 to 7: The scenes in the journey
        "gift_accepted": False,         # Whether she said YES in Scene 1
        "no_clicks": 0,                 # Playful NO button click counter
        "wish_made": False,             # Has she blown out the birthday candle?
        "selected_penguin": None,       # Which penguin was chosen (1, 2, or 3)
        "penguin_action_done": None,    # Action confirmed inside chosen penguin
        "opened_memories": set(),       # Set of unlocked memory card IDs
        "revealed_reasons": set(),      # Set of unlocked love reason IDs
        "easter_egg_clicked": False,    # Secret easter egg state
        "music_started": False          # Background music toggle
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_experience():
    """Smoothly resets all session state variables to restart the journey."""
    st.session_state.stage = 0
    st.session_state.gift_accepted = False
    st.session_state.no_clicks = 0
    st.session_state.wish_made = False
    st.session_state.selected_penguin = None
    st.session_state.penguin_action_done = None
    st.session_state.opened_memories = set()
    st.session_state.revealed_reasons = set()
    st.session_state.easter_egg_clicked = False
    st.rerun()

def next_stage():
    """Advances to the next stage in the scrapbook."""
    st.session_state.stage += 1
    st.rerun()

def prev_stage():
    """Returns to the previous stage in the scrapbook."""
    if st.session_state.stage > 0:
        st.session_state.stage -= 1
        st.rerun()


# -----------------------------------------------------------------------------
# 4. HELPER FUNCTIONS: IMAGES & AUDIO
# -----------------------------------------------------------------------------
def find_photo_file(base_name: str) -> Path:
    """Finds photo whether saved as .jpg, .jpeg, .png, or .webp."""
    extensions = [".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG", ".PNG", ".WEBP"]
    for ext in extensions:
        candidate = PHOTOS_DIR / f"{base_name}{ext}"
        if candidate.exists():
            return candidate
    return PHOTOS_DIR / f"{base_name}.jpg"

def get_image_base64(filepath: Path) -> str:
    """Reads an image and converts it to a base64 data string safely."""
    try:
        if filepath.exists():
            with open(filepath, "rb") as f:
                data = f.read()
                ext = filepath.suffix.lower().replace(".", "")
                if ext in ["jpg", "jpeg"]:
                    ext = "jpeg"
                elif ext == "png":
                    ext = "png"
                elif ext == "webp":
                    ext = "webp"
                else:
                    ext = "jpeg"
                return f"data:image/{ext};base64,{base64.b64encode(data).decode()}"
    except Exception:
        pass
    return ""

def get_audio_bytes(filepath: Path):
    """Safely reads an audio file."""
    try:
        if filepath.exists():
            with open(filepath, "rb") as f:
                return f.read()
    except Exception:
        pass
    return None

def find_music_file():
    """Finds available birthday song in mp3, wav, m4a, or ogg format."""
    candidates = [
        MUSIC_DIR / "birthday_song.mp3",
        MUSIC_DIR / "birthday_song.wav",
        MUSIC_DIR / "birthday_song.m4a",
        MUSIC_DIR / "birthday_song.ogg",
        MUSIC_DIR / "birthday_chime.wav",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


# -----------------------------------------------------------------------------
# 5. CUSTOM CSS DESIGN SYSTEM & ANIMATIONS
# -----------------------------------------------------------------------------
def inject_custom_css():
    """Injects high-end, handmade kawaii scrapbook styling and animations."""
    css = """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Patrick+Hand&family=Gaegu:wght@400;700&family=Nunito:wght@400;600;700;800&family=Sacramento&display=swap');

    /* ---------------- HIDE STREAMLIT CHROME ---------------- */
    #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"], .stDeployButton {
        display: none !important;
        visibility: hidden !important;
    }

    /* ---------------- PREVENT UNWANTED CODE BLOCKS ---------------- */
    pre, code {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        font-family: inherit !important;
        font-size: inherit !important;
        color: inherit !important;
        box-shadow: none !important;
        white-space: normal !important;
    }

    /* ---------------- GLOBAL PAGE STYLING ---------------- */
    .stApp {
        background-color: #FAF4EB;
        background-image: 
            radial-gradient(#EADECF 1.5px, transparent 1.5px),
            radial-gradient(#EADECF 1.5px, #FAF4EB 1.5px);
        background-size: 30px 30px;
        background-position: 0 0, 15px 15px;
        font-family: 'Nunito', sans-serif;
        color: #4A3525;
        min-height: 100vh;
    }

    .block-container {
        max-width: 900px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 3.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        margin: 0 auto !important;
    }

    /* ---------------- SCRAPBOOK CARD CONTAINER ---------------- */
    .scrapbook-card {
        background: #FFFDF9;
        border-radius: 28px;
        padding: 38px 30px;
        margin: 20px auto;
        box-shadow: 
            0 16px 40px rgba(138, 88, 64, 0.09),
            0 2px 10px rgba(0, 0, 0, 0.04);
        border: 2px dashed #E5D0BE;
        position: relative;
        text-align: center;
        overflow: visible;
    }

    /* Washi Tape Ribbon Effect */
    .washi-tape {
        position: absolute;
        top: -14px;
        left: 50%;
        transform: translateX(-50%) rotate(-1.5deg);
        background: rgba(246, 189, 96, 0.85);
        width: 140px;
        height: 28px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        border-left: 3px dashed rgba(255,255,255,0.7);
        border-right: 3px dashed rgba(255,255,255,0.7);
        z-index: 10;
    }
    
    .washi-tape-pink {
        background: rgba(247, 202, 208, 0.85) !important;
        transform: translateX(-50%) rotate(1.2deg) !important;
    }

    .washi-tape-corner-left {
        position: absolute;
        top: -10px;
        left: -10px;
        width: 90px;
        height: 25px;
        background: rgba(244, 162, 97, 0.8);
        transform: rotate(-35deg);
        z-index: 10;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }

    .washi-tape-corner-right {
        position: absolute;
        top: -10px;
        right: -10px;
        width: 90px;
        height: 25px;
        background: rgba(247, 202, 208, 0.85);
        transform: rotate(35deg);
        z-index: 10;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }

    /* ---------------- TYPOGRAPHY ---------------- */
    .handwritten-title {
        font-family: 'Caveat', cursive;
        font-size: 3.2rem;
        font-weight: 700;
        color: #E76F51;
        line-height: 1.15;
        margin-bottom: 0.2rem;
        text-shadow: 2px 2px 0px #FFE5D9;
    }

    .handwritten-subtitle {
        font-family: 'Patrick Hand', cursive;
        font-size: 1.7rem;
        color: #6E473B;
        margin-top: 0.2rem;
        margin-bottom: 1.2rem;
    }

    .cute-tag {
        font-family: 'Patrick Hand', cursive;
        font-size: 1.15rem;
        background: #FFE5D9;
        color: #E76F51;
        padding: 4px 14px;
        border-radius: 16px;
        display: inline-block;
        margin: 4px;
        border: 1px dashed #F4A261;
        transform: rotate(-1.5deg);
    }

    .doodle-arrow {
        font-family: 'Caveat', cursive;
        font-size: 1.6rem;
        color: #F4A261;
        display: inline-block;
    }

    /* ---------------- BUTTON STYLING ---------------- */
    div.stButton > button {
        font-family: 'Patrick Hand', cursive !important;
        font-size: 1.45rem !important;
        font-weight: 600 !important;
        padding: 12px 28px !important;
        border-radius: 50px !important;
        border: 2px solid #E76F51 !important;
        background-color: #E76F51 !important;
        color: #FFFFFF !important;
        box-shadow: 0 8px 20px rgba(231, 111, 81, 0.3) !important;
        transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        cursor: pointer !important;
        width: auto !important;
        min-height: 52px !important;
        margin: 6px auto !important;
        display: block !important;
    }

    div.stButton > button:hover {
        transform: scale(1.05) translateY(-3px) !important;
        background-color: #F4A261 !important;
        border-color: #F4A261 !important;
        color: #FFFFFF !important;
        box-shadow: 0 12px 26px rgba(244, 162, 97, 0.4) !important;
    }

    div.stButton > button:active {
        transform: scale(0.97) translateY(1px) !important;
    }

    /* Secondary soft button */
    .btn-soft div.stButton > button {
        background-color: #FFF2EB !important;
        color: #E76F51 !important;
        border: 2px dashed #E76F51 !important;
        box-shadow: 0 4px 12px rgba(231, 111, 81, 0.15) !important;
    }
    .btn-soft div.stButton > button:hover {
        background-color: #FFE5D9 !important;
        color: #D95333 !important;
    }

    /* No button special styling */
    .btn-no div.stButton > button {
        background-color: #F7CAD0 !important;
        border-color: #F8AD9D !important;
        color: #6E473B !important;
        box-shadow: 0 6px 16px rgba(247, 202, 208, 0.4) !important;
    }

    /* ---------------- POLAROID & SHAPED PHOTO STYLING ---------------- */
    .polaroid-frame {
        background: #FFFFFF;
        padding: 14px 14px 24px 14px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 2px 6px rgba(0,0,0,0.04);
        border-radius: 6px;
        display: inline-block;
        position: relative;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        max-width: 100%;
        margin: 10px 4px;
    }

    .polaroid-frame:hover {
        transform: scale(1.03) rotate(0deg) !important;
        box-shadow: 0 16px 35px rgba(231, 111, 81, 0.2);
        z-index: 15;
    }

    .polaroid-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 4px;
        display: block;
    }

    .polaroid-caption {
        font-family: 'Caveat', cursive;
        font-size: 1.55rem;
        color: #5C4033;
        margin-top: 12px;
        text-align: center;
        font-weight: 600;
    }

    /* Heart-shaped photo crop */
    .photo-heart-wrapper {
        background: #FFFDF9;
        padding: 12px;
        border-radius: 20px;
        border: 2px dashed #F8AD9D;
        box-shadow: 0 8px 22px rgba(231, 111, 81, 0.12);
        display: inline-block;
        width: 95%;
        margin: 10px auto;
    }

    .photo-heart-img {
        width: 190px;
        height: 190px;
        object-fit: cover;
        border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        border: 4px solid #FCD5CE;
        display: block;
        margin: 0 auto;
        box-shadow: 0 6px 16px rgba(231, 111, 81, 0.18);
    }

    /* Circular portrait frame */
    .photo-circle-wrapper {
        background: #FFFFFF;
        padding: 14px 14px 22px 14px;
        border-radius: 24px;
        border: 2px dashed #F4A261;
        box-shadow: 0 8px 22px rgba(0,0,0,0.06);
        display: inline-block;
        width: 95%;
        margin: 10px auto;
    }

    .photo-circle-img {
        width: 185px;
        height: 185px;
        border-radius: 50%;
        object-fit: cover;
        border: 5px solid #FFE5D9;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        display: block;
        margin: 0 auto;
    }

    /* Rounded rectangle modern card */
    .photo-rounded-wrapper {
        background: #FFFFFF;
        padding: 12px 12px 20px 12px;
        border-radius: 22px;
        border: 2px solid #EADECF;
        box-shadow: 0 8px 20px rgba(0,0,0,0.07);
        display: inline-block;
        width: 95%;
        margin: 10px auto;
    }

    .photo-rounded-img {
        width: 100%;
        height: 200px;
        border-radius: 16px;
        object-fit: cover;
        display: block;
    }

    /* Postage Stamp Frame */
    .photo-stamp-wrapper {
        background: #FFFDF9;
        padding: 12px 12px 22px 12px;
        border: 3px dashed #E76F51;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(231, 111, 81, 0.12);
        display: inline-block;
        width: 95%;
        margin: 10px auto;
    }

    /* ---------------- ANIMATIONS ---------------- */
    @keyframes floatSlow {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(1deg); }
    }

    @keyframes gentlePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    @keyframes heartBeat {
        0% { transform: scale(1); }
        14% { transform: scale(1.22); }
        28% { transform: scale(1); }
        42% { transform: scale(1.22); }
        70% { transform: scale(1); }
    }

    @keyframes flameFlicker {
        0%, 100% { transform: scale(1) rotate(-1deg); opacity: 0.95; }
        50% { transform: scale(1.15) rotate(2deg); opacity: 1; filter: drop-shadow(0 0 12px #F6BD60); }
    }

    @keyframes smokePuff {
        0% { transform: translateY(0) scale(0.6); opacity: 1; }
        100% { transform: translateY(-35px) scale(1.6); opacity: 0; }
    }

    @keyframes stagedFadeIn {
        0% { opacity: 0; transform: scale(0.9) translateY(12px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }

    .hw-line1 {
        animation: stagedFadeIn 0.9s ease-out forwards;
    }
    .hw-line2 {
        animation: stagedFadeIn 0.9s ease-out 0.6s forwards;
        opacity: 0;
    }
    .hw-line3 {
        animation: stagedFadeIn 1.1s cubic-bezier(0.175, 0.885, 0.32, 1.275) 1.2s forwards;
        opacity: 0;
    }

    .anim-float {
        animation: floatSlow 3.8s ease-in-out infinite;
    }

    .anim-pulse {
        animation: gentlePulse 2.8s ease-in-out infinite;
    }

    .anim-heartbeat {
        display: inline-block;
        animation: heartBeat 1.8s ease-in-out infinite;
    }

    .flame-anim {
        display: inline-block;
        animation: flameFlicker 1.2s ease-in-out infinite;
    }

    .smoke-anim {
        display: inline-block;
        animation: smokePuff 1.8s ease-out forwards;
    }

    /* ---------------- FLOATING PASTEL HEARTS BACKGROUND ---------------- */
    .floating-heart {
        position: absolute;
        color: #F8AD9D;
        opacity: 0.65;
        user-select: none;
        pointer-events: none;
        animation: floatSlow 4s ease-in-out infinite;
    }

    /* ---------------- SPEECH BUBBLE ---------------- */
    .speech-bubble {
        position: relative;
        background: #FFE5D9;
        border: 2px dashed #E76F51;
        border-radius: 20px;
        padding: 12px 20px;
        font-family: 'Patrick Hand', cursive;
        font-size: 1.4rem;
        color: #8C533C;
        display: inline-block;
        margin: 12px auto;
        box-shadow: 0 4px 12px rgba(231, 111, 81, 0.12);
    }

    .speech-bubble:after {
        content: '';
        position: absolute;
        bottom: -12px;
        left: 50%;
        transform: translateX(-50%);
        border-width: 12px 10px 0;
        border-style: solid;
        border-color: #FFE5D9 transparent;
        display: block;
        width: 0;
    }

    /* ---------------- SCRAPBOOK LETTER CARD ---------------- */
    .letter-paper {
        background-color: #FFFDF9;
        background-image: linear-gradient(#F0E5D8 1px, transparent 1px);
        background-size: 100% 2.2rem;
        line-height: 2.2rem;
        padding: 30px 28px;
        border-radius: 20px;
        border: 1px solid #E8DACB;
        font-family: 'Caveat', cursive;
        font-size: 1.7rem;
        color: #4A3525;
        text-align: left;
        box-shadow: inset 0 0 30px rgba(240, 229, 216, 0.4);
    }

    /* ---------------- PENGUIN SELECTION CARD ---------------- */
    .penguin-card {
        background: #FFFFFF;
        border-radius: 24px;
        padding: 20px 14px;
        border: 2px dashed #F4A261;
        box-shadow: 0 8px 22px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
        text-align: center;
        cursor: pointer;
        margin: 8px 0;
    }

    .penguin-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 14px 30px rgba(231, 111, 81, 0.22);
        border-color: #E76F51;
    }

    /* ---------------- REASON HEART CARDS ---------------- */
    .reason-box {
        background: #FFFBF5;
        border: 2px solid #FCD5CE;
        border-radius: 20px;
        padding: 18px 16px;
        margin: 8px 0;
        box-shadow: 0 4px 14px rgba(248, 173, 157, 0.15);
        transition: all 0.25s ease;
        font-family: 'Patrick Hand', cursive;
        font-size: 1.35rem;
        color: #6E473B;
        min-height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .reason-box:hover {
        transform: translateY(-4px);
        border-color: #E76F51;
        box-shadow: 0 8px 20px rgba(231, 111, 81, 0.2);
    }

    /* ---------------- FINAL GRAND HEADING ---------------- */
    .grand-love {
        font-family: 'Caveat', cursive;
        font-size: 5.5rem;
        font-weight: 700;
        color: #E76F51;
        line-height: 1.05;
        text-shadow: 4px 4px 0px #FFE5D9, 7px 7px 0px rgba(244, 162, 97, 0.3);
        margin: 15px 0;
        letter-spacing: 2px;
    }

    /* Mobile responsiveness adjustments */
    @media (max-width: 768px) {
        .handwritten-title {
            font-size: 2.3rem !important;
        }
        .handwritten-subtitle {
            font-size: 1.35rem !important;
        }
        .grand-love {
            font-size: 3.6rem !important;
        }
        .scrapbook-card {
            padding: 26px 16px !important;
            border-radius: 20px !important;
        }
        .letter-paper {
            font-size: 1.45rem !important;
            line-height: 2.0rem !important;
            background-size: 100% 2.0rem !important;
            padding: 20px 14px !important;
        }
        div.stButton > button {
            font-size: 1.25rem !important;
            padding: 10px 20px !important;
            width: 100% !important;
        }
        .polaroid-img {
            height: 190px !important;
        }
    }
    </style>
    """
    render_html(css)


# -----------------------------------------------------------------------------
# 6. CUTE SVG ARTWORK & GRAPHIC ASSET HELPERS
# -----------------------------------------------------------------------------
def render_kawaii_penguin_svg(accessory="gift", size=220):
    """
    Renders an ultra-cute, handmade kawaii SVG penguin with blushing cheeks,
    twinkling eyes, and custom accessories (gift, letter, cake, or heart).
    """
    acc_svg = ""
    if accessory == "gift":
        acc_svg = """
        <rect x="75" y="130" width="50" height="42" rx="6" fill="#F7CAD0" stroke="#E76F51" stroke-width="2"/>
        <rect x="70" y="122" width="60" height="12" rx="4" fill="#FFB5A7" stroke="#E76F51" stroke-width="2"/>
        <rect x="96" y="122" width="8" height="50" fill="#E76F51"/>
        <rect x="75" y="146" width="50" height="8" fill="#E76F51"/>
        <ellipse cx="88" cy="116" rx="10" ry="7" fill="#E76F51"/>
        <ellipse cx="112" cy="116" rx="10" ry="7" fill="#E76F51"/>
        <circle cx="100" cy="117" r="4" fill="#F6BD60"/>
        """
    elif accessory == "letter":
        acc_svg = """
        <rect x="72" y="130" width="56" height="38" rx="4" fill="#FFE5D9" stroke="#E76F51" stroke-width="2"/>
        <path d="M72 130 L100 150 L128 130" fill="none" stroke="#E76F51" stroke-width="2"/>
        <path d="M100 148 C97 144 91 144 91 150 C91 156 100 162 100 162 C100 162 109 156 109 150 C109 144 103 144 100 148 Z" fill="#E76F51"/>
        <polygon points="85,55 115,55 100,20" fill="#F4A261" stroke="#E76F51" stroke-width="2"/>
        <circle cx="100" cy="16" r="6" fill="#E76F51"/>
        """
    elif accessory == "cake":
        acc_svg = """
        <rect x="74" y="140" width="52" height="30" rx="6" fill="#FCD5CE" stroke="#E76F51" stroke-width="2"/>
        <path d="M74 140 Q80 148 87 140 Q94 148 100 140 Q107 148 114 140 Q121 148 126 140" fill="#FFF0F3" stroke="#FFF0F3"/>
        <rect x="98" y="124" width="4" height="16" fill="#FDE4CF" stroke="#E76F51" stroke-width="1.5"/>
        <ellipse cx="100" cy="118" rx="4" ry="7" fill="#F6BD60" class="flame-anim"/>
        """
    elif accessory == "heart":
        acc_svg = """
        <g class="anim-heartbeat" style="transform-origin: 100px 145px;">
            <path d="M100 135 C94 125 80 125 80 138 C80 152 100 166 100 166 C100 166 120 152 120 138 C120 125 106 125 100 135 Z" fill="#E76F51"/>
            <circle cx="90" cy="133" r="3" fill="#FFFFFF" opacity="0.8"/>
        </g>
        """
    elif accessory == "celebrate":
        acc_svg = """
        <polygon points="85,50 115,50 100,15" fill="#E76F51" stroke="#F4A261" stroke-width="2"/>
        <circle cx="100" cy="11" r="5" fill="#F6BD60"/>
        <path d="M100 130 C94 120 82 120 82 132 C82 144 100 156 100 156 C100 156 118 144 118 132 C118 120 106 120 100 130 Z" fill="#E76F51" class="anim-pulse"/>
        <circle cx="60" cy="85" r="4" fill="#F6BD60"/>
        <circle cx="140" cy="85" r="4" fill="#F8AD9D"/>
        """

    svg = f"""
    <svg width="{size}" height="{size}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="display:inline-block; filter: drop-shadow(0 6px 12px rgba(138, 88, 64, 0.15));">
        <ellipse cx="80" cy="180" rx="16" ry="9" fill="#F4A261"/>
        <ellipse cx="120" cy="180" rx="16" ry="9" fill="#F4A261"/>
        <ellipse cx="100" cy="115" rx="55" ry="65" fill="#3D405B"/>
        <ellipse cx="44" cy="120" rx="12" ry="26" fill="#3D405B" transform="rotate(20 44 120)"/>
        <ellipse cx="156" cy="120" rx="12" ry="26" fill="#3D405B" transform="rotate(-20 156 120)"/>
        <ellipse cx="100" cy="120" rx="40" ry="52" fill="#FFFDF8"/>
        <circle cx="84" cy="95" r="5.5" fill="#264653"/>
        <circle cx="82.5" cy="93" r="2" fill="#FFFFFF"/>
        <circle cx="86" cy="97" r="1" fill="#FFFFFF"/>
        <circle cx="116" cy="95" r="5.5" fill="#264653"/>
        <circle cx="114.5" cy="93" r="2" fill="#FFFFFF"/>
        <circle cx="118" cy="97" r="1" fill="#FFFFFF"/>
        <ellipse cx="74" cy="106" rx="8" ry="5" fill="#F8AD9D" opacity="0.85"/>
        <ellipse cx="126" cy="106" rx="8" ry="5" fill="#F8AD9D" opacity="0.85"/>
        <polygon points="100,100 93,109 107,109" fill="#E76F51"/>
        {acc_svg}
    </svg>
    """
    return "\n".join(line.lstrip() for line in svg.strip().splitlines())

def render_birthday_cake_svg(wish_made=False, size=240):
    """
    Renders an adorable handmade 2-layer strawberry cream birthday cake
    with animated flickering flame or smoke puff when wish is made.
    """
    candle_effect = """
    <ellipse cx="100" cy="46" rx="6" ry="11" fill="#F6BD60" class="flame-anim"/>
    <ellipse cx="100" cy="48" rx="3" ry="7" fill="#E76F51" class="flame-anim"/>
    """
    if wish_made:
        candle_effect = """
        <g class="smoke-anim">
            <circle cx="100" cy="42" r="7" fill="#D3D3D3" opacity="0.7"/>
            <circle cx="95" cy="32" r="5" fill="#E0E0E0" opacity="0.6"/>
            <circle cx="106" cy="24" r="4" fill="#EEEEEE" opacity="0.5"/>
            <text x="100" y="20" font-family="'Patrick Hand', cursive" font-size="14" fill="#E76F51" text-anchor="middle">✨ Wish Made!</text>
        </g>
        """

    svg = f"""
    <svg width="{size}" height="{size}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="display:inline-block; filter: drop-shadow(0 8px 16px rgba(138, 88, 64, 0.14));">
        <ellipse cx="100" cy="170" rx="80" ry="14" fill="#F0E5D8"/>
        <ellipse cx="100" cy="167" rx="74" ry="11" fill="#FFFFFF"/>
        <rect x="45" y="115" width="110" height="48" rx="10" fill="#FCD5CE" stroke="#E76F51" stroke-width="2"/>
        <path d="M45 125 Q52 135 60 125 Q68 135 76 125 Q84 135 92 125 Q100 135 108 125 Q116 135 124 125 Q132 135 140 125 Q148 135 155 125" fill="#FFF0F3" stroke="#FFF0F3" stroke-width="6"/>
        <rect x="46" y="116" width="108" height="12" fill="#FFF0F3"/>
        <rect x="65" y="75" width="70" height="42" rx="8" fill="#FFE5D9" stroke="#E76F51" stroke-width="2"/>
        <path d="M65 83 Q72 90 79 83 Q86 90 93 83 Q100 90 107 83 Q114 90 121 83 Q128 90 135 83" fill="#FFF0F3" stroke="#FFF0F3" stroke-width="5"/>
        <rect x="66" y="76" width="68" height="8" fill="#FFF0F3"/>
        <circle cx="62" cy="144" r="2.5" fill="#E76F51"/>
        <circle cx="85" cy="150" r="2.5" fill="#F6BD60"/>
        <circle cx="115" cy="142" r="2.5" fill="#F4A261"/>
        <circle cx="138" cy="148" r="2.5" fill="#F8AD9D"/>
        <path d="M100 92 C96 87 88 87 88 94 C88 101 100 108 100 108 C100 108 112 101 112 94 C112 87 104 87 100 92 Z" fill="#E76F51"/>
        <rect x="97.5" y="52" width="5" height="24" rx="2" fill="#FDE4CF" stroke="#E76F51" stroke-width="1.2"/>
        <line x1="100" y1="50" x2="100" y2="52" stroke="#264653" stroke-width="1.5"/>
        {candle_effect}
    </svg>
    """
    return "\n".join(line.lstrip() for line in svg.strip().splitlines())

def render_top_navigation():
    """Renders scrapbook chapter progress and back button."""
    if st.session_state.stage > 0:
        c1, c2, c3 = st.columns([1.2, 3.6, 1.2])
        with c1:
            if st.button("← Back", key="top_back_btn"):
                prev_stage()
        with c2:
            scenes = ["Gift", "Reveal", "Letter", "Scrapbook", "Memories", "Reasons", "Penguins", "Forever"]
            curr = st.session_state.stage
            dots_html = f"""
            <div style="text-align:center; margin-bottom: 8px;">
                <span class="cute-tag" style="background: #FFFDF9; border: 1px dashed #E76F51;">
                    📖 Page {curr + 1} of 8: {scenes[curr]} 🌸
                </span>
            </div>
            """
            render_html(dots_html)
        with c3:
            pass


# -----------------------------------------------------------------------------
# 7. SCENE 1: "PLS ACCEPT THE GIFT"
# -----------------------------------------------------------------------------
def scene_accept_gift():
    """Scene 1: Shy penguin with YES and playful NO buttons, and celebratory acceptance."""
    # Floating background hearts
    render_html(
        """
        <div style="text-align: center; position: relative;">
            <span class="floating-heart" style="top:-10px; left:12%; font-size:24px;">🌸</span>
            <span class="floating-heart" style="top:20px; right:15%; font-size:28px; animation-delay:1s;">❤️</span>
            <span class="floating-heart" style="top:110px; left:8%; font-size:20px; animation-delay:2s;">✨</span>
            <span class="floating-heart" style="top:120px; right:10%; font-size:22px; animation-delay:1.5s;">💕</span>
        </div>
        """
    )

    if not st.session_state.gift_accepted:
        render_html(
            """
            <div class="scrapbook-card">
                <div class="washi-tape washi-tape-pink"></div>
                <div class="handwritten-title">PLS ACCEPT THE GIFT 🎁</div>
                <div class="handwritten-subtitle">A little surprise made with love for my Sona ❤️</div>
            """
        )

        # Shy Penguin Graphic
        p1_img_path = IMAGES_DIR / "penguin1.png"
        p1_b64 = get_image_base64(p1_img_path)
        if p1_b64:
            render_html(
                f"""
                <div class="anim-float" style="text-align:center; margin: 15px 0;">
                    <img src="{p1_b64}" width="210" style="filter: drop-shadow(0 8px 16px rgba(138,88,64,0.15));" alt="Cute Shy Penguin"/>
                </div>
                """
            )
        else:
            render_html(
                f"""
                <div class="anim-float" style="text-align:center; margin: 15px 0;">
                    {render_kawaii_penguin_svg(accessory="gift", size=210)}
                </div>
                """
            )

        # Playful Speech Bubble based on NO button clicks
        no_messages = [
            "I have a little birthday surprise for you... 🥹👉👈",
            "Are you sure? 🥺",
            "Baby pleaseeee 😭",
            "Mona, don't break my heart 💔",
            "Think again Amar Paakhi 🥹",
            "Okay... but the YES button is still waiting 👀❤️"
        ]
        current_msg = no_messages[min(st.session_state.no_clicks, len(no_messages) - 1)]

        render_html(
            f"""
            <div style="text-align:center;">
                <div class="speech-bubble anim-pulse">
                    {current_msg}
                </div>
            </div>
            </div>
            """
        )

        # Interactive Buttons
        btn_col1, btn_col2 = st.columns([1, 1])

        with btn_col1:
            scale_label = "YES ❤️" if st.session_state.no_clicks == 0 else f"YES ❤️ ({'✨' * min(st.session_state.no_clicks, 4)})"
            if st.button(scale_label, key="yes_button"):
                st.session_state.gift_accepted = True
                st.balloons()
                st.rerun()

        with btn_col2:
            render_html('<div class="btn-no">')
            no_label = "NO 😤"
            if st.session_state.no_clicks == 1:
                no_label = "Still NO? 🥺"
            elif st.session_state.no_clicks >= 2:
                no_label = "Really NO? 💔"

            if st.button(no_label, key="no_button"):
                st.session_state.no_clicks += 1
                st.rerun()
            render_html('</div>')

    else:
        # Celebratory Acceptance Reveal State!
        render_html(
            """
            <div class="scrapbook-card anim-pulse">
                <div class="washi-tape washi-tape-pink"></div>
                <div class="handwritten-title" style="color: #E76F51; font-size: 3.5rem;">
                    YAYYY!! 🥹❤️
                </div>
                <div class="handwritten-subtitle" style="font-size: 2rem; color: #5C4033; font-weight: 700;">
                    I knew my Sona would accept it!
                </div>
            """
        )

        render_html(
            f"""
            <div style="text-align:center; margin: 15px 0;">
                {render_kawaii_penguin_svg(accessory="celebrate", size=220)}
            </div>
            <div style="text-align:center; margin: 10px 0;">
                <span class="cute-tag">✨ Sona accepted the birthday gift! ✨</span>
            </div>
            </div>
            """
        )

        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            if st.button("Let's open your birthday surprise! 🎂✨", key="open_surprise_btn"):
                next_stage()


# -----------------------------------------------------------------------------
# 8. SCENE 2: "HAPPY BIRTHDAY REVEAL & MAKE A WISH"
# -----------------------------------------------------------------------------
def scene_birthday_reveal():
    """Scene 2: Cake reveal, animated flame, and Make A Wish interaction."""
    render_html(
        """
        <div class="scrapbook-card">
            <div class="washi-tape"></div>
            <span class="cute-tag">✨ YAYYY!! 🥹❤️ I knew my Sona would accept it!</span>
            <div class="handwritten-title" style="margin-top: 10px;">HAPPY BIRTHDAY</div>
            <div class="handwritten-subtitle" style="font-size: 2.2rem; color: #E76F51; font-weight: 700;">
                MY SONA ❤️
            </div>
        """
    )

    # Cake illustration with flickering flame or smoke puff
    render_html(
        f"""
        <div style="text-align:center; margin: 15px 0;">
            {render_birthday_cake_svg(wish_made=st.session_state.wish_made, size=230)}
        </div>
        """
    )

    # Make a wish interactive sequence
    if not st.session_state.wish_made:
        render_html(
            """
            <div style="text-align:center; margin: 15px auto;">
                <div class="handwritten-subtitle" style="margin-bottom: 4px; font-weight: 700;">
                    MAKE A WISH ✨
                </div>
                <p style="font-size: 1.25rem; color: #6E473B; font-style: italic; margin-bottom: 2px;">
                    "Close your eyes..."
                </p>
                <p style="font-size: 1.25rem; color: #6E473B; font-style: italic; margin-bottom: 15px;">
                    "Make the most beautiful wish in your heart."
                </p>
            </div>
            """
        )

        col_w1, col_w2, col_w3 = st.columns([1, 2, 1])
        with col_w2:
            if st.button("I MADE MY WISH ❤️", key="wish_button"):
                st.session_state.wish_made = True
                st.balloons()
                st.rerun()
    else:
        render_html(
            """
            <div style="text-align:center; margin: 15px auto;" class="anim-pulse">
                <div class="speech-bubble" style="background:#FFF9F2; border-color:#E76F51;">
                    <p style="font-size: 1.35rem; color: #E76F51; margin: 0; font-weight: 600;">
                        "I hope every beautiful wish in your heart comes true."
                    </p>
                    <p style="font-size: 1.25rem; color: #6E473B; margin: 6px 0 0 0;">
                        "And I hope I'm there beside you when they do. ❤️"
                    </p>
                </div>
            </div>
            """
        )

        col_next1, col_next2, col_next3 = st.columns([1, 2, 1])
        with col_next2:
            if st.button("Open your birthday letter 💌", key="open_letter_btn"):
                next_stage()

    render_html("</div>")


# -----------------------------------------------------------------------------
# 9. SCENE 3: "PERSONAL BIRTHDAY LETTER"
# -----------------------------------------------------------------------------
def scene_birthday_letter():
    """Scene 3: Large scrapbook paper card with cutie polaroid on left & heartfelt letter."""
    render_html(
        """
        <div class="scrapbook-card">
            <div class="washi-tape washi-tape-pink"></div>
            <div class="washi-tape-corner-left"></div>
            <div class="washi-tape-corner-right"></div>
            <div class="handwritten-title">A LETTER FOR YOU 💌</div>
            <div class="handwritten-subtitle">Every word written straight from my heart...</div>
        """
    )

    col_photo, col_letter = st.columns([1, 1.35])

    with col_photo:
        p1_path = find_photo_file("photo1")
        p1_b64 = get_image_base64(p1_path)

        if p1_b64:
            render_html(
                f"""
                <div style="text-align:center;">
                    <div class="polaroid-frame" style="transform: rotate(-2.5deg);">
                        <div class="washi-tape" style="top:-10px; width:90px; height:20px;"></div>
                        <img src="{p1_b64}" class="polaroid-img" alt="My Cutie"/>
                        <div class="polaroid-caption">My Cutie ❤️</div>
                        <div style="font-size:0.95rem; color:#8C533C; font-family:'Patrick Hand', cursive;">
                            📷 our precious moment
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <span class="cute-tag">birthday girl ✨</span>
                        <span class="cute-tag">mine ❤️</span>
                    </div>
                </div>
                """
            )
        else:
            render_html(
                f"""
                <div style="text-align:center;">
                    <div class="polaroid-frame" style="transform: rotate(-2.5deg);">
                        <div class="washi-tape" style="top:-10px; width:90px; height:20px;"></div>
                        <div style="height:230px; background:#FFE5D9; border-radius:4px; display:flex; align-items:center; justify-content:center; flex-direction:column;">
                            {render_kawaii_penguin_svg(accessory="letter", size=160)}
                        </div>
                        <div class="polaroid-caption">My Cutie ❤️</div>
                        <div style="font-size:0.95rem; color:#8C533C; font-family:'Patrick Hand', cursive;">
                            (Place photo1.jpg in assets/photos/)
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <span class="cute-tag">birthday girl ✨</span>
                        <span class="cute-tag">mine ❤️</span>
                    </div>
                </div>
                """
            )

    with col_letter:
        render_html(
            """
            <div class="letter-paper">
                <div style="font-weight:700; font-size:2.0rem; color:#E76F51; margin-bottom:10px;">
                    Happy Birthday, my Sona ❤️
                </div>
                <p>
                    Today isn't special only because it's your birthday.
                    It's special because it's the day the person who became such an important part of my life came into this world.
                </p>
                <p>
                    I don't know exactly what the future will look like, but there are so many things I want to experience with you.
                </p>
                <p>
                    I want to see you achieve the dreams you keep inside your heart.
                    I want to be there when you're happy, when you're tired, when you're confused, and when you simply need someone beside you.
                </p>
                <p>
                    I hope you keep growing, smiling and becoming the person you want to become.
                    And somewhere along that journey, I hope I get to keep holding your hand.
                </p>
                <p>
                    One day I imagine us looking back at everything we went through together and smiling.
                    A peaceful home. Our silly arguments. Our random laughs. Our dreams coming true.
                    And maybe two beautiful little kids running around us while we wonder how life moved so fast.
                </p>
                <p>
                    I don't know what life has planned. But I know one thing.
                    Having you in my life has already made it more beautiful.
                </p>
                <p style="font-weight:700; color:#E76F51; margin-top:15px;">
                    Happy Birthday, Baby.
                    I love you more than I manage to say properly sometimes.
                    Always keep smiling, Amar Paakhi. ❤️
                </p>
            </div>
            """
        )

    render_html("</div>")

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("See our photo memories 📸✨", key="to_gallery_btn"):
            next_stage()


# -----------------------------------------------------------------------------
# 10. SCENE 4: "PHOTO MEMORY SCRAPBOOK" (DIFFERENT SHAPES & STYLES)
# -----------------------------------------------------------------------------
def scene_photo_scrapbook():
    """Scene 4: Scrapbook collage with different photo shapes (heart, polaroid, circle, rounded, stamp)."""
    render_html(
        """
        <div class="scrapbook-card">
            <div class="washi-tape"></div>
            <div class="handwritten-title">Beautiful ❤️</div>
            <div class="handwritten-subtitle" style="letter-spacing: 2px; font-weight: 700; color: #E76F51;">
                MY GIRLFRIEND & MY FOREVER
            </div>
            <p style="font-family: 'Patrick Hand', cursive; font-size: 1.25rem; color: #8C533C; margin-top: -10px;">
                "Every picture tells a story, but my favorite ones are with you."
            </p>
        </div>
        """
    )

    photo_configs = [
        {"base": "photo1", "label": "My Love ❤️", "shape": "polaroid", "tilt": "-3.5deg", "tape": "washi-tape-pink", "tag": "my favorite"},
        {"base": "photo2", "label": "My Baby 🌸", "shape": "heart", "tilt": "4deg", "tape": "washi-tape", "tag": "cutie"},
        {"base": "photo3", "label": "My Sona ✨", "shape": "rounded", "tilt": "-2.5deg", "tape": "washi-tape-pink", "tag": "pretty girl"},
        {"base": "photo4", "label": "My Mona 🍰", "shape": "polaroid", "tilt": "3deg", "tape": "washi-tape", "tag": "sweetest smile"},
        {"base": "photo5", "label": "My Favorite Person 🥰", "shape": "circle", "tilt": "-4deg", "tape": "washi-tape-pink", "tag": "mine ❤️"},
        {"base": "photo6", "label": "My Amar Paakhi 🐦❤️", "shape": "stamp", "tilt": "4.5deg", "tape": "washi-tape", "tag": "always & forever"}
    ]

    row1 = st.columns(3)
    row2 = st.columns(3)
    grid_cols = row1 + row2

    for idx, cfg in enumerate(photo_configs):
        with grid_cols[idx]:
            p_file = find_photo_file(cfg["base"])
            p_b64 = get_image_base64(p_file)

            if cfg["shape"] == "heart":
                img_content = f"""
                <div class="photo-heart-wrapper" style="transform: rotate({cfg['tilt']});">
                    <div style="font-size:1.6rem; text-align:center; margin-bottom:4px;">💖</div>
                    <img src="{p_b64}" class="photo-heart-img" alt="{cfg['label']}"/>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <div style="text-align:center;"><span class="cute-tag">{cfg["tag"]}</span></div>
                </div>
                """ if p_b64 else f"""
                <div class="photo-heart-wrapper" style="transform: rotate({cfg['tilt']}); text-align:center;">
                    <div style="height:190px; display:flex; align-items:center; justify-content:center; flex-direction:column; background:#FFEAD9; border-radius:50% 50% 50% 50% / 60% 60% 40% 40%;">
                        <span style="font-size:3rem;">💖</span>
                    </div>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <span class="cute-tag">{cfg["tag"]}</span>
                </div>
                """

            elif cfg["shape"] == "circle":
                img_content = f"""
                <div class="photo-circle-wrapper" style="transform: rotate({cfg['tilt']}); text-align:center;">
                    <img src="{p_b64}" class="photo-circle-img" alt="{cfg['label']}"/>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <span class="cute-tag">{cfg["tag"]}</span>
                </div>
                """ if p_b64 else f"""
                <div class="photo-circle-wrapper" style="transform: rotate({cfg['tilt']}); text-align:center;">
                    <div style="width:185px; height:185px; border-radius:50%; background:#FFEAD9; display:flex; align-items:center; justify-content:center; margin:0 auto;">
                        <span style="font-size:3rem;">🌸</span>
                    </div>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <span class="cute-tag">{cfg["tag"]}</span>
                </div>
                """

            elif cfg["shape"] == "rounded":
                img_content = f"""
                <div class="photo-rounded-wrapper" style="transform: rotate({cfg['tilt']}); text-align:center;">
                    <div class="washi-tape {cfg['tape']}" style="top:-8px; width:75px; height:18px;"></div>
                    <img src="{p_b64}" class="photo-rounded-img" alt="{cfg['label']}"/>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <span class="cute-tag">{cfg["tag"]}</span>
                </div>
                """ if p_b64 else f"""
                <div class="photo-rounded-wrapper" style="transform: rotate({cfg['tilt']}); text-align:center;">
                    <div style="height:200px; background:#FFEAD9; border-radius:16px; display:flex; align-items:center; justify-content:center;">
                        <span style="font-size:3rem;">✨</span>
                    </div>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <span class="cute-tag">{cfg["tag"]}</span>
                </div>
                """

            elif cfg["shape"] == "stamp":
                img_content = f"""
                <div class="photo-stamp-wrapper" style="transform: rotate({cfg['tilt']}); text-align:center;">
                    <img src="{p_b64}" class="polaroid-img" style="border-radius:6px;" alt="{cfg['label']}"/>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <span class="cute-tag">{cfg["tag"]}</span>
                </div>
                """ if p_b64 else f"""
                <div class="photo-stamp-wrapper" style="transform: rotate({cfg['tilt']}); text-align:center;">
                    <div style="height:200px; background:#FFEAD9; border-radius:6px; display:flex; align-items:center; justify-content:center;">
                        <span style="font-size:3rem;">💌</span>
                    </div>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <span class="cute-tag">{cfg["tag"]}</span>
                </div>
                """

            else:
                img_content = f"""
                <div class="polaroid-frame" style="transform: rotate({cfg['tilt']}); width: 92%;">
                    <div class="washi-tape {cfg['tape']}" style="top:-8px; width:75px; height:18px;"></div>
                    <img src="{p_b64}" class="polaroid-img" alt="{cfg['label']}"/>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <div><span class="cute-tag">{cfg["tag"]}</span></div>
                </div>
                """ if p_b64 else f"""
                <div class="polaroid-frame" style="transform: rotate({cfg['tilt']}); width: 92%;">
                    <div style="height:210px; background:#FFEAD9; border-radius:4px; display:flex; align-items:center; justify-content:center; flex-direction:column;">
                        <span style="font-size:3rem;">📷</span>
                    </div>
                    <div class="polaroid-caption">{cfg["label"]}</div>
                    <div><span class="cute-tag">{cfg["tag"]}</span></div>
                </div>
                """

            render_html(
                f"""
                <div style="text-align:center; margin-bottom: 24px;">
                    {img_content}
                </div>
                """
            )

    render_html(
        """
        <div style="text-align:center; margin: 15px 0;">
            <span class="doodle-arrow">✨ You make every memory look like art ✨</span>
        </div>
        """
    )

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("Our Little Memories 📖❤️", key="to_memories_btn"):
            next_stage()


# -----------------------------------------------------------------------------
# 11. SCENE 5: "OUR LITTLE MEMORIES"
# -----------------------------------------------------------------------------
def scene_little_memories():
    """Scene 5: Clickable scrapbook cards revealing treasured memories one by one."""
    memories = [
        ("Our random conversations 💬", "The way we can talk for hours about absolutely nothing, and it still feels like the best part of my entire day. Every late night chat is my comfort zone."),
        ("Your smile ✨", "That pure, gorgeous, heart-melting smile that instantly makes every heavy thing in my world disappear."),
        ("The way you get angry 😾", "Pouting and pretending to be mad, crossing your arms, but looking way too adorable for me to take seriously hehe ❤️"),
        ("Our silly fights 🙈", "Those small, funny disagreements where we both know we could never actually stay mad at each other for more than five minutes."),
        ("The way we make up again 🫂", "Because no matter what happens or how crazy the world gets, at the end of the day, it's always you and me against everything."),
        ("Moments we laugh for no reason 😂", "Bursting into uncontrollable laughter over the most random, silly jokes until our stomachs hurt."),
        ("Every small memory with you 🌸", "Every quiet walk, every gentle glance, every warm hug, and every tiny moment that became unforgettable simply because it was with you, Amar Paakhi.")
    ]

    render_html(
        """
        <div class="scrapbook-card">
            <div class="washi-tape washi-tape-pink"></div>
            <div class="handwritten-title">Some little things I never want to forget ❤️</div>
            <div class="handwritten-subtitle">Click on each memory note to open what I keep in my heart...</div>
        </div>
        """
    )

    unlocked_count = len(st.session_state.opened_memories)
    render_html(
        f"""
        <div style="text-align:center; margin-bottom: 20px;">
            <span class="cute-tag" style="font-size: 1.25rem;">
                💌 {unlocked_count} of {len(memories)} memories unlocked
            </span>
        </div>
        """
    )

    for idx, (title, detail) in enumerate(memories):
        is_opened = idx in st.session_state.opened_memories
        
        card_col1, card_col2 = st.columns([3, 1])
        with card_col1:
            if is_opened:
                render_html(
                    f"""
                    <div style="background:#FFF9F2; border:2px dashed #E76F51; border-radius:18px; padding:16px 20px; margin-bottom:12px; box-shadow:0 4px 12px rgba(231,111,81,0.12);">
                        <div style="font-family:'Caveat', cursive; font-size:1.6rem; font-weight:700; color:#E76F51;">
                            ✨ {title}
                        </div>
                        <div style="font-family:'Nunito', sans-serif; font-size:1.15rem; color:#5C4033; margin-top:6px; line-height:1.6;">
                            "{detail}"
                        </div>
                    </div>
                    """
                )
            else:
                render_html(
                    f"""
                    <div style="background:#FFFDF8; border:1px solid #E8D5C4; border-radius:18px; padding:16px 20px; margin-bottom:12px; box-shadow:0 2px 8px rgba(0,0,0,0.04);">
                        <div style="font-family:'Patrick Hand', cursive; font-size:1.4rem; color:#6E473B;">
                            🔒 {title}
                        </div>
                    </div>
                    """
                )
        with card_col2:
            btn_text = "Opened ❤️" if is_opened else "Open 💌"
            if st.button(btn_text, key=f"mem_btn_{idx}"):
                if is_opened:
                    st.session_state.opened_memories.remove(idx)
                else:
                    st.session_state.opened_memories.add(idx)
                st.rerun()

    # Unlock all shortcut
    col_u1, col_u2, col_u3 = st.columns([1, 2, 1])
    with col_u2:
        if unlocked_count < len(memories):
            if st.button("Read all memories at once ✨", key="unlock_all_memories"):
                st.session_state.opened_memories = set(range(len(memories)))
                st.rerun()

    render_html("<div style='height: 20px;'></div>")

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("Why I Love You 💖", key="to_reasons_btn"):
            next_stage()


# -----------------------------------------------------------------------------
# 12. SCENE 6: "WHY I LOVE YOU"
# -----------------------------------------------------------------------------
def scene_why_i_love_you():
    """Scene 6: Interactive heart cards revealing reasons why she is so special."""
    reasons = [
        "Because your smile can completely change my mood in a second.",
        "Because even our silly, stupid conversations become my favorite memories.",
        "Because I can genuinely imagine a beautiful future with you.",
        "Because you make ordinary days feel like celebrations.",
        "Because you're my Sona.",
        "Because you're my Mona.",
        "Because you're my Baby.",
        "Because you're my Amar Paakhi 🐦❤️",
        "And honestly... I don't need a reason to love you. Loving you is as natural as breathing. ❤️"
    ]

    render_html(
        """
        <div class="scrapbook-card">
            <div class="washi-tape"></div>
            <div class="handwritten-title">A few reasons why you're so special to me...</div>
            <div class="handwritten-subtitle">Tap each glowing heart to reveal what's inside 💖</div>
        </div>
        """
    )

    r_cols = [st.columns(3), st.columns(3), st.columns(3)]
    flat_cols = r_cols[0] + r_cols[1] + r_cols[2]

    for idx, reason in enumerate(reasons):
        with flat_cols[idx]:
            is_revealed = idx in st.session_state.revealed_reasons
            if is_revealed:
                render_html(
                    f"""
                    <div class="reason-box" style="background:#FFE5D9; border-color:#E76F51; font-weight:600;">
                        <div>
                            <div style="font-size:1.8rem; margin-bottom:4px;">💖</div>
                            {reason}
                        </div>
                    </div>
                    """
                )
            else:
                render_html(
                    f"""
                    <div class="reason-box anim-pulse">
                        <div>
                            <div style="font-size:2.2rem; margin-bottom:4px;">💌</div>
                            <span style="font-family:'Caveat', cursive; font-size:1.6rem; color:#E76F51;">
                                Reason #{idx + 1}
                            </span>
                        </div>
                    </div>
                    """
                )
            
            btn_txt = "Hide 💕" if is_revealed else f"Reveal #{idx + 1} ❤️"
            if st.button(btn_txt, key=f"reason_btn_{idx}"):
                if is_revealed:
                    st.session_state.revealed_reasons.remove(idx)
                else:
                    st.session_state.revealed_reasons.add(idx)
                st.rerun()

    if len(st.session_state.revealed_reasons) < len(reasons):
        col_ra1, col_ra2, col_ra3 = st.columns([1, 2, 1])
        with col_ra2:
            if st.button("Reveal all reasons at once ✨", key="reveal_all_reasons_btn"):
                st.session_state.revealed_reasons = set(range(len(reasons)))
                st.rerun()

    render_html("<div style='height: 25px;'></div>")

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("Choose a penguin 🐧🎁", key="to_penguin_btn"):
            next_stage()


# -----------------------------------------------------------------------------
# 13. SCENE 7: "CHOOSE A PENGUIN"
# -----------------------------------------------------------------------------
def scene_choose_penguin():
    """Scene 7: 3 adorable penguins holding gift boxes with interactive reveals and actions."""
    render_html(
        """
        <div class="scrapbook-card">
            <div class="washi-tape washi-tape-pink"></div>
            <div class="handwritten-title">Choose a penguin 🐧</div>
            <div class="handwritten-subtitle">Each one has a special surprise just for you...</div>
        </div>
        """
    )

    col_p1, col_p2, col_p3 = st.columns(3)

    with col_p1:
        render_html(
            f"""
            <div class="penguin-card">
                {render_kawaii_penguin_svg(accessory="letter", size=170)}
                <div class="polaroid-caption" style="font-size:1.4rem;">Penguin #1 💌</div>
                <div class="cute-tag">sweet reminder</div>
            </div>
            """
        )
        if st.button("Choose Penguin 1 💌", key="p1_btn"):
            st.session_state.selected_penguin = 1
            st.session_state.penguin_action_done = None
            st.rerun()

    with col_p2:
        render_html(
            f"""
            <div class="penguin-card">
                {render_kawaii_penguin_svg(accessory="gift", size=170)}
                <div class="polaroid-caption" style="font-size:1.4rem;">Penguin #2 🎁</div>
                <div class="cute-tag">gift coupons</div>
            </div>
            """
        )
        if st.button("Choose Penguin 2 🎁", key="p2_btn"):
            st.session_state.selected_penguin = 2
            st.session_state.penguin_action_done = None
            st.rerun()

    with col_p3:
        render_html(
            f"""
            <div class="penguin-card">
                {render_kawaii_penguin_svg(accessory="heart", size=170)}
                <div class="polaroid-caption" style="font-size:1.4rem;">Penguin #3 ❤️</div>
                <div class="cute-tag">the most important</div>
            </div>
            """
        )
        if st.button("Choose Penguin 3 ❤️", key="p3_btn"):
            st.session_state.selected_penguin = 3
            st.session_state.penguin_action_done = None
            st.rerun()

    sel = st.session_state.selected_penguin
    if sel is not None:
        render_html("<div style='height: 20px;'></div>")
        if sel == 1:
            render_html(
                """
                <div class="scrapbook-card anim-pulse" style="border: 2px solid #E76F51; background: #FFFBF5;">
                    <span class="cute-tag">💌 Penguin 1 gave you a reminder:</span>
                    <div class="handwritten-title" style="font-size:2.4rem; margin-top:10px;">A Little Reminder...</div>
                    <div style="font-family:'Patrick Hand', cursive; font-size:1.6rem; color:#5C4033; line-height:1.7;">
                        <p>✨ You are loved more than you realize.</p>
                        <p>🌸 You are deeply important.</p>
                        <p>💖 You are breathtakingly beautiful.</p>
                        <p>👑 And you deserve every single good thing coming your way in life.</p>
                    </div>
                </div>
                """
            )
            col_act1, col_act2, col_act3 = st.columns([1, 2, 1])
            with col_act2:
                if st.session_state.penguin_action_done != "p1":
                    if st.button("Keep this forever ❤️", key="p1_keep_btn"):
                        st.session_state.penguin_action_done = "p1"
                        st.balloons()
                        st.rerun()
                else:
                    render_html("<div style='text-align:center;'><span class='cute-tag' style='background:#FFE5D9;'>Saved in your heart forever 🌸🔐</span></div>")

        elif sel == 2:
            render_html(
                """
                <div class="scrapbook-card anim-pulse" style="border: 2px solid #E76F51; background: #FFFBF5;">
                    <span class="cute-tag">🎁 Penguin 2 opened your gift box:</span>
                    <div class="handwritten-title" style="font-size:2.4rem; margin-top:10px;">Your Lifetime Coupons 🎉</div>
                    <div style="font-family:'Patrick Hand', cursive; font-size:1.55rem; color:#5C4033; text-align:left; max-width:480px; margin:0 auto; line-height:1.8;">
                        <p>🤗 <b>A lifetime supply</b> of tight, warm hugs</p>
                        <p>😘 <b>Unlimited</b> forehead and cheek kisses</p>
                        <p>😂 <b>Unlimited</b> silly arguments and annoying jokes</p>
                        <p>❤️ <b>And one partner</b> who promises to keep loving you forever and ever</p>
                    </div>
                </div>
                """
            )
            col_act1, col_act2, col_act3 = st.columns([1, 2, 1])
            with col_act2:
                if st.session_state.penguin_action_done != "p2":
                    if st.button("Claim all coupons 🎟️❤️", key="p2_claim_btn"):
                        st.session_state.penguin_action_done = "p2"
                        st.balloons()
                        st.rerun()
                else:
                    render_html("<div style='text-align:center;'><span class='cute-tag' style='background:#F7CAD0;'>Coupons claimed & valid for life! 🥰✨</span></div>")

        elif sel == 3:
            render_html(
                """
                <div class="scrapbook-card anim-pulse" style="border: 2px solid #E76F51; background: #FFFBF5;">
                    <span class="cute-tag">❤️ Penguin 3 handed you the ultimate gift:</span>
                    <div class="handwritten-title" style="font-size:2.6rem; margin-top:10px;">YOU FOUND THE MOST IMPORTANT GIFT 💖</div>
                    <div class="anim-heartbeat" style="font-size:5rem; margin:10px 0;">❤️</div>
                    <div style="font-family:'Caveat', cursive; font-size:2.4rem; color:#E76F51; font-weight:700;">
                        My Whole Heart.
                    </div>
                    <p style="font-family:'Patrick Hand', cursive; font-size:1.6rem; color:#6E473B;">
                        It's already yours anyway, my Sona. ❤️
                    </p>
                </div>
                """
            )
            col_act1, col_act2, col_act3 = st.columns([1, 2, 1])
            with col_act2:
                if st.session_state.penguin_action_done != "p3":
                    if st.button("Take my whole heart 💖", key="p3_heart_btn"):
                        st.session_state.penguin_action_done = "p3"
                        st.balloons()
                        st.rerun()
                else:
                    render_html("<div style='text-align:center;'><span class='cute-tag' style='background:#FFE5D9;'>It will always belong to you, Baby ❤️</span></div>")

        # The Secret Finale Trigger
        render_html(
            """
            <div style="text-align:center; margin: 30px 0 15px 0;">
                <p style="font-family:'Patrick Hand', cursive; font-size:1.8rem; color:#E76F51; font-weight:700;">
                    "Wait... there is still one more thing." 👀✨
                </p>
            </div>
            """
        )

        col_fin1, col_fin2, col_fin3 = st.columns([1, 2, 1])
        with col_fin2:
            if st.button("OPEN THE LAST SURPRISE ❤️", key="open_final_btn"):
                st.balloons()
                next_stage()


# -----------------------------------------------------------------------------
# 14. FINAL SCENE: "FINAL LOVE REVEAL"
# -----------------------------------------------------------------------------
def scene_final_reveal():
    """Scene 8: Grand finale, staged handwriting I LOVE YOU, music player, easter egg, and reset."""
    st.balloons()

    render_html(
        """
        <div class="scrapbook-card">
            <div class="washi-tape washi-tape-pink"></div>
            <div class="washi-tape-corner-left"></div>
            <div class="washi-tape-corner-right"></div>
            
            <div style="padding: 20px 0;">
                <div class="hw-line1" style="font-family:'Caveat', cursive; font-size:2.8rem; color:#F4A261;">
                    I
                </div>
                <div class="hw-line2" style="font-family:'Caveat', cursive; font-size:3.6rem; color:#F4A261;">
                    LOVE
                </div>
                <div class="hw-line3 grand-love">
                    I LOVE YOU ❤️
                </div>
            </div>

            <div style="margin: 15px 0;">
                <span class="cute-tag">✨ HAPPY BIRTHDAY MY SONA ❤️ ✨</span>
            </div>

            <div style="font-family:'Caveat', cursive; font-size:2.2rem; color:#4A3525; line-height:1.6; max-width:680px; margin:20px auto; text-align:center;">
                <p>
                    Thank you for being part of my life.
                </p>
                <p>
                    I hope this birthday becomes one of those sweet memories that makes you smile whenever you look back on it.
                </p>
                <div style="font-size:2.4rem; color:#E76F51; font-weight:700; margin: 25px 0;">
                    Happy Birthday, Sona.<br/>
                    Happy Birthday, Mona.<br/>
                    Happy Birthday, Baby.<br/>
                    Happy Birthday, Amar Paakhi. 🐦❤️
                </div>
                <div style="font-size:1.8rem; color:#6E473B; font-family:'Patrick Hand', cursive;">
                    Forever & always yours, with all my love.
                </div>
            </div>

            <div style="margin: 20px 0; font-size: 2rem;">
                🌸 ✨ 🎂 💌 🐧 🎁 💖
            </div>
        </div>
        """
    )

    # Background Music Player Card
    music_file = find_music_file()
    render_html(
        """
        <div class="scrapbook-card" style="padding: 20px; background: #FFF9F2;">
            <div class="washi-tape" style="top:-10px; width:100px; height:20px;"></div>
            <div style="font-family:'Patrick Hand', cursive; font-size:1.5rem; color:#E76F51; font-weight:700; margin-bottom:8px;">
                🎵 Play our song
            </div>
        """
    )

    if music_file:
        audio_bytes = get_audio_bytes(music_file)
        if audio_bytes:
            st.audio(audio_bytes, format="audio/mp3")
            render_html(
                f"<div style='font-size:0.95rem; color:#8C533C; font-family:sans-serif;'>Playing: <b>{music_file.name}</b> 🎶</div>"
            )
    else:
        render_html(
            """
            <p style="font-family:'Patrick Hand', cursive; font-size:1.15rem; color:#8C533C;">
                Put your favorite romantic song in <code>assets/music/birthday_song.mp3</code> to hear it here!
            </p>
            """
        )
        uploaded_song = st.file_uploader("Or upload your song here right now 🎶:", type=["mp3", "wav", "m4a"], key="song_uploader")
        if uploaded_song:
            st.audio(uploaded_song)

    render_html("</div>")

    # Secret Easter Egg
    render_html("<div style='text-align:center; margin: 30px 0 10px 0;'>")
    col_e1, col_e2, col_e3 = st.columns([1, 1.5, 1])
    with col_e2:
        render_html('<div class="btn-soft">')
        if st.button("Don't click this heart 👀", key="easter_egg_btn"):
            st.session_state.easter_egg_clicked = not st.session_state.easter_egg_clicked
            st.rerun()
        render_html('</div>')

    if st.session_state.easter_egg_clicked:
        render_html(
            """
            <div style="text-align:center; margin: 15px auto;">
                <div class="speech-bubble anim-pulse" style="background:#FFE5D9; border-color:#E76F51;">
                    <div style="font-size:1.5rem; color:#E76F51; font-weight:700;">
                        You never listen 😂❤️
                    </div>
                    <div style="font-size:1.25rem; color:#6E473B; margin-top:4px;">
                        ...but that's honestly one of the things I love most about you, my Baby!
                    </div>
                </div>
            </div>
            """
        )

    # Experience Again Reset Button
    render_html("<div style='height: 35px;'></div>")
    col_r1, col_r2, col_r3 = st.columns([1, 1.6, 1])
    with col_r2:
        render_html('<div class="btn-soft">')
        if st.button("Experience it again ❤️", key="reset_btn"):
            reset_experience()
        render_html('</div>')


# -----------------------------------------------------------------------------
# 15. MAIN APPLICATION ROUTER
# -----------------------------------------------------------------------------
def main():
    """Main routing controller orchestrating the 8 scrapbook stages."""
    initialize_state()
    inject_custom_css()
    render_top_navigation()

    stage = st.session_state.stage

    if stage == 0:
        scene_accept_gift()
    elif stage == 1:
        scene_birthday_reveal()
    elif stage == 2:
        scene_birthday_letter()
    elif stage == 3:
        scene_photo_scrapbook()
    elif stage == 4:
        scene_little_memories()
    elif stage == 5:
        scene_why_i_love_you()
    elif stage == 6:
        scene_choose_penguin()
    elif stage == 7:
        scene_final_reveal()
    else:
        scene_accept_gift()


if __name__ == "__main__":
    main()
