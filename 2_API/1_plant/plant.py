import os
import argparse
import requests
import dotenv
import cv2


class Plant():
    def __init__(self, arg):
        self.name = str(arg.plant_name)

    def illusion_diffusion(self , key_ill_diff):
        payload = {
        "prompt": f"make a picture from {self.name} , as reallistic and natural as possible",
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/funky.jpeg",
        "scheduler": "Euler","image_size": "square_hd","guidance_scale": 7.5,
        "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t",
        "num_inference_steps": 40,"control_guidance_end": 1,"controlnet_conditioning_scale": 1
        }
        
        header = {"Authorization": key_ill_diff ,
                  "Content-Type": "application/json"}

        response = requests.post("https://54285744-illusion-diffusion.gateway.alpha.fal.ai/", headers=header , json=payload)
        print(response.status_code)
        res = response.text
        print(response.text)
        image_url = res["image"]["url"]
        image = requests.get(image_url).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(image)
        image = cv2.imread("image_name.jpg")
        image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
        return image


    def plant_recognition(self , key_plant_rec , generated_image):
        headers={}
        url = "https://my-api.plantnet.org/v2/identify/all"
        payload = {
            "api-key" : key_plant_rec }

        files = {
            "images" : generated_image }

        response = requests.post(url, headers=headers , params = payload , files=files)
        print(response.status_code)
        result = response.json()
        result = result["results"][3]["species"]["commonNames"]
        return result


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--plant_name" , type=str , help="Enter a plant/flower 's name")
    arg = parser.parse_args()

    dotenv = dotenv.load_dotenv()
    key_ill_diff = os.getenv("illusion_token")
    key_plant_rec = os.getenv("plantnet_token")

    p = Plant(arg)
    generated_image = p.illusion_diffusion(key_ill_diff)
    plant_name = p.plant_recognition(generated_image , key_plant_rec , generated_image)
    print(f"\n The plant's name is : {plant_name} ")
