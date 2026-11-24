import os

ENTRY = (
    "WARNING: Fridge contents do not change at 2 a.m. "
    "User will nonetheless open it again in ten minutes, just to be sure."
)

assert len(ENTRY) <= 160

os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w', encoding='utf-8') as f:
    f.write(ENTRY)
