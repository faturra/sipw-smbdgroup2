#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# Saturday, 09 October 2021 14.59
# https://www.faturrachmanmochammad.id
# V.1.0.0.0 20211023

from django import forms
from django.forms import fields
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Informasi_Publik, Pendaftaran_Wisuda, Jadwal_Wisuda

class Informasi_Publik_Form(forms.ModelForm):

    class Meta:
        model = Informasi_Publik
        fields = ('judul','isi','visibilitas')

    def __init__(self, *args, **kwargs):
        super(Informasi_Publik_Form,self).__init__(*args, **kwargs)

#--Form Pendafatr------
class Pendaftaran_Wisuda_Form(forms.ModelForm):

    class Meta:
        model = Pendaftaran_Wisuda
        fields = ('jenis_pendaftaran','ukuran_toga')

        def __init__(self, *args, **kwargs):
            super(Pendaftaran_Wisuda_Form,self).__init__(*args, **kwargs)

#--Form Periksa Pendaftar------
#Persetujuan
class Periksa_Pendaftaran_Wisuda_Persetujuan(forms.ModelForm):

    class Meta:
        model = Pendaftaran_Wisuda
        fields = ('ukuran_toga','status_approval','keterangan','yn')
        labels = {'ukuran_toga':'Ukuran Toga','status_approval':'Status Persetujuan','keterangan':'Keterangan','yn':''}

        def __init__(self, *args, **kwargs):
            super(Pendaftaran_Wisuda_Form,self).__init__(*args, **kwargs)

#Tidak Disetujui
#Disetujui
class Periksa_Pendaftaran_Wisuda_Tdisetujui(forms.ModelForm):

    class Meta:
        model = Pendaftaran_Wisuda
        fields = ('status_approval','keterangan','yn')
        labels = {'status_approval':'Status Persetujuan','keterangan':'Keterangan','yn':''}

        def __init__(self, *args, **kwargs):
            super(Periksa_Pendaftaran_Wisuda_Tdisetujui,self).__init__(*args, **kwargs)

#Disetujui
class Periksa_Pendaftaran_Wisuda_Disetujui(forms.ModelForm):

    class Meta:
        model = Pendaftaran_Wisuda
        fields = ('id_jadwal_wisuda',)
        labels = {'id_jadwal_wisuda':'Pelaksanaan'}

        def __init__(self, *args, **kwargs):
            super(Periksa_Pendaftaran_Wisuda_Disetujui,self).__init__(*args, **kwargs)

#--Form Jadwal Wisuda------
class Jadwal_Wisuda_Form(forms.ModelForm):

    class Meta:
        model = Jadwal_Wisuda
        fields = ('tanggal_wisuda','waktu_wisuda','lokasi_wisuda')
        labels = {'tanggal_wisuda':'Tanggal Pelaksanaan (yyyy-mm-dd)','waktu_wisuda':'Waktu Pelaksanaan (hh:mm:ss)','lokasi_wisuda':'Lokasi'}

        def __init__(self, *args, **kwargs):
            super(Jadwal_Wisuda_Form,self).__init__(*args, **kwargs)

#--Registrasi Akun------
class Ragistrasi_Akun_Forms(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )