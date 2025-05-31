from screenshot import photographer
import json

DATA = "data.json"
RESOURCES_FOLDER = "output"

def main():
    urls = []
    with open(DATA, "r", encoding="utf-8") as file:
        file_data = json.load(file)
        urls = set(file_data["urls"])

    for url in urls:
        photographer.screenshot(url, output_folder=RESOURCES_FOLDER)

if __name__ == "__main__":
    main()
