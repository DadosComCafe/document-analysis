from pathlib import Path
import pymupdf
import logging


def pdf_to_png(pdf_path: str, output_path: str = "pngs", dpi: int = 200) -> None:
    """Converts pdf file in png file

    Args:
        pdf_path (str): The path of pdf input
        output_path (str, optional): The path of directory output. Defaults to "pngs".
        dpi (int, optional): Image quality. Defaults to 200.

    Raises:
        FileNotFoundError: An error message indicating the file couldn't be found.
    """
    pdf = Path(pdf_path)

    if not pdf.is_file():
        raise FileNotFoundError(f"File not Found: {pdf}")

    pasta = Path(output_path)
    pasta.mkdir(parents=True, exist_ok=True)

    zoom = dpi / 72
    matriz = pymupdf.Matrix(zoom, zoom)

    file_name = pdf_path.split("/")[-1].split(".pdf")[0]
    with pymupdf.open(pdf) as doc:
        for _indice, pagina in enumerate(doc, start=1):
            pixmap = pagina.get_pixmap(matrix=matriz)
            arquivo_png = pasta / f"{file_name}.png"
            pixmap.save(arquivo_png)
            print(f"Gerado: {arquivo_png}")


if __name__ == "__main__":
    import os
    path_pdf = "invoices_pdf/indian_invoices/"
    path_img = "invoices_images/indian_invoices/"
    list_of_invoices = os.listdir(path_pdf)
    
    for invoice in list_of_invoices:
        print(invoice)
        pdf_to_png(pdf_path=f"{path_pdf}/{invoice}", output_path=path_img)



