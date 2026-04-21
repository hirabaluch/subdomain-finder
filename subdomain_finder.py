import requests

print("==== Subdomain Finder Tool ====")

domain = input("Enter domain (example: google.com): ")

subdomains = ["www", "admin", "mail", "test", "dev", "api", "blog", "shop"]

found = []

for sub in subdomains:
    url_http = f"http://{sub}.{domain}"
    url_https = f"https://{sub}.{domain}"
    
    try:
        requests.get(url_http, timeout=3)
        print(f"[+] Found: {url_http}")
        found.append(url_http)
    except:
        pass

    try:
        requests.get(url_https, timeout=3)
        print(f"[+] Found: {url_https}")
        found.append(url_https)
    except:
        pass

if found:
    with open("results.txt", "w") as f:
        for url in found:
            f.write(url + "\n")
    print("\nResults saved in results.txt")
else:
    print("No subdomains found.")