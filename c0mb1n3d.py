from PIL import Image
import numpy as np

def combine_images(image1, image2, operation):
    operations = {
        "subtract": np.subtract,
        "add": np.add,
        "xor": np.bitwise_xor,
        "or": np.bitwise_or,
        "multiply": np.multiply,
    }
    result_array = operations[operation](image1, image2)
    return Image.fromarray(result_array)

if __name__ == "__main__":
    img1 = np.array(Image.open("chall.png"))
    img2 = np.array(Image.open("incredible.png"))
    operators = ['add', 'xor', 'or', 'multiply', 'subtract']
    
    for operation in operators:
        result_image = combine_images(img1, img2, operation)
        result_image.show(operation)
