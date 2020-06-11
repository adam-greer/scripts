# Define the log location and search constraints
$path = '<log location>'
$uploadFailed = 'Upload failed:'
$searchError = 'SEARCH ERROR'
$catchall = 'fail'


# Search the log file
if (Select-String -path $path -pattern $uploadFailed){
Send-MailMessage -To self@domain.com -Subject "KnowBe4 ADSI Errors!" -from email@domain.com -SMTPServer smtp@domain.com -body 'Error were detected in the KnowBe4 log file. This needs to be corrected ASAP. Once this error has been corrected, please delete the log file and restart the service.' -Priority High
}

