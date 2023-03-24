import openai
import requests
import response
import http
import gradio as gr
from flask import Flask


openai.api_key = "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"


def get_response(prompt):
    parameters = {
        "model": "text-davinci-002",
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 500,
        "n": 1,
        "stop": None,
    }

# Generate text using Openai API
    response = openai.Completion.create(**parameters)

# Retrun generated text
    return response.choices[0].text.strip()


inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=get_response, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",).launch(share=True)
