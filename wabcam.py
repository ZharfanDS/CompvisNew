import cv2
from time import sleep
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
while True:

    try:
        check, frame = webcam.read()

        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            print("Processing image...")
            img = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img = cv2.resize(gray,(28,28))
            print("Resized...")
            imgresized = cv2.imwrite(filename='saved_img-final.jpg', img=img)
            print("Image saved!")
            
            break
        
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
    
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break