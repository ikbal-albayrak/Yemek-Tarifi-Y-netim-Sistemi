import tkinter as tk
from tkinter import messagebox, scrolledtext

class Tarif:
    def __init__(self, ad, malzemeler, yapilis, pisirme_suresi):
        self.ad = ad
        self.malzemeler = malzemeler
        self.yapilis = yapilis
        self.pisirme_suresi = pisirme_suresi

    def tarif_bilgisi(self):
        return f"Yemek: {self.ad}\nMalzemeler: {', '.join(self.malzemeler)}\nYapılış: {self.yapilis}\nPişirme Süresi: {self.pisirme_suresi} dakika\n"

class Atistirmalik(Tarif):
    def __init__(self, ad, malzemeler, yapilis, pisirme_suresi):
        super().__init__(ad, malzemeler, yapilis, pisirme_suresi)
        self.tur = "Atıştırmalık"

class AnaYemekTarif(Tarif):
    def __init__(self, ad, malzemeler, yapilis, pisirme_suresi):
        super().__init__(ad, malzemeler, yapilis, pisirme_suresi)
        self.tur = "Ana Yemek"

class TatliTarif(Tarif):
    def __init__(self, ad, malzemeler, yapilis, pisirme_suresi):
        super().__init__(ad, malzemeler, yapilis, pisirme_suresi)
        self.tur = "Tatlı"

class VeganTarif(AnaYemekTarif):
    def __init__(self, ad, malzemeler, yapilis, pisirme_suresi):
        super().__init__(ad, malzemeler, yapilis, pisirme_suresi)
        self.tur = "Vegan Ana Yemek"

class YemekTarifleriYonetimi:
    def __init__(self):
        self.tarifler = []

    def tarif_ekle(self, tarif):
        self.tarifler.append(tarif)

    def tarif_listele(self):
        return [tarif.tarif_bilgisi() for tarif in self.tarifler]

class Uygulama:
    def __init__(self, root):
        self.yonetim = YemekTarifleriYonetimi()
        self.root = root
        self.root.title("Yemek Tarifleri")
        self.root.geometry("600x700")
        self.root.configure(bg="#f9f9f9")

        self._setup_ui()

    def _setup_ui(self):
        title = tk.Label(self.root, text="Yemek Tarifleri", font=("Arial", 24, "bold"), bg="#ffcc00", fg="#333333")
        title.pack(pady=10, fill=tk.X)

        tk.Label(self.root, text="Yemek Adı:", font=("Arial", 12), bg="#f9f9f9").pack(pady=5)
        self.ad_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.ad_entry.pack(pady=5)

        tk.Label(self.root, text="Malzemeleri (virgül ile ayırarak):", font=("Arial", 12), bg="#f9f9f9").pack(pady=5)
        self.malzemeler_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.malzemeler_entry.pack(pady=5)

        tk.Label(self.root, text="Yapılışı:", font=("Arial", 12), bg="#f9f9f9").pack(pady=5)
        self.yapilis_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.yapilis_entry.pack(pady=5)

        tk.Label(self.root, text="Pişirme Süresi (dakika):", font=("Arial", 12), bg="#f9f9f9").pack(pady=5)
        self.pisirme_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.pisirme_entry.pack(pady=5)

        tk.Label(self.root, text="Tarif Türü (Ana Yemek/Tatlı/Atıştırmalık/Vegan):", font=("Arial", 12), bg="#f9f9f9").pack(pady=5)
        self.tur_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.tur_entry.pack(pady=5)

        tk.Button(self.root, text="Tarif Ekle", command=self.tarif_ekle, bg="#28a745", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
        self.tarif_listesi = scrolledtext.ScrolledText(self.root, width=58, height=15, state='disabled', font=("Arial", 12), bg="#ffffff", fg="#000000")
        self.tarif_listesi.pack(pady=10)

        tk.Button(self.root, text="Tarifleri Göster", command=self.tarifleri_goster, bg="#007bff", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

    def tarif_ekle(self):
        ad = self.ad_entry.get()
        malzemeler = self.malzemeler_entry.get()
        yapilis = self.yapilis_entry.get()
        pisirme_suresi = self.pisirme_entry.get()
        tur = self.tur_entry.get().strip().lower()

        if not all([ad, malzemeler, yapilis, pisirme_suresi, tur]):
            messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
            return

        malzemeler_listesi = malzemeler.split(',')
        
        if tur == "ana yemek":
            tarif = AnaYemekTarif(ad, malzemeler_listesi, yapilis, pisirme_suresi)
        elif tur == "tatlı":
            tarif = TatliTarif(ad, malzemeler_listesi, yapilis, pisirme_suresi)
        elif tur == "atıştırmalık":
            tarif = Atistirmalik(ad, malzemeler_listesi, yapilis, pisirme_suresi)
        elif tur == "vegan":
            tarif = VeganTarif(ad, malzemeler_listesi, yapilis, pisirme_suresi)
        else:
            messagebox.showwarning("Geçersiz Tür", "Geçersiz tarif türü, lütfen 'Ana Yemek', 'Tatlı', 'Atıştırmalık' veya 'Vegan' girin.")
            return

        self.yonetim.tarif_ekle(tarif)
        messagebox.showinfo("Başarılı", "Tarif başarıyla eklendi!")
        self.ad_entry.delete(0, tk.END)
        self.malzemeler_entry.delete(0, tk.END)
        self.yapilis_entry.delete(0, tk.END)
        self.pisirme_entry.delete(0, tk.END)
        self.tur_entry.delete(0, tk.END)
        self.tarifleri_goster()

    def tarifleri_goster(self):
        self.tarif_listesi.configure(state='normal')
        self.tarif_listesi.delete(1.0, tk.END)
        tarifler = self.yonetim.tarif_listele()
        
        if not tarifler:
            self.tarif_listesi.insert(tk.END, "Hiç tarif eklenmemiş.\n")
        else:
            for tarif in tarifler:
                self.tarif_listesi.insert(tk.END, tarif)
        
        self.tarif_listesi.configure(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = Uygulama(root)
    root.mainloop()