#### Q&A
- Is sniffing attack a concern with all the advances in cybersecurity today?
    - e.g., cloud computing vs IoT
    - Cloud providers guarantee data security and privacy. 
    - IoT vendors focus more on performance
- What conditions would make sniffing attacks more likely to succeed?
  - e.g., a non-encryption or weak-encryption channel

> **GPT answer**: Yes, sniffing attacks remain a significant concern in cybersecurity today, despite advancements in security technologies and practices.
> 1. Persistent Vulnerability of Network Traffic:
>  - Unencrypted Communication: Many networks and services still use unencrypted communication protocols. Attackers can easily capture and read data transmitted in plain text.
>  - Legacy Systems: Older systems and devices that do not support modern encryption standards are still in use, making them vulnerable to sniffing.
> 2. Complexity of Modern Networks:
>  - IoT Devices: The proliferation of Internet of Things (IoT) devices, many of which have weak or no security, increases the attack surface for sniffing attacks.
>  - BYOD Policies: Bring Your Own Device policies in workplaces can introduce unsecured devices into a network, making it easier for attackers to gain access.
> 3. Insider Threats:
>  - Malicious Insiders: Employees or contractors with legitimate access to the network can use sniffing tools to capture sensitive data.
>  - Compromised Accounts: Attackers who gain access to user credentials can deploy sniffing tools from within the network.
> 4. Advanced Attack Techniques:
>  - Man-in-the-Middle (MITM) Attacks: Attackers can intercept and alter communication between two parties, making it difficult to detect sniffing.
>  - Wi-Fi Sniffing: Public Wi-Fi networks are particularly vulnerable to sniffing attacks. Attackers can set up rogue access points to capture traffic from unsuspecting users.
> 5. Encryption and Its Limitations:
>  - Weak Encryption: Use of weak encryption algorithms that can be easily broken.
>  - Key Management: Poor key management practices can lead to exposure of encryption keys, nullifying the benefits of encryption.
> 6. Detection and Prevention Challenges:
>  - Evasion Techniques: Modern sniffing tools can evade detection by using techniques such as packet fragmentation and encrypted payloads.
>  - Volume of Traffic: The sheer volume of network traffic in modern organizations can make it challenging to detect suspicious activities.
> 
> Mitigation Strategies:
To mitigate the risk of sniffing attacks, organizations and individuals should adopt a multi-layered security approach:
> 1. Encrypt Network Traffic: Use strong encryption protocols such as TLS/SSL for all communications, including email (SMTP, IMAP, POP3), web browsing (HTTPS), and file transfers (SFTP).
> 2. Use Secure Wi-Fi: Ensure that Wi-Fi networks are secured with WPA3 encryption and avoid using public Wi-Fi networks without a VPN.
> 3. Implement Network Segmentation: Segment the network to limit access to sensitive data and reduce the impact of a potential sniffing attack.
> 4. Monitor Network Traffic: Deploy intrusion detection and prevention systems (IDPS) to monitor network traffic for unusual patterns that may indicate a sniffing attempt.
> 5. Educate Users: Train employees and users on the importance of secure communication practices and the risks associated with using unsecured networks.
> 6. Update and Patch Systems: Regularly update and patch all systems and devices to protect against known vulnerabilities.
> 7. Use Strong Authentication: Implement multi-factor authentication (MFA) to reduce the risk of compromised credentials being used in sniffing attacks.

## Remote shell
- What is it: remotely execute shell commands on a target system over the internet. 
  - shell commands, e.g., create/edit/remove files and folders, fetch data, and launch applications

- Malicious use: remote shell can be abused by malicious users to cause system damage.
  - e.g., delete all files on the system, stealing and/or corrupting  sensitive data

- Two types:
  - Forward shell
    - The malicious client executes shell commands on the server
  - Reverse shell
    - The malicious server executes shell commands on the client
### Forward shell
- Malicious clients can exploit a weakness in their normal connection with the server to gain unauthorized access, thus executing arbitrary commands on the server. 
  - e.g., we embed a weakness within a server program for our demo
- `$`: a normal user
- `#`: a root user

#### Q&A
- In what scenarios forward shell is useful?
  - e.g., steal/delete/lock sensitive data stored in a high-value server. 
- What possible countermeasure can be used to mitigate forward shell?
  - e.g., regular security patches to software
### Reverse shell
- A malicious server lures victim clients (victims) for connection
  - e.g., we craft a vulnerability within a client program for our demo 
