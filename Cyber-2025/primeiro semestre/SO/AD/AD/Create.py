# Lendo a lista de usuários do arquivo
$usuarios = Get-Content "C:\Users\Relatorios\listausuarios.txt"

# Criando usuários
foreach ($linha in $usuarios) {
    $dados = $linha -split ";"
    $username = $dados[0]
    $group = $dados[1]
    
    # Criando senha
    $password = ConvertTo-SecureString "SenhaSegura123" -AsPlainText -Force
    
    # Criando usuário no Active Directory
    if (-not (Get-ADUser -Filter {SamAccountName -eq $username})) {
        New-ADUser -SamAccountName $username `
            -UserPrincipalName "$username@exemplo.local" `
            -Name $username `
            -GivenName ($username -split "_")[0] `
            -Surname ($username -split "_")[1] `
            -Path "OU=Usuarios,DC=exemplo,DC=local" `
            -AccountPassword $password `
            -Enabled $true `
            -ChangePasswordAtLogon $true
        Write-Host "Usuário $username criado com sucesso."
    } else {
        Write-Host "Usuário $username já existe."
    }
}

# Criando grupos
$grupos = $usuarios | ForEach-Object { ($_ -split ";")[1] } | Select-Object -Unique
foreach ($grupo in $grupos) {
    if (-not (Get-ADGroup -Filter {Name -eq $grupo})) {
        New-ADGroup -Name $grupo -GroupScope Global -Path "OU=Grupos,DC=exemplo,DC=local"
        Write-Host "Grupo $grupo criado com sucesso."
    } else {
        Write-Host "Grupo $grupo já existe."
    }
}

# Adicionando usuários aos grupos
foreach ($linha in $usuarios) {
    $dados = $linha -split ";"
    $username = $dados[0]
    $group = $dados[1]
    
    if (-not (Get-ADGroupMember -Identity $group | Where-Object { $_.SamAccountName -eq $username })) {
        Add-ADGroupMember -Identity $group -Members $username
        Write-Host "Usuário $username adicionado ao grupo $group."
    } else {
        Write-Host "Usuário $username já está no grupo $group."
    }
}