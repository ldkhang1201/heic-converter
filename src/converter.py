import os
from pathlib import Path
from PIL import Image
import pillow_heif

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

def convert_heic(input_path: str, output_path: str, target_format: str = "JPEG") -> bool:
    """
    Converts a HEIC image to the target format.
    
    Args:
        input_path: Path to the input .heic file.
        output_path: Path to save the converted file.
        target_format: The format to save as (e.g., 'JPEG', 'PNG').
        
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        input_file = Path(input_path)
        if not input_file.exists():
            print(f"Error: Input file '{input_path}' does not exist.")
            return False
            
        # Ensure output directory exists
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        
        # Open the HEIC image
        img = Image.open(input_path)
        
        # If saving as JPEG, convert RGBA to RGB to avoid errors
        if target_format.upper() in ["JPEG", "JPG"] and img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        img.save(output_path, format=target_format)
        return True
    except Exception as e:
        print(f"Error converting '{input_path}': {e}")
        return False
