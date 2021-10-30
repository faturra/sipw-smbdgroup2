#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# Saturday, 09 October 2021 14.59
# https://www.faturrachmanmochammad.id
# V.1.0.0.0 20211023

from django import contrib
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .sipw_decorators import unauthenticated_user, akademik_only, mahasiswa_only

# Models & Forms
from .models import Informasi_Publik, Mahasiswa, Pendaftaran_Wisuda, Jadwal_Wisuda
from .forms import Informasi_Publik_Form, Pendaftaran_Wisuda_Form, Jadwal_Wisuda_Form, Periksa_Pendaftaran_Wisuda_Persetujuan, Periksa_Pendaftaran_Wisuda_Disetujui, Ragistrasi_Akun_Forms, Periksa_Pendaftaran_Wisuda_Tdisetujui

# Create your views here.

#----Public Outside----
@unauthenticated_user
def sipw_login(request):
    informasi_pub = Informasi_Publik.objects.filter(id_informasi=1, visibilitas='Publik')

    context = {'informasi_pub':informasi_pub}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Selamat datang di Sistem Informasi Pendaftaran Wisuda ')
            return redirect('dashboard_a')
        else:
            messages.info(request,'Email atau Password Anda Salah')
            return redirect('login')
    return render(request, 'publik/login.html', context)

def sipw_logout(request):
    logout(request)
    return redirect('login')


#----Dashboard_A----
@login_required(login_url="login")
@akademik_only
def dashboard_a(request):
    pending = Pendaftaran_Wisuda.objects.filter(status_approval='Belum Disetujui').count
    tidak_disetujui = Pendaftaran_Wisuda.objects.filter(status_approval='Tidak Disetujui',yn='Yakin, lanjutkan').count
    disetujui = Pendaftaran_Wisuda.objects.filter(status_approval='Disetujui',yn='Yakin, lanjutkan').count
    total = Pendaftaran_Wisuda.objects.all().count

    context = {
        'pending':pending,
        'tidak_disetujui':tidak_disetujui,
        'disetujui':disetujui,
        'total':total,
        }
    return render(request, 'main/akademik/dashboard_a/dashboard_a.html', context)


#----Dashboard_M----
@login_required(login_url="login")
@mahasiswa_only
def dashboard_m(request):
    jadwal_wisuda_ls = request.user.mahasiswa.pendaftaran_wisuda_set.all()
    jadwal_mhs = request.user.mahasiswa.pendaftaran_wisuda_set.filter(status_approval='Disetujui', yn='Yakin, lanjutkan').select_related('id_jadwal_wisuda')
    status_pendaftaran_wisuda = request.user.mahasiswa.pendaftaran_wisuda_set.filter(jenis_pendaftaran='Pendaftaran Wisuda')
    #initial_mahasiswa = request.user.mahasiswa
    pendaftarn_wisuda_form = Pendaftaran_Wisuda_Form() #(initial={'id_mahasiswa' : initial_mahasiswa})
    #pendaftarn_wisuda_form.fields['id_mahasiswa'].widget.attrs['disabled'] = Trueself.fields['yn'].required = True
    if request.method == 'POST':
        pendaftarn_wisuda_form = Pendaftaran_Wisuda_Form(request.POST)
        if pendaftarn_wisuda_form.is_valid():
            instance = pendaftarn_wisuda_form.save(commit=False)
            instance.id_mahasiswa = request.user.mahasiswa
            instance.save()
            messages.info(request,'Pendaftaran Berhasil. Silakan tunggu proses persetujuan Akademik')
            return redirect('dashboard_m')
            
        else: return redirect('dashboard_m')
    
    pending = Pendaftaran_Wisuda.objects.filter(status_approval='Belum Disetujui').count
    tidak_disetujui = Pendaftaran_Wisuda.objects.filter(status_approval='Tidak Disetujui',yn='Yakin, lanjutkan').count
    disetujui = Pendaftaran_Wisuda.objects.filter(status_approval='Disetujui',yn='Yakin, lanjutkan').count
    total = Pendaftaran_Wisuda.objects.all().count

    context = {
        'status_pendaftaran_wisuda':status_pendaftaran_wisuda, 
        'pendaftaran_wisuda_form':pendaftarn_wisuda_form,
        'pending':pending,
        'tidak_disetujui':tidak_disetujui,
        'disetujui':disetujui,
        'total':total,
        'jadwal_wisuda_ls':jadwal_wisuda_ls,
        'jadwal_mhs':jadwal_mhs
        }
    return render(request, 'main/mahasiswa/dashboard_m/dashboard_m.html', context)  


