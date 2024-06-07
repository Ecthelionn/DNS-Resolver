import os
import requests
import dns.resolver

def find_subdomains_and_paths(domain, entries_file):
    # Remove 'http://' or 'https://' prefix if present
    if domain.startswith('http://'):
        domain = domain[len('http://'):]
    elif domain.startswith('https://'):
        domain = domain[len('https://'):]

    # Get the current directory path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    entries_file_path = os.path.join(current_dir, entries_file)

    found_addresses = []

    try:
        with open(entries_file_path, 'r') as file:
            entries = file.readlines()

        entries = [entry.strip() for entry in entries]

        print(f"Subdomains and paths for {domain}:")
        for entry in entries:
            if entry.startswith('/'):
                # Treat entry as a path
                full_entry = f"https://{domain}{entry}"
            else:
                # Treat entry as a subdomain
                full_entry = f"https://{entry}.{domain}"

            try:
                # Bypass SSL certificate verification
                response = requests.get(full_entry, verify=False)
                if response.status_code == 200:
                    found_addresses.append(full_entry)
                    print(f"{full_entry}: Found")
                else:
                    print(f"{full_entry}: Not Found (Status code: {response.status_code})")
            except requests.exceptions.RequestException as e:
                print(f"Error resolving {full_entry}: {e}")

        print("\nFound addresses:")
        for address in found_addresses:
            print(address)

    except FileNotFoundError:
        print(f"Error: {entries_file_path} not found")

def main():
    domain_name = input("Enter the domain name: ")
    entries_file = input("Enter the entries file name: ")
    find_subdomains_and_paths(domain_name, entries_file)

if __name__ == "__main__":
    main()
