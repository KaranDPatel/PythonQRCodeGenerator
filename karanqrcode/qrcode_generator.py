import qrcode
import json
import os
def get_qrcode(json_data):
    print('calling..')

    # Convert the JSON data to a string
    json_str = json.dumps(json_data)

    # Generate the QR code
    qr = qrcode.QRCode()
    qr.add_data(json_str)
    qr.make()

    # Create an image from the QR code
    image = qr.make_image()
    image_path = '{}.png'.format(json_data['name'])
    image.save(image_path)

    # Return the image
    return image

# json_data = {
#         'name': 'Karan',
#         'age': 27
#     }

# image_qrcode=get_qrcode(json_data)
# image_qrcode.show()
