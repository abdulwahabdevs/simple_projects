import qrcode

class QRCodeGenerator:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def generate_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input("Enter a text: ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f"Successfully genereated! ({file_name})")
        except Exception as e:
            print(f'Error occured: {e}')


def main():
    qr = QRCodeGenerator(size=30,padding=2)
    qr.generate_qr("sample.png",
                   "black",
                   "white")

if __name__ == '__main__':
    main()

