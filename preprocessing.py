import cv2 
  
# Function to extract frames 
def FrameCapture(path,name): 
  
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite(f"{name}_frame{count}.jpg", image) 
        f = open(f"{name}_frame.txt","w")
        f.write()
        count += 1
  
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture("") 