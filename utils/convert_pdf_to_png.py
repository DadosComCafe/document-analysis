from pathlib import Path
import pymupdf


def pdf_para_png(caminho_pdf: str, pasta_saida: str = "pngs", dpi: int = 200) -> None:
    pdf = Path(caminho_pdf)

    if not pdf.is_file():
        raise FileNotFoundError(f"Arquivo não encontrado: {pdf}")

    pasta = Path(pasta_saida)
    pasta.mkdir(parents=True, exist_ok=True)

    zoom = dpi / 72
    matriz = pymupdf.Matrix(zoom, zoom)

    with pymupdf.open(pdf) as doc:
        for indice, pagina in enumerate(doc, start=1):
            pixmap = pagina.get_pixmap(matrix=matriz)
            arquivo_png = pasta / f"{pdf.stem}_pagina_{indice}.png"
            pixmap.save(arquivo_png)
            print(f"Gerado: {arquivo_png}")
