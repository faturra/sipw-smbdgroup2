#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# Saturday, 09 October 2021 14.59
# https://www.faturrachmanmochammad.id
# V.1.0.0.0 20211023

from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'errors/404.html')

def handler403(request, exception):
    return render(request, 'errors/403.html')