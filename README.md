MUHAMMAD ISKANDAR DANIAL BIN ALI (VC25045)
MUHAMMAD ZAKI BIN ZULKIFLY (VC25046)
AKBARUDDIN BIN AHMAD @ MOHD DIN (VC25037)

**PYTHON**
## DOWNLOAD PROMPT IN COMMAND PYTHON
* PIP INSTALL Tkinter      Builds the Graphical **User Interface (GUI)** of the application
* PIP INSTALL tkcalendar   Provides a **calendar** widget for date selection
* PIP INSTALL matplotlib   Generates **charts and graphs** for expense analysis
* PIP INSTALL reportlab    Creates and exports reports in **PDF format**
* PIP INSTALL openpyxl     Creates, edits, and manages **Excel reports** (.xlsx)

## PENERANGAN BAHASA MALAYSIA MULA BARIS **174**

# =======================================================**ENGLISH**==============================================================

# PERSONAL EXPENSE MANAGEMENT SYSTEM (DETAILED EXPLANATION)

The Personal Expense Management System is a desktop application developed using Python and the Tkinter library as the graphical user interface (GUI). The main purpose of this system is to help users record, manage, and analyze their daily expenses in a more organized and systematic manner.

## 1. LOGIN AND REGISTRATION SYSTEM

When the application starts, users are presented with a login page. Users must have an account before accessing the system. If they do not have an account, they can create one through the **“Create New Account”** feature.

During registration, users are required to enter a username and password. The system performs the following validations:

* Username **must not exceed 15 characters**.
* Password must contain numbers only and be a **maximum of 6 digits**.
* Username must be unique and cannot be duplicated.

All user information is stored in a **users.csv** file. After a successful login, the system sets the user as the **logged_user** and opens the main dashboard. Each user has a separate CSV file to store their expense records.

## 2. MAIN DASHBOARD

After logging in, users are directed to the main dashboard, which is divided into two primary sections: the left panel and the right panel.

## 3. LEFT PANEL (DATA INPUT & FINANCIAL STATUS)

The left panel is used for entering expense information and viewing financial status.

Users are required to enter:

* Monthly salary
* Expense category (e.g., Food, Transport, Bills, Shopping)
* Date using a calendar widget
* Expense amount (RM and cents)
* Expense description or notes

After entering the information, users can click the **ADD** button to save the record.

Additional features include:

* **UNDO** button to revert the most recent action.
* **CLEAR** button to delete all expense records.
* Financial status display showing conditions such as:

  * **HEALTHY**
  * **HIGH SPENDING**
  * **OVERSPENDING**

The status is determined by comparing the user's salary with the total expenses.

## 4. RIGHT PANEL (TABLE & ANALYSIS)

The right panel displays all expense records in a table using the Tkinter Treeview widget.

The table contains:

* Date
* Day
* Category
* Amount
* Description

All records are automatically sorted by date to make it easier for users to review their spending history chronologically.

## 5. SEARCH AND FILTER FUNCTION

The system provides search and filtering features that allow users to find records based on:

* Keywords
* Categories
* Date (optional calendar filter)

Users can also click the **VIEW ALL** button to display all records without any filtering.

## 6. TOTAL EXPENSE CALCULATION

The system automatically calculates the total amount of expenses based on all records stored in the table.

The total is displayed below the table as:

**Total Spending**

In addition, the system calculates the user's remaining balance using the following formula:

**Balance = Monthly Salary – Total Expenses**

Based on the balance value, the system determines the user's financial status.

## 7. GRAPHICAL ANALYSIS (CHART)

The system provides graphical analysis using the Matplotlib library.

Expense data is displayed in the form of a **pie chart**, showing the percentage distribution of expenses across categories such as:

* Food
* Transport
* Bills
* Shopping
* Others

This visualization helps users understand their spending patterns more effectively.

## 8. PDF REPORT GENERATION

The system can generate reports in **PDF format** using the ReportLab library.

The report includes:

* Report title
* Username
* Report generation date
* Expense table
* Total spending summary

If the report contains a large amount of data, the system automatically creates additional pages.

## 9. EXCEL REPORT GENERATION

Besides PDF reports, the system can generate **Excel reports** using the OpenPyXL library.

The Excel report contains:

* Report title
* Table headers
* Expense records
* Alternating row formatting
* Total Spending summary

The generated file is saved as:

**username_report.xlsx**

## 10. ADDITIONAL FEATURES

The system also includes several additional functions:

* **Undo** to restore previous data.
* **Delete** to remove selected records.
* **Clear** to delete all records.
* **Auto Save** to CSV files.
* **Temporary Backup** before any modifications are made.

These features improve data security and user convenience.

## 11. DATA STORAGE STRUCTURE

All expense records are stored in CSV format with the following structure:

* Username
* Date
* Day
* Category
* Amount
* Description

Each user has a separate data file to ensure that records remain private and do not mix with other users' data.

## 12. CONCLUSION

In conclusion, the Personal Expense Management System provides an efficient and user-friendly solution for managing daily finances. The system not only stores expense records but also offers data analysis, graphical visualization, and report generation features. These functions help users monitor their financial activities, identify spending patterns, and make better financial decisions in a more organized and systematic way.

# ===================================================**BAHASA MALAYSIA**==========================================================

# SISTEM PENGURUSAN PERBELANJAAN PERIBADI (PENJELASAN DETAIL)

Sistem ini ialah aplikasi desktop yang dibangunkan menggunakan Python dengan pustaka Tkinter sebagai antaramuka pengguna. Tujuan utama sistem ini adalah untuk membantu pengguna merekod, mengurus dan menganalisis perbelanjaan harian mereka secara lebih teratur dan sistematik.

