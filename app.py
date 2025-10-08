from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:page>")
def serve_page(page):
    
    if page.endswith(".html") and os.path.exists(page):
        return send_from_directory(".", page)
    return "Not Found", 404

@app.route("/api/send_message", methods=["POST"])
def api_send_message():
    data = request.get_json(force=True)
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    # For now print to console; you can integrate email or DB here
    print(f"\n📩 New message\nFrom: {name} <{email}>\nMessage: {message}\n")
    return jsonify({"success": True, "message": "✅ Message sent successfully! Thank you."})

# Let Flask serve static files via /static/*
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
