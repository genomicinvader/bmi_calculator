from PIL import Image, ImageDraw, ImageFont

# Create a 256x256 image
img = Image.new('RGB', (256, 256), color=(70, 130, 180))
draw = ImageDraw.Draw(img)

# Draw BMI text
try:
    font = ImageFont.truetype("arial.ttf", 80)
except:
    font = ImageFont.load_default()
draw.text((50, 80), "BMI", fill=(255, 255, 255), font=font)

# Save as ICO with multiple sizes
img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])