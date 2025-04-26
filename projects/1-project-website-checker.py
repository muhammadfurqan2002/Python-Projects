
print(f"\n🔍 Website Checker 🔎\n")

website_url = input("Enter a website URL:")

if "https" in website_url:
    print(f"🔏 This website uses HTTPS (secure)")
elif "http" in website_url:
    print("💀 This website uses HTTP (not secure)")
else:
    print(f"this does not look like website")


if website_url.startswith("https://"):
    print(f"🔏 This website uses HTTPS (secure)")
elif website_url.startswith("http://"):
    print("💀 This website uses HTTP (not secure)")
else:
    print(f"this does not look like website")
