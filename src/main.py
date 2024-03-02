from camera.Camera import Camera
import time

def main():
    #print('hello world')
    camera = Camera()
    camera.start_preview()
    camera.capture_image_previewing()
    time.sleep(3)
    camera.add_overlay_text(0, "inspiron") 
    camera.record_video(10)
    time.sleep(30)

if __name__ == "__main__":
    main()
