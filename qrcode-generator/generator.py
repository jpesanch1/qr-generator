import qrcode
from PIL import Image
import time


def generate_qr(text, output_file_name):
    img = qrcode.make(text)
    type(img)  # qrcode.image.pil.PilImage
    img.save("../images-qr/"+output_file_name+".png")


def show_png(path_file_name):
    # creating an og_image object
    og_image = Image.open(path_file_name)
    og_image.show()


if __name__ == "__main__":
    message = "Bienvenidos a 1985"
    file_text = "invitacion"
    generate_qr(message, file_text)
    time.sleep(5)
    show_png("../images-qr/invitacion.png")