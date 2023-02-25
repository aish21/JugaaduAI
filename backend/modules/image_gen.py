import clip
from clip_guided_diffusion import GuidedDiffusion

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Load Guided Diffusion model
gd = GuidedDiffusion()

# Text prompt to generate image from
text_prompt = "a red apple floating in midair"

# Generate image from text prompt
image = gd.generate_with_clip(model, preprocess, text_prompt)

# Show image
image.show()
