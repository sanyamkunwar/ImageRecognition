# Take input from user for the image file -> ask if user wants a line/rect/circle/text on the image and accordingly ask for those required parameters-> show the output and ask if user wants to save the image, if yes ask for location
import cv2 as cv

def user_interaction():
    try:

        print('Hey user!!!\n')
        image_path = input("Enter the full image path: ")
        image = cv.imread(image_path)
        if image is None:
            print("Error: Could not load image. Please check the path and try again.")
            return
        print("Image loaded")

        # DISPLAY THE IMAGE
        img_title = input("Give a title for your image to display: ")
        print("showing image...")
        cv.imshow(img_title, image)
        cv.waitKey(0)
        cv.destroyAllWindows()

        # Ask user for the operation they want to perform
        operation = input("What operation do you want to perform on the image? (line/rectangle/circle/text): ").lower()
        if operation == 'line':
            # Ask for line parameters
            x1 = int(input("Enter x1 coordinate: "))
            y1 = int(input("Enter y1 coordinate: "))
            x2 = int(input("Enter x2 coordinate: "))
            y2 = int(input("Enter y2 coordinate: "))
            color = tuple(map(int, input("Enter color (B,G,R) separated by commas: ").split(',')))
            thickness = int(input("Enter thickness of the line: "))
            cv.line(image, (x1, y1), (x2, y2), color, thickness)
        elif operation == 'rectangle':
            # Ask for rectangle parameters
            x1 = int(input("Enter top-left x coordinate: "))
            y1 = int(input("Enter top-left y coordinate: "))
            x2 = int(input("Enter bottom-right x coordinate: "))
            y2 = int(input("Enter bottom-right y coordinate: "))
            color = tuple(map(int, input("Enter color (B,G,R) separated by commas: ").split(',')))
            thickness = int(input("Enter thickness of the rectangle: "))
            cv.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        elif operation == 'circle':
            # Ask for circle parameters
            x = int(input("Enter center x coordinate: "))
            y = int(input("Enter center y coordinate: "))
            radius = int(input("Enter radius of the circle: "))
            color = tuple(map(int, input("Enter color (B,G,R) separated by commas: ").split(',')))
            thickness = int(input("Enter thickness of the circle (-1 for filled): "))
            cv.circle(image, (x, y), radius, color, thickness)
        elif operation == 'text':
            # Ask for text parameters
            text = input("Enter the text to put on the image: ")
            x = int(input("Enter x coordinate for the text: "))
            y = int(input("Enter y coordinate for the text: "))
            font_scale = float(input("Enter font scale: "))
            color = tuple(map(int, input("Enter color (B,G,R) separated by commas: ").split(',')))
            thickness = int(input("Enter thickness of the text: "))
            cv.putText(image, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
        else:
            print("Invalid operation. Please choose from line, rectangle, circle, or text.")
            return
        # Show the modified image
        cv.imshow("Modified Image", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

        # Ask if user wants to save the image
        save = input("Do you want to save the modified image? (y/n): ").lower()
        if save == 'y':
            save_path = input("Enter the full path to save the image (including filename and extension): ")
            cv.imwrite(save_path, image)
            print(f"Image saved successfully at {save_path}")
        else:
            print("Image not saved.")

        
    except Exception as error:
        print(f"Error occured: {error}")

        
user_interaction()