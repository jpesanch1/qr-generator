import qrcode


def generate_qr(text, output_file_name):
    img = qrcode.make(text)
    type(img)  # qrcode.image.pil.PilImage
    img.save("../images-qr/"+output_file_name+".png")


if __name__ == "__main__":
    message = "Bienvenidos a 1985"
    file_text = "invitacion"
    generate_qr(message, file_text)