#----Pendaftar Wisuda----
@login_required(login_url="login")
@akademik_only
def pendaftar_wisuda(request):
    pendaftar_wisuda = Pendaftaran_Wisuda.objects.filter(jenis_pendaftaran='Pendaftaran Wisuda',yn='Yakin, lanjutkan')
    pending = Pendaftaran_Wisuda.objects.filter(status_approval='Belum Disetujui').select_related('id_mahasiswa')
    tidak_disetujui = Pendaftaran_Wisuda.objects.filter(status_approval='Tidak Disetujui',yn='Yakin, lanjutkan').select_related('id_mahasiswa')
    disetujui = Pendaftaran_Wisuda.objects.filter(status_approval='Disetujui',yn='Yakin, lanjutkan').select_related('id_mahasiswa')

    context = {
        'pendaftar_wisuda':pendaftar_wisuda,
        'pending':pending,
        'tidak_disetujui':tidak_disetujui,
        'disetujui':disetujui,
        }
    return render(request, 'main/akademik/pendaftar_wisuda/pendaftar_wisuda.html', context)

@login_required(login_url="login")
@akademik_only
def periksa_pendaftar_wisuda_persetujuan(request, id_pendaftaran_wisuda):
    pendaftar = Pendaftaran_Wisuda.objects.get(pk=id_pendaftaran_wisuda)
    mahasiswa = Pendaftaran_Wisuda.objects.all().select_related('id_mahasiswa')
    periksa_pendaftar = Periksa_Pendaftaran_Wisuda_Persetujuan(request.POST or None, instance=pendaftar)
    periksa_pendaftar.fields['yn'].widget.attrs['required'] = True
    if request.method == 'POST':
        if periksa_pendaftar.is_valid():
            periksa_pendaftar.save()
            messages.info(request,'Berhasil melakukan perubahan')
            return redirect('pendaftar-wisuda')
    else: 
        pendaftar
        
        context = {'periksa_pendaftar':periksa_pendaftar,'pendaftar':pendaftar,'mahasiswa':mahasiswa}
        return render(request, 'main/akademik/pendaftar_wisuda/periksa_pendaftar_persetujuan.html', context)

@login_required(login_url="login")
@akademik_only
def periksa_pendaftaran_wisuda_tdisetujui(request, id_pendaftaran_wisuda):
    pendaftar = Pendaftaran_Wisuda.objects.get(pk=id_pendaftaran_wisuda)
    mahasiswa = Pendaftaran_Wisuda.objects.all().select_related('id_mahasiswa')
    periksa_pendaftar_tdisetujui = Periksa_Pendaftaran_Wisuda_Tdisetujui(request.POST or None, instance=pendaftar)
    periksa_pendaftar_tdisetujui.fields['yn'].widget.attrs['required'] = True
    if request.method == 'POST':
        if periksa_pendaftar_tdisetujui.is_valid():
            periksa_pendaftar_tdisetujui.save()
            messages.info(request,'Berhasil melakukan perubahan')
            return redirect('pendaftar-wisuda')
    else: 
        pendaftar
        
        context = {'periksa_pendaftar_tdisetujui':periksa_pendaftar_tdisetujui,'pendaftar':pendaftar,'mahasiswa':mahasiswa}
        return render(request, 'main/akademik/pendaftar_wisuda/periksa_pendaftar_tdisetujui.html', context)

