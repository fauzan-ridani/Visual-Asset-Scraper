from scraper.engine import VisualAssetScraper

def main():
    # Kamu bisa mengganti URL ini dengan halaman wiki atau galeri web favoritmu
    TARGET_URL = "https://books.toscrape.com/" 
    
    # CSS Selector (Bisa disesuaikan. Contoh: '.gallery-item img' atau 'div.hero-artwork img')
    # Default "img" akan mengambil semua gambar di halaman tersebut.
    CSS_SELECTOR = ".thumbnail" 

    print("\n" + "="*40)
    print(" Python Visual Asset Scraper 🕷️")
    print("="*40 + "\n")

    scraper = VisualAssetScraper(base_url=TARGET_URL)
    scraper.run(target_url=TARGET_URL, css_selector=CSS_SELECTOR)

if __name__ == "__main__":
    main()