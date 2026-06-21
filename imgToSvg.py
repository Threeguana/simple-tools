import cv2
import base64
import os
import glob

def convert_to_svg(input_path, output_path):
    img = cv2.imread(input_path)
    if img is None:
        return False

    height, width = img.shape[:2]
    ext = os.path.splitext(input_path)[1].lower()
    mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"

    try:
        with open(input_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" ')
            f.write(f'width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n')
            f.write(f'  <image width="{width}" height="{height}" href="data:{mime_type};base64,{encoded_string}" />\n')
            f.write('</svg>\n')
        return True
    except Exception:
        return False

def get_all_images():
    extensions = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']
    images = []
    for ext in extensions:
        images.extend(glob.glob(ext))
    return list(set(images))

if __name__ == "__main__":
    images = get_all_images()

    if not images:
        print("No images found in the current dictory")
        exit()

    print(f"Found {len(images)} image(s) ready for conversion.")
    choice = input("Convert to SVG and delete the original files? (y/n): ").strip().lower()

    if choice == 'y':
        success_count = 0
        for img_file in images:
            base_name, _ = os.path.splitext(img_file)
            out_file = base_name + ".svg"

            if convert_to_svg(img_file, out_file):
                try:
                    os.remove(img_file)
                    success_count += 1
                except Exception as e:
                    print(f"Warning: Could not delete {img_file} - {e}")
            else:
                print(f"Warning: Failed to convert {img_file}")

        print(f"Done! Successfully converted and removed {success_count} image(s).")
    else:
        print("Operation cancelled.")
