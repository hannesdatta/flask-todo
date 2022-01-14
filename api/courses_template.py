
course ={
  "name": "Online Data Collection and Management",
  "description": "Learn how to scrape the web!",
  "id": 1,
  "users": [], # leeg laten
  "modules": [
    {
      "name": "Week 1",
      "description": "1. Getting started with R!",
      "id": 1,
      "order": 1,
      "deadline": "", #"2022-01-31",
      "items": [
        {"category_name": "1. Get started installing your computer!",
         "id": 1,
         "description": "To follow this course and work on your team project later on, it is necessary to have installed the software, so make sure to complete this part right away!",
         "items" : [
            {
              "name": "Install R & RStudio",
              "id": "task_odcm_1_1_1",
              "description": "R & R Studio are the workhorse in this course - make sure to install it right away!",
              "links": ["https://tilburgsciencehub.com/get/r"]
            },
            {
              "name": "Install Git and make an account on GitHub",
              "id": "task_odcm_1_1_2",
              "description": "Git allows you to have an unlimited 'version history' - so you can always go back to any version of the file ever made. Get started now!",
              "links": ["https://tilburgsciencehub.com/get/git"]
            },
            {
              "name": "Install make",
              "id": "task_odcm_1_1_3",
              "description": "Make is like a robot, that runs your entire project from beginning to end! Sit back & relax, while you see your project come together!",
              "links": ["https://tilburgsciencehub.com/get/make"]
            },
            {
              "name": "Install Hugo",
              "id": "task_odcm_1_1_4",
              "description": "Hugo is a framework which we use to run our course website locally!",
              "links": ["https://gohugo.io/getting-started/installing/"]
            },
            {
              "name": "Verify that you have a premium account at Datacamp (i.e., mailed the library).",
              "id": "task_odcm_1_1_5",
              "description": "We use Datacamp in this class, but you need to go through a quite cumbersome onboarding procedure with the University library. Do this soon so you can enjoy premium content without having to pay for it!",
              "links": ["https://dprep.hannesdatta.com/docs/course/support/datacamp/"]
            }]
            },
        {"category_name": "2. Familiarize with Scrum",
        "id": 2,
        "description": "Scrum is avery flexible way to work in teams, so get acquainted with it and use it with your project group later on!",
        "items" : [
            {
            "name": "Read the page on using Scrum on TSH.",
            "id": "task_odcm_1_2_1",
            "description": "Scrum is an effective way to collaborate with team members – Read through this article on TSH!",
            "links": ["https://tilburgsciencehub.com/learn/scrum"]
            },
            {
            "name": "Understand what the benefits are of using the scrum framework.",
            "id": "task_odcm_1_2_1",
            "description": "Scrum is an effective way to collaborate with team members – Read through this article on TSH!",
            "links": ["https://tilburgsciencehub.com/learn/scrum"]
            }]
            },
        {"category_name": "3. Readings",
         "id": 3,
          "description": "This week introduces one reading on gathering and selecting data.",
          "items": [
              {
              "name": "Read the paper on data selection and procurement (Mela, 2011).",
              "id": "task_odcm_1_3_1",
              "description": "This paper shows the process of gathering and selecting data and what should be taken into account.",
              "links": ["https://pubsonline.informs.org/doi/abs/10.1287/mksc.1110.0650"]
             }
            ]},
        {"category_name": "4. R Bootcamp Tutorial",
         "id": 4,
          "description": "This tutorial will introduce you to R and teach you the basic skills that you will use a lot when working with data.",
          "items": [
              {
              "name": "Know about data types in R (characteric, numeric, vector etc.)",
              "id": "task_odcm_1_4_1",
              "description": "Data types are used to constrain the values that an expression might take. You will use these a lot while programming!",
              "links": ["https://datacarpentry.org/r-socialsci/"]
             },
             {
              "name": "Ability to load datasets in R and perform some data inspection tasks.",
              "id": "task_odcm_1_4_2",
              "description": "These are generally the first things you do; loading the data and getting a glimpse of it.",
              "links": ["https://datacarpentry.org/r-socialsci/"]
             },
             {
              "name": "Know what a factor is and how to convert and rename these.",
              "id": "task_odcm_1_4_3",
              "description": "Factors are variables which take on a certain number of different values.",
              "links": ["https://datacarpentry.org/r-socialsci/"]
             },
             {
              "name": "Understand what a pipeline (%>%) is in R and be able to work with these",
              "id": "task_odcm_1_4_4",
              "description": "Pipelines are a great way to combine multiple operations and simplify your code!",
              "links": ["https://datacarpentry.org/r-socialsci/"]
             },
             {
              "name": "Know how to use data manipulation codes such as filter, group_by and mutate",
              "id": "task_odcm_1_4_5",
              "description": "These are common manipulation tasks that you will use very often when analyzing data.",
              "links": ["https://datacarpentry.org/r-socialsci/"]
             },
             {
             "name": "Know how to export data and write a cleaned dataset to a csv file",
             "id": "task_odcm_1_4_6",
             "description": "Once you have cleaned a dataset, you can store the cleaned datafile in a csv by using the write_csv function in R!",
             "links": ["https://datacarpentry.org/r-socialsci/"]
             }
             ]
            }
            ]
  },
  {
    "name": "Week 2",
    "description": "Let's start to scrape!",
    "id": 2,
    "order": 1,
    "deadline": "2022-01-31",
    "items": [
      {"category_name": "1. Kick-starting the week",
       "id": 1,
       "description": "",
       "items" : [
          {
            "name": "Watch the energizer for this week",
            "id": "task_odcm_2_1_1",
            "description": "To get acquainted with this week's course material, watch the energizer!",
            "links": ["TBA"]
          }]},
      {"category_name": "2. Readings on workflow management",
       "id": 2,
       "description": "",
       "items" : [
          {
            "name": "Read the readings on managing your workflow and its importance on TilburgScienceHub",
            "id": "task_odcm_2_2_1",
            "description": "Managing your workflow is an important way to bring structure to your project and improve reproducability!",
            "links": ["https://tilburgsciencehub.com/learn/project-setup"]
          },
          {
            "name": "Read the optional reading on best practices for data projects",
            "id": "task_odcm_2_2_2",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["https://www.shirokuriwaki.com/programming/project-organization.html"]
          },
          {
            "name": "Read the optional reading on code and data for Social Sciences",
            "id": "task_odcm_2_2_3",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["https://www.brown.edu/Research/Shapiro/pdfs/CodeAndData.pdf"]
          },
          {
            "name": "Read the optional reading on data analysis workflow",
            "id": "task_odcm_2_2_4",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["http://www.coordinationtoolkit.org/wp-content/uploads/130907-Data-flow.pdf"]
          },
          {
            "name": "Look through this paper to further familiarize yourself with this week’s content",
            "id": "task_odcm_2_2_5",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["https://www.tse-fr.eu/sites/default/files/TSE/documents/doc/wp/2018/wp_tse_933.pdf"]
          }]},
        {"category_name": "3. Command line skills",
         "id": 3,
         "description": "",
         "items" : [
            {
              "name": "Get an understanding of what the command line/terminal is by looking through the slides.",
              "id": "task_odcm_2_3_1",
              "description": "These slides are especially beneficial for students that are using a Mac, but also gives you a good overall understanding of the command line and how we use it!",
              "links": ["https://generalassembly.github.io/prework/cl"]
            },
            {
              "name": "Complete the first chapter of the Introduction to Shell on Datacamp",
              "id": "task_odcm_2_3_2",
              "description": "Navigating through directories is a task you will often do when using Git Bash for example, so make sure to complete this tutorial!",
              "links": ["https://learn.datacamp.com/courses/introduction-to-shell"]
            }]},
        {"category_name": "4. Git & Github",
         "id": 4,
         "description": "",
         "items" : [
            {
              "name": "Follow the short Github introduction on issues, pull requests and commits",
              "id": "task_odcm_2_4_1",
              "description": "This Github introduction will walk you through the basics of using Git and Github for your project!",
              "links": ["https://lab.github.com/githubtraining/introduction-to-github"]
            },
            {
              "name": "Understand why we use Git over Google drive when working on code with others",
              "id": "task_odcm_2_4_2",
              "description": "Git is a very effective way to collaborate on projects with code. Do you understand the benefits of Git over Google Drive?",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            },
            {
              "name": "Create the version-control-exercises repository on Github and clone it",
              "id": "task_odcm_2_4_3",
              "description": "To get a repository from Github to your local computer, you will need to use git clone!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            },
            {
              "name": "Understand the process of making changes to files and pushing these using Git (git add, commit etc.)",
              "id": "task_odcm_2_4_4",
              "description": "This is an iterative process that you will be performing often, so make sure you fully understand this!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            },
            {
              "name": "Be able to clone a repository, make changes to this repository and then push these changes to Github",
              "id": "task_odcm_2_4_5",
              "description": "When you made changes on your local computer, you want this to be transferred to the main repository on Github. For that, we use git push!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            },
            {
              "name": "Know how to find the history of a project and know how to roll back to a previous version of a project on Github using a hash",
              "id": "task_odcm_2_4_6",
              "description": "Everyone makes mistakes. Luckily, Git and Github allow you to easily roll back to previous versions of a project, should this be necessary.",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            },
            {
              "name": "Understand what a gitignore file is used for and why this is used",
              "id": "task_odcm_2_4_7",
              "description": "You don't always want Git to track every file that you create or make a change to (take large csv files for example). Using gitignore, Git will stop tracking these files!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            },
            {
              "name": "Know how to work on a branch of a project and the concept of merging branches with each other",
              "id": "task_odcm_2_4_8",
              "description": "Branches are ways to work on different parts of a project simultaneously with team members. These branches can be merged after being pushed.",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            },
            {
              "name": "Know how to fork an existing repository of someone else",
              "id": "task_odcm_2_4_9",
              "description": "Forking allows you to propose changes to projects of others and is useful for open-source collaboration!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"]
            }]}],

         "modules": []
   }
 ]
}


print(course)
