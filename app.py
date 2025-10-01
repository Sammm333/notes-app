from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import notes_lib
import os

app = Flask(__name__, static_folder="static")

# Ensure notes file exists
if not os.path.exists("notes.txt"):
    open("notes.txt", "w", encoding="utf-8").close()

@app.route("/")
def index():
    notes = notes_lib.load_notes()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note")
    if note:
        notes_lib.add_note(note)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    notes_lib.delete_note(index)
    return redirect(url_for("index"))

@app.route("/clear")
def clear():
    notes_lib.clear_notes()
    return redirect(url_for("index"))

# PWA assets served from root
@app.route("/manifest.json")
def manifest():
    return send_from_directory(app.static_folder, "manifest.json", mimetype="application/json")

@app.route("/service-worker.js")
def service_worker():
    return send_from_directory(app.static_folder, "service-worker.js", mimetype="application/javascript")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
