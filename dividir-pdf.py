import PyPDF2

def split_pdf(input_pdf, output_prefix):
    # Abrir el archivo PDF en modo lectura binaria
    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)

        # Recorrer cada página y guardarla como un nuevo archivo
        for page_num in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])

            # Crear el nombre del archivo con formato EA2P-XXX.pdf
            output_filename = f"{output_prefix}-{page_num+1:03}.pdf"

            # Guardar la nueva página en un archivo separado
            with open(output_filename, "wb") as output_pdf:
                writer.write(output_pdf)

            print(f"Página {page_num+1} guardada como {output_filename}")

# Uso del script
split_pdf("libreta-Aris-parcial2.pdf", "EA2P")
