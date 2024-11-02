



- **What key information should be included in the project scope and why? Discuss and provide examples to support your answer.**

  1. Project Objectives:
     - Description: Clearly state what the project aims to achieve. This provides a high-level understanding of the project's purpose.
     - Example: "The objective of this project is to develop a mobile application for tracking fitness activities and providing personalized workout recommendations."
  2. Deliverables:
     - Description: List all the tangible and intangible items, services, or outcomes that the project will produce.
     - Example: "Deliverables for this project include the mobile app, user documentation, and a training program for the app's support staff."
  3. Project Boundaries and Limitations:
     - Description: Identify any constraints or limitations that may impact the project, such as budget constraints, resource limitations, or regulatory requirements.
     - Example: "This project is limited by a budget of $100,000 and must comply with all relevant data privacy regulations."
  4. Project Schedule:
     - Description: Provide an overview of the project timeline, including key milestones and deadlines.
     - Example: "The project is scheduled to begin on January 1st, 2023, and is expected to be completed within 6 months, with key milestones at the end of each development phase."
  5. Stakeholders:
     - Description: List all the individuals, groups, or organizations that have an interest in the project and describe their roles and responsibilities.
     - Example: "Stakeholders for this project include the project sponsor, development team, quality assurance team, and end-users."
  6. Assumptions:
     - Description: Document any assumptions made during project planning, as they can impact the project's success.
     - Example: "It is assumed that the development team will have access to the necessary hardware and software resources for app development."
  7. Risks and Dependencies:
     - Description: Identify potential risks that could affect the project and any external dependencies that the project relies on.
     - Example: "The project is dependent on third-party APIs for weather data, and there is a risk of API changes affecting app functionality."
  8. Acceptance Criteria:
     - Description: Define the criteria that must be met for the project to be considered complete and successful.
     - Example: "The project will be considered complete when the mobile app has been tested and approved by the quality assurance team, and user feedback is positive."
  9. Change Management:
     - Description: Explain how changes to the project scope will be managed and approved.
     - Example: "Any proposed changes to the project scope must be submitted in writing to the project manager and approved by the project sponsor."

  ![image-20240602145139622](/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240602145139622.png)

  

- **What key information should be included in the project charter and why? Discuss.**

  1. Project Title:
     - **Why**: The project title provides a concise and clear name for the project, making it easy to refer to and communicate about.
     - **Example**: "New Product Development - XYZ Widget."
  2. Project Purpose or Justification:
     - **Why**: This section outlines why the project is necessary and how it aligns with the organization's goals and strategic objectives.
     - **Example**: "The project is necessary to expand our product line and capture new market segments, aligning with our growth strategy."
  3. Project Objectives and Deliverables:
     - **Why**: Clearly state what the project aims to achieve and what will be delivered upon completion.
     - **Example**: "The project's objective is to design, develop, and launch a new widget product, including a prototype and marketing materials."
  4. Key Stakeholders and Roles:
     - **Why**: Identify the main project stakeholders, their roles, and responsibilities to ensure clarity in project communication and accountability.
     - **Example**: "Stakeholders include the project sponsor, project manager, development team, marketing team, and quality assurance team."
  5. Project Scope:
     - **Why**: Define the boundaries of the project to avoid scope creep and ensure everyone understands what is included and excluded.
     - **Example**: "The project scope includes product design, development, and marketing. It does not include post-launch customer support."
  6. Project Constraints and Assumptions:
     - **Why**: Document any limitations, constraints, or assumptions that could impact the project's execution.
     - **Example**: "Budget constraints limit project spending to $500,000. An assumption is that the necessary raw materials will be readily available."
  7. High-Level Schedule or Timeline:
     - **Why**: Provide an overview of the project timeline, including key milestones and deadlines.
     - **Example**: "The project is scheduled to start on January 1, 2023, and aims to complete product development within 12 months."
  8. Project Authority:
     - **Why**: Clearly state who has the authority to initiate, approve, and oversee the project.
     - **Example**: "The project sponsor, John Smith, has the authority to approve changes to the project scope and budget."
  9. Project Risks and Initial Mitigation Plans:
     - **Why**: Identify potential risks that could affect the project and outline initial plans to mitigate or manage them.
     - **Example**: "A risk is that market demand may shift. Mitigation plan: Regular market research to adapt the product."

![image-20240602145112304](/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240602145112304.png)



- **What is the Program Evaluation Review Technique (PERT network diagram)? Discuss and provide examples to substantiate your answer.**

  Program Evaluation & Review Technique (Network Diagram) provides a picture of the project’s logic, which the WBS accurately recorded in table format only.

  Advantages: • Excellent visual & interactive graphic to demonstrate the schedule • Participative decision making • Joint risk identification & response strategy • Negotiated concessions • Improved team ownership • Shows Critical Path • Eliminates idle time

  Disadvantages: • Difficult to read if the project is large • No timeline • Difficult to monitor & report performance • Not always easy to understand • Limited amount of information that can display

  ![image-20240602170303801](/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240602170303801.png)

- **What is the difference between a schedule drawn “\*in series\*” and one drawn “\*in parallel\*”? Discuss and provide examples to substantiate your answer.**

  1. **Scheduling in Series (Sequential Scheduling):**

     In series scheduling, tasks are arranged one after the other in a linear fashion. Each task depends on the completion of the previous task, forming a sequential chain of activities. This approach is often used when tasks are highly dependent on each other, and one task must be completed before the next one can begin.

     **Example:** Construction of a house can be a good example of series scheduling. You must complete the foundation before building the walls, and the walls must be finished before you can add the roof.

     ```mathematica
     mathematicaCopy code
     Task 1: Excavate foundation (Duration: 2 weeks)
     Task 2: Pour concrete foundation (Duration: 1 week)
     Task 3: Construct walls (Duration: 6 weeks)
     Task 4: Install roof (Duration: 2 weeks)
     ```

     In this example, Task 2 depends on Task 1, Task 3 depends on Task 2, and so on. Each task follows the completion of the previous one, and any delay in one task can impact the entire project's timeline.

  2. **Scheduling in Parallel (Concurrent Scheduling):**

     In parallel scheduling, tasks are executed simultaneously or overlapped to some extent, rather than being strictly sequential. This approach is used when tasks have minimal dependencies or when resources can be allocated to multiple tasks simultaneously, speeding up the project's overall timeline.

     **Example:** In software development, different teams might work on different modules of a large project concurrently.

     ```java
     javaCopy code
     Task 1: Develop user interface (Duration: 4 weeks)
     Task 2: Develop backend functionality (Duration: 5 weeks)
     Task 3: Conduct system testing (Duration: 3 weeks)
     ```

     Here, Task 1 and Task 2 can be worked on simultaneously because they involve different aspects of the project. While there may be some dependencies (e.g., integration of the user interface with the backend), the tasks are largely independent, allowing for parallel work.

  **Key Differences:**

  - Sequential (In Series):
    - Tasks are performed one after the other.
    - Strong task dependencies.
    - Delays in one task can cause delays in subsequent tasks.
    - Suitable for projects with strong dependencies and a clear sequence of activities.
  - Concurrent (In Parallel):
    - Tasks are performed concurrently or with some overlap.
    - Reduced task dependencies, if any.
    - Can speed up project completion.
    - Suitable for projects with tasks that can be done independently or when resources are available simultaneously.

