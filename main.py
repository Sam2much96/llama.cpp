
from llama_cpp import Llama

llm = Llama("./models/llama-2-7b/ggml-model-q4_0.gguf" , n_ctx=128)
output = llm("Q: What is Godot Game Engine?\n  A: ", max_tokens=25, stop=["Q:", "\n"], echo=True)
print(output)


