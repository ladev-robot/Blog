from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path

src = Path(r"C:\Users\Ao\.cursor\projects\c-Users-Ao-Desktop-home-study-blog-v2\assets\c__Users_Ao_AppData_Roaming_Cursor_User_workspaceStorage_71f3b6ed3727a5aa177fa7735e4ea6c4_images_profile-line-art-detailed-dbeab12b-6e08-4092-b4e0-2ee934589925.png")
out = Path(r"C:\Users\Ao\Desktop\home\study\blog_v2\ladev-robot.github.io\assets\img\avatar.png")
out_2x = Path(r"C:\Users\Ao\Desktop\home\study\blog_v2\ladev-robot.github.io\assets\img\avatar@2x.png")

im = Image.open(src).convert("RGB")
w, h = im.size
side = min(w, h)
left = (w - side) // 2
top = max(0, int((h - side) * 0.08))
top = min(top, h - side)
crop = im.crop((left, top, left + side, top + side))


def make(size):
    img = crop.resize((size, size), Image.Resampling.LANCZOS)
    img = img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=140, threshold=2))
    img = ImageEnhance.Contrast(img).enhance(1.08)
    img = ImageEnhance.Sharpness(img).enhance(1.15)
    return img


mid = make(440)
hi = make(640)

mid.save(out, format="PNG", optimize=True)
hi.save(out_2x, format="PNG", optimize=True)
print("saved", out, mid.size, out.stat().st_size)
print("saved", out_2x, hi.size, out_2x.stat().st_size)