![image-20240602151513130](/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240602151513130.png)



- **What information should be found in the project ‘close-out report’ and why? Discuss.**

  1. Project Overview:
     - **Why**: Provide a brief introduction to the project, including its objectives, scope, and key stakeholders. This sets the context for the report.
     - **Benefits**: Helps readers quickly understand the project's purpose and scope.
  2. Project Deliverables and Milestones:
     - **Why**: List the major deliverables and milestones achieved during the project, providing a clear record of what was accomplished.
     - **Benefits**: Demonstrates project progress and completion of key objectives.
  3. Project Timeline and Schedule Adherence:
     - **Why**: Compare the planned project timeline to the actual timeline, highlighting any deviations or delays.
     - **Benefits**: Helps assess the project's efficiency and identifies areas where scheduling improvements can be made in future projects.
  4. Budget and Cost Analysis:
     - **Why**: Detail the budget allocated, actual expenditures, and any variations, explaining the reasons for budget changes.
     - **Benefits**: Allows for cost analysis, budget optimization, and financial accountability.
  5. Scope Changes and Variations:
     - **Why**: Document any changes or variations in the project scope, along with reasons and impacts.
     - **Benefits**: Provides insights into scope management and helps avoid scope creep in future projects.
  6. Quality and Performance Metrics:
     - **Why**: Discuss the quality standards used in the project and assess whether they were met. Include any performance metrics or key performance indicators (KPIs).
     - **Benefits**: Offers an evaluation of project quality and identifies areas for improvement.
  7. Risks and Issue Management:
     - **Why**: Summarize the project's risk management strategy, the identified risks, and how they were mitigated or resolved.
     - **Benefits**: Helps in refining risk management practices in future projects.
  8. Stakeholder Satisfaction:
     - **Why**: Gather feedback from key stakeholders regarding their satisfaction with project outcomes and the project management process.
     - **Benefits**: Provides insights into stakeholder expectations and areas for improved stakeholder engagement.
  9. Lessons Learned:
     - **Why**: Reflect on what went well, what didn't, and the lessons learned from the project's successes and challenges.
     - **Benefits**: Promotes continuous improvement by identifying best practices and areas for improvement in future projects.
  10. Recommendations:
      - **Why**: Offer recommendations for future projects based on the lessons learned and the project's overall performance.
      - **Benefits**: Guides future project planning and execution.
  11. Project Closure Process:
      - **Why**: Describe the formal procedures followed to close the project, including documentation, handovers, and sign-offs.
      - **Benefits**: Ensures a systematic and organized project closure process.
  12. Acknowledgments and Thank You:
      - **Why**: Acknowledge and thank all individuals and teams involved in the project, showing appreciation for their contributions.
      - **Benefits**: Fosters a positive project culture and team morale.

![image-20240602154829524](/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240602154829524.png)



- **What is procurement management planning and what benefits does it bring to any project? Discuss and provide examples to support your answer.**

  Procurement management planning consists of processes necessary to purchase or acquire products, services or results needed from outside the project team.

  Process-based function driven by a particular department or local division seeking to get possession of something that solves an operational issue.

  Value-adding function that focuses on the efficient attainment of goods, services, or results that deliver a number of very specific and measured benefits to the project.

  Make the best possible use of supplier’s products & or services while supporting the changing scope, goals & objectives of the project itself (if/when necessary);

  TBL and life cycle thinking as the core of Procurement.

  Procurement management process includes:

  - Identify the requirements of all goods and services from all business units.
  - Identify and evaluate a list of suppliers.
  - Negotiate the contracts with the selected supplier.
  - Raise a purchase requisition and release the purchase order.
  - Complete the payment process upon receiving an invoice.
  - Receive and audit delivery of requested goods/services.
  - Maintain proper records of invoices.

  From Managing Coastal Vulnerability project, they have purchased the BIS (Bathymetric Information System) using the Department of Transport tender. Also, they purchased MCP using the tender system and the supplier is ESRI Australia.

  It benefits the project in different ways:

  - If the project doesn’t have enough capability (technical or resources), procurement management would help to acquire the services from outside the project.
  - Moreover, it helps to purchase goods required for the project to execute the project successfully.

