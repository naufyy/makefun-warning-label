"""Warning Label for Humans: one-line entry.

The joke is a deadpan safety notice, written in the flat voice of a real
printed warning label, about a very human habit: opening the fridge at
2 a.m., finding nothing new, and doing it again ten minutes later. The label
treats this as a hazard to be formally flagged, and the humor lands in the
last few words ("just to be sure").
"""
import os

ENTRY = (
    "WARNING: Fridge contents do not change at 2 a.m. "
    "User will nonetheless open it again in ten minutes, just to be sure."
)

assert len(ENTRY) <= 160

os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w', encoding='utf-8') as f:
    f.write(ENTRY)
