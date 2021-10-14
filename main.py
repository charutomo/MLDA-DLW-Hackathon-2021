from image import Image

def main():
    run = init_program()

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
    if type(_input) is not Image:
        print("Please pass an image into the program.")
    else:
        pass

# Processes the image using the ML and returns a score
def process_image(_image):
    pass

if __name__ == '__main__':
    main()