- **Explain how team conflict can have both positive and negative outcomes in a project. Provide examples to support your answer.**

  Team conflict in a project can have both positive and negative outcomes, depending on how it is managed and resolved. Here are explanations and examples of how team conflict can lead to both positive and negative results:

  **Positive Outcomes of Team Conflict:**

  1. Enhanced Creativity and Innovation:
     - **Explanation**: Conflict can stimulate diverse perspectives and ideas, leading to innovative solutions and creative problem-solving.
     - **Example**: In a software development team, conflict over the design of a new feature may lead to the exploration of different approaches, ultimately resulting in a more user-friendly and efficient solution.
  2. Improved Decision-Making:
     - **Explanation**: Healthy conflict encourages thorough discussion and examination of options, leading to better-informed decisions.
     - **Example**: In a project management team, conflicting opinions on whether to prioritize cost or quality may lead to a balanced decision that considers both factors.
  3. Enhanced Team Cohesion:
     - **Explanation**: Successfully resolving conflict can strengthen team bonds by fostering open communication and trust.
     - **Example**: A marketing team that resolves conflicts related to campaign strategy can emerge with stronger teamwork and a shared commitment to the chosen approach.
  4. Identification of Hidden Issues:
     - **Explanation**: Conflict can bring underlying problems and concerns to the surface, allowing teams to address them proactively.
     - **Example**: In a construction project, conflicts over project delays may reveal issues with the project's scheduling or resource allocation, which can then be addressed to prevent further delays.

  **Negative Outcomes of Team Conflict:**

  1. Decreased Productivity:
     - **Explanation**: Unresolved or destructive conflict can lead to distractions, reduced focus, and lower productivity.
     - **Example**: In an engineering team, ongoing disputes between team members can lead to missed deadlines and a decrease in project progress.
  2. Negative Impact on Team Morale:
     - **Explanation**: Prolonged or unresolved conflict can lead to stress and decreased morale among team members.
     - **Example**: Continuous conflicts over task assignments and roles can result in frustration and demotivation within a project team.
  3. Increased Turnover and Disengagement:
     - **Explanation**: Persistent conflict may cause team members to disengage or leave the project or organization altogether.
     - **Example**: In a research group, unresolved conflicts among researchers can lead to talent loss as researchers seek more collaborative and harmonious work environments.
  4. Project Delays and Quality Issues:
     - **Explanation**: Conflict that remains unresolved can disrupt project schedules and potentially compromise the quality of deliverables.
     - **Example**: In a construction project, disputes between subcontractors and the main contractor can lead to delays and subpar workmanship if not addressed promptly.

![image-20240602161827317](/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240602161827317.png)

- **What are the 10 key competencies for running a team based on PMBOK**

  1. **Project Stakeholder Management:** This includes the processes needed to identify, plan, manage, and control stakeholder engagement throughout the project.
  2. **Project Scope Management:** This involves the processes required to determine and manage project expectations and deliverables. It includes planning, authorization, and controls throughout the project.
  3. **Project Time Management:** This encompasses the processes needed to determine and implement the project schedule and manage agreed timelines with appropriate intervention strategies throughout the project.
  4. **Project Cost Management:** This includes the processes required to identify, analyze, refine project costs and ensure that project costs are managed, reported, and controlled throughout the project.
  5. **Project Quality Management:** This covers the processes required to manage quality planning, assurance, control, and improvement processes and policies throughout the project.
  6. **Project Human Resources Management:** This involves the processes required to determine resource needs, prioritize assignments, address development needs, manage performance issues, and conduct evaluations throughout the project.
  7. **Project Communications Management:** This includes the processes required to ensure that timely and appropriate information is collected, disseminated, and evaluated through the management of formal and/or semi-formal structures throughout the project.
  8. **Project Risk Management:** This encompasses the processes required to manage the identification, assessment, treatment, monitoring, controlling, and evaluation of project risks throughout the project.
  9. **Project Procurement Management:** This involves the processes required to manage procurement activities throughout the project.
  10. **Project Integration Management:** This includes the processes required to integrate and balance the project management knowledge areas (all other competencies) throughout the project.

![image-20240602163432456](/Users/lianggeliang/Library/Application Support/typora-user-images/image-20240602163432456.png)



- **What is the difference between ‘lag time’ and ‘lead time’? Discuss and provide examples to support your answer.**

  **1. Lag Time:**

  - **Definition**: Lag time represents a delay or waiting period between the completion of one activity and the start of a successor activity. It introduces a time gap between the two activities.
  - **Effect**: Lag time extends the project schedule by delaying the start of the next task, allowing for a pause or waiting period.
  - **Example**: In construction, after pouring concrete for a foundation (Activity A), there may be a lag time of one week before starting the framing of walls (Activity B). This lag allows the concrete to cure properly before construction continues.

  **2. Lead Time:**

  - **Definition**: Lead time represents a reduction in the time required to complete a task or activity. It allows the successor activity to start before the predecessor activity is fully completed.
  - **Effect**: Lead time compresses the project schedule by overlapping activities and starting the next task earlier.
  - **Example**: In manufacturing, the production of a custom-designed part (Activity A) might take two weeks, but the design team can start working on the next custom part's design (Activity B) one week into the production of the first part. This overlap shortens the overall production time.

  **Key Differences:**

  - **Direction of Time**: Lag time extends the project schedule by adding waiting time, while lead time compresses the schedule by allowing tasks to overlap.
  - **Effect on Schedule**: Lag time introduces delays, while lead time accelerates the schedule.
  - **Purpose**: Lag time is often used to account for natural delays or dependencies between activities, while lead time is used to expedite tasks or gain efficiencies.
  - **Examples**: Lag time involves waiting between activities, while lead time involves starting the next activity before the current one finishes.

- **What scheduling tools are available to the project manager and team to plan the project activities? Discuss.**

  The project schedule is the time-based-sequenced description of all of the project activities. There are 4 main tools in capturing and/or communicating the schedule to the stakeholders: • work breakdown structure (WBS) • program evaluation review technique (PERT) or network diagram • critical path analysis (CPA) • Gantt Chart

  Work Breakdown Structure is essential as part of a project’s lifecycle and timeline. An important part of project planning, the WBS begins with a hierarchy of tasks and levels that help to identify how the project will flow within a designed timeline set by the project manager. Also, it helps to define the specifics of the project outlined in the project scope.

  Network Diagram is essentially a flowchart of the project tasks. The network is created by determining predecessor and successor relationships and connecting the tasks based upon those relationships. In a complex project with many organizations/individuals involved, this technique can provide guidance as to who is the internal customer for each task.

  Critical path analysis is used to determine what the shortest time to complete the project (the longest path through the network). It offers a visual representation of the project activities, presents the time to complete the tasks and the overall project and tracks of critical activities.

  Gantt chart is excellent for tracking progress or activity for tasks once they have been scheduled. It is used for daily/weekly tracking of project progress and it is easy to use and maintain. It creates focus for tracking progress because it is clear to see whether a task should be completed, underway, or pending at any given time.

