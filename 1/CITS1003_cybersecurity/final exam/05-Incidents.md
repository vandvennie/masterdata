# Incidents

1. Definitions:

* Any event that has compromised confidentiality, integrity or availability of an organisation’s assets
任何损害组织资产的机密性、完整性或可用性的事件
* From a VERIS perspective, an incident is the result of an Actor, taking some Action, on an Asset, resulting in the Attributes of an incident, i.e., how it was affected. In this case, the action exploits a vulnerability in the asset
从VERIS的角度来看，事件是参与者对资产采取某些操作的结果，导致事件的属性，即它是如何受到影响的。在这种情况下，操作利用了资产中的漏洞
* An incident is when there is actual loss or imminent threat of loss. Otherwise, it is an Event
事故是指存在实际损失或迫在眉睫的损失威胁。否则，它是一个事件
* Standard for incident handling is NIST SP800-61 it defines an incident as: "A computer security incident is a violation or imminent threat of violation of computer security policies, acceptable use policies, or standard security practices"
事件处理的标准是NIST SP800-61，它将事件定义为:“计算机安全事件是违反或即将违反计算机安全策略，可接受的使用策略或标准安全实践的威胁。”
2. **Hack back**

* In the process of investigation and remediation, there may be the temptation to take direct action against hackers. This is known as “Hack back”. 在调查和补救的过程中，可能会有对黑客采取直接行动的诱惑。这就是所谓的“黑客反击”。
* Very few organisations or governments think this is a good idea and there is no legal basis for it as hacking back may involve other countries, other infrastructure and innocent third parties 很少有组织或政府认为这是一个好主意，而且没有法律依据，因为黑客攻击可能涉及其他国家、其他基础设施和无辜的第三方
* It is not the role of a business to engage in cyber actions and this should be left to legal authorities 从事网络行动不是企业的职责，这应该留给法律当局

3. **Incident Response Team**事件响应团队

* Not all organisations can afford并非所有组织都能负担得起
* A service can offered by outside contractors as well as through cybersurance companies这项服务可以由外部承包商提供，也可以通过网络保险公司提供
* always be ready 24h时刻准备着
* Can be involved in security awareness training能参与安全意识培训

4. **Detection**检测

	1. Incidents can be detected from:事故可从以下途径检测:
   * IDPS(intrusion Detection and Prevention System)
   * Anti-malware software
   * Irregular behaviours noted by users on their computers or accounts用户在其电脑或帐户上发现的不正常行为
   * Breached data surfacing on the Dark Web

	2. Dwell Time停留时间: Amount of time an attacker spent on a system攻击者在系统上花费的时间

5. **Making detection and analysis easier**使检测和分析更容易

* Understand normal behaviours
* Have a log retention policy是否有日志保留策略
* Perform event correlation执行事件关联
* Keeping all host clocks synchronized保持所有主机时钟同步
* Use packet sniffers for additional data使用数据包嗅探器获取其他数据

6. **Indicators of Compromise**:威胁指标

Indicators of compromise (IOC) are pieces of forensic data that identify a malicious attack. They include:妥协指示器(IOC)是识别恶意攻击的取证数据片段。它们包括:

* Unusual (outbound) network traffic 异常(出站)网络流量 
* Anomalies in privileged account behaviour特权帐户行为异常
* Geographical irregularities: logins from new locations and countries, network traffic from specific IP addresses地理异常:从新的位置和国家登录，来自特定IP地址的网络流量
* Unusual database activity异常的数据库活动
* Presence of malware or other files存在恶意软件或其他文件
* Signs of DDoS(Distributed Denial of Service) attacks. Typically, however, they are specific MD5 hashes of malware, IP addresses, or URLs of domain names or botnets
  DoS(分布式拒绝服务)攻击迹象。但是，它们通常是恶意软件、IP地址或域名或僵尸网络的url的特定MD5哈希值
  

7. **Tactics, Techniques and Procedures**

* Tactics, Techniques and Procedures (TTPs) are descriptions of the behaviours of threat actors. 战术、技术和程序(TTPs)是对威胁行为者行为的描述。

* Tactics are the high-level overall objective of an attacker split into phases of the kill-chain. 战术是攻击者的高级总体目标，将其分解为击杀链的各个阶段。

