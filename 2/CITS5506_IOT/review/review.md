#### 6大组成：

Hardware, sensor, data storage, computing entity, software, connectivity 

#### 4大机会：机会留给功能可靠的高使用的传统产品

Functionality, reliability, high utilisation, cut across and transcend 

#### 3大核心要素：物理要素让聪明的人链接

physical, smart, connectivity(1:1:M:M)

#### 4大区域：监控4个区域控制了怪物自主的优化

monitoring, controlling, optimisation, Autonomy



#### 元件

senior, transducer, actuator

#### categorization

Analog and digital

active and passive

#### 4种规格Specification：这4个规格都可以准确分辨，重复去做也一样灵敏 和精准

Accuracy，resolution，sensitivity， repeatability/precision

#### 3大选择：选澳洲的原因，环境经济的特征好

Environment, economic, characteristics

#### sensor type

Strain gauge, accelerometer, piezoelectric



#### 安全漏洞security flaws：市场利益让制造商忽略了安全法律

​	profit driven business

​	time-to-market constraint 

​	absence of related legislation

​	manufacturers overlook security considerations 

#### Vulnerabilities缺陷：这个设备的缺陷是有网络也不能用软件

​	device: pe

​		physical, energy

​	network: aep

​		authentication, encryption, port 

​	software: appa

​		access, path, programming, audit

#### 安全目标Objectives: CIAA

​	confidentiality , integrity availability accountability 

#### 对策countermeasures：对策是签一个协议，认证他的情况

​	authentication, protocol, situation awareness 

#### 攻击类型 attack: cia

​	authentication

​	data integrity

​	denial of service



#### 5 competitive force竞争力: 

bargaining power of buyer, bargaining of supplier, competitors, New entrants, substitute product 

#### 7 ethical AI: 代理和监督，鲁棒性，安全，隐私，透明度，多样性，社会福利，问责制

Human agency and oversignt

robustness and safety

Privacy

transparency

diversity

Social well being

Accountability

#### TML 3 process: 

​	input process output

#### TML 3 challenge: 

​	hardware, software, machine learning

#### 3 Model compression techniques 模型压缩技术

​	pruning, Quantization, knowledge distillation 剪量蒸



#### Comfusion Matrix:

Precision = TP/(TP+FP)

Accuracy = (TP+TN)/S

Sensitive = Recall = TPR = TP/(TP+FN)

Specificity = FPR = FP/(FP+TN)

F1 score= 2*[(PxR)/(P+R)]

Balanced Accuracy =(Se+Sp)/2



#### Q1

A company sells IoT-enabled household devices, such as smart refrigerators and thermostats, to consumers. These devices were rushed to market, and security was not given adequate consideration. What are the typical security vulnerabilities that arise in IoT devices when manufacturers focus on reducing time-to-market? 

How can consumers protect themselves against these vulnerabilities?



When IoT devices are rushed to market with security not prioritized, several common security vulnerabilities can arise, including:

1. **Device-Based Vulnerabilities**:
   - **Deficient Physical Security**: Many IoT devices lack sufficient protection against physical tampering.
   - **Insufficient Energy Harvesting**: IoT devices often have limited power resources, which restricts the ability to implement robust security features.

2. **Network-Based Vulnerabilities**:
   - **Inadequate Authentication**: Weak authentication protocols can allow unauthorized access.
   - **Improper Encryption**: Some devices may not encrypt data sufficiently, making it vulnerable to interception.
   - **Open Ports**: Devices may have unnecessary open ports, increasing the attack surface.

3. **Software-Based Vulnerabilities**:
   - **Insufficient Access Control**: Weak access control mechanisms make it easier for attackers to gain unauthorized control over devices.
   - **Improper Patch Management**: Updates are often neglected, leaving vulnerabilities unpatched.
   - **Weak Programming Practices**: Lack of coding standards can lead to exploitable flaws in the device's software.



How Consumers Can Protect Themselves

Consumers can take several measures to protect themselves from these vulnerabilities:

1. **Use Strong, Unique Passwords**: Change default passwords and use strong, unique passwords for each device.

2. **Regularly Update Devices**: If the device allows for it, ensure it is updated with the latest firmware and patches provided by the manufacturer.

3. **Secure the Home Network**:
   - Enable strong Wi-Fi passwords and consider segmenting the network to separate IoT devices from more sensitive devices.
   - Use encryption on the Wi-Fi network, such as WPA3.

4. **Limit Device Permissions**: Review the device’s access permissions and disable any features that are unnecessary, such as location tracking or microphones.

5. **Consider Disabling Remote Access**: If remote access isn’t needed, it’s safer to disable this functionality, as it limits external entry points.

