import os
import io

from flask import Flask, Response, request, abort, render_template
import pdfkit

from models import XCM_osenniy, Triathlon

app = Flask(__name__)

@app.route("/xcm_kabanova/2023/<int:user_id>/html/")
def xcm_osenniy_2023_html(user_id):
    result = XCM_osenniy.get(user_id)
    if result is None: abort(404)

    return render_template('xcm_osenniy_2023/diploma.html', result=result)

@app.route("/xcm_kabanova/2023/<int:user_id>/pdf/")
def xcm_osenniy_2023_pdf(user_id):
    # Note: use absolute URL. Wkhtmltopdf does not work with relative urls on the same server (why?)
    html_url = f"https://brevet.omskvelo.ru/diploma/xcm_kabanova/2023/{user_id}/html/"
    pdf = pdfkit.from_url(html_url)

    return Response(pdf, mimetype="application/pdf")


@app.route("/triathlon/<int:id>/html/")
def triathlon_html(id):
    result = Triathlon.get(id)
    if result is None: abort(404)

    return render_template('triathlon/diploma.html', result=result)


@app.route("/triathlon/<int:id>")
def triathlon_pdf(id):
    # Note: use absolute URL. Wkhtmltopdf does not work with relative urls on the same server (why?)
    html_url = f"https://brevet.omskvelo.ru/diploma/triathlon/{id}/html/"
    pdf = pdfkit.from_url(html_url)

    return Response(pdf, mimetype="application/pdf")
