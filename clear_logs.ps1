$targetDate = Get-Date "2023-07-18"
$eventID = 4624  # Event ID for account creation

# Filter the events based on Event ID and date
$events = Get-WinEvent -FilterHashtable @{
    LogName='Security'
    ID=$eventID
    StartTime=$targetDate
    EndTime=$targetDate.AddDays(1)
}

#foreach ($event in $events) {
#    Write-Host "Event ID: $($event.Id)"
#    Write-Host "Time Created: $($event.TimeCreated)"
#    Write-Host "Message: $($event.Message)"
#    Write-Host "-----------------------------------"
#}

# Clear the filtered events
foreach ($event in $events) {
    $eventLog = New-Object System.Diagnostics.EventLog($log, $machineName)
    $eventLog.ClearEvent($eventId)
}	
