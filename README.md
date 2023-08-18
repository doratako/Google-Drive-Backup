# Google Drive Backup <br>

## Introduction
This solution facilitates the backup of chosen files to Google Drive. The tool operates within a console-based environment, providing the user with a straightforward way to interact with it. The authentication method to interact with Google Drive API is service account  <br>

## Functionality

<b> Local Folder Selection:</b> The tool initiates by prompting the user to designate a local folder. This folder will be the source for files intended for backup.<br>

<b> Backup Options:</b> User is presented with two distinct backup choices: <br>
<ol type="a">
<li><i>Full Folder Backup:</i>The option is provided to create a backup of the entire designated folder. In this mode, any newly created files within the source folder will be automatically backed up during subsequent tool runs. Files that have already been backed up will also be updated. </li>
<li><i>Selective File Backup:</i> Alternatively, the user can select specific files for backup. Irrespective of newly created files in the source folder, only the chosen files will be considered. The tool will update the content of these selected files in subsequent runs. </li>
</ol>

<b> Google Drive Destination:</b> Upon selecting the backup mode, the user can opt for the backup destination within their Google Drive.<br>
Alternatively, the user can browse and choose from a list of all folders, including parent and child folders (if the folders are shared with the service account). 

<b> Backup Process:</b> Ensuring exception handling to address potential errors during interactions with the Google Drive API or due to incorrect user inputs.

## Use
<ul>
<li> Create your Google Drive API https://cloud.google.com/apis/docs/getting-started </li>
<li> Create Service Account to authenticate and save your key as 'service_account_key.json' </li>
<li> Choose either parent or child folder(s) where you want to back up your local files. Generally, you will need to share the folder(s) with the email address associated with the service account and grant it editing access. </li>
<li> Create a virtual environment and install Goolge API Python client library  </li>
<li> Put the python scripts into the same folder as your 'service_account_key.json' is. Run <i>create_config.py</i> and follow the instructions in the terminal, this will eventually generate a 'config.json' file. Execute <i>backup.py</i> to manage uploads and updates based on the configuration file. </li>
<li> Use Task Scheduler or cron jobs to run <i>backup.py</i> at a specific times or intervals </li>
</ul>