@login_required(login_url="login")
@akademik_only
def periksa_pendaftar_wisuda_disetujui(request, id_pendaftaran_wisuda):
    periksa_disetujui = Pendaftaran_Wisuda.objects.get(pk=id_pendaftaran_wisuda)
    pendaftar_disetujui_form = Periksa_Pendaftaran_Wisuda_Disetujui(request.POST or None, instance=periksa_disetujui)
    pendaftar_disetujui_form.fields['id_jadwal_wisuda'].widget.attrs['required'] = True
    if request.method == 'POST':
        if pendaftar_disetujui_form.is_valid():
            instance = pendaftar_disetujui_form.save(commit=False)
            instance.save()
            messages.info(request,'Berhasil melakukan perubahan')
            return redirect('pendaftar-wisuda')
    else: 
        periksa_disetujui
        
        context = {'pendaftar_disetujui_form':pendaftar_disetujui_form,'periksa_disetujui':periksa_disetujui}
        return render(request, 'main/akademik/pendaftar_wisuda/periksa_pendaftar_disetujui.html', context)

@login_required(login_url="login")
@akademik_only
def pembatalan_pendaftar_wisuda(request, id_pendaftaran_wisuda):
    pembatalan_pendaftar = Pendaftaran_Wisuda.objects.get(pk=id_pendaftaran_wisuda)
    pembatalan_pendaftar.delete()
    messages.info(request,'Berhasil melakukan pembatalan pendaftar')

    return redirect('pendaftar-wisuda')


#----Registrasi Akun----
@login_required(login_url="login")
@akademik_only
def registrasi_akun(request):
    if request.method == 'POST':
        registrasi_akun = Ragistrasi_Akun_Forms(request.POST)
        if registrasi_akun.is_valid():
            registrasi_akun.save()
            messages.info(request,'Registrasi Akun Berhasil')
            return redirect('dashboard_a')

        context={'registrasi_akun':registrasi_akun}
        return render(request,'main/akademik/registrasi/registrasi_akun.html', context)


#----Jadwal Wisuda----
@login_required(login_url="login")
@akademik_only
def jadwal_wisuda(request):
    jadwal_wisuda_ls = Jadwal_Wisuda.objects.all()
    
    context = {'jadwal_wisuda_ls':jadwal_wisuda_ls}
    return render(request,'main/akademik/jadwal_wisuda/jadwal_wisuda.html', context)
    
@login_required(login_url="login")
@akademik_only
def perbarui_jadwal(request, id_jadwal_wisuda):
    perbarui_jadwal = Jadwal_Wisuda.objects.get(pk=id_jadwal_wisuda)
    perbarui_jadwal_form = Jadwal_Wisuda_Form(request.POST or None, instance=perbarui_jadwal)
    if request.method == 'POST':
        if perbarui_jadwal_form.is_valid():
            perbarui_jadwal_form.save()
            messages.info(request,'Berhasil melakukan perubahan jadwal')
            return redirect('jadwal-wisuda')
    else: 
        perbarui_jadwal
        
        context = {'perbarui_jadwal_form':perbarui_jadwal_form,'perbarui_jadwal':perbarui_jadwal}
        return render(request, 'main/akademik/jadwal_wisuda/perbarui_jadwal.html', context)


#----Informasi Publik----
@login_required(login_url="login")
@akademik_only
def informasi_publik(request):
    informasi_ls = Informasi_Publik.objects.all()

    context = {'informasi_ls':informasi_ls}
    return render(request, 'main/akademik/informasi_publik/informasi_publik.html', context)

@login_required(login_url="login")
@akademik_only
def edit_informasi_publik(request, id_informasi):
    informasi = Informasi_Publik.objects.get(pk=id_informasi)
    edit_informasi_pub = Informasi_Publik_Form(request.POST or None, instance=informasi)
    if request.method == 'POST':
        if edit_informasi_pub.is_valid():
            edit_informasi_pub.save()
            return redirect('informasi-publik')
    else: 
        informasi
        
        context = {'edit_informasi_pub':edit_informasi_pub, 'informasi':informasi}
    return render(request, 'main/akademik/informasi_publik/perbarui_informasi.html', context)


#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# V.1.0.0.0 20211023