import struct

def check_magic_and_version(filename):
    with open(filename, 'rb') as f:
        # Read the first 6 bytes from the file
        data = f.read(6)

    # Unpack the binary data, interpreting the first 4 bytes as a little-endian unsigned int
    # and the next 2 bytes as a little-endian unsigned short
    magic, version = struct.unpack('<I H', data)

    print(f"magic: 0x{magic:08x}, version: 0x{version:04x}, file: {filename}")

    return magic, version


check_magic_and_version("./models/llama-2-7b/ggml-model-f32.bin")
