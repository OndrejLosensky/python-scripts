# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:39:14 2023

@author: ondra
"""

import os
import shutil
import time
from PIL import Image

def load_watermark(path_to_file):
    
    watermark_path = os.path.join(path_to_file, 'watermark.png') 
    
    if os.path.exists(watermark_path):
        watermark = Image.open(watermark_path)
        print("Watermark was loaded!")
        return watermark
    else: 
        print("Watermark wasn't found!")
        return None

def apply_watermark(path_to_image, watermark):
    try:
        image = Image.open(path_to_image)

        # Very simply scaling for landscape or portrait photos
        if (image.width < image.height):
            scaling_factor = image.width / 400.0

        elif (image.width > image.height):
            scaling_factor = image.width / 900.0

       

        new_width = int(watermark.width * scaling_factor)
        new_height = int(watermark.height * scaling_factor)

        watermark_resized = watermark.resize((new_width, new_height), Image.ANTIALIAS)

        position = (
            image.width - watermark_resized.width ,
            image.height - watermark_resized.height 
        )

        print("Original size of the picture:", image.size)
        print("Size of the watermark:", watermark_resized.size)
        print("Attaching the watermark...")

        image.paste(watermark_resized, position, watermark_resized)
        image.save(path_to_image)

        print("Watermark was successfully added")

    except Exception as e:
        print(f"Something went wrong: {e}")


def load_images_from_folder(input_folder):
    files = os.listdir(input_folder)

    images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.NEF',))]

   
    print("Number of images:", len(images))

    return images

def save_images_to_folder(input_folder,output_folder, images,watermark, move=False):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for image in images:
        input_image_path = os.path.join(input_folder, image)
        
        output_image_path = os.path.join(output_folder, image)
        
        if move:
            shutil.move(input_image_path, output_image_path)
            
        else:
            shutil.copy(input_image_path, output_image_path)
            
        if watermark:
            apply_watermark(output_image_path, watermark)
        
    print("Number of processed images: ",len(images))
    
    return 

def log_to_file(log_message, log_file):
    timestamp = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"{timestamp}   {log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")
    
    print("log was saved successfully!!")


def main():
    
    watermark_path = '/path/to/your/folder'
    input_folder = '/path/to/your/folder'
    output_folder = '/path/to/your/folder'

   
    print("Welcome in this script where you can attacht watermark to multiple images")
    # ----------------------------------------------------------
    start_time = time.time()
    print("Loading images...")
    images = load_images_from_folder(input_folder)
    time.sleep(2)
    
    print("Preparing the watermark...")
    watermark = load_watermark(watermark_path)
    if not watermark:
        return 
    
    print("I am saving data to output folder")
    print("-----------------------------------------------")
    save_images_to_folder(input_folder, output_folder, images, watermark, move=False)
    
    print("Done!")
    time_total = (time.time() - start_time) 
    time_taken = "{:.2f}".format(time_total)
    print("Time taken:", time_taken ,"s")

    log_file = "log.txt"
    log_message = f'Process took {time_taken}s | processed {len(images)} images'
    log_to_file(log_message, log_file)
    
    
    return 


if __name__ == "__main__":
    main()