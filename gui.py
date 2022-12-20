import PySimpleGUI as sg
from techniques import *
import os
import cv2

layout = [[sg.Text("Select an image to view it.")],
          [sg.FileBrowse(enable_events=True)], [sg.Image(key="image")],
          [sg.OK(), sg.Cancel()]]

image_selection_window = sg.Window("Select Image", layout, margins=(10, 10))

# for storing temporary files
if not '.tmp' in os.listdir():
    os.mkdir('.tmp')

while True:
    event, values = image_selection_window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Cancel"):
        image_selection_window.close()
        exit()

    if event == "Browse":
        image_path = values["Browse"]

        # check if the path is for an image
        if not image_path.endswith((".png", ".jpg", ".jpeg")):
            sg.popup("Please select an image file.")
            continue
    
        # convert to PNG
        img = cv2.imread(image_path)

        if img.shape[0] > 500 or img.shape[1] > 500:
            if img.shape[0] > img.shape[1]:
                x = int((500/img.shape[0]) * img.shape[1])
                img = cv2.resize(img, (x, 500))
            else:   
                x = int((500/img.shape[1]) * img.shape[0])
                img = cv2.resize(img, (500, x))

        # w, h
        # 500, x

        cv2.imwrite(".tmp/og.png", img)

        image_path = ".tmp/og.png"

        image_selection_window["image"].update(image_path)

    if event == "OK":
        print(image_path)
        image_selection_window.close()
        break


og_image_path = image_path
tools_layout = [[
    sg.Column([
        [
            sg.Text("Value for the the selected technique"),
            sg.Input(key="value", default_text="0", size=10)
        ],
        [sg.Button("Grayscale"),sg.Button("Blur"), sg.Button("Thresholding"),sg.Button("Edge Detection")],
        [sg.Button("Brightness Enhancement"), sg.Button("Cropping"), sg.Button("Sketch")],
        [sg.Button("Rotation"), sg.Button("Translation"), sg.Button("Scale")],
        [sg.Button("Reset"), sg.Button("save")],
    ],scrollable=True, expand_y=True),
    sg.Column([[sg.Image(image_path, key="image")]]),
]]

tools = sg.Window("tools", tools_layout, margins=(10, 10))

