#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# Saturday, 09 October 2021 14.59
# https://www.faturrachmanmochammad.id
# V.1.0.0.0 20211023

from django.urls import include, path
from django.contrib import admin
from django.urls.resolvers import URLPattern
from pendaftaran_wisuda.views import *
from . import views, sipw_surat

urlpatterns = [
    #--Publik--
    path('', sipw_login, name="login"),

    #--Dashboard A--
    path('akademik/dashboard', dashboard_a, name="dashboard_a"),
    path('akademik/pendaftar-wisuda', pendaftar_wisuda, name="pendaftar-wisuda"),
    path('akademik/pendaftar-wisuda/periksa-pendaftar/?ca4238a0b923820dcc509a6f75849b<id_pendaftaran_wisuda>4?c81e728d9d4c2f636f067f89cc14862cc', periksa_pendaftar_wisuda_persetujuan, name="periksa-pendaftar-persetujuan"),
    path('akademik/pendaftar-wisuda/periksa-pendaftar-tdisetujui/?ca4238a0b923820dcc509a6f75849b<id_pendaftaran_wisuda>4?c81e728d9d4c2f636f067f89cc14862cc', periksa_pendaftaran_wisuda_tdisetujui, name="periksa-pendaftar-tdisetujui"),
    path('akademik/pendaftar-wisuda/periksa-pendaftar-disetujui/?ca4238a0b923820dcc509a6f75849b<id_pendaftaran_wisuda>4?c81e728d9d4c2f636f067f89cc14862cc', periksa_pendaftar_wisuda_disetujui, name="periksa-pendaftar-disetujui"),
    path('akademik/pendaftar-wisuda/pembatalan/?c3238a0b923820dcc509a6f75849b<id_pendaftaran_wisuda>4?c81e728d9d4c2f636f067f89cc14862cc', pembatalan_pendaftar_wisuda, name="pembatalan-pendaftar"),
    path('akademik/jadwal-wisuda', jadwal_wisuda, name="jadwal-wisuda"),
    path('akademik/jadwal-wisuda/perbarui-jadwal/?<id_jadwal_wisuda>', perbarui_jadwal, name="perbarui-jadwal"),
    path('akademik/registrasi-akun', registrasi_akun, name="registrasi-akun"),
    path('akademik/informasi-publik', informasi_publik, name="informasi-publik"),
    path('akademik/informasi-publik/?c81e728d9d4c2f636f067f89cc14862c<id_informasi>4?cca4238a0b923820dcc509a6f75849b', edit_informasi_publik, name="edit-informasi"),
    
    #--Dashboard B--
    path('mahasiswa/dashboard', dashboard_m, name="dashboard_m"),
    
    #--Auth LL--
    path('logout', sipw_logout, name="logout"),

    #--Surat--
    path('view?id=9342d1a7b59455aks24124bs23131b7a7b5d14be096003f2cde3ce16a25620537?77699a8cb42f842a168beaa80b2c0483d1dfa1707cefe03f0550d9b660c05c0d/', login_required(login_url="login")(sipw_surat.view_pdf_hasil.as_view()), name="view-surat-pendaftaran"),
    path('unduh?id=9342d1a7b59455c24ff959a2a2991b7a7b5d14be096003f2cde3ce16a25620537?a049e96782003b92e4f06443b23e841438fcb095875b90177480e173be52e91b/', login_required(login_url="login")(sipw_surat.download_pdf_hasil.as_view()), name="download-surat-pendaftaran"),
]