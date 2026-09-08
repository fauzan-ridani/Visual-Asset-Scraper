# Visual-Asset-Scraper
Eksperimen web scraping dengan Python menggunakan BeautifulSoup4 untuk mengunduh gambar secara efisien

Sebuah script eksperimental berbasis Python untuk mengekstrak dan mengunduh aset visual secara otomatis dari halaman web menggunakan `BeautifulSoup4` dan `Requests`.

## Fitur
- Mendukung pembersihan URL otomatis dan penanganan *lazy-loading* (`data-src`).
- Mengunduh file secara *streaming* sehingga ramah memori (RAM).
- *Logging system* yang terstruktur.
- Sanitasi nama file untuk menghindari *error* pada sistem operasi.

## Cara Penggunaan
Buka file main.py menggunakan teks editor pilihan Anda. Modifikasi variabel TARGET_URL dan CSS_SELECTOR sesuai dengan elemen target dari website yang ingin di-scrape.
• Setelah selesai mengatur target, jalankan program di terminal dengan perintah:
/Bash
• python main.py



Setelah selesai mengatur target, jalankan program di terminal dengan perintah:

## Cara Instalasi

1. Pastikan Python sudah terinstal di sistem Anda.
2. *Clone* repositori ini:
   ```bash
   git clone [https://github.com/fauzan-ridani/Visual-Asset-Scraper.git](https://github.com/fauzan-ridani/Visual-Asset-Scraper.git)
   cd Visual-Asset-Scraper
