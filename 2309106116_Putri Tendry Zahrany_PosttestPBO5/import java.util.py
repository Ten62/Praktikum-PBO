import java.util.ArrayList;
import java.util.Scanner;

public class KlinikGigiSmileCare {
    private ArrayList<Pasien> daftarPasien;
    private Scanner scanner;
    public final String namaKlinik; // FINAL atribut

    public KlinikGigiSmileCare() {
        daftarPasien = new ArrayList<>();
        scanner = new Scanner(System.in);
        this.namaKlinik = "SmileCare Dental Clinic";
    }

    public void tampilMenu() {
        while (true) {
            System.out.println("\n+=============================================+");
            System.out.printf("|   %-43s|\n", "Sistem Manajemen Klinik Gigi " + namaKlinik);
            System.out.println("+=============================================+");
            System.out.printf("| %-3s | %-35s |\n", "No", "Menu");
            System.out.println("+-----+---------------------------------------+");
            System.out.printf("| %-3s | %-35s |\n", "1", "Tambah Pasien Baru");
            System.out.printf("| %-3s | %-35s |\n", "2", "Tambah Pasien Lama");
            System.out.printf("| %-3s | %-35s |\n", "3", "Lihat Daftar Pasien");
            System.out.printf("| %-3s | %-35s |\n", "4", "Update Data Pasien");
            System.out.printf("| %-3s | %-35s |\n", "5", "Hapus Data Pasien");
            System.out.printf("| %-3s | %-35s |\n", "6", "Cari Pasien");
            System.out.printf("| %-3s | %-35s |\n", "7", "Keluar");
            System.out.println("+-----+---------------------------------------+");

            System.out.print("Pilih menu: ");
            int pilihan = scanner.nextInt();
            scanner.nextLine();

            switch (pilihan) {
                case 1 -> tambahPasienBaru();
                case 2 -> tambahPasienLama();
                case 3 -> lihatDaftarPasien();
                case 4 -> updateDataPasien();
                case 5 -> hapusDataPasien();
                case 6 -> cariPasien();
                case 7 -> {
                    System.out.println("Terima kasih!");
                    return;
                }
                default -> System.out.println("Pilihan tidak valid.");
            }
        }
    }

    private void tambahPasienBaru() {
        System.out.print("Nama: ");
        String nama = scanner.nextLine();
        System.out.print("Umur: ");
        int umur = scanner.nextInt(); scanner.nextLine();
        System.out.print("Nomor Telepon: ");
        String nomorTelepon = scanner.nextLine();
        System.out.print("Alamat: ");
        String alamat = scanner.nextLine();
        System.out.print("Keluhan: ");
        String keluhan = scanner.nextLine();

        PasienBaru pasienBaru = new PasienBaru(nama, umur, nomorTelepon, alamat, keluhan);
        daftarPasien.add(pasienBaru);
        System.out.println("Pasien baru berhasil ditambahkan.");
    }

    private void tambahPasienLama() {
        System.out.print("Nama: ");
        String nama = scanner.nextLine();
        System.out.print("Umur: ");
        int umur = scanner.nextInt(); scanner.nextLine();
        System.out.print("Nomor Telepon: ");
        String nomorTelepon = scanner.nextLine();
        System.out.print("Alamat: ");
        String alamat = scanner.nextLine();
        System.out.print("Keluhan: ");
        String keluhan = scanner.nextLine();
        System.out.print("Nomor Rekam Medis: ");
        String nomorRekamMedis = scanner.nextLine();

        PasienLama pasienLama = new PasienLama(nama, umur, nomorTelepon, alamat, keluhan, nomorRekamMedis);
        daftarPasien.add(pasienLama);
        System.out.println("Pasien lama berhasil ditambahkan.");
    }

    private void lihatDaftarPasien() {
        if (daftarPasien.isEmpty()) {
            System.out.println("Daftar pasien kosong.");
        } else {
            System.out.println("--- Daftar Pasien ---");
            for (int i = 0; i < daftarPasien.size(); i++) {
                System.out.println((i + 1) + ". " + daftarPasien.get(i).getInfo());
            }
        }
    }

    private void updateDataPasien() {
        lihatDaftarPasien();
        if (daftarPasien.isEmpty()) return;

        System.out.print("Masukkan nomor pasien yang ingin diupdate: ");
        int nomorPasien = scanner.nextInt(); scanner.nextLine();

        if (nomorPasien > 0 && nomorPasien <= daftarPasien.size()) {
            Pasien pasien = daftarPasien.get(nomorPasien - 1);

            System.out.print("Nama baru (" + pasien.getNama() + "): ");
            String namaBaru = scanner.nextLine();
            if (!namaBaru.isEmpty()) pasien.setNama(namaBaru);

            System.out.print("Umur baru (" + pasien.getUmur() + "): ");
            String umurBaru = scanner.nextLine();
            if (!umurBaru.isEmpty()) {
                try {
                    pasien.setUmur(Integer.parseInt(umurBaru));
                } catch (NumberFormatException e) {
                    System.out.println("Umur tidak valid.");
                }
            }

            System.out.print("Nomor Telepon baru (" + pasien.getNomorTelepon() + "): ");
            String telpBaru = scanner.nextLine();
            if (!telpBaru.isEmpty()) pasien.setNomorTelepon(telpBaru);

            System.out.print("Alamat baru (" + pasien.getAlamat() + "): ");
            String alamatBaru = scanner.nextLine();
            if (!alamatBaru.isEmpty()) pasien.setAlamat(alamatBaru);

            System.out.print("Keluhan baru (" + pasien.getKeluhan() + "): ");
            String keluhanBaru = scanner.nextLine();
            if (!keluhanBaru.isEmpty()) pasien.setKeluhan(keluhanBaru);

            if (pasien instanceof PasienLama pl) {
                System.out.print("Nomor Rekam Medis baru (" + pl.getNomorRekamMedis() + "): ");
                String rekamMedisBaru = scanner.nextLine();
                if (!rekamMedisBaru.isEmpty()) pl.setNomorRekamMedis(rekamMedisBaru);
            }

            System.out.println("Data pasien berhasil diperbarui.");
        } else {
            System.out.println("Nomor pasien tidak valid.");
        }
    }

