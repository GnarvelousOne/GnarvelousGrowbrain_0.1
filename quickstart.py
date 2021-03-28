#!/usr/bin/python

def dhtUpload():
    
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import os
    
    gauth = GoogleAuth()
    #gauth.CommandLineAuth()
    gauth.LoadCredentialsFile("mycreds.txt")
    gauth.SaveCredentialsFile("mycreds.txt")
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    
    folderName = "dhtdata"
    file_name = "dhtdata.xlsx"
    file_list = drive.ListFile({'q':"'1kL3pkVo30oNpywCL2CzXyJsdAyvblpdj'  in parents and  trashed=False"}).GetList()

    for x in range(len(file_list)):
        if file_list[x]['title'] == file_name:
            file_id = file_list[x]['id']

    file1 = drive.CreateFile({'id':file_id})
    file1.SetContentFile(file_name)
    file1.Upload()

    
    #file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    #file_list = drive.ListFile({'q': "'parents': [{'id': folder['id']}] and trashed=false"}).GetList()
    
    '''
    folders = drive.ListFile({'q': "title='" + folderName +
                              "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for file in folders:
        #print(file)
        if file['title'] == 'dhtdata.xlsx':
            file.Trash()
    '''
    '''
    
    for files in file_list:
        #print('title: %s, id: %s' % (files['title'],files['id']))
        if files['title'] == 'dhtdata.xlsx':
            files.Delete()
    '''
    '''
    folders = drive.ListFile({'q': "title='" + folderName +
                              "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile({'title': 'dhtdata.xlsx', 'parents': [{'id': folder['id']}]})
            file2.SetContentFile('dhtdata.xlsx')
            file2.Upload()
    '''
    os.system("pkill chromium")