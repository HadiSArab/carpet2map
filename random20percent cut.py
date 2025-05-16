import os
import random
import shutil

# مسیر فولدر تصاویر
source_folder = 'carpets\dataset\\final'  # تغییر دهید به مسیر فولدر خود

# ساخت یک فولدر برای ذخیره تصاویر منتقل شده
destination_folder = 'pic2pat_dataset\\testA'
os.makedirs(destination_folder, exist_ok=True)

# دریافت لیست تمام تصاویر
all_images = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# محاسبه 20 درصد تصاویر به صورت رندوم
num_to_move = int(0.2 * len(all_images))
images_to_move = random.sample(all_images, num_to_move)

# انتقال تصاویر انتخاب شده
for image in images_to_move:
    src_path = os.path.join(source_folder, image)
    dest_path = os.path.join(destination_folder, image)
    shutil.move(src_path, dest_path)

print(f'✅ تعداد {num_to_move} تصویر به صورت رندوم منتقل شد.')
