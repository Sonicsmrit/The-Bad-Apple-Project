from PIL import Image as img


frame_count = 0

pixels_frame = []

pixels_user = []

#users image data
with img.open("Test/makima.jpg") as user_img:
    width, height = user_img.size
    gray_user_img = user_img.convert("L")
    for x in range(width):
        for y in range(height):
            pixels_user.append(
                {
                    "coords":((x,y)),
                    "color": user_img.getpixel((x,y)),
                    "lumin": gray_user_img.getpixel((x,y))
                }
            )

pixels_user.sort(key=lambda a:a["lumin"])



def load(frame_count, width, height):
    #frame(Bad Apple) image data
    pixels_frame.clear()
    frame_image = img.open(f"frames/frame_{frame_count:03d}.jpg")

    frame_image = frame_image.resize((width,height))

    gray_frame_img = frame_image.convert("L")

    for x in range(width):
        for y in range(height):
            pixels_frame.append({
                "coords": ((x,y)),
                "lumin": gray_frame_img.getpixel((x,y)),
                "color": frame_image.getpixel((x,y))
            })

    pixels_frame.sort(key=lambda a:a["lumin"])
    return pixels_frame