import argparse
import glob
import os
from vtf2img import Parser
from PIL import Image
from typing import List
from concurrent.futures import ThreadPoolExecutor

DEFAULT_OUTPUT_DIR: str = "Textures"

def to_bmp(input_file: str) -> None:
    try:
        if input_file.lower().endswith('.vtf'):
            parser: Parser = Parser(input_file)
            img: Image.Image = parser.get_image()
        else:
            img: Image.Image = Image.open(input_file).convert("RGB")

        quantized: Image.Image = img.quantize(
            colors=256,
            method=Image.Quantize.FASTOCTREE,
            dither=Image.Dither.NONE
        )

        file_name, _ = os.path.splitext(os.path.basename(input_file))
        output_path: str = os.path.join(DEFAULT_OUTPUT_DIR, f"{file_name}.bmp")
        quantized.save(output_path, format="BMP")

    except Exception as error:
        print(f"Error processing {input_file}: {error}")

def parse_arguments() -> List[str]:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        type=str,
        nargs='+',
        help="Paths to image files or directories containing images."
    )
    args: argparse.Namespace = parser.parse_args()
    return args.path

def get_files(paths: List[str]) -> List[str]:
    files: List[str] = []
    for path in paths:
        if '*' in path:
            files.extend(glob.glob(path))
        elif os.path.isdir(path):
            files.extend([os.path.join(path, file) for file in os.listdir(path)])
        else:
            files.append(path)
    return files

def main() -> None:
    paths: List[str] = parse_arguments()
    files: List[str] = get_files(paths)

    if not os.path.exists(DEFAULT_OUTPUT_DIR):
        os.makedirs(DEFAULT_OUTPUT_DIR)

    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(to_bmp, files)

if __name__ == "__main__":
    main()
