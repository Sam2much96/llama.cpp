
from llama_cpp import Llama

llm = Llama("./models/llama-2-7b/ggml-model-q4_0.gguf" , n_ctx=2048)
output = llm("Q: What is Godot Game Engine?\n  A: ", max_tokens=250, stop=["Q:", "\n"], echo=True)
print(output)


