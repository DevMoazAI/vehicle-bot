# # app.py
# import gradio as gr
# from app_logic import handle_user_query

# def chat_interface(user_input):
#     return handle_user_query(user_input)

# with gr.Blocks() as demo:
#     gr.Markdown("#  Vehicle Issue Diagnostic Bot")
#     gr.Markdown("Ask any question related to your car or bike problems. The assistant will help you professionally.")
    
#     with gr.Row():
#         user_input = gr.Textbox(placeholder="Describe your vehicle issue here...", lines=2, label="Your Question")
    
#     output = gr.Textbox(label="Assistant's Response", lines=10)

#     submit_btn = gr.Button("Diagnose")
#     submit_btn.click(chat_interface, inputs=user_input, outputs=output)

# demo.launch()
# 
import gradio as gr
from app_logic import handle_user_query

def chat_interface(user_input):
    return handle_user_query(user_input)

with gr.Blocks(css="""
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

body {
    background: #eef1f7;
    font-family: 'Segoe UI', sans-serif;
    color: #333333;
}

.card {
    background-color: #ffffff;
    width: 96%;
    max-width: 1000px;
    margin: 50px auto;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

/* Title */
h1 {
    font-size: 30px;
    color: #ffffff;
    background: linear-gradient(to right, #54c472, #43b75d);
    padding: 20px 28px;
    border-radius: 14px;
    margin-bottom: 16px;
    text-align: center;
}

/* Subheading */
.subhead {
    color: #444444;
    font-size: 17px;
    text-align: center;
    margin-bottom: 30px;
}

/* FontAwesome icon color */
.icon {
    margin-right: 10px;
    color: #ffffff;
}

/* Labels for "Your Question" and "Assistant's Response" */
label {
    font-weight: bold !important;
    font-size: 16px !important;
    color: #000000 !important;
    background: #d3f5e0;
    padding: 10px 14px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 10px;
}

/* Input textarea */
.gr-textbox textarea {
    font-size: 16px !important;
    border-radius: 12px !important;
    padding: 14px;
    border: 1px solid #ccc !important;
    background-color: #fcfcfc !important;
    color: #333333;
}

/* Output textarea */
.output-area textarea {
    background: #f4fdf7 !important;
    border-radius: 12px !important;
    font-family: 'Courier New', monospace;
    font-size: 15px;
    color: #222222;
    padding: 14px;
    border: 1px solid #ccc !important;
}

/* Button style */
.gr-button {
    background: #2cb3a8 !important;
    color: white !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    padding: 12px 26px !important;
    margin-top: 18px;
    transition: background 0.3s ease;
}

.gr-button:hover {
    background: #1d9389 !important;
}

/* Responsive Layout */
@media screen and (max-width: 768px) {
    .card {
        padding: 24px;
    }

    h1 {
        font-size: 24px;
        padding: 16px 20px;
    }

    .subhead {
        font-size: 15px;
    }

    .gr-textbox textarea,
    .output-area textarea {
        font-size: 15px !important;
    }

    .gr-button {
        font-size: 15px !important;
        width: 100%;
    }
}

@media screen and (max-width: 480px) {
    h1 {
        font-size: 22px;
    }

    .subhead {
        font-size: 13px;
    }

    label {
        font-size: 14px !important;
    }
}
""") as demo:
    with gr.Column(elem_classes="card"):
        gr.HTML("<h1><i class='fas fa-car-crash icon'></i>Vehicle Issue Diagnostic Bot</h1>")
        gr.HTML("<div class='subhead'>Get expert-level help for car, bike, or scooter issues. Describe the problem and let the assistant guide you.</div>")

        user_input = gr.Textbox(
            placeholder="Describe your vehicle issue here...",
            lines=2,
            label="Your Question"
        )

        output = gr.Textbox(
            label="Assistant's Response",
            lines=18,
            elem_classes="output-area",
            interactive=False
        )

        submit_btn = gr.Button("Diagnose My Vehicle")
        submit_btn.click(chat_interface, inputs=user_input, outputs=output)

demo.launch()
