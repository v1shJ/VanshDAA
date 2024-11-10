import heapq
from collections import Counter
from docx import Document
from pdfminer.high_level import extract_text
from graphviz import Digraph  # For tree visualization
import os

class HuffmanNode:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char  # Character
        self.freq = freq  # Frequency
        self.left = left  # Left child (node)
        self.right = right  # Right child (node)

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Step 1: Count the frequency of each character
    frequency = Counter(text)

    # Step 2: Create a priority queue (min-heap)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Step 3: Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge them into a new node with combined frequency
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]  # The root of the Huffman tree

def generate_huffman_codes(node, prefix="", huffman_codes={}):
    if node is None:
        return

    # If the node is a leaf, assign the current prefix as the code
    if node.char is not None:
        huffman_codes[node.char] = prefix

    generate_huffman_codes(node.left, prefix + "0", huffman_codes)
    generate_huffman_codes(node.right, prefix + "1", huffman_codes)

    return huffman_codes

def huffman_encode(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

def save_compressed(encoded_text, filename):
    with open(filename, 'w') as file:
        file.write(encoded_text)

def print_huffman_tree(node, indent=0):
    """Print the Huffman tree in a structured format."""
    if node is None:
        return

    # If it's a leaf node, print the character and its frequency
    if node.char is not None:
        print(' ' * indent + f"'{node.char}': {node.freq}")
    else:
        print(' ' * indent + f"Node({node.freq})")

    # Traverse left and right child nodes
    if node.left:
        print(' ' * (indent + 2) + "Left:")
        print_huffman_tree(node.left, indent + 4)

    if node.right:
        print(' ' * (indent + 2) + "Right:")
        print_huffman_tree(node.right, indent + 4)

def plot_huffman_tree(node, graph=None, node_id=0):
    """Generate a visual representation of the Huffman Tree using graphviz."""
    if graph is None:
        graph = Digraph(format='png')

    if node is not None:
        node_label = f"Freq: {node.freq}"
        if node.char is not None:
            node_label = f"'{node.char}'\nFreq: {node.freq}"

        graph.node(str(node_id), label=node_label)

        if node.left:
            graph.edge(str(node_id), str(node_id * 2 + 1), label="0")
            plot_huffman_tree(node.left, graph, node_id * 2 + 1)

        if node.right:
            graph.edge(str(node_id), str(node_id * 2 + 2), label="1")
            plot_huffman_tree(node.right, graph, node_id * 2 + 2)

    return graph

def display_binary_codes(huffman_codes):
    """Display the binary representation (Huffman code) for each character."""
    print("\nHuffman Codes (Binary Representation):")
    for char, code in huffman_codes.items():
        print(f"Character: '{char}' -> Code: {code}")

def read_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def read_pdf(file_path):
    """Extract text from a PDF using pdfminer.six"""
    return extract_text(file_path)

def determine_file_type(file_path):
    """Determine the file type based on the extension."""
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()

def calculate_compression_ratio(original_size, compressed_size_bits):
    """Calculate and display the compression ratio."""
    compressed_size_bytes = compressed_size_bits / 8  # Convert bits to bytes
    compression_ratio = original_size / compressed_size_bytes
    print(f"\nOriginal File Size: {original_size} bytes")
    print(f"Compressed File Size: {compressed_size_bytes:.2f} bytes")
    print(f"Compression Ratio: {compression_ratio:.2f}")

def compress_file(file_path):
    # Determine the file type based on the file extension
    file_extension = determine_file_type(file_path)

    if file_extension == '.txt':
        text = read_txt(file_path)
    elif file_extension == '.docx':
        text = read_docx(file_path)
    elif file_extension == '.pdf':
        text = read_pdf(file_path)
    elif file_extension == '.html':
        text = read_txt(file_path)
    else:
        return (f"Unsupported file type: {file_extension}")

    # Get the original file size
    original_file_size = os.path.getsize(file_path)

    # Build Huffman tree
    root = build_huffman_tree(text)

    # Generate Huffman codes
    huffman_codes = generate_huffman_codes(root)

    # Encode the text
    encoded_text = huffman_encode(text, huffman_codes)

    # Save the compressed text
    compressed_filename = f"{file_path}_compressed.txt"
    save_compressed(encoded_text, compressed_filename)

    # Calculate the size of the compressed text (in bits)
    compressed_size_bits = len(encoded_text)  # Each character in the encoded text is 1 bit

    # Calculate the compression ratio
    calculate_compression_ratio(original_file_size, compressed_size_bits)

    # Display the binary representation of each character
    display_binary_codes(huffman_codes)

    # Plot the Huffman Tree and save it as a PNG image
    graph = plot_huffman_tree(root)
    graph.render(f"{file_path}_huffman_tree")  # Saves as PNG
    print(f"Huffman Tree saved as: {file_path}_huffman_tree.png")

if __name__ == "__main__":
    # Specify the file path
    file_path = r"C:\Users\Vansh_Prac\SY_Prac\Python\DAA-LAB\Lab5\huffprac.docx"  # Change this to your file's path
    compress_file(file_path)