# tools window
while True:
    event, values = tools.read()
    print(event, values)

    if event == "Grayscale":
        print("grayscale")
        img = cv2.imread(image_path)
        img = gray_scale(img)
        cv2.imwrite(".tmp/grayscale.png", img)
        image_path = ".tmp/grayscale.png"
        tools["image"].update(image_path)

    if event == "Blur":
        print("blur")
        val = values["value"]
        if not val.isdigit():
            sg.popup("Please enter a valid number.")
            continue
        val = int(val)

        img = cv2.imread(image_path)
        try:
            img = median_blur(img, val)
        except Exception as e:
            print(e)
            sg.popup("please enter a positive odd number.")
            continue

        

        cv2.imwrite(".tmp/blur.png", img)
        image_path = ".tmp/blur.png"

        tools["image"].update(image_path)

    if event == "Thresholding":
        print("thresholding")
        val = values["value"]
        if not val.isdigit():
            sg.popup("Please enter a valid number.")
            continue
        val = int(val)

        img = cv2.imread(image_path)
        try:
            img = thresholding(img, val)
        except Exception as e:
            print(e)
            sg.popup("please enter a valid number.")
            continue

        cv2.imwrite(".tmp/thresholding.png", img)
        image_path = ".tmp/thresholding.png"
        tools["image"].update(image_path)

    if event == "Edge Detection":
        print("edge detection")
        val = values["value"]
        if not val.isdigit():
            sg.popup("Please enter a valid number.")
            continue
        val = int(val)

        img = cv2.imread(image_path)
        try:
            img = sobel_edge_detection(img, val)
        except Exception as e:
            print(e)
            sg.popup("please enter a valid number.")
            continue

        cv2.imwrite(".tmp/edge_detection.png", img)
        image_path = ".tmp/edge_detection.png"
        tools["image"].update(image_path)

    if event == "Brightness Enhancement":
        print("brightness")

        val = values["value"]
        if not val.isdigit():
            sg.popup("Please enter a valid number.")
            continue
        val = int(val)

        img = cv2.imread(image_path)
        img = brightness_enhancement(img, val)

        cv2.imwrite(".tmp/brightness.png", img)
        image_path = ".tmp/brightness.png"
        tools["image"].update(image_path)

    if event == "Cropping":
        print("cropping")
        val = values["value"]
        val = val.split(",")
        if len(val) != 4:
            sg.popup("Please enter a valid number.")
            continue

        try:
            val = [int(i) for i in val]
        except Exception as e:
            print(e)
            sg.popup("Please enter a valid number.")
            continue

        img = cv2.imread(image_path)
        try:
            img = image_cropping(img, *val)
        except Exception as e:
            print(e)
            sg.popup("please enter a valid number.")
            continue

        cv2.imwrite(".tmp/cropping.png", img)
        image_path = ".tmp/cropping.png"
        tools["image"].update(image_path)

        
    if event == "Sketch":
        print("Sketch")

        val = values["value"]
        if not val.isdigit():
            sg.popup("Please enter a valid number.")
            continue

        val = int(val)

        img = cv2.imread(image_path)

        try:
            img = image_to_sketch(img, val)
        except Exception as e:
            print(e)
            sg.popup("please enter a valid number.")
            continue

        cv2.imwrite(".tmp/sketch.png", img)
        image_path = ".tmp/sketch.png"
        tools["image"].update(image_path)

    if event == "Rotation":
        print("rotation")
        val = values["value"]
        if not val.isdigit():
            sg.popup("Please enter a valid number.")
            continue
        val = int(val)

        img = cv2.imread(image_path)
        try:
            img = image_rotation(img, val)
        except Exception as e:
            print(e)
            sg.popup("please enter a valid number.")
            continue

        cv2.imwrite(".tmp/rotation.png", img)
        image_path = ".tmp/rotation.png"
        tools["image"].update(image_path)

    if event == "Scale":
        print("Scale")
        val = values["value"]
        val = val.split(",")
        if len(val) != 2:
            sg.popup("Please enter a valid number.")
            continue


        try:
            val = [float(i) for i in val]
            for i in val:
                if i > 5:
                    sg.popup("Max scale is 5.")
                    continue

                if i < 0:
                    sg.popup("Min scale is 0.")
                    continue
        except Exception as e:
            print(e)
            sg.popup("Please enter a valid number.")
            continue

        img = cv2.imread(image_path)
        try:
            img = image_scaling(img, *val)
        except Exception as e:
            print(e)
            sg.popup("please enter a valid number.")
            continue
        
        cv2.imwrite(".tmp/resize.png", img)
        image_path = ".tmp/resize.png"
        tools["image"].update(image_path)

    if event == "Translation":
        print("translation")
        val = values["value"]
        val = val.split(",")
        if len(val) != 2:
            sg.popup("Please enter a valid number.")
            continue

        try:
            val = [int(i) for i in val]
        except Exception as e:
            print(e)
            sg.popup("Please enter a valid number.")
            continue

        img = cv2.imread(image_path)
        try:
            img = translation(img, *val)
        except Exception as e:
            print(e)
            sg.popup("please enter a valid number.")
            continue

        cv2.imwrite(".tmp/translation.png", img)
        image_path = ".tmp/translation.png"
        tools["image"].update(image_path)


    if event == "Reset":
        image_path = og_image_path
        tools["image"].update(image_path)

    if event == "save":
        # ask for path
        path = sg.popup_get_file("Save image",
                                 save_as=True,
                                 file_types=(("PNG", "*.png"), ("JPEG",
                                                                "*.jpg")))
        if path:
            try:
                cv2.imwrite(path, cv2.imread(image_path))
            except Exception as e:
                print(e)
                sg.popup("Image not saved.")
                continue
            # send notification
            sg.popup("Image saved successfully.")
        else:
            sg.popup("Image not saved.")

    if event in (sg.WIN_CLOSED, ):
        tools.close()
        exit()

if '.tmp' in os.listdir():
    os.rmdir('.tmp')