* Techniques are the next level down and describe the general behaviour to achieve the tactical objective技术是下一个层次，描述实现战术目标的一般行为
* Procedures are specific instances of behaviour to carry out a technique using particular software程序是使用特定软件执行技术的特定行为实例
* TTPs are thought to be specific to particular threat actor groups because of the Pyramid of Pain由于痛苦金字塔，ttp被认为是针对特定威胁行为者群体的

8. **Containment**控制

* Stop further impact: Disabling accounts, blocking network and isolating a computer of the network停止进一步的影响:禁用帐户，阻塞网络和隔离网络中的计算机

* Balance the strategy against: Potential damage and theft of resources, need for evidence preservation, service availablity, time and resources needed, effectiveness of the strategy, duration and alerting attackers.在以下方面平衡策略:资源的潜在损害和盗窃、证据保存的需要、服务的可用性、所需的时间和资源、策略的有效性、持续时间和提醒攻击者

9. **Post-Incident Activity**事后的活动

Lessons learned, breach notification to appropriate authorities, notification of affected users, reputation management. insurance claims and analysis of incident data.经验教训、向相关机构发出违规通知、通知受影响的用户、声誉管理。保险索赔和事故数据分析。

10. **CALDERA:** 

It is an open-source cyber security platform designed to automate adversary emulation, automate incident response, etc.它是一个开源的网络安全平台，旨在自动模拟对手，自动事件响应等

* Adversary is a profile of instructions that describe various TTPs (tactics, techniques and procedures) to be performed on a targeted system. An adversary profile can be used to simulate an attack or evaluate the effectiveness of a security defense. 对手是描述在目标系统上执行的各种ttp(战术、技术和程序)的指令概要。攻击者配置文件可用于模拟攻击或评估安全防御的有效性

* Agent works as a spy program that is installed on the targeted system and responsible for executing TTPs specified in the adversary profile. Agent作为一个间谍程序，安装在目标系统上，负责执行敌手配置文件中指定的ttps

* Ability refers to an attack step in an attack, e.g., find all the local users, compromise the current active user and gain privilege escalation. 能力是指攻击中的一个攻击步骤，例如，找到所有本地用户，危及当前活动用户并获得权限升级。

* Operation is to create an adversary profile and executes the profile via agent.操作是创建对手配置文件并通过代理执行该配置文件。
  
### Q&A
1. Why is CALDERA developed?为什么要开发CALDERA ?
* cyber range simulates real-world network environment that can be used to replicate real-world cyber scenarios.网络范围模拟真实世界的网络环境，可用于复制真实世界的网络场景。
* red team is a group of security professionals who simulate cyber attacks and thus identify weaknesses that can be exploited by real attackers, which is to test the incident-response mechanisms that are deployed. 红队是一组安全专业人员，他们模拟网络攻击，从而识别可能被真正的攻击者利用的弱点，这是为了测试部署的事件响应机制。
* blue team is a group of security professionals who respond to the simulated attacks and test their incident responses, better preparing for real-world cyber threats and mitigating the risks associated with cyber attacks.蓝队是一组安全专业人员，他们对模拟攻击做出反应，并测试他们的事件响应，更好地为现实世界的网络威胁做好准备，并降低与网络攻击相关的风险。

### 2. What is ADTool?

ADTool, short for Attack-Defense Tree Tool, allows a user to model and analyze attack-defense scenarios using attack-defense trees.
ADTool (Attack-Defense Tree Tool)是攻击防御树工具的缩写，用户可以使用攻击防御树对攻击防御场景进行建模和分析
![image-20240522111710643](/Users/suzhenyi/Library/Application Support/typora-user-images/image-20240522111710643.png)

```
op(
			ap(
						card,
						op(
									Eavesdrop,
									Force,
									cp(
												Find Note,
												Memorize
									)
						)
			),
			cp(
						ap(
									User Name,
									op(
												Phishing,
												Key Logger
									)
						),
						co(
									oo(
												Key Fobs,
												PIN Pad
									),
									op(
												Browser,
												OS				
									)									
						)
			)		
)
```

​				

![image-20240524100853424](/Users/suzhenyi/Library/Application Support/typora-user-images/image-20240524100853424.png)

```
op(
			op(
						Shield Tag,
						cp(
									Jam Signal,
									oo(
												Secure Warehouse,
												Faraday Around Tag and Reader
									)
						)
			),
			op(
						Dos in Network
			)
)
```

![image-20240524124055231](/Users/suzhenyi/Library/Application Support/typora-user-images/image-20240524124055231.png)





