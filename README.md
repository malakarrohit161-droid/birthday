# ❤️ Happy Birthday Sona - Interactive Romantic Scrapbook Website

An emotional, cute, playful, and deeply personal interactive birthday website built with **Python & Streamlit**.

Designed with a warm **handmade kawaii scrapbook / diary aesthetic** featuring soft pastel tones, washi tape, polaroids, sweet illustrations, and gentle micro-animations.

---

## 📁 Project Structure

```text
babyy/
│
├── app.py                      # Main Streamlit application with all 8 interactive scenes
├── requirements.txt            # Minimal dependencies (streamlit, Pillow)
├── .gitignore                  # Clean repository ignore rules
├── README.md                   # Complete beginner guide & deployment instructions
├── create_assets.py            # Helper script that generated the starter graphics
│
└── assets/
    │
    ├── photos/                 # Place your wife's photos here!
    │   ├── photo1.jpg          # Main polaroid photo for Scene 3 (Birthday Letter)
    │   ├── photo2.jpg          # Scrapbook Memory photo 2 ("My Baby")
    │   ├── photo3.jpg          # Scrapbook Memory photo 3 ("My Sona")
    │   ├── photo4.jpg          # Scrapbook Memory photo 4 ("My Mona")
    │   ├── photo5.jpg          # Scrapbook Memory photo 5 ("My Favorite Person")
    │   └── photo6.jpg          # Scrapbook Memory photo 6 ("My Amar Paakhi")
    │
    ├── music/                  # Romantic background music
    │   ├── birthday_song.mp3   # Drop your favorite romantic song here
    │   └── birthday_chime.wav  # Built-in sweet chime
    │
    └── images/                 # Cute starter illustrations (penguins, cake, heart, gift)
        ├── penguin1.png
        ├── penguin2.png
        ├── penguin3.png
        ├── cake.png
        ├── heart.png
        └── gift.png
```

> **Note:** The app includes built-in fallbacks with cute illustrations. If any photo or audio file is missing, the application will **never crash**; it will simply display a charming placeholder.

---

## 📖 Experience Journey (8 Interactive Scenes)

1. **Scene 1: "PLS ACCEPT THE GIFT 🎁"**  
   Shy blushing penguin holding a gift with floating pastel hearts. Features a playful **NO 😤** button that cycles through funny pleading messages without ever letting her leave, and a glowing **YES ❤️** button.
2. **Scene 2: "HAPPY BIRTHDAY REVEAL & MAKE A WISH 🎂"**  
   Celebration reveal with a 2-tier strawberry cake and a flickering candle flame. Clicking **"I MADE MY WISH ❤️"** animates the candle blowing out with a smoke puff and reveals a sweet blessing.
3. **Scene 3: "PERSONAL BIRTHDAY LETTER 💌"**  
   A vintage scrapbook page with her polaroid photo (`photo1.jpg`) on the left and a heartfelt, romantic letter on lined paper on the right.
4. **Scene 4: "PHOTO MEMORY SCRAPBOOK 📸"**  
   Artistic scrapbook collage featuring 6 tilted polaroid photos with custom washi tape, stamps, and personalized nicknames (*"My Love"*, *"My Baby"*, *"My Sona"*, *"My Mona"*, *"My Favorite Person"*, *"My Amar Paakhi"*).
5. **Scene 5: "OUR LITTLE MEMORIES 📖"**  
   Interactive diary cards where she can click to reveal 7 treasured memories one by one (*"Our random conversations"*, *"Your smile"*, *"The way you get angry"*, *"Our silly fights"*, etc.).
6. **Scene 6: "WHY I LOVE YOU 💖"**  
   Clickable glowing heart cards that flip to reveal reasons why she's so special to you.
