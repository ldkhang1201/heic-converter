# HEIC Converter

A simple and efficient command-line tool to convert HEIC (High Efficiency Image Coding) images to more widely compatible formats like JPEG, PNG, WEBP, and more.

## Features

- **Batch Conversion:** Convert all HEIC files in a directory at once.
- **Multiple Formats:** Support for JPEG, PNG, WEBP, BMP, TIFF, and GIF.
- **Custom Output:** Specify a target directory for your converted images.
- **Smart Handling:** Automatically handles transparency when converting to formats like JPEG.

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management, but you can also use standard `pip`.

### Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/ldkhang1201/heic-converter.git
cd heic-converter

# Install dependencies and run
uv sync
uv run src/main.py --help
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/ldkhang1201/heic-converter.git
cd heic-converter

# Install dependencies
pip install pillow pillow-heif

# Run the script
python src/main.py --help
```

## Usage

### Basic Conversion

Convert a single file to JPEG (default):
```bash
python src/main.py path/to/image.heic
```

Convert all HEIC files in a directory:
```bash
python src/main.py path/to/folder
```

### Advanced Options

**Specify Output Format:**
```bash
python src/main.py image.heic -f PNG
```

**Specify Output Directory:**
```bash
python src/main.py path/to/images -o ./converted_output -f WEBP
```

### Full Options

```text
usage: main.py [-h] [-o OUTPUT] [-f {JPEG,PNG,WEBP,BMP,TIFF,GIF}] input

Convert HEIC images to other formats (e.g., JPEG, PNG).

positional arguments:
  input                 Path to a HEIC file or a directory containing HEIC files.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Directory to save the converted images. Defaults to the same directory as the input.
  -f {JPEG,PNG,WEBP,BMP,TIFF,GIF}, --format {JPEG,PNG,WEBP,BMP,TIFF,GIF}
                        Target output format (e.g., JPEG, PNG). Defaults to JPEG.
```

## Requirements

- Python >= 3.10
- Pillow
- pillow-heif

## License

MIT (or your preferred license)
