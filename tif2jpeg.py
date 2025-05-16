import os
from PIL import Image

# مسیر فولدر تصاویر
image_folder = 'carpets\dataset\Pattern'  # تغییر دهید به مسیر فولدر خود

# ساخت یک فولدر برای ذخیره تصاویر JPEG
output_folder = 'carpets\dataset\pat'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(image_folder):
    if filename.lower().endswith('.tif'):
        image_path = os.path.join(image_folder, filename)

        try:
            # باز کردن تصویر TIFF
            with Image.open(image_path) as img:
                # تعیین مسیر ذخیره تصویر با فرمت JPEG
                jpeg_filename = os.path.splitext(filename)[0] + '.jpeg'
                jpeg_path = os.path.join(output_folder, jpeg_filename)

                # ذخیره تصویر با فرمت JPEG
                img.convert('RGB').save(jpeg_path, 'JPEG', quality=95)
                print(f'تبدیل شد: {filename} -> {jpeg_filename}')

        except Exception as e:
            print(f'خطا در پردازش {filename}: {e}')

print("فرایند تبدیل به پایان رسید.")
