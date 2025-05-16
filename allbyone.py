import os
import random
import shutil
# from rembg import remove
from PIL import Image

# مسیر فولدر تصاویر
image_folder = 'carpets\dataset\Carpet'  # تغییر دهید به مسیر فولدر خود
output_folder = 'carpets\dataset\\final'  # ذخیره تصاویر نهایی
os.makedirs(output_folder, exist_ok=True)

# پردازش تصاویر
for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)

    try:
        # باز کردن تصویر و حذف بک‌گراند
        with Image.open(image_path) as img:
            # img = remove(img)

            # چرخش افقی در صورت نیاز
            if img.height > img.width:
                img = img.rotate(90, expand=True)

            # تغییر اندازه با حفظ نسبت و عرض 512 پیکسل
            width = 512
            aspect_ratio = img.height / img.width
            new_height = int(width * aspect_ratio)
            img = img.resize((width, new_height))

            # تبدیل تصویر به حالت RGB
            img = img.convert('RGB')

            # ذخیره به صورت JPG
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            img.save(os.path.join(output_folder, jpg_filename), 'JPEG', quality=95)
            print(f'✅ پردازش شد: {filename} -> {jpg_filename}')

    except Exception as e:
        print(f'❌ خطا در پردازش {filename}: {e}')

print("✅ فرایند به پایان رسید.")
