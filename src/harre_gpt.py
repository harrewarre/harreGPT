import re

from simple_tokenizer_v2 import SimpleTokenizerV2


with open ("the-verdict.txt", "r") as file:
    raw_text = file.read()
pre_processed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
pre_processed = [item.strip() for item in pre_processed if item.strip()]

all_tokens = sorted(list(set(pre_processed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer, token in enumerate(all_tokens)}

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)

tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.decode(tokenizer.encode(text)))
