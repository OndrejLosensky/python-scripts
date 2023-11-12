
  # **EXTRACT EMAILS TO EXCEL** #
  
  This is simple Python projects, that will access your gmail and then it will read all emails, check then as SEEN and then i creates an Excel file. 
  In this file the script will create table with content of your e-mail. There will be BODY, SUBJECT, FROM, TO, DATE, Unique ID and NUMBER. Then it saves to
  the given PATH. IF you want to use this program for your usage, you can. Additionally I recommend you to set the script to run automatically for example every week
  you can achieve this by using 'filename.sh' file on Linux-based OS, or via 'filename.bat' on Windows. REMEMBER YOU NEED TO HAVE INSTALLED ALL THE LIBRARIES THAT IT USES!!

  Also if you want to just read emails automatically, just use my second script, which is in other repo thats PINned on my profile 📌
<h2> Patch notes: </h2>
<div>
<h3> 1.1.0 </h3>
  <p> I switched from library called OPENPYXL to XLSXWRITER as the old one wasn't able to process IllegalCharacters ** \x07 ** or other </p>
<h2> </h2>
 <p></p> 
<p></p>

</div>

<h2 align="left"> How to install: </h2>
<div>
    You will need all those libraries:

```bash
  pip install xlsxwriter
  pip install imaplib
  pip install email
  pip install time
  pip install yaml
  pip install random
```

  Then you need to have folder thats called **Excel_folder**

  also you need to insert your email adress and Google app password to the **login.yaml**
  
  *if you dont know to to do it, find some tutorial on how to authorize access to Google account*
</div>
    
  <h2 align="left"> Preview: </h2>
  This is what the code looks like when you run the program
  <div>
    <img width="342" alt="preview1" src="https://github.com/OndrejLosensky/extract-emails/assets/127244546/1e33a99e-a033-4875-83c4-56e4b58a53e3">
  </div>
  If its successfull then at the end it should print: 'SCRIPT PROCESS FINISHED'
  <div>
    
  </div>
  
  <p align="left">  </p> 
  <h3 align="left"> Author</h3>
  <p align="left"> OndrejLosensky </p>
  <h3 align="left"> Version </h3>
  <p align="left"> 1.0.0  </p>
  <h3 align="left">License </h3>
  <p align="left"> Open Software License 3.0 </p>

  <h3 align="left">How can you contact me? </h3>
  <p align="left"> you can contact me on my email: losenskyondrej@gmail.com </p>
<h3 align="left"> Languages and tools i used: </h3>
 <div align="left">
    <img alt="test" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
    <img width="16"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" alt="git logo"  />
   <img width="16"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />  
   <img width="16"/>
   <img src="https://github.com/OndrejLosensky/extract-emails/assets/127244546/86f50d07-63d3-4f53-9c37-7f83fc2bef87" width="40" />
   <img width="16" />
   <img src="https://github.com/OndrejLosensky/extract-emails/assets/127244546/339f4e92-cba8-414e-ad1a-876610fdef7a" wiodth="40" height="40" />
  </div>


  <p> </p>
  <p> </p>
  <p align="center"> name of the file: Readme.md |  date of creating : 2023-10-30 </p>
  