7. **Scene 7: "CHOOSE A PENGUIN 🐧"**  
   Three cute penguins offering unique surprises:
   - **Penguin 1 💌:** An emotional reminder of how loved and important she is.
   - **Penguin 2 🎁:** Lifetime supply of hugs, unlimited kisses, and laughter coupons.
   - **Penguin 3 ❤️:** *"YOU FOUND THE MOST IMPORTANT GIFT: My heart. It's already yours anyway."*
8. **Final Scene: "FINAL LOVE REVEAL & OUR SONG 🎶"**  
   Grand finale with handwriting animation, massive **I LOVE YOU ❤️**, celebration balloons, a romantic music player, a secret easter egg (*"Don't click this heart 👀"*), and a reset button to experience it all over again.

---

## 🚀 Beginner Setup Guide (Step-by-Step)

### Step 1: Open the Project in VS Code
1. Open **VS Code** (or Antigravity IDE).
2. Go to **File** → **Open Folder...**
3. Select this folder: `c:\Users\malak\OneDrive\Desktop\babyy`

---

### Step 2: Open Terminal & Create Virtual Environment
Open the built-in terminal in VS Code (`Ctrl + ` ` or **Terminal** → **New Terminal**) and run:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

*(If PowerShell blocks script execution, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first).*

---

### Step 3: Install Dependencies
Run:

```powershell
pip install -r requirements.txt
```

---

### Step 4: Run the Website Locally
Start the Streamlit application:

```powershell
streamlit run app.py
```

Your default web browser will automatically open:
```text
http://localhost:8501
```

---

## 📸 Customizing Photos & Music

### 1. Adding Your Wife's Real Photos
Simply copy 6 of her prettiest photos into the `assets/photos/` folder:
- `assets/photos/photo1.jpg` (Used in the Birthday Letter card)
- `assets/photos/photo2.jpg`
- `assets/photos/photo3.jpg`
- `assets/photos/photo4.jpg`
- `assets/photos/photo5.jpg`
- `assets/photos/photo6.jpg`

*(Supported formats: `.jpg`, `.jpeg`, `.png`)*

### 2. Adding Romantic Background Music
Copy your song file into:
```text
assets/music/birthday_song.mp3
```
The music card at the end will automatically detect and play it! If you don't have the file ready, there is also an instant file uploader right inside the web page.

### 3. Personalizing Nicknames & Messages
All text is organized clearly inside `app.py`. If you want to customize any memories or add inside jokes:
- **Letter text:** Search for `def scene_birthday_letter()` in `app.py`.
- **Little Memories:** Search for `memories = [...]` in `app.py`.
- **Reasons Why I Love You:** Search for `reasons = [...]` in `app.py`.

---

## 📱 Testing on Mobile (Phone / Tablet)

Because she will likely open it on her phone, you can test it directly on your mobile device while connected to the same Wi-Fi network:

1. When you run `streamlit run app.py`, Streamlit shows a **Network URL**:
   ```text
   Network URL: http://192.168.x.x:8501
   ```
2. Make sure your phone is connected to the same Wi-Fi.
3. Open Chrome or Safari on your phone and type that URL.
4. The page is completely mobile-responsive with centered cards and touch-friendly buttons!

---

## ☁️ How to Deploy Online (Free Public Link for Her!)

To send her a clean link (e.g. `https://sona-birthday.streamlit.app`) so she can open it anywhere on her phone:

### Step 1: Push Project to GitHub
1. Create a free account at [GitHub.com](https://github.com).
2. Create a new repository named `birthday-surprise`.
3. In your VS Code terminal, run:
   ```bash
   git init
   git add .
   git commit -m "Happy Birthday surprise for my wife"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/birthday-surprise.git
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Community Cloud (100% Free)
1. Go to [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.
2. Click **"New app"**.
3. Select your repository: `birthday-surprise`.
4. Branch: `main`.
5. Main file path: `app.py`.
6. Click **"Deploy!"**.

In about 1-2 minutes, you will get a permanent public link to send to her with love! ❤️
