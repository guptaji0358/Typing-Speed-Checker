import requests

path = r"E:\Documents_Files\RobinData\PYTHON\RawDataoftxt\TYPING_MASTER_PARAGRAPH.txt"

try:
    with open(path, "r", encoding="utf-8") as f:
        Sample_text = f.read()
except:
    Sample_text = "Offline file not found. Using fallback text."


def Get_Online_API_Words(count):
    try:
        response = requests.get(
            f"https://random-word-api.herokuapp.com/word?number={count}",
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                print("API Success:", len(data))
                return data

        print("API returned invalid data")
        return []

    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return []


def Filter_as_words(words, level):
    if level == "Easy":
        return [w for w in words if 3 <= len(w) <= 5]
    elif level == "Medium":
        return [w for w in words if 5 <= len(w) <= 8]
    elif level == "Hard":
        return words
    return words


def Build_a_Paragraph(words):
    if not words:
        return Sample_text

    paragraph = " ".join(words)
    return paragraph.capitalize() + "."