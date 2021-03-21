#!/usr/bin/python

def dhtUpload():
    
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    #gauth.LoadCredentialsFile("mycreds.txt")
    #gauth.SaveCredentialsFile("mycreds.txt")
    
    drive = GoogleDrive(gauth)
    
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    
    for files in file_list:
        #print('title: %s, id: %s' % (files['title'],files['id']))
        if files['title'] == 'dhtdata.xlsx':
            files.Delete()
            #file1 = drive.CreateFile({'id': '15fsKHU7-8NhE4b9_MNVoLDny__pgI3RC'})
            #file1.Trash()
            #print(file1)
    file2 = drive.CreateFile({'title': 'dhtdata.xlsx'})
    file2.SetContentFile('dhtdata.xlsx')
    file2.Upload()
    '''
    file0 = drive.CreateFile()
    file0.GetContentFile('dhtdata.xlsx')
    file0.Trash()
    '''
    '''
    fileold = drive.CreateFile({'title': 'dhtdata.xlsx'})
    fileold.Delete()
    '''
    '''
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    try:
            for fileold in file_list:
                    if fileold['title'] == 'dhtdata.xlsx':
                        fileold.Delete()
                        f = drive.CreateFile()
                        f.SetContentFile("dhtdata.xlsx")
                        f.Upload()
                    else:
                        f = drive.CreateFile()
                        f.SetContentFile("dhtdata.xlsx")
                        f.Upload()
    except:
        pass
        
'''
    