- **Discuss the differences between ‘transactional’ and ‘transformational’ project leadership. Provide examples to support your answer.**

  **1. Transactional Project Leadership:**

  - **Focus**: Transactional leadership is primarily concerned with the efficient execution of tasks and meeting predefined project objectives.

  - **Leadership Approach**: Transactional leaders use a more traditional and structured leadership approach, emphasizing clear roles, responsibilities, and rules.

  - **Motivation**: Motivation is often based on rewards and punishments, such as recognition, bonuses, or consequences for performance.

  - **Communication**: Communication tends to be one-way, with an emphasis on task instructions and compliance with established processes.

  - Examples

    :

    - A project manager uses a performance-based bonus system to incentivize team members to complete tasks on time and within budget.
    - In a manufacturing project, the project manager relies on strict quality control processes and performance metrics to ensure product quality and compliance with standards.

  **2. Transformational Project Leadership:**

  - **Focus**: Transformational leadership emphasizes long-term vision, innovation, and fostering positive team dynamics.

  - **Leadership Approach**: Transformational leaders inspire and motivate team members to go beyond their self-interests for the benefit of the project.

  - **Motivation**: Motivation is driven by a shared vision, intrinsic rewards, and a sense of purpose and achievement.

  - **Communication**: Transformational leaders engage in open and frequent communication, encouraging team members to express their ideas and providing feedback.

  - Examples

    :

    - A project manager inspires a software development team by sharing a compelling vision of how their work will revolutionize a specific industry, igniting their passion and commitment.
    - A project manager encourages team members to participate in brainstorming sessions, fostering a culture of innovation and creative problem-solving.

  **Key Differences:**

  - **Focus on Vision and Inspiration**: Transformational leadership focuses on inspiring and motivating team members through a shared vision, whereas transactional leadership focuses on task completion and adherence to established procedures.
  - **Motivation Approach**: Transactional leadership uses external rewards and consequences for motivation, while transformational leadership relies on intrinsic motivation and a sense of purpose.
  - **Communication Style**: Transactional leadership often involves one-way communication and task-oriented instructions, while transformational leadership emphasizes open, two-way communication that encourages idea-sharing.
  - **Team Engagement**: Transformational leaders encourage active participation and engagement from team members in shaping the project's direction and outcomes, while transactional leaders rely more on authority and predefined processes.

- **Explain why some conflict is natural and beneficial. Provide examples to support your answer**

  Conflict, to some extent, is a natural and beneficial aspect of human interactions, including those within project teams and organizations. It can foster growth, creativity, and better decision-making when managed constructively. Here are reasons why some conflict is considered natural and beneficial, along with examples to illustrate these points:

  **1. Diverse Perspectives and Ideas:**

  - **Benefit**: Conflict can arise when team members have different perspectives, experiences, and ideas. This diversity can lead to innovative solutions and creative problem-solving.
  - **Example**: In a product development team, engineers and designers may initially have conflicting views on the design of a new product feature. Through constructive conflict, they may develop a more well-rounded and user-friendly solution that combines technical feasibility with aesthetic appeal.

  **2. Improved Decision-Making:**

  - **Benefit**: Conflict encourages thorough discussion and examination of options. When team members with varying viewpoints engage in constructive conflict, it often leads to better-informed decisions.
  - **Example**: During a project planning meeting, team members may have differing opinions on whether to prioritize cost savings or product quality. A healthy debate allows the team to consider various aspects and make a balanced decision that aligns with project goals.

  **3. Identification of Hidden Issues:**

  - **Benefit**: Conflict can bring underlying problems, concerns, or issues to the surface. This allows teams to address these issues proactively, preventing them from becoming more significant challenges later on.
  - **Example**: In a marketing team, a conflict over the effectiveness of a marketing campaign may reveal deeper issues with data accuracy or communication channels. Addressing these underlying problems can lead to more successful future campaigns.

  **4. Increased Engagement and Ownership:**

  - **Benefit**: When team members have the opportunity to voice their opinions and actively participate in discussions, they may feel a stronger sense of ownership and commitment to the project's outcomes.
  - **Example**: In a project team, involving team members in decisions related to task allocation can lead to a higher level of engagement and accountability for completing those tasks successfully.

  **5. Strengthened Relationships:**

  - **Benefit**: When conflict is resolved constructively, it can lead to stronger relationships among team members. Conflict resolution often involves active listening, empathy, and compromise, which can foster trust and respect.
  - **Example**: In a cross-functional project team, conflicts may arise due to differences in work styles or priorities. Through open communication and conflict resolution, team members can better understand each other and collaborate more effectively in the long run.

  While some level of conflict is natural and beneficial, it's essential to differentiate between constructive conflict (which leads to positive outcomes) and destructive conflict (which can be detrimental). Constructive conflict is characterized by respectful disagreement, a focus on issues rather than personal attacks, and a willingness to find mutually beneficial solutions.

- **Describe 5 ways to terminate a project and give examples.**

  1. Extinction:
     - *Definition:* This is the deliberate decision to terminate a project, regardless of its success or progress.
     - *Example:* A pharmaceutical company decides to terminate a drug development project after conducting extensive clinical trials and realizing the drug is not effective and has serious side effects.
  2. Murder:
     - *Definition:* This is a silent and abrupt decision to terminate a project without formal communication or acknowledgment.
     - *Example:* A software development project is quietly abandoned by the management due to internal disagreements, without notifying the project team.
  3. Inclusion:
     - *Definition:* In this case, a successful project is institutionalized, meaning its outcomes, processes, or products become a permanent part of the organization's operations.
     - *Example:* A manufacturing company successfully implements a new lean production process in one of its factories, and the company decides to apply this process to all its other facilities as a standard practice.
  4. Integration:
     - *Definition:* When a project is terminated, but its successful elements or components are integrated into other ongoing projects or business operations.
     - *Example:* An IT project to develop a customer relationship management (CRM) system is terminated due to budget constraints. However, the CRM system's user interface design and data integration features are incorporated into another project aimed at improving customer support.
  5. Starvation:
     - *Definition:* Termination occurs gradually due to budget cutbacks, resource reallocation, or changing organizational priorities.
     - *Example:* A marketing campaign project for a product is starved of resources when the company decides to allocate more resources to a new product launch. As a result, the marketing campaign project is unable to meet its objectives and eventually fizzles out.

