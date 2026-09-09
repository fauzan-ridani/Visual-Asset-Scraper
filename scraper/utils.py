import os
import re
import requests
import logging

# Setup sistem logging agar terminal terlihat profesional (tidak sekadar menggunakan print)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def sanitize_filename(filename: str) -> str:
    """Membersihkan karakter ilegal dari nama file agar bisa disimpan di Windows/Linux."""
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def download_image(url: str, save_path: str, headers: dict) -> bool:
    """Mengunduh gambar secara streaming (aman untuk file besar)."""
    try:
        response = requests.get(url, headers=headers, stream=True, timeout=15)
        response.raise_for_status() # Akan memicu error jika status code bukan 200 (OK)
        
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        
        logger.info(f"Berhasil mengunduh: {os.path.basename(save_path)}")
        return True
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Gagal mengunduh {url}: {e}")
        return False