- A reverse shell, also known as a remote shell or “connect-back shell,” takes advantage of the target system’s vulnerabilities to initiate a shell session and then access the victim’s computer. The goal is to connect to a remote computer and redirect the input and output connections of the target system’s shell so the attacker can access it remotely.
- Reverse shells allow attackers to open ports to the target machines, forcing communication and enabling a complete takeover of the target machine. Therefore it is a severe security threat. This method is also commonly used in penetration tests.
#### Q&A
- Is reverse shell as easy as forward shell? Why?
  - No, e.g., a high-value server might enforce more strict security polices, compared to a client.
- Can mitigations for forward shell be used for reverse shell? Why?
  - Yes, e.g., regular security patches to software
- How to prevent Reverse Shell? (**Extra question**)
  - **Lock all outgoing connectivity** except for specific ports and remote IP addresses for required services. To achieve this, sandbox or run your servers in minimal containers.
  - **Set up a proxy server** with restricted destinations and tight controls. It is impossible to eliminate the risk, given that attackers can create reverse shell connections over DNS, but this hardening can minimize the risk.
  - **Remove unnecessary interpreters** and tools to restrict the execution of reverse shell code and make it harder for attackers to exploit your system. This approach is not always a viable solution, as it is only practical for highly specialized and hardened servers, while attackers can still find a shell script that works.
  - **Prevent exploits** such as code injection vulnerabilities. Attackers usually execute shell scripts by exploiting an existing code injection vulnerability, then escalating to root privileges. Regularly patch your web applications and servers and use a reliable vulnerability scanner to test them.

***Extra question**: Not mentioned in class.

# Past final exam (answered by GPT)
## Question 1.1
### 1. Skills Needed for Incident Response Team (5 points)
1. Cybersecurity Expertise:
   - Role: Identifying and mitigating threats.
   - Skills: Knowledge of malware, encryption, network security, and incident handling procedures.
2. Forensics Specialist:
   - Role: Analyzing compromised systems and tracing the origin of attacks.
   - Skills: Digital forensics, data recovery, and understanding of file systems.
3. Systems Administrator:

   - Role: Restoring and maintaining system functionality.
   - Skills: Server management, backup restoration, and system hardening.
4. Legal and Compliance Advisor:

   - Role: Ensuring compliance with legal and regulatory requirements.
   - Skills: Knowledge of data protection laws, incident reporting regulations, and experience with legal processes in cybersecurity incidents.
5. Communication Specialist:

   - Role: Managing internal and external communication.
   - Skills: Crisis communication, public relations, and stakeholder management.
### 2. Four Stages of Handling the Incident (10 points)
1. Preparation:

   - Activity 1: Establish an incident response plan and train staff.
   - Activity 2: Set up and test backup systems and disaster recovery plans.
2. Identification:

   - Activity 1: Detect and confirm the ransomware attack through system alerts and user reports.
   - Activity 2: Identify compromised systems and affected data using forensic tools.
3. Containment, Eradication, and Recovery:

   - Activity 1: Isolate infected systems from the network to prevent further spread.
   - Activity 2: Remove ransomware and restore systems from backups, ensuring all traces of the attack are eradicated.
4. Post-Incident Activity:

   - Activity 1: Conduct a post-incident review to analyze the attack vector and effectiveness of the response.
   - Activity 2: Update security policies and incident response plans based on lessons learned to prevent future incidents.
## Question 1.2
### 1. Brief Explanation of Terms (6 points)
1. Confidentiality: Ensuring that information is accessible only to those authorized to have access.
2. Integrity: Maintaining the accuracy and completeness of data over its lifecycle.
3. Availability: Ensuring that authorized users have access to information and resources when needed.
4. Authorization: The process of giving someone permission to do or have something.
5. Authentication: Verifying the identity of a user, process, or device.
6. Accountability: Ensuring that actions can be attributed to individuals or processes, typically through logging and auditing.
### 2. Impact on the Company's Systems and Data (9 points)
1. Confidentiality:

   - Impact: Compromised. The attackers exfiltrated sensitive customer data, exposing confidential information.
   - Relation: Data exfiltration means unauthorized entities now have access to private customer details.
2. Integrity:

   - Impact: Potentially compromised. While the primary concern is the encryption of data, any alterations during the attack could affect data integrity.
   - Relation: If data was altered or corrupted during the ransomware attack, the integrity of customer and financial records could be at risk.
