import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .config import OUTPUT_DIR, DEFAULT_HEADERS
from .utils import download_image, sanitize_filename, logger

class VisualAssetScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        
        # Buat folder 'downloads' jika belum ada
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def fetch_page(self, url: str) -> BeautifulSoup:
        """Mengambil halaman web dan mengubahnya menjadi objek BeautifulSoup."""
        logger.info(f"Mengakses target: {url}")
        response = self.session.get(url, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'lxml')

    def extract_images(self, soup: BeautifulSoup, css_selector: str) -> list:
        """Mencari semua URL gambar berdasarkan CSS Selector."""
        images = []
        for img in soup.select(css_selector):
            # Beberapa web menggunakan data-src untuk lazy loading
            src = img.get('src') or img.get('data-src') 
            if src:
                # Memastikan URL lengkap (menggabungkan path relatif dengan base url)
                full_url = urljoin(self.base_url, src)
                images.append(full_url)
                
        return list(set(images)) # Hapus URL duplikat

    def run(self, target_url: str, css_selector: str = "img"):
        """Fungsi utama untuk mengeksekusi seluruh alur scraping."""
        logger.info("=== Memulai Ekstraksi Aset Visual ===")
        try:
            soup = self.fetch_page(target_url)
            image_urls = self.extract_images(soup, css_selector)
            
            logger.info(f"Ditemukan {len(image_urls)} aset visual potensial.")
            
            for index, img_url in enumerate(image_urls, start=1):
                # Mengambil nama asli file dari URL (contoh: hero_skin_01.png)
                filename = img_url.split("/")[-1].split("?")[0]
                if not filename or len(filename) > 50:
                    filename = f"asset_img_{index}.jpg"
                
                clean_name = sanitize_filename(filename)
                save_path = os.path.join(OUTPUT_DIR, clean_name)
                
                download_image(img_url, save_path, DEFAULT_HEADERS)
                
            logger.info("Operasi selesai dengan sukses!")
            
        except Exception as e:
            logger.error(f"Operasi dihentikan karena kesalahan: {e}")