- **Differentiate the 3 numerical methods of categorising a project. Which is the mist exhaustive one?**

  1. **Payback period:** The time taken to earn back the money invested in a project, calculated as: **`Payback period = Cost of project / Annual revenue`***Issues:* Doesn't consider the time value of money or the cash-flow period of the project.
  2. **Return on Investment (ROI):** The overall profit on an investment calculated as a percentage (%) of the total amount invested, calculated as: **`ROI = (Net profit / Total investment) × 100`***Issues:* Doesn't consider the time value of money.
  3. **Net Present Value (NPV):** The projected profitability of an investment, based on the future anticipated cash flows and discounting at a stated interest rate. This method is the most exhaustive and is calculated as: **`NPV = Cash flow x Discount factorDiscount factor = 1 / (1 + interest rate)`**

  The most exhaustive method among the three is the **Net Present Value (NPV)** because it takes into account the time value of money by discounting future cash flows at a specified interest rate.

- **What is PERT and list 5 advantages and disadvantages.**

  **PERT (Program Evaluation and Review Technique)** is a project management method used for planning and scheduling complex projects. Here are five advantages and disadvantages of PERT:

  **Advantages:**

  1. **Improved Planning:** PERT helps create a structured project plan.
  2. **Effective Time Management:** It identifies critical paths for better scheduling.
  3. **Risk Assessment:** PERT incorporates uncertainty for better risk management.
  4. **Resource Allocation:** It aids in efficient resource management.
  5. **Visualization:** PERT diagrams provide a visual representation of the project.

  **Disadvantages:**

  1. **Complexity:** PERT can be complex and require expertise.
  2. **Time-Consuming:** Gathering data and estimating activity times can be time-consuming.
  3. **Overemphasis on Critical Paths:** It may overlook non-critical activities.
  4. **Assumptions:** It relies on estimates, leading to uncertainties.
  5. **Limited Flexibility:** PERT may be less adaptable to changes during project execution.

- **What is Life Cycle Thinking? Why is it important?**

  Lifecycle thinking is the consideration of factors beyond the traditional boundaries. Lifecycle thinking is an ideological technique used to analyse and assess projects. In a project management context, life cycle thinking is breaking the project down. The lifecycle is a series of phased stages or decision gates that the project endures from start to close. Each of the stages triggers important documents throughout the project.

  Life Cycle Thinking – ‘Cradle to Grave’

  - Resource Extraction → Production → Consumption → Pollution
  - Extend product life through appropriate design to enhance product. Replacement decision can be influenced through these design strategies. Design for:
    - Reliability & robustness → not easily broken
    - Reparability → simple so that the consumer can perform it
    - Upgradability → simple again
    - Variability → more enduring interest in the product
    - Attachment → disposal of products made harder when emotional attachment
  - 70% of total product costs saved in design.

  Lifecycle Impact Assessment: An impact is a positive or negative result of an effect of a product, process and/or activity including all the social, economic and environmental consequences and implications.

  Lifecycle thinking allows the project manager to see the lasting impact of the project. A lot of project managers see the end of the project as being the handover. With life cycle thinking, the project manager is able to see the impacts their decisions and implementations make on an environmental, social and economic standard.

  The lifecycle thinking provides a holistic view of the project, better able to identify risks and problems, and better able to treat them.

  Benefits:

  - Communicates graphical framework of the total project (an overriding narrative of the total project)
  - Details responsibility
  - Prescribes manageable portions
  - Identifies control gates (limits and/or orders the project’s progress through clearly defined stages)
  - Flags key decisions
  - Nominates milestones and deliverables
  - Provides a point of reference against which stakeholders can assess progress
  - Facilitates appropriate levels of governance throughout the project
  - Promotes a sense of urgency throughout the project

- **Explain the steps in risk management. Give examples for each step.**

  1. Identification:
     - *Definition:* Identify all internal and external sources of risk that have the potential to impact the project.
     - *Example:* In a construction project, potential risks might include adverse weather conditions, labor strikes, material shortages, or changes in building codes. The project team uses risk registers and historical data to identify these risks.
  2. Assessment:
     - *Definition:* Determine both the probability and impact arising from the identified risk sources to calculate their priority.
     - *Example:* Using a 5x5 priority matrix, a project manager assesses that the risk of labor strikes during the construction project has a high probability and a high impact on project timelines and budget, giving it a high priority.
  3. Analysis:
     - *Definition:* Work through all tasks to clearly determine how each risk will impact the project's success.
     - *Example:* For a software development project, a SWOT analysis is conducted to identify strengths, weaknesses, opportunities, and threats. It is determined that a potential threat is a lack of skilled developers, which could lead to delays. An analysis of this risk involves assessing how it might impact the project schedule and budget.
  4. Management:
     - *Definition:* Plan appropriate response strategies to accept, reject, or manage the identified risks.
     - *Example:* In response to the risk of labor strikes, the project manager might decide to mitigate the risk by negotiating labor contracts in advance or by having a contingency plan in place to hire temporary workers if needed. This is done to reduce the impact of the risk on the project.
  5. Evaluation:
     - *Definition:* Review the risk management process and the adequacy of the nominated strategies after the project has been completed.
     - *Example:* After the construction project is finished, the project team reviews the risk register to see how well the identified risks were managed. They find that the strategies put in place to address labor strikes were effective in avoiding delays and cost overruns, but they also identify areas for improvement in handling other risks.

