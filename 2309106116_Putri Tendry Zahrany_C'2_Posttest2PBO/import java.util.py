import java.util.ArrayList;
import java.util.Scanner;

public class KlinikGigiSmileCare {
    private ArrayList<Pasien> daftarPasien;
    private Scanner scanner;
    public String namaKlinik; // Contoh penerapan public

    public KlinikGigiSmileCare() {
        daftarPasien = new ArrayList<>();
        scanner = new Scanner(System.in);
        this.namaKlinik = "SmileCare Dental Clinic"; // Inisialisasi nama klinik
    }

    public void tampilMenu() {
        while (true) {
            System.out.println("\n--- Sistem Manajemen Klinik Gigi " + namaKlinik + " ---");
            System.out.println("1. Tambah Pasien");
            System.out.println("2. Lihat Daftar Pasien");
            System.out.println("3. Update Data Pasien");
            System.out.println("4. Hapus Data Pasien");
            System.out.println("5. Cari Pasien");
            System.out.println("6. Keluar");
            System.out.print("Pilih menu: ");

            int pilihan = scanner.nextInt();
            scanner.nextLine(); // Membersihkan newline

            switch (pilihan) {
                case 1:
                    tambahPasien();
                    break;
                case 2:
                    lihatDaftarPasien();
                    break;
                case 3:
                    updateDataPasien();
                    break;
                case 4:
                    hapusDataPasien();
                    break;
                case 5:
                    cariPasien();
                    break;
                case 6:
                    System.out.println("Terima kasih!");
                    return;
                default:
                    System.out.println("Pilihan tidak valid.");
            }
        }
    }

    private void tambahPasien() {
        System.out.print("Nama: ");
        String nama = scanner.nextLine();
        System.out.print("Umur: ");
        int umur = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Nomor Telepon: ");
        String nomorTelepon = scanner.nextLine();
        System.out.print("Alamat: ");
        String alamat = scanner.nextLine();
        System.out.print("Keluhan: ");
        String keluhan = scanner.nextLine();

        Pasien pasienBaru = new Pasien(nama, umur, nomorTelepon, alamat, keluhan);
        daftarPasien.add(pasienBaru);
        System.out.println("Pasien berhasil ditambahkan.");
    }

    private void lihatDaftarPasien() {
        if (daftarPasien.isEmpty()) {
            System.out.println("Daftar pasien kosong.");
        } else {
            System.out.println("--- Daftar Pasien ---");
            for (int i = 0; i < daftarPasien.size(); i++) {
                System.out.println((i + 1) + ". " + daftarPasien.get(i));
            }
        }
    }

    private void updateDataPasien() {
        lihatDaftarPasien();
        if (daftarPasien.isEmpty()) {
            return;
        }

        System.out.print("Masukkan nomor pasien yang ingin diupdate: ");
        int nomorPasien = scanner.nextInt();
        scanner.nextLine();

        if (nomorPasien > 0 && nomorPasien <= daftarPasien.size()) {
            Pasien pasien = daftarPasien.get(nomorPasien - 1);

            System.out.print("Nama baru (" + pasien.getNama() + "): ");
            String namaBaru = scanner.nextLine();
            if (!namaBaru.isEmpty()) {
                pasien.setNama(namaBaru);
            }

            System.out.print("Umur baru (" + pasien.getUmur() + "): ");
            String umurBaru = scanner.nextLine();
            if (!umurBaru.isEmpty()) {
                try {
                    pasien.setUmur(Integer.parseInt(umurBaru));
                } catch (NumberFormatException e) {
                    System.out.println("Input umur tidak valid. Harap masukkan angka.");
                }
            }

            System.out.print("Nomor Telepon baru (" + pasien.getNomorTelepon() + "): ");
            String nomorTeleponBaru = scanner.nextLine();
            if (!nomorTeleponBaru.isEmpty()) {
                pasien.setNomorTelepon(nomorTeleponBaru);
            }

            System.out.print("Alamat baru (" + pasien.getAlamat() + "): ");
            String alamatBaru = scanner.nextLine();
            if (!alamatBaru.isEmpty()) {
                pasien.setAlamat(alamatBaru);
            }

            System.out.print("Keluhan baru (" + pasien.getKeluhan() + "): ");
            String keluhanBaru = scanner.nextLine();
            if (!keluhanBaru.isEmpty()) {
                pasien.setKeluhan(keluhanBaru);
            }

            System.out.println("Data pasien berhasil diupdate.");
        } else {
            System.out.println("Nomor pasien tidak valid.");
        }
    }

    private void hapusDataPasien() {
        lihatDaftarPasien();
        if (daftarPasien.isEmpty()) {
            return;
        }

        System.out.print("Masukkan nomor pasien yang ingin dihapus: ");
        int nomorPasien = scanner.nextInt();
        scanner.nextLine();

        if (nomorPasien > 0 && nomorPasien <= daftarPasien.size()) {
            daftarPasien.remove(nomorPasien - 1);
            System.out.println("Pasien berhasil dihapus.");
        } else {
            System.out.println("Nomor pasien tidak valid.");
        }
    }

    private void cariPasien() {
        if (daftarPasien.isEmpty()) {
            System.out.println("Daftar pasien kosong.");
            return;
        }

        System.out.print("Masukkan nama pasien yang ingin dicari: ");
        String namaCari = scanner.nextLine();

        boolean ditemukan = false;
        System.out.println("--- Hasil Pencarian ---");
        for (int i = 0; i < daftarPasien.size(); i++) {
            if (daftarPasien.get(i).getNama().toLowerCase().contains(namaCari.toLowerCase())) {
                System.out.println((i + 1) + ". " + daftarPasien.get(i));
                ditemukan = true;
            }
        }

        if (!ditemukan) {
            System.out.println("Pasien dengan nama '" + namaCari + "' tidak ditemukan.");
        }
    }

    public static void main(String[] args) {
        KlinikGigiSmileCare klinik = new KlinikGigiSmileCare();
        klinik.tampilMenu();
    }
}

class Pasien {
    private String nama;
    private int umur;
    private String nomorTelepon;
    private String alamat;
    private String keluhan;
    protected String catatanMedis; // Contoh penerapan protected
    String status; // Contoh penerapan default

    public Pasien(String nama, int umur, String nomorTelepon, String alamat, String keluhan) {
        this.nama = nama;
        this.umur = umur;
        this.nomorTelepon = nomorTelepon;
        this.alamat = alamat;
        this.keluhan = keluhan;
        this.catatanMedis = "Belum ada catatan medis.";
        this.status = "Baru";
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public int getUmur() {
        return umur;
    }

    public void setUmur(int umur) {
        if (umur >= 0) {
            this.umur = umur;
        } else {
            System.out.println("Umur tidak valid. Harus lebih dari atau sama dengan 0.");
        }
    }

    public String getNomorTelepon() {
        return nomorTelepon;
    }

    public void setNomorTelepon(String nomorTelepon) {
        this.nomorTelepon = nomorTelepon;
    }

    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }

    public String getKeluhan() {
        return keluhan;
    }

    public void setKeluhan(String keluhan) {
        this.keluhan = keluhan;
    }

    public String getCatatanMedis() {
        return catatanMedis;
    }

    protected void setCatatanMedis(String catatanMedis) {
        this.catatanMedis = catatanMedis;
    }

    public String getStatus() {
        return status;
    }

    void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Nama: " + nama + ", Umur: " + umur + ", No. Telp: " + nomorTelepon + ", Alamat: " + alamat + ", Keluhan: " + keluhan + ", Status: " + status;
    }
}