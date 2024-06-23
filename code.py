import ftplib
 
ftp_server = ftplib.FTP("ftp.nasdaqtrader.com")
ftp_server.login()
ftp_server.encoding = "utf-8"
 
filenames = ["nasdaqlisted.txt", "otherlisted.txt"]
 
ftp_server.cwd('Symboldirectory')
ftp_server.dir()

for filename in filenames:
    with open(filename, "wb") as file:
        ftp_server.retrbinary(f"RETR {filename}", file.write)
 
ftp_server.quit()
