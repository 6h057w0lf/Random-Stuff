# Title:  reboot_check.ps1
# Author: 6h057W0lf
# Date:   July 27, 2020
# modified: July 27, 2020
<# This script checks windows registory for any pending reboots that might be needed for a server. You can run it and if there a reboot need it will reboot the computer to.
* allowing updates or other servers to complet.
#>

#Pending reboot check param
Set-ExecutionPolicy Bypass -Scope Process -Force
$date = Get-Date -format G
$pendingRebootTests = @(
    @{
        Name = 'RebootPending'
        Test = { Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing'  Name 'RebootPending' -ErrorAction Ignore }
        TestType = 'ValueExists'
    }
    @{
        Name = 'RebootRequired'
        Test = { Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update'  Name 'RebootRequired' -ErrorAction Ignore }
        TestType = 'ValueExists'
    }
    @{
        Name = 'PendingFileRenameOperations'
        Test = { Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager' -Name 'PendingFileRenameOperations' -ErrorAction Ignore }
        TestType = 'NonNullValue'
    }
)

# Logging function. 
$logpath = "c:\pending_reboot.log"
function Write-Log {
    param($msg)
    "$date : $msg" | Out-file -FilePath $logpath -Append -Force
    Write-Output "$date : $msg"
}
Write-Log "***** Starting Log. *****"

#Checking if computer pending reboot.
Write-Log "***** Checking for pending reboot. *****"
function check_reboot {
    foreach ($test in $pendingRebootTests) {
        $result = Invoke-Command -ScriptBlock $test.Test
        if ($test.TestType -eq 'ValueExists' -and $result) {
            Write-Log "A reboot is Pending/Required. We will be rebooting the computer now."
            Restart-Computer -ComputerName localhost
        } elseif ($test.TestType -eq 'NonNullValue' -and $result -and $result.($test.Name)) {
            Write-Log "The computer has a Pending File Rename Operations. We will be rebooting the computer now."
            Restart-Computer -ComputerName localhost
        } else {
            Write-Log "No reboot Pending/Required at this time."
        }
    }
}
check_reboot
Write-Log "***** completed Checking for pending reboot. *****"