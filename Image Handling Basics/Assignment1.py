import cv2

############################################## TRIAL 1 ####################################################
# image = cv2.imread('./images/python-ball.jpg')

# if image is not None:
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert the image to grayscale

#     #show image
#     cv2.imshow('Grayscale Image', gray_image) #open the grayscale image in a window
#     cv2.waitKey(0) #wait for a key press to close the window
#     cv2.destroyAllWindows() #close the window

#     cv2.imwrite('images/grayscale_image.jpg', gray_image) #save the grayscale image to a file
# else:
#     print("Error: Could not load image.")
###########################################################################################################

############################################## TRIAL 2 ####################################################
# path = input("Enter the path of the image: ")
# image = cv2.imread(path)

# if image is not None:
#     #ask if user wants to convert the image to grayscale
#     convert = input("Do you want to convert the image to grayscale? (y/n): ")
#     if convert.lower() == 'y':
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert the image to grayscale
#         print("Image converted to grayscale successfully.")
#     else:
#         gray_image = image #if user does not want to convert the image to grayscale, keep the original image
#         print("Image will not be converted to grayscale.")
#         #ask if user wants to display the grayscale image or save it to a file
#     display_or_save = input("Do you want to display the grayscale image or save it to a file? (d/s): ")
#     if display_or_save.lower() == 'd':
#         cv2.imshow('Grayscale Image', gray_image) #open the grayscale image in a window
#         cv2.waitKey(0) #wait for a key press to close the window
#         cv2.destroyAllWindows() #close the window
#     elif display_or_save.lower() == 's':
#         save_path = input("Enter the path to save the grayscale image: ")
#         cv2.imwrite(save_path, gray_image) #save the grayscale image to a file
#         print("Grayscale image saved successfully as '{}'.".format(save_path))
#     else:
#         print("Invalid input. Please enter 'd' to display or 's' to save the image.")
# else:
#     print("Error: Could not load image.")

# # main function to run the program
# if __name__ == "__main__":
#     #ask if user wants to run the program again
#     run_again = input("Do you want to run the program again? (y/n): ")
#     if run_again.lower() == 'y':
#         #run the program again
#         exec(open(__file__).read())
#     else:
#         print("Exiting the program.")
###########################################################################################################

############################################## TRIAL 3 ####################################################
def base_opr():
    try:
        # READ THE IMAGE
        image_path = input("Enter the full image path: ")
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Could not load image. Please check the path and try again.")
            return
        print("Image loaded")

        # DISPLAY THE IMAGE
        img_title = input("Give a title for your image to display: ")
        print("showing image...")
        cv2.imshow(img_title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # CONVERT THE IMAGE TO GRAYSCALE
        convert_to_grayscale(image)
        
        # SAVE THE IMAGE
        save_image(image, cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    
        print("Thanks for using :)")
    
    except Exception as error:
        print(f"Error occured: {error}")

def convert_to_grayscale(image):
    try:
        grayscale_confirm = input("Do you wish to convert this image into grayscale format?: ").lower()
        if grayscale_confirm == "yes" or grayscale_confirm == "y":
            print("Converting into grayscale format...")
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            print("Displaying image...")
            cv2.imshow("grayscaled_image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif grayscale_confirm == "no" or grayscale_confirm == "n":
            print("Okay no problem")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            convert_to_grayscale(image)

    except Exception as error:
        print(f"Error occured while converting to grayscale: {error}")

def save_image(image, gray_image):
    try:
        save_confirm = input("Willing to save the image?: ").lower()

        if save_confirm == "yes" or save_confirm == "y":
            format_ = input("What format btw (grayscale/colored): ").lower().strip()
            name = input("Name it also brah: ")
            if format_ == "grayscale" or format_ == "gray" or format_ == "g":
                cv2.imwrite(f"{name}.jpg", gray_image)
                print(f"Image saved as {name}.jpg")
            elif format_ == "colored" or format_ == "color" or format_ == "c":
                cv2.imwrite(f"{name}.jpg", image)
                print(f"Image saved as {name}.jpg")
            else:
                print("Invalid format specified. Please choose 'grayscale' or 'colored'.")
                #reun the function to ask for format again
                save_image(image, gray_image)
        else:
            print("No prob pal")


    except Exception as error:
        print(f"Error occured while saving image: {error}")

def main():
    base_opr()
    #ask if user wants to run the program again
    run_again = input("Do you want to run the program again? (y/n): ")
    if run_again.lower() == 'y':
        #run the program again
        main()
    else:
        print("Exiting the program.")


main()