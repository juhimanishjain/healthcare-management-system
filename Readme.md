CS 520: Project Documentation Template


Spring 2025, University of Massachusetts Amherst
Name: Steven Tang /Fukiburi              Name: Isha Bang / ibang@umass.edu         
Name: Juhi Manish Jain /juhimanishjain             Name: Anthony Rozet /AnthonyRoze
Team Name: The Chefs        
Github Repo Link: https://github.com/juhimanishjain/healthcare-management-system
Google Doc Link: https://docs.google.com/document/d/1876DfGrd9LIjBCxCrz_2MzmZrnob5vEW_sdT3phsg-w/edit?usp=sharing


1. Requirements


        1.1. Overview


The importance of digitalized patient information management comes from efficiency and accessibility, as by eliminating manual paperwork the accessibility to patient records becomes easier and more efficient. In addition to this, with digital systems patient records can be updated in real time. There is also increased patient safety as there would be less room for error and updates can be easily made if needed. AI tools can help provide personalized treatments, and telehealth support allows accessibility to healthcare from wherever people need. 


        1.2. Features


* Calendar
* Appointment Scheduler
* Adjustable font size / theme / icon size etc for accessibility.
* Securely store and view health documents
* Prescription viewer


















        1.3. Functional Requirements (Use cases)



- As an admin, I want to manage user roles and permissions to control access to patient data. If a user  does not have an account, they should be denied access. If they have an account but do not have the appropriate user role and permissions, they should be denied access. (They should be able to ask to be granted access.) If they have an account and do have the appropriate user role and permissions, they should be granted access.
- As a patient, I want to be able to view the doctor’s open time slots and schedule appointments for myself. As an assistant (or doctor), I want to be able to rearrange the schedule and notify those affected.
- As a patient I want to view current (or past) medications, and their purposes/directions.
- As a doctor, I want the ability to view patient medical history and outcomes of treatment from previous physicians. This privilege should come to effect only while I am professionally involved with the patient. I should still be able to see and append to any patient records that I previously submitted. 
- As a patient I want to be able to view my own medical history, including any vaccinations I have been given in the past or medications I have been prescribed to. I should be able to do this regardless of which physician I am currently seeking treatment from.
- As a nurse, or any care provider at a visit, or procedure, I want to be able to track and log patients' vitals in real-time. This will ensure all of the patients’ records are updated and available. 
- As a patient, I want to be able to securely message my doctor or healthcare provider so that I can ask follow-up questions, discuss concerns about my treatment, or request prescription refills without needing an in-person visit.


- As an administrator, I want to monitor system usage and detect unauthorized access attempts so that I can ensure data security and prevent potential breaches that might compromise sensitive patient information.
        
















        1.4. Non-Functional Requirements

- Telehealth services will have a wait or hold time shorter than one hour. 
- The platform should accommodate users with disabilities, with a simple and accessible layout as well as the ability to customize their experience. 


- The system should be able to handle a sizable amount of users. If the system is under stress, doctors will be prioritized at the expense of other users. 


- The login portal will have two factor authentication.


        1.5. Challenges & Risks


           Briefly discuss the potential challenges and risks with your project.
* It may be difficult to account for and encompass all possible accommodations as the interface may be limited to visual and perhaps auditory services.


* Many hospitals and clinics already use various Electronic Health Record (EHR) platforms. Seamlessly integrating with these systems can be challenging due to differing data formats, standards, and proprietary APIs, potentially slowing adoption or causing data inconsistencies.


* Ensuring secure storage and transmission of sensitive patient data is essential, especially given stringent regulations (e.g., HIPAA). Any breach or mishandling of information could lead to legal repercussions and loss of user trust.