- **Explain how conflicts can be resolved. If the conflict is rapidly evolving, which strategy would you use and why?**

  1. Communication and Open Dialogue:
     - **Description**: Encourage parties involved in the conflict to openly communicate and express their concerns, perspectives, and feelings.
     - **Use When**: This approach is suitable for conflicts where miscommunication, misunderstandings, or lack of information are at the core of the issue. It fosters better understanding and empathy among parties.
  2. Negotiation:
     - **Description**: Parties involved in the conflict engage in discussions to reach a mutually acceptable solution or compromise.
     - **Use When**: Negotiation is effective when both parties are willing to find a middle ground and when the conflict involves differing interests, needs, or preferences.
  3. Mediation:
     - **Description**: A neutral third party (mediator) helps facilitate communication between conflicting parties, assisting them in finding common ground and reaching a resolution.
     - **Use When**: Mediation is valuable when direct communication is strained, and parties need assistance from an unbiased mediator to bridge their differences.
  4. Conflict Coaching:
     - **Description**: A trained conflict coach works with individuals or teams to develop conflict resolution skills and strategies, enabling them to address conflicts more effectively.
     - **Use When**: Conflict coaching is suitable when individuals or teams need guidance and skill-building to handle conflicts autonomously in the future.
  5. Collaborative Problem-Solving:
     - **Description**: Parties work together to analyze the conflict, identify root causes, and collaboratively develop solutions that benefit all parties.
     - **Use When**: Collaborative problem-solving is ideal for conflicts in which a win-win solution is possible, and parties are willing to cooperate to find the best outcome.
  6. Avoidance (for minor conflicts):
     - **Description**: In some cases, it may be appropriate to avoid addressing minor conflicts if they are not critical to the project or relationship. The conflict may naturally resolve itself over time.
     - **Use When**: Avoidance is suitable for minor conflicts that do not have a significant impact and are not worth investing time and resources to resolve.

  If a conflict is rapidly evolving and immediate resolution is required, the strategy to use depends on the specific circumstances:

  - **Communication and Open Dialogue**: This approach is useful when the conflict is escalating due to misunderstandings or miscommunication. Rapidly engaging in open communication can help de-escalate tensions and address the issue promptly.
  - **Negotiation**: If the conflict involves differing interests or demands and requires a quick resolution, negotiation can be effective if the parties are willing to engage in focused discussions.
  - **Mediation**: When the conflict is escalating rapidly and direct communication between parties is deteriorating, involving a mediator can help facilitate a swift resolution by providing an objective perspective and guiding the conversation.

- **Referring to your own group experience, explain the stages of team development.**

  - Forming: Member join and begin the process of defining the group’s purpose,

    structure and leadership.

  - Storming: Intragroup conflict occurs as individuals resist control by the group and

    disagree over leadership.

  - Norming: Close relationship develop as the group becomes cohesive and establishes

    its norms for acceptable behaviour.

  - Performing: A fully functional group structure allows the group to focus on

    performing the task at hand.

  - Adjourning: The group prepares to disband and is no longer concerned with high

    levels of performance.

- **What are the important considerations for good communication? Choose two stakeholders and discuss the some of the barriers to communication.**

  Important considerations for good communication:

  - Information provided in the right format, at the right time, to the right audience with the right impact.
  - Full engagement of speaker and listeners.
  - Continually improve the communication chain.
  - Consider the field of expertise of the stakeholder.
  - Project meetings with a clear agenda and clear objectives.
  - Kick-off meeting to detail the project objectives, expectations, deliverables, outcomes, and benefits; review of all scope inclusions and exclusions.
  - Kick-out meetings to formally close the project.
  - Project performance reports: concise and honest summary of the project’s progression, status, and likely conclusion.
  - Reporting along the reporting continuum (progress, status, and forecast).

  Barriers to communication:

  - Lack of client involvement.
  - Poorly informed stakeholders.
  - Lack of meetings and/or too many meetings leading to little action.
  - Lack of reporting requirements.
  - Poor and incomplete documentation.
  - Frequent scope change.
  - Changing project personnel.
  - Lack of auditing the project to identify lessons learned.

  The reporting continuum: Progress Report (time zero to present): reports on information after it has happened. Status Report (present): reports on the current position of the project against the plan. Forecast Report (completion-oriented): reports against the original completion date, anticipated scope changes, pending risks, approvals pending, escalating issues, expected delays, etc.

- **What are the stages of quality management?**

  Planning: all mandated quality standards, operational definitions, and business requirements relevant to the project are clearly identified and agreed. It then aims to ensure that those same standards can be achieved and measured throughout the project. Eg. benchmarking.

  Assurance: A declaration or guarantee that the overall project performance is evaluated on a regular basis to give all stakeholders the confidence that the relevant quality standards will be satisfied. Eg. Quality audits, a management plan, integrated change control.

  Control: Monitors specific task and project results to identify, measure, eliminate the causes of unsatisfactory performance while ensuring that quality compliance is always demonstrated and achieved. Eg, cause-effect diagrams, Pareto charts, data flow diagrams, etc.

  Improvement: A continuous process performed throughout the project to ensure that a culture, a commitment, and an ownership of what the project is delivering and ultimately, how well it is being delivered. Eg. Regular performance reporting, meetings and debriefs, peer reviews.

- **What are the main budgeting techniques learnt in the course?**

  Traditional: Previous year’s level of performance is the foundation for next year’s figures. Zero-based: Previous years are ignored, and each activity is outlaid and justified. Starts off with zero spending to begin with. Program: Activities are grouped together for projecting costs generated by each major activity or program. Top down: Senior managers pool their knowledge together and use past results to estimate costs, and then these are further broken down to lower level managers. Bottom up: People responsible for directly managing/doing the work will estimate costs, and then these are aggregated to give total project cost

**GENG5505 – Exam Sample questions for ‘Section C’ (answer up to 1- page per question)**

- What are the benefits of managing a project ethically? Discuss and provide examples to support your answer.

  1. **Serving and protecting the public:** Engineering involves advanced expertise that professionals have and the public lacks. Accordingly, professionals stand in a fiduciary relationship with the public. Trust and trustworthiness are essential.
  2. **Guidance:** Codes provide helpful guidance by articulating the main obligations of engineers.
  3. **Inspiration:** Codes provide a positive stimulus for ethical conduct.
  4. **Shared standards:** Since professionals have different moral viewpoints, it is essential that professions establish explicit standards. In this way, the public is assured of a standard of excellence.
  5. **Support for responsible professionals:** Codes provide support to professionals seeking to act ethically.
  6. **Education and mutual understanding:** Codes encourage a shared understanding among professionals, the public, and government organizations about the moral responsibilities of engineers.
  7. **Deterrence and discipline:** Codes can serve as the formal basis for investigating unethical conduct. Professional societies do suspend members whose professional conduct has been proven unethical.
  8. **Contributing to the profession's image:** The reputation of a profession, like the reputation of an individual professional, is essential in sustaining the trust of the public.

  Case 1: “A cafeteria in an office building has comfortable tables and chairs, indeed too comfortable: They invite people to linger longer than the management desires.” Designing uncomfortable chairs and tables to discourage such lingering is not a good idea as it is not ethical. A manager should find other ways to address the issue and communicate the desired behavior without resorting to creating discomfort for customers.

