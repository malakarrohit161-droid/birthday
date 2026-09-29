"""
Asset Generator for Romantic Birthday Website
Generates cute kawaii placeholder images (penguins, cake, heart, gift, polaroid photos)
using Pillow.
"""
from PIL import Image, ImageDraw, ImageFont
import os
import math

os.makedirs("assets/images", exist_ok=True)
os.makedirs("assets/photos", exist_ok=True)
os.makedirs("assets/music", exist_ok=True)

def draw_heart(draw, center, size, color):
    x, y = center
    # Heart shape using bezier or circles + polygon
    r = size / 2
    # Two circles and a triangle
    draw.ellipse([x - r, y - r, x, y], fill=color)
    draw.ellipse([x, y - r, x + r, y], fill=color)
    draw.polygon([x - r * 0.95, y - r * 0.2, x + r * 0.95, y - r * 0.2, x, y + r * 0.9], fill=color)

def create_penguin(filename, accessory="letter"):
    # 400x400 cute kawaii penguin
    img = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Body shadow
    draw.ellipse([100, 320, 300, 360], fill=(230, 210, 200, 140))
    
    # Feet (orange)
    draw.ellipse([120, 310, 180, 345], fill="#F4A261")
    draw.ellipse([220, 310, 280, 345], fill="#F4A261")
    
    # Main Body (navy/charcoal #3D405B)
    draw.ellipse([100, 90, 300, 330], fill="#3D405B")
    
    # White Tummy / Face
    draw.ellipse([125, 125, 275, 320], fill="#FFFBF2")
    
    # Wings / Flippers
    # Left wing
    draw.ellipse([70, 160, 125, 260], fill="#3D405B")
    # Right wing
    draw.ellipse([275, 160, 330, 260], fill="#3D405B")
    
    # Eyes (shiny kawaii black dots with white sparkles)
    # Left eye
    draw.ellipse([160, 165, 178, 185], fill="#264653")
    draw.ellipse([163, 167, 169, 173], fill="#FFFFFF")
    draw.ellipse([171, 176, 175, 180], fill="#FFFFFF")
    # Right eye
    draw.ellipse([222, 165, 240, 185], fill="#264653")
    draw.ellipse([225, 167, 231, 173], fill="#FFFFFF")
    draw.ellipse([233, 176, 237, 180], fill="#FFFFFF")
    
    # Rosy Cheeks (blush)
    draw.ellipse([140, 185, 165, 202], fill="#F8AD9D")
    draw.ellipse([235, 185, 260, 202], fill="#F8AD9D")
    
    # Beak (orange triangle)
    draw.polygon([(200, 180), (188, 195), (212, 195)], fill="#E76F51")
    
    # Party hat or bow or accessory
    if accessory == "letter":
        # Envelope held in flippers
        draw.rectangle([160, 220, 240, 275], fill="#FFE5D9", outline="#E76F51", width=3)
        draw.polygon([(160, 220), (200, 248), (240, 220)], fill="#FCD5CE", outline="#E76F51")
        # Little red heart wax seal
        draw_heart(draw, (200, 248), 16, "#E76F51")
        # Cute birthday party hat
        draw.polygon([(170, 95), (230, 95), (200, 30)], fill="#F4A261")
        draw.line([(170, 95), (200, 30)], fill="#E76F51", width=3)
        draw.line([(230, 95), (200, 30)], fill="#E76F51", width=3)
        draw.ellipse([193, 22, 207, 36], fill="#E76F51") # pompom
        
    elif accessory == "gift":
        # Gift Box held in center
        draw.rectangle([155, 220, 245, 290], fill="#F7CAD0", outline="#E76F51", width=3)
        # Ribbon vertical & horizontal
        draw.rectangle([192, 220, 208, 290], fill="#E76F51")
        draw.rectangle([155, 248, 245, 262], fill="#E76F51")
        # Bow on top
        draw.ellipse([175, 205, 200, 225], fill="#E76F51")
        draw.ellipse([200, 205, 225, 225], fill="#E76F51")
        draw.ellipse([193, 212, 207, 226], fill="#F4A261")
        # Small flower on head
        draw.ellipse([185, 80, 215, 105], fill="#FFD166")
        draw.ellipse([195, 87, 205, 97], fill="#E76F51")
        
    elif accessory == "heart":
        # Big glowing heart held in flippers
        draw_heart(draw, (200, 245), 65, "#E76F51")
        # Sparkle
        draw.line([(185, 225), (185, 235)], fill="#FFFFFF", width=3)
        draw.line([(180, 230), (190, 230)], fill="#FFFFFF", width=3)
        # Little bow on top of head
        draw.ellipse([182, 85, 200, 100], fill="#F8AD9D")
        draw.ellipse([200, 85, 218, 100], fill="#F8AD9D")
        draw.ellipse([195, 90, 205, 98], fill="#E76F51")
        
    img.save(filename, "PNG")

