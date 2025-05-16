from PIL import Image
import os

# مسیر فولدر تصاویر شما
input_folder = 'pytorch-CycleGAN-and-pix2pix-master\datasets\carpet2map\\trainB'
output_folder = 'pytorch-CycleGAN-and-pix2pix-master\datasets\carpet2map\\trainBB'
os.makedirs(output_folder, exist_ok=True)

# تغییر اندازه همه تصاویر به 256x256
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize((256, 256))
        img_resized.save(os.path.join(output_folder, filename))

print("✅ تغییر اندازه تصاویر به پایان رسید.")
