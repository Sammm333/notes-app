FILENAME = "notes.txt"

def load_notes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")

def add_note(text):
    text = text.strip()
    if not text:
        return
    notes = load_notes()
    notes.append(text)
    save_notes(notes)

def delete_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)

def clear_notes():
    open(FILENAME, "w", encoding="utf-8").close()
