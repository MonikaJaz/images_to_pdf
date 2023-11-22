from PIL import Image
from fpdf import FPDF
import os


def merge_images_to_pdf(input_folder, output_pdf):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]


    if not image_files:
        print("There is no photos to convert to pdf!.")
        return

    # sorting files by order
    image_files.sort()

    pdf = FPDF()

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        pdf.add_page()
        pdf.image(image_path, 0, 0, pdf.w, pdf.h)


    pdf.output(output_pdf, "File")

    print(f"The images have been merged to the pdf file: {output_pdf}")



input_folder = "file path"
output_pdf = "name of the pdf file.pdf"
merge_images_to_pdf(input_folder, output_pdf)
