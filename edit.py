import os
from PIL import Image

# مسیر فولدر تصاویر
image_folder = 'carpets\\dataset\\final'  # تغییر دهید به مسیر فولدر خود

for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)

    try:
        # باز کردن تصویر
        img = Image.open(image_path)
        
        # بررسی نسبت عرض به ارتفاع
        if img.width >= 3 * img.height:
            img.close()  # بستن تصویر به صورت دستی
            os.remove(image_path)
            print(f"✅ حذف شد: {filename}")
        else:
            img.close()  # بستن تصویر به صورت دستی

    except Exception as e:
        print(f'❌ خطا در پردازش {filename}: {e}')

print("✅ فرایند به پایان رسید.")
