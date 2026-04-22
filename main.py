İŞ: Mevcut projeye basit bir gelir-gider takip (muhasebe) modülü eklenmesi.

```python
# accounting_module.py

import datetime

class AccountManager:
    def __init__(self):
        self.transactions = []
        self._next_id = 1

    def add_transaction(self, type, amount, description, category="Genel"):
        """
        Yeni bir gelir veya gider işlemi ekler.
        type: 'gelir' veya 'gider'
        amount: İşlem miktarı (float)
        description: İşlemin açıklaması (str)
        category: İşlemin kategorisi (str, varsayılan 'Genel')
        """
        if type not in ['gelir', 'gider']:
            print("Hata: İşlem tipi 'gelir' veya 'gider' olmalıdır.")
            return

        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Hata: Miktar pozitif bir sayı olmalıdır.")
            return

        transaction = {
            'id': self._next_id,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': type,
            'amount': float(amount),
            'description': description,
            'category': category
        }
        self.transactions.append(transaction)
        self._next_id += 1
        print(f"İşlem eklendi: ID {transaction['id']}")

    def get_transactions(self, category=None):
        """
        Tüm işlemleri veya belirli bir kategoriye ait işlemleri döndürür.
        """
        if not self.transactions:
            return []
        
        if category:
            return [t for t in self.transactions if t['category'].lower() == category.lower()]
        return self.transactions

    def get_summary(self):
        """
        Toplam gelir, toplam gider ve net bakiyeyi hesaplar.
        """
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'gelir')
        total_expense = sum(t['amount'] for t in self.transactions if t['type'] == 'gider')
        net_balance = total_income - total_expense
        return {
            'total_income': total_income,
            'total_expense': total_expense,
            'net_balance': net_balance
        }

    def display_transactions(self, transactions_list=None):
        """
        İşlemleri düzenli bir şekilde ekrana basar.
        """
        if transactions_list is None:
            transactions_list = self.transactions

        if not transactions_list:
            print("Henüz hiç işlem yok.")
            return

        print("\n--- İşlemler ---")
        for t in transactions_list:
            print(f"ID: {t['id']} | Tarih: {t['date']} | Tip: {t['type'].upper()} | Miktar: {t['amount']:.2f} TL | Açıklama: {t['description']} | Kategori: {t['category']}")
        print("-----------------\n")

def run_accounting_cli():
    """
    Muhasebe modülü için basit bir komut satırı arayüzü başlatır.
    """
    manager = AccountManager()
    print("Doffa AI Muhasebe Modülüne Hoş Geldiniz!")

    while True:
        print("\n--- Menü ---")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. İşlemleri Görüntüle")
        print("4. Kategoriye Göre İşlemleri Görüntüle")
        print("5. Özet Görüntüle")
        print("6. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == '1' or choice == '2':
            trans_type = 'gelir' if choice == '1' else 'gider'
            try:
                amount = float(input(f"{trans_type.capitalize()} miktarı girin: "))
                description = input(f"{trans_type.capitalize()} açıklaması girin: ")
                category = input(f"{trans_type.capitalize()} kategorisi girin (Varsayılan: Genel): ") or "Genel"
                manager.add_transaction(trans_type, amount, description, category)
            except ValueError:
                print("Hata: Miktar geçerli bir sayı olmalıdır.")
        elif choice == '3':
            manager.display_transactions()
        elif choice == '4':
            category_filter = input("Hangi kategoriye ait işlemleri görmek istersiniz? ")
            filtered_transactions = manager.get_transactions(category=category_filter)
            manager.display_transactions(filtered_transactions)
        elif choice == '5':
            summary = manager.get_summary()
            print("\n--- Muhasebe Özeti ---")
            print(f"Toplam Gelir: {summary['total_income']:.2f} TL")
            print(f"Toplam Gider: {summary['total_expense']:.2f} TL")
            print(f"Net Bakiye: {summary['net_balance']:.2f} TL")
            print("-----------------------\n")
        elif choice == '6':
            print("Muhasebe modülünden çıkılıyor. Güle güle!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    run_accounting_cli()

```
```markdown
# Muhasebe Modülü

Bu modül, projenize basit bir gelir ve gider takip sistemi eklemek için tasarlanmıştır. Kullanıcıların finansal işlemlerini kaydetmelerine, görüntülemelerine ve genel bir özet almalarına olanak tanır.

## Özellikler

*   **Gelir ve Gider Ekleme**: Tarih, miktar, açıklama ve kategori ile yeni işlemler kaydedin.
*   **İşlemleri Görüntüleme**: Kaydedilen tüm işlemleri listeleyin.
*   **Kategoriye Göre Filtreleme**: Belirli bir kategoriye ait işlemleri görüntüleyin.
*   **Özet Görüntüleme**: Toplam gelir, toplam gider ve net bakiyeyi gösteren bir özet alın.
*   **Basit CLI (Komut Satırı Arayüzü)**: Modülü kolayca test etmek ve kullanmak için temel bir arayüz.

## Kurulum

Herhangi bir özel kurulum gerektirmez. `accounting_module.py` dosyasını projenize dahil etmeniz yeterlidir.

## Kullanım

### Komut Satırı Üzerinden

Modülü çalıştırmak için terminalinizde aşağıdaki komutu kullanın:

```bash
python accounting_module.py
```

Bu komut, size aşağıdaki seçenekleri sunan interaktif bir menü başlatacaktır:

1.  **Gelir Ekle**: Yeni bir gelir işlemi girmenizi sağlar.
    *   Miktar: Sayısal değer (örneğin, `1500.00`)
    *   Açıklama: Metin (örneğin, `Maaş`)
    *   Kategori: Metin (örneğin, `Çalışma`, `Varsayılan: Genel`)
2.  **Gider Ekle**: Yeni bir gider işlemi girmenizi sağlar.
    *   Miktar: Sayısal değer (örneğin, `50.75`)
    *   Açıklama: Metin (örneğin, `Market Alışverişi`)
    *   Kategori: Metin (örneğin, `Gıda`, `Varsayılan: Genel`)
3.  **İşlemleri Görüntüle**: Tüm kaydedilmiş gelir ve gider işlemlerini listeler.
4.  **Kategoriye Göre İşlemleri Görüntüle**: Belirli bir kategoriye ait işlemleri listeler.
5.  **Özet Görüntüle**: Toplam gelir, toplam gider ve net bakiyeyi gösterir.
6.  **Çıkış**: Uygulamadan çıkar.

### Kendi Projenizde Kullanım (API)

Modülü kendi Python kodunuzda bir sınıf olarak kullanabilirsiniz:

```python
from accounting_module import AccountManager

