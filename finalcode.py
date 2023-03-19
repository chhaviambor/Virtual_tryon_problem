import numpy as np
import cv2
while True:  
    print("\nVIRTUAL TRY ON!")  
    print("Experience and imagine yourself in your favourite clothes")
    print(" ")
    print("1. MALE")   
    print("2. FEMALE")
    print("3. KID")  
    print(" ")

    choice1 = int(input("Enter the Choice:"))  
    

    if choice1 == 1:   

        print("1. Blue Print")  
        print("2. Grey Print")  
        print("3. Brown Print")
        print("4. Exit")
        print(" ")
        choice2 = int(input("Enter the Choice:"))  
  
        if choice2 == 1:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\trial1.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\1.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey()  
              
        elif choice2 == 2:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\trial1.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\2.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey() 
              
        elif choice2 == 3:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\trial1.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\3.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey()  
  
        elif choice2 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 2:    
        print("1. Brown Print")  
        print("2. Purple Print")  
        print("3. Peach Print")  
        print("4. Exit")
        print(" ")  
        choice3 = int(input("Enter the Choice:"))  
  
        if choice3 == 1:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\girl.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\WOMEN1.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey()   
              
        elif choice3 == 2:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\girl.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\WOMEN2.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey() 
              
        elif choice3 == 3:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\girl.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\WOMEN3.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey()
  
        elif choice3 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 3:    
        print("1. Grey Print")  
        print("2. Yellow Print")  
        print("3. Green Print")  
        print("4. Exit")  
        print(" ")
        choice4 = int(input("Enter the Choice:"))  

        if choice4 == 1:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\kid.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\kid1.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey()

        if choice4 == 2:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\kid.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\kid2.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey()

        if choice4 == 3:  
            frame = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\kid.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            mask_white = cv2.inRange(hsv,lower_green, upper_green)
            mask_black = cv2.bitwise_not(mask_white)
            W,L = mask_black.shape
            mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_black_3CH[:, :, 0] = mask_black
            mask_black_3CH[:, :, 1] = mask_black
            mask_black_3CH[:, :, 2] = mask_black
            dst3 = cv2.bitwise_and(mask_black_3CH,frame)
            W,L = mask_white.shape
            mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
            mask_white_3CH[:, :, 0] = mask_white
            mask_white_3CH[:, :, 1] = mask_white
            mask_white_3CH[:, :, 2] = mask_white
            dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
            design = cv2.imread('C:\\Users\\hp\\Desktop\\requirements\\kid3.png')
            design = cv2.resize(design, mask_black.shape[1::-1])
            design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
            final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
            cv2.imshow('final_out',final_mask_black_3CH)
            cv2.waitKey()

        elif choice4 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  