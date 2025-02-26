# to-bmp

This script converts .vtf (Valve Texture File) or other image files (such as .png, .jpg, etc.) into a format accepted by studiomdl. It supports batch processing of both individual files and directories.

---

## Features

- Batch Conversion: Process multiple image files or entire directories.
- Quantization: Converts images to 256 colors using the FastOctree quantization method to reduce the color palette.
- Multithreading: Uses ThreadPoolExecutor to process multiple files concurrently for faster execution.

---

## Requirements

- Python 3.x
- Libraries:
  - argparse (for command-line argument parsing)
  - glob (for file pattern matching)
  - os (for file system operations)
  - PIL (Python Imaging Library)
  - vtf2img (for reading .vtf files)

---

## Usage

1. Command-Line Arguments

- path: The paths to image files or directories containing images.
  - You can pass multiple file paths or directories. Wildcards (e.g., *.vtf, *.png) are also supported.

---

### Example:

```bash
python vtf2bmp.py "textures/*.vtf" "images/*.png"
```

This command will process all .vtf files in the textures folder and all .png files in the images folder.

---

## Example Output

- Input: textures/my_image.vtf
- Output: Textures/my_image.bmp

---

## Notes

- The output directory (Textures) is created if it doesn't exist.