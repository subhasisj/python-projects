### Data extractor for PDF invoices - invoice2data

A modular Python library to support your accounting process. Tested on Python 2.7 and 3.4+. Main steps:

extracts text from PDF files using different techniques, like pdftotext, pdfminer or OCR – tesseract, tesseract4 or gvision (Google Cloud Vision).
searches for regex in the result using a YAML-based template system
saves results as CSV, JSON or XML or renames PDF files to match the content.
With the flexible template system you can:

precisely match content PDF files
plugins available to match line items and tables
define static fields that are the same for every invoice
define custom fields needed in your organisation or process
have multiple regex per field (if layout or wording changes)
define currency
extract invoice-items using the lines-plugin developed by Holger Brunn