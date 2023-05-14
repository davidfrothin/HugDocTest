from transformers.tools import HfAgent 
import textract 

#text = textract.process('sample.pdf').decode('utf-8') 
text = "I am an AI called Simon but call me Simple"
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder") 
agent.run("Can you summarize 'text for me?", text=text) 
agent.run("Based on 'text', tell me a joke", text=text) 
