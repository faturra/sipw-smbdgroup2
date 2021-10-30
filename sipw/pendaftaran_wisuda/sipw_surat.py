#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# Saturday, 09 October 2021 14.59
# https://www.faturrachmanmochammad.id
# V.1.0.0.0 20211023

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from datetime import datetime
from .models import Jadwal_Wisuda, Mahasiswa, Pendaftaran_Wisuda
import mimetypes

#surat pdf
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class view_pdf_hasil(View):
	def get(self, request, *args, **kwargs):
		jadwal_wisuda_ls = request.user.mahasiswa.pendaftaran_wisuda_set.all()
		jadwal_mhs = request.user.mahasiswa.pendaftaran_wisuda_set.all().select_related('id_jadwal_wisuda')
		data_mhs = Mahasiswa.objects.filter(user = request.user)

		context = {'jadwal_wisuda_ls':jadwal_wisuda_ls,'data_mhs':data_mhs,'jadwal_mhs':jadwal_mhs}
		pdf = render_to_pdf('main/surat/surat_pendaftaran.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

class download_pdf_hasil(View):
	def get(self, request, *args, **kwargs):
		jadwal_wisuda_ls = request.user.mahasiswa.pendaftaran_wisuda_set.all()
		jadwal_mhs = request.user.mahasiswa.pendaftaran_wisuda_set.all().select_related('id_jadwal_wisuda')
		data_mhs = Mahasiswa.objects.filter(user = request.user)

		context = {'jadwal_wisuda_ls':jadwal_wisuda_ls,'data_mhs':data_mhs,'jadwal_mhs':jadwal_mhs}
		pdf = render_to_pdf('main/surat/surat_pendaftaran.html', context)
        
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = 'Bukti_Pendaftaran_%s.pdf' %(request.user.mahasiswa.nim)
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response