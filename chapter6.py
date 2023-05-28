"""
Made by Afik
"""
import tkinter as tk
import base64
import pyttsx3


# 6.1.3
def show_image():
    image_label.configure(image=photo)
    image_label.image = photo


# 6.1.3
def create_window():
    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Who is the GOAT?")

    # Create a label with the question
    question_label = tk.Label(window, text="Who is the GOAT?")
    question_label.pack()

    # Create a button
    button = tk.Button(window, text="Show Image", command=show_image)
    button.pack()

    # Create a label for the image (initially empty)
    global image_label
    image_label = tk.Label(window)
    image_label.pack()

    # Load the image
    global photo
    photo = tk.PhotoImage(file="ronaldo.gif")

    # Start the main loop
    window.mainloop()


# 6.1.4 (Permission)
def decode():
    encoded_message = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo= "

    # Decode the Base64-encoded message
    decoded_bytes = base64.b64decode(encoded_message)

    # Decode the UTF-8 encoded bytes to string
    decoded_message = decoded_bytes.decode("utf-8")
    print(decoded_message)


# 6.3.3
def read_sentence():
    sentence = "first time i'm using a package in next.py course"

    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()


def main():
    # 6.1.3
    create_window()

    # 6.1.4 (Permission)
    decode()

    # 6.3.3
    read_sentence()


if __name__ == "__main__":
    main()
