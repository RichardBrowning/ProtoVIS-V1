from PVCore import PVCore
from exceptions.ExceptionsSet import TerminateException, ResetCoreException
from config import SLAVE_ADDR

def main():
    core = PVCore()
    while True:
        try:
            # trap function
            core.loop()
        except TerminateException:
            # terminate flag reached
            break
        except ResetCoreException:
            # reset flag reached
            continue
        except KeyboardInterrupt:
            core.i2c_controller.send_byte(5, SLAVE_ADDR)
    '''
    #print('hello world')
    camera = Camera()
    camera.start_preview()
    camera.capture_image_previewing()
    time.sleep(3)
    camera.add_overlay_text(0, "inspiron") 
    camera.record_video(10)
    time.sleep(30)
    '''
    exit(0)

if __name__ == "__main__":
    main()
