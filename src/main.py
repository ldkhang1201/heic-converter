import argparse
import sys
from pathlib import Path
from converter import convert_heic

def process_file(input_file: Path, output_dir: Path, target_format: str):
    """Processes a single HEIC file and saves it."""
    # Construct output file path
    output_filename = input_file.with_suffix(f'.{target_format.lower()}').name
    output_path = output_dir / output_filename
    
    print(f"Converting '{input_file.name}' to '{output_filename}'...")
    success = convert_heic(str(input_file), str(output_path), target_format)
    if success:
        print(f"Successfully saved to '{output_path}'")
    else:
        print(f"Failed to convert '{input_file.name}'")

def main():
    parser = argparse.ArgumentParser(description="Convert HEIC images to other formats (e.g., JPEG, PNG).")
    parser.add_argument("input", help="Path to a HEIC file or a directory containing HEIC files.")
    parser.add_argument("-o", "--output", help="Directory to save the converted images. Defaults to the same directory as the input.", default=None)
    parser.add_argument("-f", "--format", help="Target output format (e.g., JPEG, PNG). Defaults to JPEG.", default="JPEG", choices=["JPEG", "PNG", "WEBP", "BMP", "TIFF", "GIF"])
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    target_format = args.format.upper()
    
    if not input_path.exists():
        print(f"Error: Input path '{input_path}' does not exist.")
        sys.exit(1)
        
    # Determine default output directory
    if args.output:
        output_dir = Path(args.output)
    else:
        output_dir = input_path.parent if input_path.is_file() else input_path
        
    if not output_dir.exists():
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating output directory '{output_dir}': {e}")
            sys.exit(1)

    # Process input path
    if input_path.is_file():
        if input_path.suffix.lower() == '.heic':
            process_file(input_path, output_dir, target_format)
        else:
            print(f"Error: Input file '{input_path}' does not appear to be a .heic file.")
            sys.exit(1)
    elif input_path.is_dir():
        # Find all .heic and .HEIC files
        heic_files = list(input_path.glob("*.heic")) + list(input_path.glob("*.HEIC"))
        if not heic_files:
            print(f"No HEIC files found in directory '{input_path}'.")
            sys.exit(0)
            
        print(f"Found {len(heic_files)} HEIC files in '{input_path}'.")
        for file in heic_files:
            process_file(file, output_dir, target_format)
    else:
        print(f"Error: Input path '{input_path}' is neither a file nor a directory.")
        sys.exit(1)

if __name__ == "__main__":
    main()
