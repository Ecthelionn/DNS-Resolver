import os
import dns.resolver

def find_subdomains_and_paths(domain, entries_file):
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
            full_entry = f"{entry}.{domain}"
            try:
                answers = dns.resolver.resolve(full_entry, 'A')
                for rdata in answers:
                    found_addresses.append(f"{full_entry}: {rdata}")
                    print(f"{full_entry}: {rdata}")
            except dns.resolver.NoAnswer:
                print(f"{full_entry}: No answer available")
            except dns.exception.DNSException as e:
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