6. **Monitor Network Traffic**: Use network monitoring tools to identify any unusual activity from IoT devices, which could signal potential security breaches.

These measures help mitigate risks associated with rushed, security-deficient IoT devices and provide an extra layer of protection for consumers.



#### Q2

A machine learning model was developed to classify emails as spam or non-spam. Out of 2000 emails, 500 are spam. The model correctly identifies 400 spam emails and 1400 non-spam emails. It incorrectly flags 100 non-spam emails as spam and fails to detect 100 spam emails. 

What are the values of True Positive (TP), False Positive (FP)? 

Calculate the model's accuracy.

Let’s calculate the values based on the information provided:

1. **True Positives (TP)**: The model correctly identifies spam emails.
   - \( \text{TP} = 400 \)

2. **False Positives (FP)**: The model incorrectly flags non-spam emails as spam.
   - \( \text{FP} = 100 \)

3. **True Negatives (TN)**: The model correctly identifies non-spam emails.
   - \( \text{TN} = 1400 \)

4. **False Negatives (FN)**: The model fails to identify spam emails.
   - \( \text{FN} = 100 \)

### Accuracy Calculation

Accuracy is the ratio of correctly classified emails (both spam and non-spam) to the total number of emails:

\[
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
\]

Substitute the values:

\[
\text{Accuracy} = \frac{400 + 1400}{400 + 1400 + 100 + 100} = \frac{1800}{2000} = 0.9
\]

### Answer Summary

- **True Positive (TP)**: 400
- **False Positive (FP)**: 100
- **Accuracy**: 0.9 or 90%

---

### Case 1: Machine Learning Model for Loan Approval

A financial institution has implemented a machine learning model to automate the loan approval process. The model was trained on historical data, but it has been noticed that many low-risk applicants are denied loans while some high-risk applicants are approved.

1. **What potential issues in the training data or model selection could lead to these errors?**
2. **What steps can the institution take to improve the accuracy and fairness of the loan approval model?**

---

### Case 2: Smart Home Lighting System

An electronics company released a new smart lighting system that connects to a mobile app. However, users report frequent malfunctions where the lights turn on and off unpredictably, and the app experiences delays.

1. **What could be the possible causes of these malfunctions, considering the IoT infrastructure?**
2. **What measures can the company take to improve system stability and user experience?**

---

### Case 3: Data Privacy in Health Monitoring Devices

A startup develops wearable health monitoring devices that collect and transmit real-time health data, such as heart rate and activity levels, to a mobile app. However, users are concerned about how their health data is stored and shared, especially if it could be accessed by third parties.

1. **What data privacy and security challenges are associated with IoT health devices?**
2. **What steps can the startup take to protect user data and build trust with consumers?**

---

### Case 4: Autonomous Vehicle Testing

A company is developing an autonomous vehicle and has started testing in real-world urban environments. Although the vehicle performs well in many conditions, it sometimes misinterprets complex traffic scenarios, leading to sudden stops or other unexpected actions.

1. **What limitations in machine learning models for autonomous driving could lead to these issues?**
2. **How can the company enhance the vehicle’s performance to handle complex traffic situations more reliably?**

---

### Case 5: Retail Inventory Management with IoT

A retail chain deployed IoT-enabled inventory management systems in their stores to monitor product levels in real-time. However, the system often sends inaccurate alerts, either notifying that stock is low when it’s not or vice versa, disrupting the replenishment process.

1. **What common IoT sensor issues could cause these inaccuracies in inventory tracking?**
2. **What actions can the retail chain take to ensure more reliable inventory monitoring?**

---

### Case 6: TinyML for Wildlife Monitoring

An environmental organization is using TinyML devices in a conservation area to monitor wildlife sounds for endangered species. The devices, designed for ultra-low power consumption, sometimes miss critical sounds or misclassify background noises as species-specific sounds.

1. **What challenges related to model training and device limitations might cause these inaccuracies?**
2. **What strategies can the organization use to enhance detection accuracy without significantly increasing power usage?**

---

### Case 7: Predictive Maintenance in Smart Factories

A manufacturing company uses IoT sensors to implement predictive maintenance in its machinery, aiming to reduce downtime. Recently, the company noticed an increase in false alerts for maintenance, causing unnecessary inspections and interruptions.

1. **What factors might contribute to the high rate of false alerts in IoT-enabled predictive maintenance systems?**
2. **How can the company adjust its system to improve the accuracy of its predictive maintenance alerts?**

---

### Case 8: Cybersecurity in Connected Medical Devices

A healthcare provider introduced connected medical devices, such as pacemakers and insulin pumps, that patients can monitor via a mobile app. However, a security flaw was identified that could allow unauthorized access to these devices.

