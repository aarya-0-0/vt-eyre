import argparse
from vt_eyre import scanner

def main():
    parser = argparse.ArgumentParser(description="VT-Eyre CLI Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="File path to scan")
    group.add_argument("--url", help="URL to scan")
    parser.add_argument("--server-url", help="Optional custom server URL (default: http://127.0.0.1:8000)")

    args = parser.parse_args()

    # Use custom server URL if provided
    server_url = args.server_url or scanner.SERVER_URL

    try:
        if args.file:
            scanner.scan_file(args.file, server_url)
        elif args.url:
            scanner.scan_url(args.url, server_url)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
