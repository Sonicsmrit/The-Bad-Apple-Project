import cv2 as cv
from tqdm import tqdm

#c:\Users\dell\Downloads\BadApple.mp4
VideoPath = input("Enter Video path: ") ##Repalce with your own video path
while True:
    try:
        vid = cv.VideoCapture(f"{VideoPath}") 
        break
    except:
        continue

if not vid.isOpened:
    print("Error opening video")

running = True
saved_id = 0
N = 20 #how many frames to skip before taking another frame from the video

totalframes = int(vid.get(cv.CAP_PROP_FRAME_COUNT))


for frame_id in tqdm(range(totalframes)):
    rel, frame = vid.read()

    if rel == False:
        break

    if frame_id % N == 0:
        cv.imwrite(f"frames/frame_{saved_id:03d}.jpg", frame)
        saved_id += 1
        

vid.release()
cv.destroyAllWindows()