- What are the strengths and weaknesses of the ‘utilitarian’ (or consequences based) ethical theory? Discuss and provide an example to support your answer.

  **Strengths of Utilitarianism:**

  1. **Focus on Well-being:** Utilitarianism places a strong emphasis on promoting the well-being of individuals and society as a whole. It seeks to maximize happiness and minimize suffering, which is a laudable moral goal.

     *Example*: In a healthcare setting, a utilitarian approach may involve allocating limited medical resources, such as vaccines during a pandemic, to prioritize those at the highest risk of severe illness or death, ultimately minimizing overall suffering.

  2. **Objective and Quantifiable:** Utilitarianism provides a relatively objective and quantifiable framework for evaluating ethical dilemmas. It allows for the measurement of consequences and the comparison of alternative actions.

     *Example*: In business ethics, a company may use utilitarian principles to assess the environmental impact of its manufacturing processes. By quantifying the reduction in emissions achieved through a certain environmental initiative, the company can make decisions that maximize utility.

  3. **Flexibility and Adaptability:** Utilitarianism is flexible and adaptable to a wide range of situations and moral dilemmas. It can be applied to personal decisions, public policy, and organizational ethics.

     *Example*: When making public policy decisions related to education, policymakers may use utilitarian principles to allocate resources where they can have the greatest positive impact on students' overall well-being and future prospects.

  **Weaknesses of Utilitarianism:**

  1. **Potential for Minority Suffering:** Utilitarianism may disregard the rights and interests of minorities or individuals if it leads to greater overall happiness. This raises ethical concerns about the treatment of minority groups or individuals with unpopular views.

     *Example*: In a democracy, if the majority supports a policy that restricts the rights of a minority group, a utilitarian perspective may justify this policy, even if it results in the suffering of the minority.

  2. **Difficulty in Predicting Consequences:** Predicting all the consequences of an action accurately can be challenging, making it difficult to apply utilitarian principles in complex situations. Unintended consequences may arise.

     *Example*: In economic decision-making, a government's decision to implement austerity measures to reduce public debt may lead to economic hardship for certain vulnerable populations, even if the initial intention was to improve overall economic stability.

  3. **Quantifying Happiness:** Measuring happiness or utility in a standardized and objective manner is challenging. Different people have varying definitions of happiness, and it's difficult to assign a numeric value to it.

     *Example*: Evaluating the happiness generated by two different policies, such as a tax cut and increased spending on healthcare, may involve subjective judgments and difficulty in quantifying the emotional and social well-being of citizens.

  4. **Lack of Consideration for Rights and Justice:** Utilitarianism may prioritize the majority's happiness at the expense of individual rights and justice. It may justify actions that violate fundamental principles of fairness.

     *Example*: Utilitarianism might support sacrificing the rights of an innocent individual if it prevents widespread panic during a crisis, raising ethical questions about justice and individual rights.

- What is a code of ethics? Discuss the limitations of a code of ethics and provide examples to substantiate your answer.

  Code of ethics state the moral responsibilities of professionals as seen by the profession and as represented by a professional society. It functions as a commitment by the profession as a whole, that engineers will serve the public health, safety and welfare. The code should only be a starting point for ethical behaviour.

  The role of the Code of Ethics for engineers:

  1. **Serving and protecting the public:** Professionals have a fiduciary relationship with the public, and trust and trustworthiness are crucial in ensuring the public's welfare.
  2. **Guidance:** Codes provide valuable guidance by articulating the primary obligations of engineers.
  3. **Inspiration:** They serve as a positive stimulus for ethical behavior, inspired by the collective commitment of professionals.
  4. **Shared standards:** Due to the diversity of moral viewpoints among individual engineers, it is essential for professionals to establish explicit standards that can be universally understood and followed.
  5. **Support for responsible professionals:** The code offers positive support to professionals who are committed to acting ethically.
  6. **Education and mutual understanding:** It encourages a shared understanding among professionals, promoting mutual understanding of ethical expectations.
  7. **Deterrence and discipline:** Professional societies may take disciplinary actions, such as suspension or expulsion, against members whose professional conduct has been proven unethical, serving as a deterrent to unethical behavior.
  8. **Contributing to the profession’s image:** Maintaining ethical standards is vital for sustaining the public's trust in the engineering profession.

  What they can do:

  - Help find answers to ethical dilemmas.
  - Protect against pressures to compromise privacy.
  - Define professional standards of behavior.

  What they cannot do:

  - Force individuals to behave ethically.
  - Provide all the answers to every ethical dilemma.
  - Serve as a universal solution to all ethical challenges.

  Limitations:

  - No substitute for individual responsibility when dealing with real-world ethical dilemmas.
  - Codes may sometimes include only general wording, leaving room for interpretation and vagueness.
  - Despite their value in guiding professional conduct, codes may not cover every ethical nuance and may not be the final word in all situations.

- What are the key attributes of an ethical project manager? Discuss and provide examples to substantiate your answer.

  1. Integrity:
     - **Attribute**: Ethical project managers exhibit honesty and truthfulness in all their dealings. They uphold moral and professional principles even when facing difficult decisions.
     - **Example**: An ethical project manager openly communicates project risks, including potential delays or budget overruns, to stakeholders, even when such information may be unfavorable.
  2. Transparency:
     - **Attribute**: Ethical project managers are transparent in their actions and decisions, providing stakeholders with accurate and complete information about project progress, challenges, and risks.
     - **Example**: A project manager shares all relevant project documentation, such as project plans, budgets, and schedules, with team members and stakeholders, ensuring everyone is well-informed.
  3. Accountability:
     - **Attribute**: Ethical project managers take responsibility for their actions and decisions. They acknowledge mistakes and work to rectify them.
     - **Example**: If a project manager realizes that a critical task was overlooked, they admit the oversight, adjust the project plan, and work with the team to find a solution without blaming others.
  4. Fairness and Equity:
     - **Attribute**: Ethical project managers treat all team members and stakeholders fairly and impartially, ensuring that opportunities and resources are distributed equitably.
     - **Example**: When assigning tasks or responsibilities, an ethical project manager considers team members' skills and workload, avoiding favoritism or bias.
  5. Respect for Diversity and Inclusion:
     - **Attribute**: Ethical project managers value and respect diversity among team members and stakeholders, fostering an inclusive and respectful work environment.
     - **Example**: An ethical project manager encourages open dialogue and welcomes diverse perspectives, ensuring that all team members' voices are heard and valued.
  6. Confidentiality:
     - **Attribute**: Ethical project managers safeguard sensitive or confidential information, respecting the privacy of individuals and the organization.
     - **Example**: When handling proprietary or confidential data in a technology project, an ethical project manager ensures that access is restricted to authorized personnel and that data security measures are in place.
  7. Stakeholder Consideration:
     - **Attribute**: Ethical project managers prioritize the interests and well-being of all project stakeholders, including clients, team members, and the broader community.
     - **Example**: In an urban development project, an ethical project manager balances the project's economic benefits with its potential impact on the local environment and community, striving for a sustainable and socially responsible outcome.
  8. Ethical Leadership:
     - **Attribute**: Ethical project managers lead by example, demonstrating ethical behavior and values to inspire their teams and stakeholders.
     - **Example**: An ethical project manager consistently adheres to ethical principles and encourages team members to do the same, fostering a culture of integrity within the project team.
  9. Adherence to Ethical Codes and Standards:
     - **Attribute**: Ethical project managers follow established ethical codes and standards relevant to their profession or industry, ensuring compliance with best practices.
     - **Example**: In healthcare project management, an ethical project manager adheres to the industry's ethical guidelines, such as patient confidentiality and informed consent, to ensure ethical healthcare delivery.

