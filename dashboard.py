wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes, colors in wardrobe.items():
    print(clothes)
    for color in colors:
        print("{} {}".format(color, clothes))

