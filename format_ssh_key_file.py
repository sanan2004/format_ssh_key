import sys

def format_openssh_key(raw_key):
    header = "-----BEGIN OPENSSH PRIVATE KEY-----"
    footer = "-----END OPENSSH PRIVATE KEY-----"
    key_content = raw_key.replace(header, "").replace(footer, "").replace("\n", "").replace(" ", "").strip()
    formatted_key_content = "\n".join([key_content[i:i+64] for i in range(0, len(key_content), 64)])
    formatted_key = f"{header}\n{formatted_key_content}\n{footer}\n"
    return formatted_key

def main():
    if len(sys.argv)!= 3:
        print("Usage: python3 format_ssh_key_file.py <input_filename> <output_filename>")
        return

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, 'r') as infile:
            raw_key = infile.read()
        formatted_key = format_openssh_key(raw_key)
        with open(output_filename, 'w') as outfile:
            outfile.write(formatted_key)
        print(f"\nKey formatted and saved to {output_filename}")
    except FileNotFoundError:
        print(f"File {input_filename} not found.")

if __name__ == "__main__":
    main()