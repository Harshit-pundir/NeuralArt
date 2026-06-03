import gradio as gr
import torch
from PIL import Image
from torchvision import transforms
from huggingface_hub import hf_hub_download

from models import VGGEncoder, Decoder
from utils import adaptive_instance_normalization

device = torch.device("cpu")

vgg_path = hf_hub_download(
    repo_id="harshitpundir/neuralart-models",
    filename="vgg_normalised.pth"
)

decoder_path = hf_hub_download(
    repo_id="harshitpundir/neuralart-models",
    filename="decoder_final.pth"
)

encoder = VGGEncoder(vgg_path).to(device)
decoder = Decoder().to(device)

decoder.load_state_dict(
    torch.load(decoder_path, map_location=device)
)

encoder.eval()
decoder.eval()

def tensor_to_pil(tensor):
    tensor = tensor.squeeze(0).cpu().clamp(0, 1)
    return transforms.ToPILImage()(tensor)

def style_transfer(content_img, style_img, alpha):
    content_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor()
    ])

    style_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor()
    ])

    content = content_transform(content_img).unsqueeze(0).to(device)
    style = style_transform(style_img).unsqueeze(0).to(device)

    with torch.no_grad():
        content_feat = encoder(content, is_test=True)
        style_feat = encoder(style, is_test=True)

        feat = adaptive_instance_normalization(
            content_feat,
            style_feat
        )

        feat = alpha * feat + (1 - alpha) * content_feat

        output = decoder(feat)

    return tensor_to_pil(output)

demo = gr.Interface(
    fn=style_transfer,
    inputs=[
        gr.Image(type="pil", label="Content Image"),
        gr.Image(type="pil", label="Style Image"),
        gr.Slider(0, 1, value=1.0, step=0.1, label="Alpha")
    ],
    outputs=gr.Image(type="pil", label="Stylized Output"),
    title="🎨 NeuralArt",
    description="Neural Style Transfer using AdaIN"
)

demo.launch()