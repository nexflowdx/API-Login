param(
    [Parameter(Mandatory=$true)]
    [string]$Arquivo
)

(Get-Content $Arquivo -Encoding UTF8) -replace '\[DATA[^\]]*\]', (Get-Date -Format "dd/MM/yyyy HH:mm") | Set-Content $Arquivo -Encoding UTF8

Write-Host "Data atualizada em: $Arquivo"