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

custom_css = """
.gradio-container {
    max-width: 1200px !important;
    margin: auto;
}

#title {
    text-align: center;
    margin-bottom: 20px;
}

.generate-btn {
    height: 55px;
    font-size: 18px !important;
    font-weight: bold !important;
}

footer {
    display: none !important;
}
"""

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="violet"
    ),
    css=custom_css,
    title="NeuralArt"
) as demo:

    gr.HTML("""
    <div id="title">
        <h1>🎨 NeuralArt</h1>
        <h3>AI Powered Neural Style Transfer</h3>
        <p>
            Transform ordinary photos into artistic masterpieces using
            <b>AdaIN</b> and <b>VGG19</b>.
        </p>
        <p><i>Developed by Harshit Pundir</i></p>
    </div>
    """)

    with gr.Row():

        content = gr.Image(
            type="pil",
            label="📸 Content Image",
            height=350
        )

        style = gr.Image(
            type="pil",
            label="🎭 Style Image",
            height=350
        )

    alpha = gr.Slider(
        minimum=0,
        maximum=1,
        value=1.0,
        step=0.1,
        label="🎨 Style Strength"
    )

    generate_btn = gr.Button(
        "✨ Generate Artwork",
        elem_classes=["generate-btn"]
    )

    output = gr.Image(
        type="pil",
        label="🖼️ Generated Artwork",
        height=500
    )

    generate_btn.click(
        fn=style_transfer,
        inputs=[content, style, alpha],
        outputs=output
    )

    gr.Markdown("""
    ---
    ### 🚀 How it Works

    1. Upload a content image.
    2. Upload a style image.
    3. Adjust style strength.
    4. Click **Generate Artwork**.
    5. Download your AI-generated result.

    **Tech Stack:** PyTorch • AdaIN • VGG19 • Gradio • Hugging Face Spaces
    """)

demo.launch()