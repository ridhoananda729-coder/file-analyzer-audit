"""
File Analyzer Module
Modul ini menyediakan fungsionalitas untuk menganalisis properti dasar sebuah file,
termasuk ukuran dan waktu modifikasi terakhir.
"""

import os
import datetime

BYTES_PER_KB = 1024
DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"
SEPARATOR_WIDTH = 40


class FileNotFoundError(Exception):
    """Exception khusus untuk menangani kasus file tidak ditemukan."""
    pass


class FileAnalyzer:
    """Menganalisis properti dasar dari sebuah file di sistem."""

    def __init__(self, file_path: str):
        """
        Inisialisasi FileAnalyzer dengan path file yang diberikan.

        Args:
            file_path: Path lengkap atau relatif ke file yang akan dianalisis.

        Raises:
            FileNotFoundError: Jika file tidak ditemukan di path yang diberikan.
        """
        self._file_path = file_path
        self._file_name = os.path.basename(file_path)
        self._validate_file_exists()
        self._file_size_bytes = os.path.getsize(file_path)

    def _validate_file_exists(self):
        """Memvalidasi keberadaan file; raise exception jika tidak ada."""
        if not os.path.exists(self._file_path):
            raise FileNotFoundError(
                f"File '{self._file_path}' tidak ditemukan."
            )

    def get_file_size(self, unit: str = "bytes") -> float:
        """
        Mengembalikan ukuran file dalam satuan yang diminta.

        Args:
            unit: Satuan ukuran — 'bytes' (default) atau 'kb'.

        Returns:
            Ukuran file sebagai float dalam satuan yang dipilih.
        """
        if unit.lower() == "kb":
            return self._file_size_bytes / BYTES_PER_KB
        return float(self._file_size_bytes)

    def get_modification_time(self) -> str:
        """
        Mengembalikan waktu modifikasi terakhir file sebagai string terformat.

        Returns:
            String waktu dalam format 'DD-MM-YYYY HH:MM:SS'.
        """
        timestamp = os.path.getmtime(self._file_path)
        modification_datetime = datetime.datetime.fromtimestamp(timestamp)
        return modification_datetime.strftime(DATETIME_FORMAT)

    def print_report(self):
        """Mencetak laporan analisis file ke konsol."""
        separator = "=" * SEPARATOR_WIDTH
        size_kb = self.get_file_size(unit="kb")
        modification_time = self.get_modification_time()

        print(f"\n{separator}")
        print(f"Laporan Analisis File: {self._file_name}")
        print(separator)
        print(f"Nama File        : {self._file_name}")
        print(f"Path File        : {self._file_path}")
        print(f"Ukuran File      : {size_kb:.2f} KB ({self._file_size_bytes} Bytes)")
        print(f"Waktu Modifikasi : {modification_time}")
        print(separator)


def analyze_file(file_path: str):
    """
    Fungsi helper untuk menganalisis satu file dengan penanganan error.

    Args:
        file_path: Path ke file yang akan dianalisis.
    """
    try:
        analyzer = FileAnalyzer(file_path)
        analyzer.print_report()
    except FileNotFoundError as e:
        print(f"\n[ERROR] {e}")
        print(f"Status File '{file_path}': TIDAK ADA")


if __name__ == "__main__":
    print("--- Analisis Kasus 1: File ADA ---")
    analyze_file("dokumen.txt")

    print("\n--- Analisis Kasus 2: File TIDAK ADA (Uji Error Handling) ---")
    analyze_file("file_khayalan.txt")
