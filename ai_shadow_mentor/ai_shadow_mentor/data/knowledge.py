"""Static knowledge base: roles, required skills, learning resources, salaries, trends."""

ROLES = {
  "Machine Learning Engineer": {
    "skills": {"Python":1,"Statistics":1,"Machine Learning":1,"Deep Learning":2,"TensorFlow/PyTorch":2,"SQL":1,"Git":1,"MLOps":3,"Docker":3,"Cloud (AWS/GCP/Azure)":3},
    "salary": {"Fresher":(6,12),"1-3 years":(12,22),"3-5 years":(22,38),"5+ years":(38,70)},
    "demand": 92, "growth": "+34% YoY", "companies": ["Google","Microsoft","Amazon","Flipkart","NVIDIA"]},
  "Data Scientist": {
    "skills": {"Python":1,"Statistics":1,"SQL":1,"Pandas/NumPy":1,"Data Visualization":1,"Machine Learning":2,"Feature Engineering":2,"A/B Testing":3,"Big Data (Spark)":3},
    "salary": {"Fresher":(5,10),"1-3 years":(10,20),"3-5 years":(20,34),"5+ years":(34,60)},
    "demand": 88, "growth": "+28% YoY", "companies": ["Deloitte","Fractal","Mu Sigma","Accenture","Swiggy"]},
  "Data Analyst": {
    "skills": {"Excel":1,"SQL":1,"Python":2,"Data Visualization":1,"Power BI/Tableau":2,"Statistics":2,"Communication":2},
    "salary": {"Fresher":(3,7),"1-3 years":(6,12),"3-5 years":(12,20),"5+ years":(20,35)},
    "demand": 85, "growth": "+22% YoY", "companies": ["TCS","Infosys","Wipro","Amazon","Zomato"]},
  "AI/NLP Engineer": {
    "skills": {"Python":1,"Machine Learning":1,"Deep Learning":2,"NLP":2,"Transformers":3,"LLMs & Prompting":3,"Vector Databases":3,"APIs":2,"Docker":3},
    "salary": {"Fresher":(7,14),"1-3 years":(14,26),"3-5 years":(26,45),"5+ years":(45,85)},
    "demand": 95, "growth": "+48% YoY", "companies": ["OpenAI","Anthropic","Google","Sarvam AI","Krutrim"]},
  "Full Stack Developer": {
    "skills": {"HTML/CSS":1,"JavaScript":1,"React":2,"Node.js":2,"SQL":2,"REST APIs":2,"Git":1,"Docker":3,"System Design":3},
    "salary": {"Fresher":(4,9),"1-3 years":(9,18),"3-5 years":(18,32),"5+ years":(32,55)},
    "demand": 86, "growth": "+18% YoY", "companies": ["Zoho","Freshworks","Atlassian","Razorpay","Paytm"]},
  "Cloud Engineer": {
    "skills": {"Linux":1,"Networking":1,"Cloud (AWS/GCP/Azure)":1,"Docker":2,"Kubernetes":3,"Terraform":3,"CI/CD":2,"Python":2},
    "salary": {"Fresher":(4,9),"1-3 years":(9,18),"3-5 years":(18,32),"5+ years":(32,58)},
    "demand": 87, "growth": "+26% YoY", "companies": ["AWS","Microsoft","Infosys","Capgemini","Oracle"]},
  "Cybersecurity Analyst": {
    "skills": {"Networking":1,"Linux":1,"Security Fundamentals":1,"Python":2,"SIEM Tools":2,"Ethical Hacking":3,"Cryptography":3,"Cloud Security":3},
    "salary": {"Fresher":(4,8),"1-3 years":(8,16),"3-5 years":(16,28),"5+ years":(28,50)},
    "demand": 84, "growth": "+31% YoY", "companies": ["Palo Alto","CrowdStrike","Cisco","Wipro","IBM"]},
}

