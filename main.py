import argparse
import glob
import os

from PIL import Image
from typing import List
from concurrent.futures import ThreadPoolExecutor

default_output_dir: str = "Textures"

def to_bmp(input: str) -> None:
  try:
    rgb: Image.Image = Image.open(input).convert("RGB")
    quantized: Image.Image = rgb.quantize(
      colors=256,
      method=Image.Quantize.MEDIANCUT,
      dither=Image.Dither.NONE
    )
    output_path: str = f"{default_output_dir}/{os.path.basename(input)}.bmp"
    quantized.save(output_path, format="BMP")
  except Exception as error:
    print(f"{input}: {error}")

def parse_arguments() -> List[str]:
  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  parser.add_argument(
    "path", 
    type=str,
    nargs='+'
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

  if not os.path.exists(default_output_dir):
    os.makedirs(default_output_dir)

  with ThreadPoolExecutor(max_workers=8) as executor:
    executor.map(to_bmp, files)  

if __name__ == "__main__":
  main()
