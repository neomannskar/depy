import sys
import base64

# Contains lambda functions like base64 and more

methods = [
  lambda s: base64.b64decode(s).decode("utf-8"),  # Base64 decoding
  lambda s: s[::-1],  # Example: Reverse string
]

def main():
  length = len(sys.argv)
  if length < 3:
    print("Usage depy.py <decryption-method-flag> <string-to-decrypt>")
    sys.exit();
  
  input_str = sys.argv[2]
  
  if sys.argv[1] == "--try-all":
    for method in methods:
      # Call method and try to decrypt the string with that method
      try:
        print(method(input_str))
      except Exception as e:
        print(f"Method failed: {e}")

if __name__ ==  "__main__":
  main();