RESOURCES = {
  "Python":("Python for Everybody","https://www.py4e.com","2-4 weeks"),
  "Statistics":("Khan Academy Statistics","https://www.khanacademy.org/math/statistics-probability","3 weeks"),
  "Machine Learning":("Andrew Ng ML Specialization","https://www.coursera.org/specializations/machine-learning-introduction","6 weeks"),
  "Deep Learning":("fast.ai Practical Deep Learning","https://course.fast.ai","6 weeks"),
  "TensorFlow/PyTorch":("PyTorch Tutorials","https://pytorch.org/tutorials","3 weeks"),
  "SQL":("Mode SQL Tutorial","https://mode.com/sql-tutorial","2 weeks"),
  "Git":("Git & GitHub for Beginners","https://www.freecodecamp.org/news/git-and-github-for-beginners","1 week"),
  "MLOps":("Made With ML","https://madewithml.com","4 weeks"),
  "Docker":("Docker Get Started","https://docs.docker.com/get-started","2 weeks"),
  "Cloud (AWS/GCP/Azure)":("AWS Cloud Practitioner Essentials","https://aws.amazon.com/training","3 weeks"),
  "Pandas/NumPy":("Kaggle Pandas Course","https://www.kaggle.com/learn/pandas","2 weeks"),
  "Data Visualization":("Kaggle Data Visualization","https://www.kaggle.com/learn/data-visualization","1 week"),
  "Feature Engineering":("Kaggle Feature Engineering","https://www.kaggle.com/learn/feature-engineering","2 weeks"),
  "A/B Testing":("Udacity A/B Testing","https://www.udacity.com/course/ab-testing--ud257","2 weeks"),
  "Big Data (Spark)":("Apache Spark Docs","https://spark.apache.org/docs/latest","3 weeks"),
  "Excel":("ExcelIsFun (YouTube)","https://www.youtube.com/user/ExcelIsFun","2 weeks"),
  "Power BI/Tableau":("Microsoft Learn Power BI","https://learn.microsoft.com/power-bi","3 weeks"),
  "Communication":("Storytelling with Data","https://www.storytellingwithdata.com","2 weeks"),
  "NLP":("Hugging Face NLP Course","https://huggingface.co/learn/nlp-course","4 weeks"),
  "Transformers":("The Illustrated Transformer","https://jalammar.github.io/illustrated-transformer","2 weeks"),
  "LLMs & Prompting":("Prompt Engineering Guide","https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview","2 weeks"),
  "Vector Databases":("Pinecone Learning Center","https://www.pinecone.io/learn","2 weeks"),
  "APIs":("REST API Tutorial","https://restfulapi.net","1 week"),
  "REST APIs":("REST API Tutorial","https://restfulapi.net","1 week"),
  "HTML/CSS":("freeCodeCamp Responsive Web Design","https://www.freecodecamp.org/learn","3 weeks"),
  "JavaScript":("JavaScript.info","https://javascript.info","4 weeks"),
  "React":("React Official Tutorial","https://react.dev/learn","3 weeks"),
  "Node.js":("Node.js Learn","https://nodejs.org/en/learn","3 weeks"),
  "System Design":("System Design Primer","https://github.com/donnemartin/system-design-primer","6 weeks"),
  "Linux":("Linux Journey","https://linuxjourney.com","2 weeks"),
  "Networking":("Professor Messer Network+","https://www.professormesser.com","3 weeks"),
  "Kubernetes":("Kubernetes Basics","https://kubernetes.io/docs/tutorials/kubernetes-basics","3 weeks"),
  "Terraform":("HashiCorp Terraform Tutorials","https://developer.hashicorp.com/terraform/tutorials","3 weeks"),
  "CI/CD":("GitHub Actions Docs","https://docs.github.com/actions","1 week"),
  "Security Fundamentals":("Cybrary Intro to IT & Security","https://www.cybrary.it","3 weeks"),
  "SIEM Tools":("Splunk Fundamentals","https://www.splunk.com/en_us/training.html","2 weeks"),
  "Ethical Hacking":("TryHackMe","https://tryhackme.com","6 weeks"),
  "Cryptography":("Cryptography I (Stanford)","https://www.coursera.org/learn/crypto","4 weeks"),
  "Cloud Security":("Cloud Security Alliance Training","https://cloudsecurityalliance.org/education","3 weeks"),
}

PROJECTS = {
  "Machine Learning Engineer":["Build and deploy an image classifier with FastAPI + Docker","Predictive maintenance model with MLflow tracking"],
  "Data Scientist":["Customer churn prediction with a dashboard","Kaggle competition top-20% submission"],
  "Data Analyst":["Sales dashboard in Power BI","SQL + Python analysis of a public dataset"],
  "AI/NLP Engineer":["RAG chatbot over your own documents","Fine-tune a sentiment classifier on Hugging Face"],
  "Full Stack Developer":["E-commerce app with payments","Real-time chat app with WebSockets"],
  "Cloud Engineer":["Deploy a 3-tier app on AWS with Terraform","CI/CD pipeline to Kubernetes"],
  "Cybersecurity Analyst":["Home SOC lab with Splunk","Complete 20 TryHackMe rooms"],
}

LEVEL = {1:"Beginner",2:"Intermediate",3:"Advanced"}

FAQ = [
 (["hello","hi","hey"],"Hi! I'm your AI Shadow Mentor. Ask me about career paths, skills to learn, salaries, interviews or resumes."),
 (["start","begin","beginner","where do i"],"Start with Python + SQL, build 2-3 small projects, then pick a specialization (ML, Data, Cloud, Full Stack). Use the Skill Gap Analyzer to see exactly what you're missing."),
 (["resume","cv"],"Keep your resume to 1 page. Lead with projects (problem, approach, measurable result), list skills by relevance, and add GitHub/LinkedIn links."),
 (["interview"],"Prepare: 1) fundamentals of your role, 2) two projects you can explain deeply, 3) DSA/SQL practice, 4) STAR-format behavioral stories. Do mock interviews weekly."),
 (["project"],"Pick projects that mirror real work: end-to-end, deployed, with a README and demo. The Roadmap page lists role-specific project ideas."),
 (["certif"],"Useful certifications for freshers: AWS Cloud Practitioner, Google Data Analytics, TensorFlow Developer, Azure AI-900. Projects plus certs beat either alone."),
 (["fresher","no experience","entry"],"Freshers: build 3 solid projects, contribute to open source, do internships, and network on LinkedIn. Target Junior/Associate/Trainee titles."),
 (["switch","transition","change career"],"Map your transferable skills first (the Skill Gap Analyzer helps), learn the 2-3 missing core skills, build a bridge project, then target hybrid roles."),
 (["thank"],"You're welcome! Keep going. Consistency beats intensity."),
]
