# To define a function to convert giving rbg value to HEX value
def rgbToHex (r, g, b):
    # To convert each of the rgb value into HEX value and then concatenate together
    def dectohex(num):
        hex_chars = "0123456789ABCDEF"
        return hex_chars[num // 16] + hex_chars[num % 16]

    hex_value = dectohex(r) + dectohex(g) + dectohex(b)
    return hex_value

# Set the corresponding RGB value and call the conversion function
while True:
    red = int(input("Please input the value of R: "))
    green = int(input("Please input the value of G: "))
    blue = int(input("Please input the value of B: "))
    # To make sure the value input is within 0 to 255
    if 0 <= red <= 255 or 0 <= green <= 255 or 0 <= blue <= 255:
        break
    else:
        print("Please enter an integer value within 0 to 255 for RGB value!")

print(f"The input RGB value is: ({red}, {green}, {blue})")

hex_color = rgbToHex(red, green, blue)
print("The HEX value of correspond RGB value is:", hex_color)