## 1. SISTEM LOGIN DAN REGISTER

Apabila aplikasi dimulakan, pengguna akan melihat halaman login. Pengguna perlu mempunyai akaun untuk memasuki sistem. Jika belum mempunyai akaun, pengguna boleh mendaftar melalui fungsi **“Create New Account”**.

Semasa pendaftaran, pengguna perlu memasukkan username dan password. Sistem akan menyemak:

* Username **tidak boleh melebihi 15 aksara**
* Password mesti terdiri daripada nombor sahaja dan **maksimum 6 digit**
* Username tidak boleh sama dengan pengguna lain

Semua maklumat pengguna akan disimpan dalam fail **users.csv**. Selepas berjaya log masuk, sistem akan menetapkan pengguna sebagai **logged_user** dan membuka dashboard utama. Setiap pengguna akan mempunyai fail CSV sendiri untuk menyimpan data perbelanjaan.

## 2. DASHBOARD UTAMA

Selepas log masuk, pengguna akan masuk ke dashboard utama yang mengandungi dua bahagian utama iaitu panel kiri dan panel kanan.

## 3. PANEL KIRI (INPUT DATA & STATUS)

Panel kiri digunakan untuk memasukkan data perbelanjaan dan melihat status kewangan.

Pengguna perlu memasukkan:

* Gaji bulanan (salary)
* Kategori perbelanjaan (contoh: Food, Transport, Bills, Shopping)
* Tarikh menggunakan calendar
* Jumlah perbelanjaan (RM dan sen)
* Penerangan atau nota perbelanjaan

Selepas data dimasukkan, pengguna boleh menekan butang **ADD** untuk menyimpan data ke dalam sistem.

Selain itu, terdapat juga:

* Butang **UNDO** untuk membatalkan tindakan terakhir
* Butang **CLEAR** untuk memadam semua data
* Paparan status kewangan yang menunjukkan keadaan kewangan pengguna seperti **“HEALTHY”**, **“HIGH SPENDING”** atau **“OVERSPENDING”** berdasarkan perbandingan gaji dan jumlah perbelanjaan

## 4. PANEL KANAN (JADUAL & ANALISIS)

Panel kanan memaparkan semua data perbelanjaan dalam bentuk jadual (Treeview). Jadual ini mengandungi:

* Tarikh
* Hari
* Kategori
* Jumlah
* Penerangan

Data akan disusun mengikut tarikh secara automatik untuk memudahkan pengguna melihat urutan perbelanjaan.

## 5. FUNGSI CARIAN DAN FILTER

Sistem menyediakan fungsi carian untuk menapis data berdasarkan:

* Kata kunci (keyword)
* Kategori
* Tarikh (optional filter menggunakan calendar)

Pengguna juga boleh menekan butang **“VIEW ALL”** untuk memaparkan semua data semula tanpa penapis.

## 6. PENGIRAAN JUMLAH PERBELANJAAN

Sistem akan mengira jumlah keseluruhan perbelanjaan secara automatik berdasarkan semua data dalam jadual. Jumlah ini akan dipaparkan di bawah jadual sebagai **“Total Spending”**.

Selain itu, sistem juga mengira baki kewangan pengguna dengan formula:

**Baki = Gaji bulanan - Jumlah perbelanjaan**

Berdasarkan nilai ini, sistem akan menentukan status kewangan pengguna.

## 7. ANALISIS GRAF (CHART)

Sistem juga menyediakan fungsi grafik menggunakan matplotlib. Data perbelanjaan akan dipaparkan dalam bentuk **pie chart** untuk menunjukkan peratusan perbelanjaan mengikut kategori seperti Food, Transport, Bills dan lain-lain.

## 8. GENERATE LAPORAN PDF

Sistem boleh menghasilkan laporan dalam bentuk **PDF** menggunakan ReportLab. Laporan ini mengandungi:

* Tajuk laporan
* Nama pengguna
* Tarikh penjanaan laporan
* Jadual perbelanjaan
* Jumlah keseluruhan perbelanjaan

Jika data terlalu banyak, sistem akan automatik membuat halaman baru.

## 9. GENERATE LAPORAN EXCEL

Selain PDF, sistem juga boleh menjana laporan **Excel** menggunakan openpyxl. Fail Excel ini mengandungi:

* Tajuk laporan 
* Header jadual
* Data perbelanjaan
* Format selang-seli 
* Jumlah keseluruhan (TOTAL SPENDING)

Fail ini disimpan sebagai:
**username_report.xlsx**

## 10. FUNGSI TAMBAHAN

Sistem juga menyediakan beberapa fungsi tambahan seperti:

* **Undo** untuk kembali ke data sebelumnya
* **Delete** untuk memadam data terpilih
* **Clear** untuk memadam semua data
* **Auto save** ke dalam CSV
* **Backup data** sementara sebelum perubahan dibuat

## 11. STRUKTUR PENYIMPANAN DATA

Semua data disimpan dalam format CSV dengan struktur berikut:

* Username
* Tarikh
* Hari
* Kategori
* Jumlah
* Penerangan

Setiap pengguna mempunyai fail berasingan untuk memastikan data tidak bercampur.

## 12. KESIMPULAN

Secara keseluruhan, sistem ini membantu pengguna mengurus kewangan harian dengan lebih mudah, tersusun dan sistematik. Ia bukan sahaja menyimpan data perbelanjaan, tetapi juga menyediakan analisis, laporan dan visualisasi data untuk membantu pengguna memahami corak perbelanjaan mereka.