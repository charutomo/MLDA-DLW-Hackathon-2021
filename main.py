from PIL import Image

def main():
    run = init_program()

    image = handle_image("test.png")
    display_image(image)

    while (run):
        pass

    # Take in image
    
    term_program()

def init_program():
    return True

def term_program():
    pass

# Takes in the input file and determines if it is an image
def handle_image(_input):
    # Handle wrong inputs
    return Image.open(_input)

def display_image(_image):
    _image.show()

# Processes the image using the ML and returns a score
def process_image(_image):
    pass

if __name__ == '__main__':
    main()