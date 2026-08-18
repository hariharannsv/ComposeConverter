
import os
import subprocess

from flask import (
    Flask,
    request,
    render_template,
    send_file,
    redirect,
    url_for
)

from werkzeug.utils import secure_filename


app = Flask(__name__)


# -----------------------------------
# Project directories
# -----------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "generated")


# Create directories if they don't exist

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# -----------------------------------
# Home / Upload Route
# -----------------------------------

@app.route("/", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        # Check if file exists
        if "file" not in request.files:

            return render_template(
                "index.html",
                error="Please select a file."
            )


        file = request.files["file"]


        # Check filename
        if file.filename == "":

            return render_template(
                "index.html",
                error="Please select a file."
            )


        # Check extension
        if not file.filename.endswith((".yml", ".yaml")):

            return render_template(
                "index.html",
                error="Please upload a .yml or .yaml file."
            )


        # Secure filename
        filename = secure_filename(file.filename)


        # Save uploaded file
        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        file.save(filepath)


        # Output file
        output_file = os.path.join(
            OUTPUT_FOLDER,
            "k8s.yaml"
        )


        # -----------------------------------
        # Run Kompose
        # -----------------------------------

        try:

            result = subprocess.run(
                [
                    "kompose",
                    "convert",
                    "-f",
                    filepath,
                    "-o",
                    output_file
                ],
                capture_output=True,
                text=True
            )


            # Kompose error
            if result.returncode != 0:

                return render_template(
                    "index.html",
                    error=result.stderr
                )


        except FileNotFoundError:

            return render_template(
                "index.html",
                error="Kompose is not installed or not available in PATH."
            )


        # Redirect to download
        return redirect(
            url_for("download")
        )


    return render_template("index.html")


# -----------------------------------
# Download Route
# -----------------------------------

@app.route("/download")
def download():

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "k8s.yaml"
    )


    if os.path.exists(output_file):

        return send_file(
            output_file,
            as_attachment=True,
            download_name="k8s.yaml"
        )


    return "Generated file not found.", 404


# -----------------------------------
# Run Flask
# -----------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False
    )