    private void hapusDataPasien() {
        lihatDaftarPasien();
        if (daftarPasien.isEmpty()) return;

        System.out.print("Masukkan nomor pasien yang ingin dihapus: ");
        int nomorPasien = scanner.nextInt(); scanner.nextLine();

        if (nomorPasien > 0 && nomorPasien <= daftarPasien.size()) {
            daftarPasien.remove(nomorPasien - 1);
            System.out.println("Data pasien berhasil dihapus.");
        } else {
            System.out.println("Nomor tidak valid.");
        }
    }

    private void cariPasien() {
        if (daftarPasien.isEmpty()) {
            System.out.println("Daftar pasien kosong.");
            return;
        }

        System.out.print("Masukkan nama pasien: ");
        String keyword = scanner.nextLine();

        boolean ditemukan = false;
        for (int i = 0; i < daftarPasien.size(); i++) {
            if (daftarPasien.get(i).getNama().toLowerCase().contains(keyword.toLowerCase())) {
                System.out.println((i + 1) + ". " + daftarPasien.get(i).getInfo());
                ditemukan = true;
            }
        }

        if (!ditemukan) {
            System.out.println("Pasien tidak ditemukan.");
        }
    }

    public static void main(String[] args) {
        KlinikGigiSmileCare klinik = new KlinikGigiSmileCare();
        klinik.tampilMenu();
    }
}

// ABSTRACT CLASS
abstract class Pasien {
    private String nama;
    private int umur;
    private String nomorTelepon;
    private String alamat;
    private String keluhan;
    protected String catatanMedis;
    String status;

    public Pasien(String nama, int umur, String nomorTelepon, String alamat, String keluhan) {
        this.nama = nama;
        this.umur = umur;
        this.nomorTelepon = nomorTelepon;
        this.alamat = alamat;
        this.keluhan = keluhan;
        this.catatanMedis = "Belum ada catatan medis.";
        this.status = "Baru";
    }

    public String getNama() { return nama; }
    public void setNama(String nama) { this.nama = nama; }
    public int getUmur() { return umur; }
    public void setUmur(int umur) { if (umur >= 0) this.umur = umur; }
    public String getNomorTelepon() { return nomorTelepon; }
    public void setNomorTelepon(String nomorTelepon) { this.nomorTelepon = nomorTelepon; }
    public String getAlamat() { return alamat; }
    public void setAlamat(String alamat) { this.alamat = alamat; }
    public String getKeluhan() { return keluhan; }
    public void setKeluhan(String keluhan) { this.keluhan = keluhan; }

    public String getCatatanMedis() { return catatanMedis; }
    protected void setCatatanMedis(String catatanMedis) { this.catatanMedis = catatanMedis; }

    public final String getStatus() { return status; } // FINAL METHOD
    void setStatus(String status) { this.status = status; }

    public String getInfo() {
        return "Nama: " + nama + ", Umur: " + umur + ", Telp: " + nomorTelepon +
                ", Alamat: " + alamat + ", Keluhan: " + keluhan + ", Status: " + status;
    }

    public abstract void pemeriksaan(); // ABSTRACT METHOD
}

// FINAL CLASS
final class PasienLama extends Pasien {
    private String nomorRekamMedis;

    public PasienLama(String nama, int umur, String nomorTelepon, String alamat, String keluhan, String nomorRekamMedis) {
        super(nama, umur, nomorTelepon, alamat, keluhan);
        this.nomorRekamMedis = nomorRekamMedis;
        this.setStatus("Lama");
    }

    public String getNomorRekamMedis() { return nomorRekamMedis; }
    public void setNomorRekamMedis(String nomorRekamMedis) { this.nomorRekamMedis = nomorRekamMedis; }

    @Override
    public String getInfo() {
        return super.getInfo() + ", No. Rekam Medis: " + nomorRekamMedis + ", Jenis: Pasien Lama";
    }

    @Override
    public void pemeriksaan() {
        System.out.println("Pemeriksaan dilakukan untuk pasien lama.");
    }
}

class PasienBaru extends Pasien {
    public PasienBaru(String nama, int umur, String nomorTelepon, String alamat, String keluhan) {
        super(nama, umur, nomorTelepon, alamat, keluhan);
    }

    @Override
    public String getInfo() {
        return super.getInfo() + ", Jenis: Pasien Baru";
    }

    @Override
    public void pemeriksaan() {
        System.out.println("Pemeriksaan awal untuk pasien baru.");
    }
}
