def main():

    CODE_TO_COLOR = {"black": "#000000", "blue1": "#0000ff", "brown	": "#a52a2a", "coral": "#ff7f50",
                     "white": "	#ffffff", "violet": "#ee82ee","tan": "#d2b48c", "springgreen1": "##00ff7f",
                     "skyblue": "#87ceeb", "salmon": "#fa8072"}

    colour_name = input("Enter a colour: ").lower()

    while colour_name != "":

        print("{} --- {}".format(colour_name,CODE_TO_COLOR.get(colour_name,'invalid')))
        colour_name = input("Enter a colour: ")


main()
