from PIL import Image
import os

def compress_image(input_path, output_path=None, max_size_mb=1.0, quality=85):
    """
    Compress an image file to a target maximum file size.
    """
    # Verify input file exists
    if not os.path.exists(input_path):
        print(f"Error: Could not find input file at: {input_path}")
        return
    
    # If no output path specified, create one
    if output_path is None:
        file_name, file_ext = os.path.splitext(input_path)
        output_path = f"{file_name}_compressed{file_ext}"
    
    # Open the image
    img = Image.open(input_path)
    
    # Convert to RGB if necessary
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # Initial save
    img.save(output_path, 'JPEG', quality=quality, optimize=True)
    
    # Check file size and reduce quality until it's under max_size_mb
    while os.path.getsize(output_path) > (max_size_mb * 1024 * 1024) and quality > 5:
        quality -= 5
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
    
    # Print results
    original_size = os.path.getsize(input_path) / (1024 * 1024)
    compressed_size = os.path.getsize(output_path) / (1024 * 1024)
    
    print(f"Original size: {original_size:.2f}MB")
    print(f"Compressed size: {compressed_size:.2f}MB")
    print(f"Final quality setting: {quality}")
    print(f"Compressed image saved to: {output_path}")

if __name__ == "__main__":
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List all jpg files in the current directory
    jpg_files = [f for f in os.listdir(current_dir) if f.endswith('.jpg')]
    
    if not jpg_files:
        print("No JPG files found in the current directory.")
        print(f"Please place your JPG file in: {current_dir}")
    else:
        print("Available JPG files:")
        for i, file in enumerate(jpg_files, 1):
            print(f"{i}. {file}")
        
        if len(jpg_files) == 1:
            input_image = os.path.join(current_dir, jpg_files[0])
            print(f"\nCompressing: {jpg_files[0]}")
            compress_image(input_image, max_size_mb=0.5)
        else:
            try:
                choice = int(input("\nEnter the number of the file you want to compress: "))
                if 1 <= choice <= len(jpg_files):
                    input_image = os.path.join(current_dir, jpg_files[choice-1])
                    print(f"\nCompressing: {jpg_files[choice-1]}")
                    compress_image(input_image, max_size_mb=0.5)
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a valid number!")