3. Availability:

   - Impact: Severely compromised. The encryption of the disks rendered the server and its data unavailable until the ransom is paid or data is restored from backups.
   - Relation: The primary function of the server and access to its data was disrupted, affecting business operations.
4. Authorization:

   - Impact: Misused. Bob’s administrator privileges were exploited to gain unauthorized access to sensitive systems.
   - Relation: The attackers used valid credentials with elevated privileges, bypassing normal authorization controls.
5. Authentication:

   - Impact: Bypassed. The attackers used Bob’s credentials, which they obtained, to authenticate themselves and gain access.
   - Relation: Although authentication mechanisms were in place, the compromise of credentials undermined this security measure.
6. Accountability:

   - Impact: Non-existent. Lack of logging means there is no record of the attackers’ actions or when the attack occurred.
   - Relation: Without logs, it’s impossible to trace the actions back to specific users or identify the timeline of the attack, failing to hold any entity accountable for specific actions.
## Question 2.1
### Threat Actors and Vulnerabilities
1. Criminals:

   - Vulnerability: Physical theft of laptops and mobile phones.
   - Impact: Loss of sensitive data, disruption of work, and potential data breaches.
2. Cyber criminals:

   - Vulnerability: Malware infection through phishing attacks.
   - Impact: Data exfiltration, financial loss, and compromise of sensitive information.
3. Hardware failure:

   - Vulnerability: Lack of hardware maintenance and monitoring.
   - Impact: Data loss, downtime, and reduced productivity.
4. Hard surfaces:

   - Vulnerability: Physical damage from dropping devices.
   - Impact: Device malfunction, data loss, and repair costs.
5. Cups of tea:

   - Vulnerability: Liquid spills causing damage to devices.
   - Impact: Device failure, data loss, and increased maintenance costs.
## Question 2.2
### Risks and Controls
1. Criminals - Physical theft of devices

- Control: Use of physical security measures such as locks and secure storage.

  - Control Type: Physical
  - Control Function: Preventive
- Control: Employee training on securing devices when not in use.

  - Control Type: Administrative
  - Control Function: Preventive
2. Cyber criminals - Malware infection through phishing

- Control: Implementation of anti-malware software.

  - Control Type: Technical
  - Control Function: Preventive
- Control: Regular cybersecurity awareness training for employees.

  - Control Type: Administrative
  - Control Function: Preventive
- Control: Email filtering and spam detection systems.

  - Control Type: Technical
  - Control Function: Preventive
3. Hardware failure - Lack of hardware maintenance

- Control: Regular hardware maintenance schedule and checks.

  - Control Type: Administrative
  - Control Function: Preventive
- Control: Implementation of redundant systems and backup devices.

  - Control Type: Technical
  - Control Function: Corrective
4. Hard surfaces - Physical damage from dropping devices

- Control: Use of protective cases and shock-absorbing covers.

  - Control Type: Physical
  - Control Function: Preventive
- Control: Employee training on proper handling and transport of devices.

  - Control Type: Administrative
  - Control Function: Preventive
5. Cups of tea - Liquid spills causing damage

- Control: Use of spill-resistant keyboards and protective covers for devices.

  - Control Type: Physical
  - Control Function: Preventive
- Control: Implementing a policy to keep liquids away from work areas.

  - Control Type: Administrative
  - Control Function: Preventive
## Question 3.1
### Verifying the Image Authenticity (10 points)
To determine whether the image is fake, you can perform several forensic analysis techniques:

1. Metadata Analysis:

   - Activity 1: Inspect the EXIF metadata of the image. Check for details such as the date and time the photo was taken, the camera model, and GPS coordinates. Tools like ExifTool can be used for this purpose.
   - Activity 2: Compare the metadata against the claimed time and location. Ensure there are no inconsistencies or signs of tampering (e.g., missing or altered metadata).
2. Image Analysis:

   - Activity 1: Use forensic tools to detect signs of manipulation. Tools like Adobe Photoshop Forensic Suite or Amped Authenticate can help identify inconsistencies in lighting, shadows, or pixelation that suggest image editing.
   - Activity 2: Perform Error Level Analysis (ELA) to detect areas of the image that may have been altered. ELA highlights parts of the image that differ in compression levels, which is often a sign of editing.
