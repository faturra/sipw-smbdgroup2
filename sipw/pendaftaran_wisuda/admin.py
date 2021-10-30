#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# Saturday, 09 October 2021 14.59
# https://www.faturrachmanmochammad.id
# V.1.0.0.0 20211023

from django.contrib import admin

# Register your models here.
from .models import Akademik, Fakultas, Gelar_Vokasi_Belakang, Gelar_Vokasi_Depan, Informasi_Publik, Jadwal_Wisuda, Mahasiswa, Pendaftaran_Wisuda, Program_Studi

admin.site.register(Informasi_Publik)
admin.site.register(Mahasiswa)
admin.site.register(Akademik)
admin.site.register(Program_Studi)
admin.site.register(Gelar_Vokasi_Depan)
admin.site.register(Gelar_Vokasi_Belakang)
admin.site.register(Jadwal_Wisuda)
admin.site.register(Pendaftaran_Wisuda)
admin.site.register(Fakultas)
