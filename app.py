from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_form():
    company_url = request.form.get("company_url")
    job_position = request.form.get("job_position")
    recipient = request.form.get("recipient")
    resume_attached = "resume_attached" in request.form

    # For now, just return the submitted data for verification
    return f"""
    Company URL: {company_url}<br>
    Job Position: {job_position}<br>
    Recipient: {recipient}<br>
    Resume Attached: {'Yes' if resume_attached else 'No'}
    """

if __name__ == '__main__':
    app.run(debug=True)