- What are the Universal Moral Values for Corporate Codes of Ethics studied in the course? Discuss and provide examples to support your answer.

  According to Schwartz, universal moral values are generated by considering three sources: (1) Corporate codes of ethics; (2) Global codes of ethics; and (3) The business ethics literature.

  The proposed universal moral values include:

  1. Trustworthiness (i.e., integrity, honesty, loyalty, transparency, etc.);
  2. Respect (i.e., respect for human rights);
  3. Responsibility (i.e., accountability, self-restraint, etc.);
  4. Fairness (i.e., equity, impartiality, etc.);
  5. Caring (i.e., do no harm); and
  6. Citizenship (i.e., triple bottom line, life cycle thinking, obeying the law, etc.).

  Due to globalization, companies operate in many countries and often work with people from different nationalities and cultures. It is important to respect other cultures and avoid discrimination based on religion, culture, or other factors, in alignment with these universal moral values.

- Who are value-based project leaders? How do they help in thinking about putting ethics and leadership together?

  **Value-based project leaders** are individuals who prioritize and integrate ethical values and principles into their project leadership roles. They recognize the importance of aligning their leadership practices with ethical considerations and guiding their teams and organizations toward responsible and morally sound outcomes. Here's how value-based project leaders contribute to the intersection of ethics and leadership:

  1. Setting Ethical Expectations:
     - Value-based project leaders establish clear expectations regarding ethical behavior within their teams and organizations. They communicate the importance of ethical conduct and the adherence to ethical codes and principles.
  2. Modeling Ethical Behavior:
     - These leaders lead by example, demonstrating ethical behavior in their actions and decisions. They serve as role models for their teams, showing that ethical conduct is not just a theoretical concept but an integral part of leadership.
  3. Promoting Accountability:
     - Value-based project leaders hold themselves and their teams accountable for ethical conduct. They create a culture of accountability where individuals are responsible for their actions and ethical decision-making.
  4. Ethical Decision-Making:
     - They guide their teams through ethical decision-making processes, helping them assess complex situations and make choices that align with ethical values and organizational goals.
  5. Balancing Stakeholder Interests:
     - Value-based project leaders consider the interests of all stakeholders, including employees, clients, communities, and the environment, when making project decisions. They seek to balance these interests ethically.
  6. Addressing Ethical Dilemmas:
     - When faced with ethical dilemmas, these leaders engage in open and transparent discussions with their teams to explore possible solutions that align with ethical principles.
  7. Supporting Ethical Training and Development:
     - They invest in the ethical training and development of their team members, providing resources and opportunities for individuals to enhance their ethical decision-making skills.
  8. Environmental and Social Responsibility:
     - Value-based project leaders incorporate considerations of environmental and social responsibility into their project planning and execution. They strive to minimize negative impacts and promote positive contributions to society.
  9. Promoting Diversity and Inclusion:
     - They foster diverse and inclusive work environments, recognizing that diversity of perspectives and backgrounds can lead to better ethical decision-making and innovation.
  10. Stakeholder Engagement:
      - These leaders actively engage with stakeholders to understand their concerns, needs, and ethical expectations. They incorporate stakeholder feedback into project planning and decision-making.
  11. Long-Term Sustainability:
      - Value-based project leaders prioritize the long-term sustainability of projects and organizations, considering the ethical implications of decisions on future generations.
  12. Ethical Communication:
      - They communicate openly and honestly about ethical matters, including potential risks and dilemmas, with their teams and stakeholders.

- **Describe the utilitarianism, deontology, and virtue-based approaches to Ethics.**

  Utilitarianism: An action is judged as ethical or unethical based on the consequence or outcome. This is a future-looking approach with the thinking that ‘the end justifies the means’. It considers the action which has the greatest good for the greatest number.

  **Issues**: • Minority rights at risk • Who decides what ‘good’ is? • Assumes that the end justifies the means (regardless of the means) • Who decides what counts as the benefit and costs to be measured in cost-benefit analysis? • Can a standard measure be reached? • What counts as consequences? • How far into the future should we look?

  **Examples**: • Cost-benefit analysis • A pharmaceutical company releasing a new drug with a few side effects. The drug is beneficial to many people and side effects trouble a smaller amount. • Ford Pinto case: decision to not reposition fuel tank in vehicle design from a vulnerable position to collision due to cost-benefit analysis.

  Deontological: Actions are judged as ethical standing along and without regard to consequence. This is a backward-looking, duty-based approach and the idea of ‘means rather than ends’. Based on the idea that we are all morally obliged to follow fundamental rules and principles regardless of consequences. Unconditional requirements:

  1. Act as if, through your actions, you were making universal law for everyone to follow.

  2. Always treat any human being (self-included) as an end in himself/herself, never as a means to an end.

  3. Act as if you were a member of a community of fellow moral legislators who were ends in themselves.

     **Issues**: • Suppose that the impacts are known • Is the list of principles to follow exhaustive? • What if an individual has values over and above the set values?

     **Example**: • (video) Man turning down the promotion offer which required him to commit forgery as it when against principles.

  