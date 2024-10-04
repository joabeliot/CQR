from PIL import Image

lut = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
       "+", "-", "*", "/", ".", ",", ":", ";", "\"", "\'", "\\", "%", "@", "!", "#", "(", ")", "[", "]", "&", "?", "`", "~", "{", "}",
       "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
       "_", " "]

def PixtoPixels(name, pixels):

    image = Image.new('RGB', (10, 10))
    
    image.putdata(pixels)

    image.save(f"{name}.png")
    
    image.show

def allocator(chain):
    return [tuple(chain[i:i+3]) for i in range(0, len(chain), 3)]

def translator(chain):
    pix = []

    for i in chain:
        if i in lut:
            pix.append((lut.index(i) * 4) - 2)
        else:
            print(f"Character {i} not found in LUT")
            pix.append(None)
    return pix

def processMessage(msg):
    msg = msg.upper()

    if not msg.startswith("`"):
        msg = "`" + msg

    if not msg.endswith("`"):
        msg = msg + "`"

    if isinstance(msg, str):
        msg = list(msg)

    while len(msg) % 3 != 0:
        msg[-1] = " "
        msg.append("`")
    
    translated = translator(msg)
    return allocator(translated)

msg = "hey beethoven how are you? What do you think will this be a good idea or not? Ig this is working but am not sure how to check this shit and this is actually pretty cool idk, I want you to see it and then tell me. Guess i've gotta add more stuff! and still more to make it 10X10. Numbers actually "
PixtoPixels("msg",processMessage(msg))
# print(len(msg))