def create_cake(filename):
    img = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Cake stand
    draw.ellipse([80, 310, 320, 350], fill="#E9ECEF")
    draw.polygon([(185, 330), (215, 330), (230, 370), (170, 370)], fill="#CED4DA")
    draw.ellipse([160, 360, 240, 380], fill="#ADB5BD")
    
    # Bottom Layer (Strawberry cream)
    draw.rounded_rectangle([110, 230, 290, 320], radius=15, fill="#FCD5CE", outline="#E76F51", width=3)
    # Icing drips
    for cx in range(120, 285, 28):
        draw.ellipse([cx, 240, cx + 24, 260], fill="#FFF0F3")
    draw.rectangle([112, 232, 288, 250], fill="#FFF0F3")
    
    # Top Layer
    draw.rounded_rectangle([135, 160, 265, 235], radius=12, fill="#FFE5D9", outline="#E76F51", width=3)
    for cx in range(145, 260, 24):
        draw.ellipse([cx, 168, cx + 20, 185], fill="#FFF0F3")
    draw.rectangle([137, 162, 263, 175], fill="#FFF0F3")
    
    # Sprinkles / Candies
    colors = ["#E76F51", "#F4A261", "#F6BD60", "#F7CAD0"]
    coords = [(140, 275), (175, 285), (220, 270), (265, 280), (160, 205), (195, 210), (235, 200)]
    for i, (sx, sy) in enumerate(coords):
        draw.ellipse([sx, sy, sx + 8, sy + 8], fill=colors[i % len(colors)])
        
    # Candle
    draw.rectangle([193, 110, 207, 162], fill="#FDE4CF", outline="#E76F51", width=2)
    # Candle stripes
    draw.line([(193, 125), (207, 120)], fill="#E76F51", width=2)
    draw.line([(193, 145), (207, 140)], fill="#E76F51", width=2)
    
    # Wick
    draw.line([(200, 100), (200, 110)], fill="#264653", width=2)
    
    # Flame (glowing teardrop)
    draw.ellipse([190, 75, 210, 102], fill="#F6BD60")
    draw.ellipse([194, 82, 206, 98], fill="#E76F51")
    
    # Tiny heart on cake
    draw_heart(draw, (200, 195), 18, "#E76F51")
    
    img.save(filename, "PNG")

def create_heart_img(filename):
    img = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Glowing shadow
    draw_heart(draw, (200, 205), 180, (247, 202, 208, 120))
    # Main heart
    draw_heart(draw, (200, 200), 160, "#E76F51")
    # Soft highlight
    draw.ellipse([145, 140, 175, 170], fill="#F8AD9D")
    draw.ellipse([150, 145, 165, 160], fill="#FFFFFF")
    img.save(filename, "PNG")

