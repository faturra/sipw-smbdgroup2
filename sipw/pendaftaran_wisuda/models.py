from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.http import request

# Create your models here.
class Fakultas(models.Model):
    id_fakultas = models.AutoField(primary_key=True)
    nama_fakultas = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nama_fakultas

class Program_Studi(models.Model):
    id_program_studi = models.AutoField(primary_key=True)
    id_fakultas = models.ForeignKey(Fakultas, null=True, blank=True, on_delete=models.CASCADE)
    nama_program_studi = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_program_studi

class Gelar_Vokasi_Depan(models.Model):
    id_gelar_depan = models.AutoField(primary_key=True)
    gelar_depan = models.CharField(max_length=200, null=True, blank=True)
    gelar_akademik = models.CharField(max_length=200, null=True, blank=True)
    lulusan = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gelar_depan

class Gelar_Vokasi_Belakang(models.Model):
    id_gelar_belakang = models.AutoField(primary_key=True)
    gelar_belakang = models.CharField(max_length=200, null=True, blank=True)
    gelar_akademik = models.CharField(max_length=200, null=True, blank=True)
    lulusan = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gelar_belakang

class Informasi_Publik(models.Model):
    STATUS_CHOICES = {
        ('Hanya Staf', 'Hanya Staf'),
        ('Publik', 'Publik'),
    }
    id_informasi = models.IntegerField(primary_key=True)
    judul = models.CharField(max_length=200, null=True, blank=True)
    isi = models.TextField(null=True, blank=True, default='...')
    visibilitas = models.CharField(max_length=150, choices=STATUS_CHOICES, default='Hanya Staf')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul

class Mahasiswa(models.Model):
    JENIS_KELAMIN = {
        ('Laki-laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
    }

    STATUS_KEAKTIFAN = {
        ('Aktif', 'Aktif'),
        ('Non-Aktif', 'Non-Aktif'),
    }

    KELAS = {
        ('A', 'A'),
        ('B', 'B'),
    }
    id_mahasiswa = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nama_mahasiswa = models.CharField(max_length=200, null=True, blank=True)
    tempat_lahir = models.CharField(max_length=200, null=True, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    jenis_kelamin = models.CharField(max_length=150, null=True, blank=True, choices=JENIS_KELAMIN)
    nim = models.CharField(max_length=200, null=True, blank=True)
    program_studi = models.ForeignKey(Program_Studi, null=True, blank=True, on_delete=models.CASCADE)
    fakultas = models.ForeignKey(Fakultas, null=True, blank=True, on_delete=models.CASCADE)
    alamat = models.CharField(max_length=300, null=True, blank=True)
    kelas = models.CharField(max_length=10, choices=KELAS, default='A')
    status_keaktifan = models.CharField(max_length=150, choices=STATUS_KEAKTIFAN, default='Aktif')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_mahasiswa

class Akademik(models.Model):
    JENIS_KELAMIN = {
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    }

    STATUS_KEAKTIFAN = {
        ('Aktif', 'Aktif'),
        ('Non-Aktif', 'Non-Aktif'),
    }
    id_akademik = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_akademik = models.CharField(max_length=200, null=True)
    nidn = models.CharField(max_length=200, null=True, blank=True)
    gelar_depan = models.ForeignKey(Gelar_Vokasi_Depan, null=True, on_delete=models.CASCADE)
    gelar_belakang = models.ForeignKey(Gelar_Vokasi_Belakang, null=True, on_delete=models.CASCADE)
    tanggal_lahir = models.DateField(null=True, blank=True)
    tempat_lahir = models.CharField(max_length=200, null=True)
    jenis_kelamin = models.CharField(max_length=150, null=True, blank=True, choices=JENIS_KELAMIN)
    prodi_yang_diampu = models.ForeignKey(Program_Studi, null=True, on_delete=models.CASCADE)
    no_ktp = models.CharField(max_length=100, null=True, blank=True)
    status_keaktifan = models.CharField(max_length=150, choices=STATUS_KEAKTIFAN, default='Aktif')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_akademik

class Jadwal_Wisuda(models.Model):
    PELAKSANAAN = {
        ('Geladi Bersih', 'Geladi Bersih'),
        ('Utama', 'Utama'),
    }

    id_jadwal_wisuda = models.AutoField(primary_key=True)
    pelaksanaan = models.CharField(max_length=150, choices=PELAKSANAAN, default='Geladi Bersih')
    tanggal_wisuda = models.DateField(null=True, blank=True)
    waktu_wisuda = models.TimeField(null=True, blank=True)
    lokasi_wisuda = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pelaksanaan


class Pendaftaran_Wisuda(models.Model):
    UKURAN_TOGA = {
        ('S','S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    }

    STATUS_APPROVAL = {
        ('Belum Disetujui', 'Belum Disetujui'),
        ('Tidak Disetujui', 'Tidak Disetujui'),
        ('Disetujui', 'Disetujui'),
    }

    JENIS_PENDAFTARAN = {
        ('Pendaftaran Wisuda', 'Pendaftaran Wisuda')
    }

    YN = {
        ('Yakin, lanjutkan', 'Yakin, lanjutkan')
    }
    id_pendaftaran_wisuda = models.AutoField(primary_key=True)
    id_mahasiswa = models.ForeignKey(Mahasiswa, null=True, on_delete=models.CASCADE)
    id_jadwal_wisuda = models.ForeignKey(Jadwal_Wisuda, null=True, blank=True, on_delete=models.CASCADE)
    jenis_pendaftaran = models.CharField(max_length=150, choices=JENIS_PENDAFTARAN, default='Pendaftaran Wisuda')
    ukuran_toga = models.CharField(max_length=150, choices=UKURAN_TOGA, default='L')
    status_approval = models.CharField(max_length=150, choices=STATUS_APPROVAL, default='Belum Disetujui')
    keterangan = models.CharField(max_length=200, null=True, blank=True)
    yn = models.CharField(max_length=100, null=True, blank=True, choices=YN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jenis_pendaftaran