import os
import io

from flask import Flask, Response, request, abort, render_template
app = Flask(__name__)

import pdfkit
pdf_config = pdfkit.configuration(wkhtmltopdf=r"C:\cmd_utils\wkhtmltopdf\bin\wkhtmltopdf.exe")
# pdfkit.configuration(wkhtmltopdf=os.environ['wkhtmltopdf'])


from models import Mock as Result

@app.route("/xcm_kabanova/2023/<int:user_id>/html/")
def xcm_osenniy_2023_html(user_id):
    print(request.base_url)
    result = Result.get(user_id)
    if result is None: abort(404)

    return render_template('xcm_osenniy_2023/diploma.html', result=result)

@app.route("/xcm_kabanova/2023/<int:user_id>/pdf/")
def xcm_osenniy_2023_pdf(user_id):
    html_url = request.base_url.replace("pdf", "html")
    pdf = pdfkit.from_url(html_url, configuration=pdf_config)

    return Response(pdf, mimetype="application/pdf")