3. Contextual Verification:

   - Activity 1: Verify the location by comparing the background in the image with known photographs or Google Street View images of the central square in Berlin. Ensure landmarks and structures match.
   - Activity 2: Cross-reference the weather conditions and lighting in the image with historical weather data for the claimed date and time. Tools like Wolfram Alpha or weather archives can provide this information.
4. Technical Consistency:

   - Activity 1: Check for inconsistencies in the photo's technical attributes such as resolution, aspect ratio, and color balance. These attributes should be consistent across the entire image if it hasn't been altered.
   - Activity 2: Use tools to detect cloning or duplication artifacts, which can indicate parts of the image have been copied and pasted.
## Question 3.2
### Analyzing Memory Capture and Network Logs (10 points)
To investigate whether the head of sales had been negotiating a deal with the competitor company, you can look for the following in the memory capture and network logs:

1. Memory Capture Analysis:

   - Activity 1: Search for relevant keywords in the memory capture file. Keywords can include the competitor's name, the CEO's name, and terms related to negotiations or deals. Tools like Volatility can be used for memory analysis.
   - Activity 2: Analyze running processes and open files at the time of the memory capture. Look for email clients, document editors, and chat applications that might have been used for communication.
2. Network Log Analysis:

   - Activity 1: Identify and inspect any network traffic between the head of sales’ laptop and the competitor company’s domain or IP addresses. Look for email exchanges, file transfers, and chat communications. Tools like Wireshark can help analyze network logs.
   - Activity 2: Check for encrypted traffic that could indicate the transfer of sensitive information. Analyze the frequency, volume, and timing of the traffic to determine if it coincides with the suspected negotiation period.
3. Email and Document Examination:

   - Activity 1: If email logs are available, search for emails sent to and received from the competitor company. Examine the content of these emails for any negotiation details.
   - Activity 2: Look for attachments in the emails and examine their content for any sensitive information or agreements.
4. Behavioral Analysis:

   - Activity 1: Review login times and remote access logs to identify unusual activity or access patterns that could indicate unauthorized communication.
   - Activity 2: Correlate the network activity with the timeline of the alleged meetings to see if there are any patterns that match the accused behavior.

By thoroughly analyzing the metadata, image content, memory capture, and network logs, you can gather evidence to either support or refute the claims of the head of sales meeting with the competitor’s CEO.

## Question 4.1
### Type of Testing (check the security of the application for any issues)
- Penetration Testing (Pen Test)

  - Description: This type of testing involves simulating an attack on the web application to identify vulnerabilities that could be exploited by attackers. It provides a comprehensive assessment of the application's security posture.
### Agreement with the CEO
  
Before starting the penetration test, it is crucial to agree on several points with the company CEO:

1. Scope of the Test:

   - Define the boundaries of the testing environment (e.g., specific URLs, application features).
   - Identify which parts of the application are in scope and which are out of scope.
2. Testing Window:

   - Agree on a timeframe for conducting the test to minimize disruption to business operations.
   - Ensure testing times do not conflict with critical business periods.
3. Authorization:

   - Obtain written consent to conduct the penetration test to ensure legal protection.
   - Ensure all relevant stakeholders are informed and approve the testing.
4. Objectives:

   - Clearly define the goals of the penetration test (e.g., identify security weaknesses, evaluate security controls).
   - Establish what success looks like (e.g., a detailed report of findings and recommendations).
5. Communication Plan:

   - Agree on how findings will be communicated and the level of detail required.
   - Determine points of contact for both the testing team and the company.
6. Confidentiality:

   - Ensure that the results of the penetration test are kept confidential.
   - Define how sensitive information will be handled and stored.
### Tools for Penetration Testing
- OWASP ZAP (Zed Attack Proxy): An open-source tool for finding vulnerabilities in web applications.
- Burp Suite: A comprehensive tool for web application security testing, offering features like scanning, manual testing, and reporting.
- Nmap: A network scanning tool that can help identify open ports and services.
- Nikto: A web server scanner that identifies potential issues like outdated software and misconfigurations.
- Metasploit: A penetration testing framework that allows for the development and execution of exploit code against target systems.
## Question 4.2
### 1. Concentration on a Set of Vulnerabilities
Focus on the OWASP Top 10 Vulnerabilities

