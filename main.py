import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk


with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="sky", 
        secondary_hue="violet",
        neutral_hue="slate",
        font=["Inter", "sans-serif"],
    ),
    css="""
    #app-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        color: #0ea5e9;
        margin-bottom: 0.75rem;
    }
    #app-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 2rem;
    }
    #report-box {
        padding: 1rem;
        border-radius: 0.75rem;
        background: #f8fafc;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        max-height: 500px;
        overflow-y: auto;
    }
    /* Button Styling + Animations */
    #deep-research-btn {
        border-radius: 0.75rem !important;
        font-weight: 600 !important;
        padding: 0.9rem 1.5rem !important;
        font-size: 1.1rem !important;
        background: linear-gradient(135deg, #0ea5e9, #6366f1) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease-in-out;
        animation: pulse 2s infinite;
    }
    #deep-research-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }
    """
) as ui:
    # Title
    gr.Markdown("<div id='app-title'>🔎 Deep Research Agent</div>")
    gr.Markdown("<div id='app-subtitle'>Ask me to research any topic in depth, and I’ll return a detailed report.</div>")
    
    # Input area
    query_textbox = gr.Textbox(
        label="Enter your research topic",
        placeholder="e.g. Future of quantum computing...",
        lines=2
    )
    
    # Button below textbox
    run_button = gr.Button("🚀 Start Deep Research", variant="primary", elem_id="deep-research-btn")

    # Report box
    report = gr.Markdown(label="Report", elem_id="report-box")

    # Bind events
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)
