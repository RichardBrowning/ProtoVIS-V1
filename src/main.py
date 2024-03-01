from camera.Camera import Camera
import time

def main():
    #print('hello world')
    camera = Camera()
    camera._start_preview()
    camera.capture_image_previewing()
    time.sleep(30)

if __name__ == "__main__":
    main()
