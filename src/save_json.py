import json
from pathlib import Path


def save_json(data, output_file):

    output = Path(output_file)

    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Saved to {output}")