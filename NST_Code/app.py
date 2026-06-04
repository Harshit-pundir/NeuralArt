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

css = """
.gradio-container{
    background: linear-gradient(135deg,#020617,#0f172a,#111827);
}

.hero{
    text-align:center;
    padding:50px;
    border-radius:25px;
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(20px);
    border:1px solid rgba(255,255,255,0.1);
    margin-bottom:25px;
}

.hero h1{
    font-size:4rem;
    font-weight:900;
    margin-bottom:10px;
    background:linear-gradient(
        90deg,
        #38bdf8,
        #8b5cf6,
        #ec4899
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero p{
    font-size:1.1rem;
}

.feature-card{
    padding:20px;
    border-radius:20px;
    text-align:center;
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,0.08);
    transition:0.3s;
}

.feature-card:hover{
    transform:translateY(-6px);
    box-shadow:0 0 30px rgba(168,85,247,0.5);
}

.stats{
    text-align:center;
    padding:15px;
    border-radius:20px;
    background:rgba(255,255,255,0.04);
}

.generate-btn{
    height:70px !important;
    font-size:22px !important;
    font-weight:bold !important;
}

.footer{
    text-align:center;
    padding-top:30px;
}
"""

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="purple"
    ),
    css=css,
    title="NeuralArt"
) as demo:

    gr.HTML("""
        <div class="hero">
        <h1>🎨 NeuralArt</h1>
        <h2>Turn Photos Into Masterpieces Using AI</h2>
        <p>Powered by AdaIN • PyTorch • Hugging Face</p>
        </div>
        """)

    with gr.Row():
            gr.HTML('<div class="feature-card">⚡ Fast Inference</div>')
            gr.HTML('<div class="feature-card">🎭 Artistic Styles</div>')
            gr.HTML('<div class="feature-card">🧠 Deep Learning</div>')
            gr.HTML('<div class="feature-card">☁️ Cloud Hosted</div>')

    with gr.Row():
            gr.HTML('<div class="stats"><h2>🚀 AI Powered</h2></div>')
            gr.HTML('<div class="stats"><h2>🎨 Unlimited Creativity</h2></div>')
            gr.HTML('<div class="stats"><h2>⚡ Real Time</h2></div>')

    gr.Markdown("## 🖼️ Upload Your Images")

    with gr.Row():
            content = gr.Image(
                type="pil",
                label="📸 Content Image",
                height=450
            )

            style = gr.Image(
                type="pil",
                label="🎨 Style Image",
                height=450
            )

    gr.Markdown("""
        ### ⚡ Create Stunning AI Artwork

        Upload a content image and a style image,
        then let NeuralArt transform it into a masterpiece.
        """)

    alpha = gr.Slider(
            minimum=0,
            maximum=1,
            value=1,
            step=0.1,
            label="✨ Style Strength"
        )

    btn = gr.Button(
            "🚀 Generate Masterpiece",
            variant="primary",
            elem_classes="generate-btn"
        )

    output = gr.Image(
            type="pil",
            label="🌟 AI Generated Artwork",
            height=650,
            show_download_button=True
        )

    btn.click(
            fn=style_transfer,
            inputs=[content, style, alpha],
            outputs=output
        )

    gr.Markdown("## 🎯 Try Sample Styles")

    gr.Examples(
            examples=[
                [
                    "examples/brad_pitt.jpg",
                    "examples/picasso_seated_nude_hr.jpg",
                    1.0
                ]
            ],
            inputs=[content, style, alpha]
        )

    gr.HTML("""
        <div class="footer">
        <hr>
        <h2>🚀 Built by Harshit Pundir</h2>
        <p>BTech CSE • AI/ML Engineer</p>
        <p>PyTorch • Hugging Face • AdaIN</p>
        <p>Made with ❤️ and Deep Learning</p>
        </div>
        """)

demo.launch(show_error=True)