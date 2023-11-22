from PIL import Image
from fpdf import FPDF
import os

def merge_images_to_pdf(input_folder, output_pdf):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("There is no photos to convert to pdf!.")
        return

    # sorting files by order
    image_files.sort(key=lambda x: int(x.split('.')[0]))

    pdf = FPDF()

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        if image.width > pdf.w or image.height > pdf.h:
            ratio = min(pdf.w / image.width, pdf.h / image.height)
            width = image.width * ratio
            height = image.height * ratio
        else:
            width = image.width
            height = image.height

        pdf.add_page()
        pdf.image(image_path, x=pdf.w / 2 - width / 2, y=pdf.h / 2 - height / 2, w=width, h=height)

        pdf.add_page()
        pdf.image(image_path, 10, 10, pdf.w - 20, pdf.h)


    output_pdf_path = os.path.join(input_folder, output_pdf)

    pdf.output(output_pdf_path, "F")

    print(f"The images have been merged to the pdf file: {output_pdf_path}")

input_folder = "folder path"
output_pdf = "name.pdf"
merge_images_to_pdf(input_folder, output_pdf)