# Bir AccountManager nesnesi oluştur
my_account = AccountManager()

# Gelir ekle
my_account.add_transaction('gelir', 2500.00, 'Maaş Ödemesi', 'Çalışma')
my_account.add_transaction('gelir', 100.00, 'Ek İş Geliri', 'Yan Gelir')

# Gider ekle
my_account.add_transaction('gider', 750.50, 'Kira Ödemesi', 'Konut')
my_account.add_transaction('gider', 120.00, 'Elektrik Faturası', 'Faturalar')
my_account.add_transaction('gider', 300.00, 'Market Alışverişi', 'Gıda')

# Tüm işlemleri görüntüle
print("\nTüm İşlemler:")
my_account.display_transactions()

# Sadece 'Gıda' kategorisindeki işlemleri görüntüle
print("\nGıda Kategorisindeki İşlemler:")
food_transactions = my_account.get_transactions(category='Gıda')
my_account.display_transactions(food_transactions)

# Özeti görüntüle
summary = my_account.get_summary()
print("\nGüncel Bakiye Özeti:")
print(f"Toplam Gelir: {summary['total_income']:.2f} TL")
print(f"Toplam Gider: {summary['total_expense']:.2f} TL")
print(f"Net Bakiye: {summary['net_balance']:.2f} TL")
```

## Geliştirme Notları

*   **Veri Kalıcılığı**: Şu anki sürümde veriler yalnızca uygulama çalıştığı sürece bellekte tutulur. Verileri kalıcı hale getirmek için bir veritabanı (SQLite, PostgreSQL vb.) veya JSON/CSV dosyaları kullanılabilir.
*   **Gelişmiş Raporlama**: Belirli tarih aralıklarına göre raporlama, grafikler veya detaylı kategori analizleri eklenebilir.
*   **Kullanıcı Arayüzü**: Daha gelişmiş bir kullanıcı deneyimi için bir web (Flask, Django) veya masaüstü (PyQt, Kivy) arayüzü entegre edilebilir.
*   **Hata Yönetimi**: Daha sağlam bir hata yönetimi ve giriş doğrulama mekanizmaları eklenebilir.
*   **İşlem Silme/Güncelleme**: Mevcut işlemleri silme veya düzenleme yeteneği eklenebilir.
```