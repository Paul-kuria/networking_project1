@REM backkup current path 
$env:Path | Out-File -FilePath "$env:USERPROFILE\path_backup.txt"

@REM Remove item from path
Remove-Item "$env:LOCALAPPDATA\Programs\Python\Python310\Scripts\pdm.exe" -ErrorAction SilentlyContinue
Remove-Item "$env:APPDATA\Python\Scripts\pdm.exe" -ErrorAction SilentlyContinue