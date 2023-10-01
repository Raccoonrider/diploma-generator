import os
import io

from flask import Flask, Response, request, abort, render_template
import pdfkit

from models import Mock as Result

app = Flask(__name__)

@app.route("/xcm_kabanova/2023/<int:user_id>/html/")
def xcm_osenniy_2023_html(user_id):
    result = Result.get(user_id)
    if result is None: abort(404)

    return render_template('xcm_osenniy_2023/diploma.html', result=result)

@app.route("/xcm_kabanova/2023/<int:user_id>/pdf/")
def xcm_osenniy_2023_pdf(user_id):
    html_url = request.base_url.replace("pdf", "html").replace("http", "https")
    pdf = pdfkit.from_url(html_url)

    return Response(pdf, mimetype="application/pdf")