- Reason: The OWASP Top 10 provides a well-recognized list of the most critical security risks to web applications. Addressing these vulnerabilities can significantly improve the security posture of the application.
### 2. Examples of Vulnerabilities from the OWASP Top 10
1. Injection: Flaws like SQL injection where untrusted data is sent to an interpreter as part of a command or query.
2. Broken Authentication: Issues that allow attackers to compromise passwords, keys, or session tokens.
3. Cross-Site Scripting (XSS): Flaws that allow attackers to inject client-side scripts into web pages viewed by other users.
### 3. Advice for Implementing Controls
1. Implement Strong Input Validation:

   - Ensure all user inputs are validated and sanitized to prevent injection attacks.
   - Use whitelisting techniques to allow only acceptable input values.
2. Strengthen Authentication Mechanisms:

   - Use multi-factor authentication (MFA) to add an extra layer of security.
   - Ensure password policies enforce strong, unique passwords and regular updates.
3. Conduct Regular Security Assessments:

   - Perform regular security audits and vulnerability scans to identify and address potential issues.
   - Encourage a culture of security awareness and continuous improvement within the organization.
   - By focusing on these key areas and implementing robust security controls, the company can significantly reduce the risk of vulnerabilities in their web application and enhance their overall security posture.

## Question 5.1
### [1] What key did ES need to communicate with LP?
Edward Snowden (ES) needed Laura Poitras' (LP) public key to encrypt messages sent to her. Using LP's public key would ensure that only LP could decrypt the messages with her corresponding private key.

### [2] How could he trust that he had the correct key from LP?
To trust that he had the correct public key from LP, ES could follow these steps:

1. Key Verification through a Trusted Third Party:

   - Since ES trusted Micah Lee (ML) and already had ML's public key, ML could act as a trusted intermediary.
   - ML could obtain LP's public key directly from LP or from a trusted source and verify its authenticity.
2. Signing the Public Key:

   - ML could sign LP's public key using his (ML's) private key.
   - This signature would confirm that the public key indeed belongs to LP and that it was endorsed by ML, a trusted intermediary.
3. Fingerprint Verification:

   - ES could verify the fingerprint of LP's public key. The fingerprint is a shorter version of the public key that is easier to compare and verify.
   - LP or ML could provide the fingerprint through a secure channel (e.g., verbally over a secure call) to ensure ES is verifying the correct key.
### [3] Sequence of Messages and Ensuring Sender's Identity
1. ES Requests LP’s Public Key via ML:

   - ES sends an encrypted message to ML (using ML's public key) requesting LP's public key.
   - Message from ES to ML: ES -> ML: {Request LP's public key}_(Encrypted with ML's public key)
2. ML Obtains and Signs LP’s Public Key:

   - ML contacts LP and securely obtains her public key.
   - ML verifies LP's public key and then signs it using his private key.
   - Signed public key from LP to ML: LP's Public Key (Signed by ML)
3. ML Sends Signed Public Key to ES:

   - ML sends the signed public key of LP to ES, encrypted with ES’s public key for confidentiality.
   - Message from ML to ES: ML -> ES: {LP's Public Key (Signed by ML)}_(Encrypted with ES's public key)
4. ES Verifies LP’s Public Key:

   - ES receives the signed public key of LP and decrypts it using his private key.
   - ES verifies the signature of ML on LP’s public key to ensure it is authentic and not tampered with.
   - Once verified, ES can now use LP's public key to encrypt messages intended for her.

**Ensuring the Sender's Identity**
1. Digital Signatures:

   - Whenever ES, ML, or LP send a message, they should sign the message with their private key. This digital signature ensures that the message was sent by the purported sender and has not been altered.
   - Recipients can verify the signature using the sender’s public key.
2. Encrypted Communication:

   - All communications between ES, ML, and LP should be encrypted using the recipient's public key to ensure confidentiality.
3. Key Fingerprint Verification:

   - ES, ML, and LP should verify each other’s public key fingerprints through a secure channel to ensure they are using the correct keys.
4. Regular Key Exchange and Updates:

   - Regularly updating and verifying keys through trusted intermediaries can further ensure the authenticity and integrity of their communications.

**Example Message Exchange with Digital Signatures and Encryption:**

- ES to LP:

   - ES wants to send a message to LP.
   - ES signs the message with his private key and encrypts it with LP's public key.
   - `Message: {Message, Signed with ES's private key}_(Encrypted with LP's public key)`
- LP Receives and Verifies:

   - LP decrypts the message with her private key.
   - LP verifies the signature with ES's public key to ensure it is indeed from ES and the message has not been tampered with.
   - 
By following this process, ES can securely and confidently communicate with LP, ensuring that the keys used are authentic and that the sender's identity can be trusted.