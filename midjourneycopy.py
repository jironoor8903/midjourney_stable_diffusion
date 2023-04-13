REPLICATE_API_TOKEN = ""

import replicate

client = replicate.Client(api_token="")

# client.run(
#         "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
#         input={"prompt": "a 19th century portrait of a wombat gentleman"}
#     )

output = client.run(
    "tstramer/midjourney-diffusion:436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b",
    input={"prompt": "Sofa in a living room"}
)
print("Here" , output)