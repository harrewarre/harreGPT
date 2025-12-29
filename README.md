# Stuff to note

When trying to install PyTorch, use the `uv pip` backend (not `uv add`) eg:

```shell
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```