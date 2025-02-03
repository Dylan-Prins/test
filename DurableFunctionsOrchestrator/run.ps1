param($Context)

$output = @()

Connect-AzAccount -Identity | Out-Null

$output += Invoke-DurableActivity -FunctionName 'Hello' -Input 'Tokyo'
$output += Invoke-DurableActivity -FunctionName 'Hello' -Input 'Seattle'
$output += Invoke-DurableActivity -FunctionName 'Hello' -Input 'London'

$output
