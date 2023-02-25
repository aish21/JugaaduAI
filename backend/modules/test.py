import torch
import clip
import gpt_2_simple as gpt2
import numpy as np
from PIL import Image
from torchvision.utils import make_grid
from torchvision.transforms import functional as F
import dnnlib
import legacy

# set device to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# load GPT-2 model
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

# load StyleGAN2 generator model
url = 'https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/ffhq.pkl'
with dnnlib.util.open_url(url) as f:
    G = legacy.load_network_pkl(f)['G_ema'].to(device)

# define function to generate image from text
def generate_image(text, image_size=256):
    # generate text embedding using CLIP
    text_embedding = clip.tokenize(text).to(device)
    
    # generate text description using GPT-2
    gen_text = gpt2.generate(sess, prefix=text, return_as_list=True)[0]
    
    # generate image from text embedding using StyleGAN2
    latent = np.random.randn(1, G.z_dim)
    style = G.mapping(torch.from_numpy(latent).to(device), None)
    image = G.synthesis(style, noise_mode='const', force_fp32=True, **G.synthesis_kwargs)
    image = (image + 1) / 2.0
    
    # resize image to desired size
    image = F.resize(image, (image_size, image_size))
    
    # convert image to PIL format
    image = Image.fromarray(np.uint8(image[0].cpu().numpy() * 255))
    
    return image, gen_text

text = 'a beautiful landscape with mountains and trees'
image, gen_text = generate_image(text)
image.show()
print(gen_text)
