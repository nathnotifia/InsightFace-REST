import sys
import json
import base64
from ifr_client import IFRClient  # refactor your class into ifr_client.py

def main():
    # Read JSON input from stdin
    raw_input = sys.stdin.read()
    input_data = json.loads(raw_input)

    images = input_data.get("images", {}).get("data", [])
    threshold = input_data.get("threshold", 0.6)
    extract_embedding = input_data.get("extract_embedding", True)
    return_face_data = input_data.get("return_face_data", False)

    client = IFRClient(host='http://localhost', port=18081)
    result = client.extract(
        data=images,
        mode='data',
        threshold=threshold,
        extract_embedding=extract_embedding,
        return_face_data=return_face_data,
        use_msgpack=False
    )

    # Print result JSON to stdout
    print(json.dumps(result))

if __name__ == "__main__":
    main()