1. **What types of vulnerabilities are common in connected medical devices that might lead to unauthorized access?**
2. **What measures can healthcare providers take to improve device security and protect patient safety?**

---

Here are answers for each case in English:

---

### Case 1: Machine Learning Model for Loan Approval

1. **Model Issues**: The model may have biases if the training dataset has historical discrimination or mislabeled samples. It could also ignore essential features like repayment capability or financial history.
   
2. **Improvement Measures**: Conduct fairness analysis to identify bias, diversify data to reduce bias, and apply techniques such as regularization to improve model robustness and prevent overfitting.

---

### Case 2: Smart Home Lighting System

1. **Failure Causes**: Unstable network connections, device compatibility issues, or delays in instruction response could lead to poor user experience.
   
2. **Improvement Measures**: Enhance firmware for compatibility, improve network stability, or integrate local storage and processing to reduce latency.

---

### Case 3: Data Privacy in Health Monitoring Devices

1. **Data Privacy Challenges**: Data security risks can arise from insecure storage, insufficient control over third-party data sharing, and potential data breaches.
   
2. **Protection Measures**: Implement end-to-end encryption for secure data transmission, increase user control over data sharing, and ensure storage and access permissions comply with regulations like GDPR.

---

### Case 4: Testing Autonomous Driving Vehicles

1. **Model Limitations**: Machine learning models may perform poorly in complex scenarios, such as sudden traffic situations, due to insufficient data for handling these complexities.
   
2. **Enhancement Measures**: Collect more data from complex scenarios for training, use ensemble models to improve generalization, and reduce misjudgment in specific scenarios.

---

### Case 5: IoT-Enabled Retail Inventory Management

1. **Sensor Issues**: IoT sensors might produce inaccurate inventory data due to measurement errors, delays, or limited battery life.
   
2. **Improvement Measures**: Regularly calibrate sensors, implement multi-sensor verification for accuracy, and add backup power to ensure device stability.

---

### Case 6: TinyML for Wildlife Monitoring

1. **Challenges**: TinyML devices may have limited processing power, leading to missed important sounds or misclassification. Insufficient sensor sensitivity can make it challenging to filter out background noise.
   
2. **Improvement Strategies**: Optimize the model to reduce computational load, use noise-reduction techniques, or deploy more sensitive sensors for improved detection. Techniques like model compression can retain critical features and boost detection accuracy.

---

### Case 7: Predictive Maintenance in a Smart Factory

1. **False Alarm Causes**: Sensor anomalies, environmental interference, or incorrect model thresholds may cause false alarms in predictive maintenance.
   
2. **Adjustment Measures**: Re-evaluate model thresholds, use environmental detection algorithms to filter out external factors, or implement multi-sensor verification to reduce false alarms.

---

### Case 8: Cybersecurity in Connected Medical Devices

1. **Vulnerabilities**: Common issues include a lack of encryption, weak authentication mechanisms, and outdated firmware, exposing systems to security risks.
2. **Security Measures**: Strengthen encryption and authentication, regularly update device firmware, establish secure update mechanisms, reduce the attack surface, and promptly address known vulnerabilities.





### CN

---

### 案例1：用于贷款审批的机器学习模型

一家金融机构使用机器学习模型来自动化贷款审批流程。该模型基于历史数据进行训练，但发现许多低风险的申请人被拒，而一些高风险的申请人却获得了批准。

1. **在训练数据或模型选择上存在哪些可能导致这些错误的问题？**
2. **该机构可以采取哪些步骤来提高贷款审批模型的准确性和公平性？**

---

### 案例2：智能家居照明系统

一家电子公司推出了一款新的智能照明系统，可与手机应用程序连接。但用户报告称灯光经常无法正常工作，出现无法预测的开关问题，且应用程序存在延迟。

1. **考虑到物联网基础架构，这些故障可能由什么原因引起？**
2. **公司可以采取哪些措施来提高系统的稳定性和用户体验？**

---

### 案例3：健康监测设备中的数据隐私问题

一家初创公司开发了可穿戴健康监测设备，能够实时收集和传输心率、活动水平等健康数据到手机应用程序。然而，用户对健康数据的存储和共享方式表示担忧，特别是如果第三方可以访问这些数据。

1. **物联网健康设备涉及哪些数据隐私和安全挑战？**
2. **初创公司可以采取哪些措施来保护用户数据并赢得消费者信任？**

---

### 案例4：自动驾驶汽车测试

一家公司正在开发自动驾驶汽车，并已开始在真实的城市环境中进行测试。尽管车辆在很多条件下表现良好，但在复杂交通场景中有时会出现误判，导致车辆突然停车或出现其他意外操作。

1. **自动驾驶中的机器学习模型存在哪些限制，可能导致这些问题？**
2. **公司可以采取哪些措施来增强车辆的性能，以更可靠地处理复杂的交通情况？**

