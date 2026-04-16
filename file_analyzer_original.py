import os
import datetime


class FileAnalyzer:
    """
    Class untuk menganalisis properti dasar dari sebuah file.
    """

    def __init__(self, file_path):
        """
        Constructor yang menerima path file dan memeriksa keberadaannya.
        """
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.__file_ada = os.path.exists(file_path)
        self.__file_size_bytes = 0

        if self.__file_ada:
            # Mengambil ukuran file (dalam bytes) dan menyimpannya di atribut privat
            self.__file_size_bytes = os.path.getsize(file_path)
        else:
            print(f"ERROR: File '{file_path}' tidak ditemukan.")
            self.__file_ada = False

    def get_file_size(self, unit="bytes"):
        """
        Mengembalikan ukuran file. Dapat dikonversi ke Kilobytes (KB).
        """
        if not self.__file_ada:
            return 0

        if unit.lower() == "kb":
            # Konversi dari bytes ke KB (1 KB = 1024 Bytes)
            size_kb = self.__file_size_bytes / 1024
            return size_kb
        else:
            # Default mengembalikan dalam bytes
            return self.__file_size_bytes

    def get_modification_time(self):
        """
        Mengembalikan waktu modifikasi terakhir file dalam format yang dapat dibaca.
        """
        if not self.__file_ada:
            return "N/A"

        # 1. Dapatkan timestamp (detik sejak epoch)
        timestamp = os.path.getmtime(self.file_path)

        # 2. Konversi timestamp ke objek datetime
        dt_object = datetime.datetime.fromtimestamp(timestamp)

        # 3. Format ke string yang mudah dibaca
        formatted_time = dt_object.strftime("%d-%m-%Y %H:%M:%S")
        return formatted_time

    def analyze(self):
        """
        Method utama untuk menganalisis dan mencetak laporan file.
        """
        print("\n" + "="*40)
        print(f"Laporan Analisis File: {self.file_name}")
        print("="*40)

        if self.__file_ada:
            # Mendapatkan data analisis
            size_kb = self.get_file_size(unit="KB")
            mod_time = self.get_modification_time()

            print(f"Nama File      : {self.file_name}")
            print(f"Path File      : {self.file_path}")
            print(f"Status File    : ADA")
            print(f"Ukuran File    : {size_kb:.2f} KB ({self.__file_size_bytes} Bytes)")
            print(f"Waktu Modifikasi: {mod_time}")
        else:
            print(f"File '{self.file_path}' tidak dapat dianalisis karena tidak ditemukan.")
            print("Status File    : TIDAK ADA")

        print("="*40)


if __name__ == "__main__":
    # 4.a & 4.b: Membuat objek untuk file yang ada ("dokumen.txt")
    print("--- Analisis Kasus 1: File ADA ---")
    file_analyser_1 = FileAnalyzer("dokumen.txt")
    file_analyser_1.analyze()

    # 4.c (Opsional): Membuat objek kedua untuk file yang tidak ada
    print("\n--- Analisis Kasus 2: File TIDAK ADA (Uji Error Handling) ---")
    file_analyser_2 = FileAnalyzer("file_khayalan.txt")
    file_analyser_2.analyze()