def create_gift_img(filename):
    img = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Shadow
    draw.ellipse([90, 320, 310, 360], fill=(220, 200, 190, 130))
    # Box base
    draw.rounded_rectangle([110, 170, 290, 330], radius=15, fill="#F7CAD0", outline="#E76F51", width=4)
    # Lid
    draw.rounded_rectangle([95, 140, 305, 185], radius=10, fill="#FFB5A7", outline="#E76F51", width=4)
    # Vertical ribbon
    draw.rectangle([185, 140, 215, 330], fill="#E76F51")
    # Horizontal ribbon
    draw.rectangle([110, 235, 290, 265], fill="#E76F51")
    # Big Bow loops
    draw.ellipse([140, 95, 195, 145], fill="#E76F51")
    draw.ellipse([150, 105, 185, 135], fill="#FFB5A7")
    draw.ellipse([205, 95, 260, 145], fill="#E76F51")
    draw.ellipse([215, 105, 250, 135], fill="#FFB5A7")
    draw.ellipse([185, 120, 215, 145], fill="#F6BD60")
    # Sparkles around
    for sx, sy in [(80, 120), (320, 110), (70, 270), (330, 260)]:
        draw_heart(draw, (sx, sy), 15, "#F8AD9D")
        
    img.save(filename, "PNG")

def create_sample_photo(filename, title, subtitle, bg_color):
    # 600x600 romantic polaroid-style image
    img = Image.new("RGB", (600, 600), "#FFFDF7")
    draw = ImageDraw.Draw(img)
    
    # Inner photo canvas
    draw.rectangle([35, 35, 565, 475], fill=bg_color)
    
    # Cute illustration inside photo canvas
    # Soft sun/circle
    draw.ellipse([200, 100, 400, 300], fill="#FFF9F0")
    # Cute hearts
    draw_heart(draw, (300, 220), 80, "#E76F51")
    draw_heart(draw, (230, 160), 35, "#F8AD9D")
    draw_heart(draw, (370, 170), 30, "#F8AD9D")
    
    # Little sparkles
    draw.line([(290, 90), (310, 90)], fill="#F6BD60", width=3)
    draw.line([(300, 80), (300, 100)], fill="#F6BD60", width=3)
    
    # Handwritten style label on bottom of polaroid
    try:
        font_big = ImageFont.truetype("arial.ttf", 36)
        font_sub = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font_big = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    # Bottom text
    draw.text((300, 500), title, fill="#5C4033", anchor="mm", font=font_big)
    draw.text((300, 540), subtitle, fill="#8C533C", anchor="mm", font=font_sub)
    
    # Polaroid border line
    draw.rectangle([35, 35, 565, 475], outline="#F4A261", width=2)
    
    img.save(filename, "JPEG", quality=95)

if __name__ == "__main__":
    print("Generating cute penguin illustrations...")
    create_penguin("assets/images/penguin1.png", "letter")
    create_penguin("assets/images/penguin2.png", "gift")
    create_penguin("assets/images/penguin3.png", "heart")
    
    print("Generating cake, heart and gift box...")
    create_cake("assets/images/cake.png")
    create_heart_img("assets/images/heart.png")
    create_gift_img("assets/images/gift.png")
    
    print("Generating starter romantic polaroid photos...")
    photos = [
        ("assets/photos/photo1.jpg", "My Cutie ❤️", "The prettiest smile in the world", "#FFE5D9"),
        ("assets/photos/photo2.jpg", "My Baby 🌸", "Every day is brighter with you", "#FCD5CE"),
        ("assets/photos/photo3.jpg", "My Sona ✨", "My favorite adventure partner", "#FDE4CF"),
        ("assets/photos/photo4.jpg", "My Mona 🍰", "Sweeter than any birthday cake", "#F7CAD0"),
        ("assets/photos/photo5.jpg", "My Favorite Person 🥰", "Forever and always my number one", "#FFE8D6"),
        ("assets/photos/photo6.jpg", "My Amar Paakhi 🐦❤️", "The one who owns my whole heart", "#FFD7BA")
    ]
    for p, t, s, c in photos:
        create_sample_photo(p, t, s, c)
        
    print("Assets successfully generated!")