---

### 案例5：使用物联网的零售库存管理

一家零售连锁店在店内部署了物联网库存管理系统，实时监控产品库存。然而系统经常发送不准确的警报，要么通知库存不足实际却不缺，要么库存充足却被通知不足，导致补货过程受到干扰。

1. **在库存追踪中，物联网传感器常见的哪些问题可能导致这些不准确的情况？**
2. **零售连锁店可以采取哪些措施确保库存监控的可靠性？**

---

### 案例6：用于野生动物监测的TinyML

一家环境组织在保护区使用TinyML设备来监测野生动物声音，以跟踪濒危物种。这些设备设计为超低功耗，但有时会漏掉关键声音，或将背景噪声误分类为特定物种的声音。

1. **模型训练和设备限制方面存在哪些挑战，可能导致这些不准确？**
2. **组织可以使用哪些策略在不显著增加功耗的情况下提高检测准确性？**

---

### 案例7：智能工厂中的预测性维护

一家制造公司使用物联网传感器实现预测性维护，以减少停机时间。但最近公司发现维护的误报增加，导致了不必要的检查和生产中断。

1. **在物联网预测性维护系统中，哪些因素可能导致误报率过高？**
2. **公司可以如何调整系统来提高预测性维护警报的准确性？**

---

### 案例8：连接的医疗设备中的网络安全

一家医疗服务提供商引入了连接的医疗设备，如心脏起搏器和胰岛素泵，患者可以通过手机应用程序监控这些设备。然而，发现了一个安全漏洞，可能允许未经授权的用户访问这些设备。

1. **哪些常见的连接医疗设备漏洞可能导致未经授权的访问？**
2. **医疗服务提供商可以采取哪些措施来提高设备安全性，保护患者安全？**

---

以下是每个案例的简答参考答案。

---

### 案例1：用于贷款审批的机器学习模型

1. **模型问题**：模型可能存在偏差，例如使用的数据集存在历史歧视或错误标记的样本。同时，模型可能忽略了某些关键特征（如还款能力或财务历史）。
   
2. **改进措施**：进行公平性分析，确保模型没有偏见；使用更多多样化的数据，减少偏差；通过正则化等技术提高模型的鲁棒性，减少过拟合。

---

### 案例2：智能家居照明系统

1. **故障原因**：可能由不稳定的网络连接或设备兼容性问题引起；也可能因为延迟的指令响应而影响用户体验。
   
2. **改进措施**：优化设备的固件以提高兼容性，优化网络连接稳定性，或增加本地存储和处理功能以减少延迟。

---

### 案例3：健康监测设备中的数据隐私问题

1. **数据隐私挑战**：涉及数据存储的安全性、与第三方数据共享的控制不足以及数据泄露的风险。
   
2. **保护措施**：采用端到端加密确保数据传输安全，增加用户对数据共享的控制权限，确保数据存储和访问权限符合相关法律规定（如GDPR）。

---

### 案例4：自动驾驶汽车测试

1. **模型限制**：机器学习模型在复杂场景中可能表现不佳，如突发交通状况；可能是由于模型缺乏足够的数据处理复杂场景。
   
2. **增强措施**：收集更多复杂场景的数据进行训练，使用多模型集成的方法，提高模型的泛化能力，避免对少数场景的错误判断。

---

### 案例5：使用物联网的零售库存管理

1. **传感器问题**：物联网传感器可能因传感误差、延迟或设备电池寿命问题，导致不准确的库存数据。
   
2. **改进措施**：定期校准传感器，采用多传感器验证策略以提高数据准确性，或增加备用电源以确保设备稳定性。

---

### 案例6：用于野生动物监测的TinyML

1. **挑战**：由于TinyML设备处理能力有限，导致漏掉重要声音或误分类；传感器灵敏度不足，难以精确区分背景噪声。
   
2. **改进策略**：优化模型以降低计算负载，使用降噪处理或更灵敏的传感器来提高检测率；通过模型压缩技术保留重要特征，提升检测准确性。

---

### 案例7：智能工厂中的预测性维护

1. **误报原因**：传感器数据异常、环境干扰或模型阈值设置不合理，可能导致预测性维护中的误报。
   
2. **调整措施**：重新设置模型阈值，使用环境感知算法排除外界因素影响，或使用多传感器数据验证以减少误报率。

---

### 案例8：连接的医疗设备中的网络安全

1. **漏洞**：常见漏洞包括设备缺乏加密，认证机制不完善，固件不更新导致的系统安全隐患。
   
2. **安全措施**：强化加密和认证措施，定期更新设备固件，设置安全更新机制，减少攻击面并及时修复已知漏洞。