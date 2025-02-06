
# Image Compressor 

## Overview

This is a simple Python script that compresses JPEG images while maintaining an optimal balance between quality and file size. It automatically scans the current directory for JPG files and allows the user to select an image to compress. The script reduces the file size by adjusting the JPEG quality while ensuring the image remains within a specified maximum file size.

## Features

- Compresses JPEG images to a target maximum size (default: **0.5MB**).
- Reduces image quality iteratively while optimizing the output.
- Works with JPG files in the current directory.
- Allows user selection if multiple images are present.
- Converts images with **RGBA** or **P** mode to **RGB** to ensure compatibility.

## Requirements

- **Python 3.x**
- **Pillow (PIL) library**

## Installation

Ensure you have Python installed. You also need the Pillow library, which can be installed via pip:

```bash
pip install pillow
```

## Usage

1. Place your JPG images in the same directory as the script.
2. Run the script:

   ```bash
   python image_compressor.py
   ```

3. If multiple JPG images exist, select the one you want to compress by entering its corresponding number.
4. The compressed image will be saved in the same directory with **"_compressed"** appended to its filename.

## Example

```
Available JPG files:
1. image1.jpg
2. image2.jpg

Enter the number of the file you want to compress: 1

Compressing: image1.jpg
Original size: 2.50MB
Compressed size: 0.48MB
Final quality setting: 65
Compressed image saved to: image1_compressed.jpg
```

## Customization

You can modify the following parameters in the script:

- `max_size_mb`: Adjust the maximum output file size (default: **0.5MB**).
- `quality`: Initial quality setting for compression (**default: 85**, reduces dynamically if needed).

Example modification to set a different max file size:

```python
compress_image("image1.jpg", max_size_mb=1.0)  # Compress to max 1MB
```

## Limitations

- The script only supports **JPG** images.
- Reducing quality too much may lead to noticeable image degradation.
- Doesn't support batch processing (**only compresses one image at a time**).

## License

This project is open-source and available for modification and distribution.

**Authors:** Harsh Sarvaiya, chatGPT (for this readme)
**GitHub:** [YourGitHubProfile](https://github.com/harsh-sarvaiya)
