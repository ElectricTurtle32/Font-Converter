from PIL import Image, ImageFont, ImageDraw


font_path = "font.ttf" 
font_size = 32  
font_name = "roboto"
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open("font.py", "w")

f.write("import framebuffer \n" + font_name + " = [")
for char in characters:
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Get the size of the character
    char_width, char_height = font.getbbox(char)[2], font.getbbox(char)[3]

    # Create an image with a white background
    image = Image.new("1", (char_width, char_height), color=1)  # '1' for 1-bit pixels
    draw = ImageDraw.Draw(image)
    
    # Draw the character in black
    draw.text((0, 0), char, font=font, fill=0)

    # Create a bytearray to hold the byte representation
    f.write(str([char_width, char_height, image.tobytes()])+",\n")
    print([char_width, char_height, image.tobytes()])
f.write("""
]
def text(string, x, y, buffer):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    for i in string:
        char_index = characters.index(i)  # Find the index of the character
        char_data = roboto[char_index]  # Get the font data

     
        charBuf = framebuf.FrameBuffer(bytearray(char_data[2]), char_data[0], char_data[1], framebuf.MONO_HLSB)

        buffer.blit(charBuf, x+index, y)
        index += characters.index('i')[0]
    
""")
