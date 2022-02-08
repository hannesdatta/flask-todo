from tinydb import TinyDB, Query
from flask_login import UserMixin
from datetime import datetime


course_dprep ={
  "name": "Data Preparation and Workflow Management",
  "description": "Learn how to efficiently manage empirical research projects!",
  "id": 1,
  "users": [], # leeg laten
  "modules": [
    {
      "name": "Week 1",
      "description": "Getting started with R!",
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
              "id": "task_dprep_1_1_1",
              "description": "R & R Studio are the workhorses in this course - make sure to install them right away!",
              "links": ["https://tilburgsciencehub.com/get/r"],
              "optional": True
            },
            {
              "name": "Install Git and make an account on GitHub",
              "id": "task_dprep_1_1_2",
              "description": "Git allows you to have an unlimited 'version history' - so you can always go back to any version of the file ever made. Get started now!",
              "links": ["https://tilburgsciencehub.com/get/git"],
              "optional":  False
            },
            {
              "name": "Install make",
              "id": "task_dprep_1_1_3",
              "description": "Make is like a robot, that runs your entire project from beginning to end! Sit back & relax, while you see your project come together!",
              "links": ["https://tilburgsciencehub.com/get/make"],
              "optional":  False
            },
            {
              "name": "Install Hugo",
              "id": "task_dprep_1_1_4",
              "description": "Hugo is a framework which we use to run our course website on your local computer!",
              "links": ["https://gohugo.io/getting-started/installing/"],
              "optional":  False
            },
            {
              "name": "Verify that you have a premium account at Datacamp (i.e., mailed the library)",
              "id": "task_dprep_1_1_5",
              "description": "We use Datacamp in this class, but you need to go through a quite cumbersome onboarding procedure with the University library. Do this soon so you can enjoy premium content without having to pay for it!",
              "links": ["https://dprep.hannesdatta.com/docs/course/support/datacamp/"],
              "optional":  False
            }]
            },
        {"category_name": "2. Familiarize with Scrum",
        "id": 2,
        "description": "Scrum is a very flexible way to work in teams, so get acquainted with it and use it with your project group later on!",
        "items" : [
            {
            "name": "Read the page on using Scrum on TSH",
            "id": "task_dprep_1_2_1",
            "description": "Scrum is an effective way to collaborate with team members – Read through this article on TSH!",
            "links": ["https://tilburgsciencehub.com/learn/scrum"],
            "optional" : False
            },
            {
            "name": "Understand what the benefits are of using the scrum framework",
            "id": "task_dprep_1_2_1",
            "description": "Scrum is a very flexible way to work in teams, so get acquainted with it and use it with your project group later on!",
            "links": ["https://tilburgsciencehub.com/learn/scrum"],
            "optional" : False
            }]
            },
        {"category_name": "3. Readings",
         "id": 3,
          "description": "This week introduces one reading on gathering and selecting data",
          "items": [
              {
              "name": "Read the paper on data selection and procurement (Mela, 2011)",
              "id": "task_dprep_1_3_1",
              "description": "This paper shows the process of gathering and selecting data and what should be taken into account",
              "links": ["https://pubsonline.informs.org/doi/abs/10.1287/mksc.1110.0650"],
              "optional" : False
             }
            ]},
        {"category_name": "4. R Bootcamp Tutorial",
         "id": 4,
          "description": "This tutorial will introduce you to R and teach you the basic skills that you will use a lot when working with data",
          "items": [
              {
              "name": "Know about data types in R (characteric, numeric, vector etc.)",
              "id": "task_dprep_1_4_1",
              "description": "Data types are used to constrain the values that an expression might take. You will use these a lot while programming!",
              "links": ["https://datacarpentry.org/r-socialsci/"],
              "optional" : False
             },
             {
              "name": "Ability to load datasets in R and perform some data inspection tasks",
              "id": "task_dprep_1_4_2",
              "description": "These are generally the first things you do; loading the data and getting a glimpse of it",
              "links": ["https://datacarpentry.org/r-socialsci/"],
              "optional" : False
             },
             {
              "name": "Know what a factor is and how to convert and rename these",
              "id": "task_dprep_1_4_3",
              "description": "Factors are variables which take on a certain number of different values",
              "links": ["https://datacarpentry.org/r-socialsci/"],
              "optional" : False
             },
             {
              "name": "Understand what a pipeline (%>%) is in R and be able to work with these",
              "id": "task_dprep_1_4_4",
              "description": "Pipelines are a great way to combine multiple operations and simplify your code!",
              "links": ["https://datacarpentry.org/r-socialsci/"],
              "optional" : False
             },
             {
              "name": "Know how to use data manipulation codes such as filter, group_by and mutate",
              "id": "task_dprep_1_4_5",
              "description": "These are common manipulation tasks that you will use very often when analyzing data",
              "links": ["https://datacarpentry.org/r-socialsci/"],
              "optional" : False
             },
             {
             "name": "Know how to export data and write a cleaned dataset to a csv file",
             "id": "task_dprep_1_4_6",
             "description": "Once you have cleaned a dataset, you can store the cleaned datafile in a csv by using the write_csv function in R!",
             "links": ["https://datacarpentry.org/r-socialsci/"],
             "optional" : False
             }
             ]
            }
            ]
  },
  {
    "name": "Week 2",
    "description": "Versioning projects with Git and GitHub!",
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
            "id": "task_dprep_2_1_1",
            "description": "To get acquainted with this week's course material, watch the energizer!",
            "links": ["TBA"],
            "optional" : False
          }]},
      {"category_name": "2. Readings on workflow management",
       "id": 2,
       "description": "",
       "items" : [
          {
            "name": "Read the readings on managing your workflow and its importance on TilburgScienceHub",
            "id": "task_dprep_2_2_1",
            "description": "Managing your workflow is an important way to bring structure to your project and improve reproducability!",
            "links": ["https://tilburgsciencehub.com/learn/project-setup"],
            "optional" : False
          },
          {
            "name": "Read the optional reading on best practices for data projects",
            "id": "task_dprep_2_2_2",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["https://www.shirokuriwaki.com/programming/project-organization.html"],
            "optional" : True
          },
          {
            "name": "Read the optional reading on code and data for Social Sciences",
            "id": "task_dprep_2_2_3",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["https://www.brown.edu/Research/Shapiro/pdfs/CodeAndData.pdf"],
            "optional" : True
          },
          {
            "name": "Read the optional reading on data analysis workflow",
            "id": "task_dprep_2_2_4",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["http://www.coordinationtoolkit.org/wp-content/uploads/130907-Data-flow.pdf"],
            "optional" : True
          },
          {
            "name": "Look through this paper to further familiarize yourself with this week’s content",
            "id": "task_dprep_2_2_5",
            "description": "These optional readings will elaborate on the data analysis workflow and the version control of your project. Read through these to further improve your understanding of these concepts!",
            "links": ["https://www.tse-fr.eu/sites/default/files/TSE/documents/doc/wp/2018/wp_tse_933.pdf"],
            "optional" : True
          }]},
        {"category_name": "3. Command line skills",
         "id": 3,
         "description": "",
         "items" : [
            {
              "name": "Get an understanding of what the command line/terminal is by looking through the slides",
              "id": "task_dprep_2_3_1",
              "description": "These slides are especially beneficial for students that are using a Mac, but also gives you a good overall understanding of the command line and how we use it!",
              "links": ["https://generalassembly.github.io/prework/cl"],
              "optional" : False
            },
            {
              "name": "Complete the first chapter of the Introduction to Shell on Datacamp",
              "id": "task_dprep_2_3_2",
              "description": "Navigating through directories is a task you will often do when using Git Bash for example, so make sure to complete this tutorial!",
              "links": ["https://learn.datacamp.com/courses/introduction-to-shell"],
              "optional" : False
            }]},
        {"category_name": "4. Git & Github",
         "id": 4,
         "description": "",
         "items" : [
            {
              "name": "Follow the short Github introduction on issues, pull requests and commits",
              "id": "task_dprep_2_4_1",
              "description": "This Github introduction will walk you through the basics of using Git and Github for your project!",
              "links": ["https://lab.github.com/githubtraining/introduction-to-github"],
              "optional" : False
            },
            {
              "name": "Understand why we use Git over Google drive when working on code with others",
              "id": "task_dprep_2_4_2",
              "description": "Git is a very effective way to collaborate on projects with code. Do you understand the benefits of Git over Google Drive?",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            },
            {
              "name": "Create the version-control-exercises repository on Github and clone it",
              "id": "task_dprep_2_4_3",
              "description": "To get a repository from Github to your local computer, you will need to use git clone!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            },
            {
              "name": "Understand the process of making changes to files and pushing these using Git (git add, commit etc.)",
              "id": "task_dprep_2_4_4",
              "description": "This is an iterative process that you will be performing often, so make sure you fully understand this!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            },
            {
              "name": "Be able to clone a repository, make changes to this repository and then push these changes to Github",
              "id": "task_dprep2_4_5",
              "description": "When you made changes on your local computer, you want this to be transferred to the main repository on Github. For that, we use git push!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            },
            {
              "name": "Know how to find the history of a project and know how to roll back to a previous version of a project on Github using a hash",
              "id": "task_dprep_2_4_6",
              "description": "Everyone makes mistakes. Luckily, Git and Github allow you to easily roll back to previous versions of a project, should this be necessary",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            },
            {
              "name": "Understand what a gitignore file is used for and why this is used",
              "id": "task_dprep_2_4_7",
              "description": "You don't always want Git to track every file that you create or make a change to (take large csv files for example). Using gitignore, Git will stop tracking these files!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            },
            {
              "name": "Know how to work on a branch of a project and the concept of merging branches with each other",
              "id": "task_dprep_2_4_8",
              "description": "Branches are ways to work on different parts of a project simultaneously with team members. These branches can be merged after being pushed",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            },
            {
              "name": "Know how to fork an existing repository of someone else",
              "id": "task_dprep_2_4_9",
              "description": "Forking allows you to propose changes to projects of others and is useful for open-source collaboration!",
              "links": ["https://dprep.hannesdatta.com/docs/tutorials/version-control/version-control.html"],
              "optional" : False
            }]}],

         "modules": []
   },
   {
     "name": "Week 3",
     "description": "Improving your R skills and introducing RMarkdown!",
     "id": 3,
     "order": 1,
     "deadline": "2022-01-31",
     "items": [
       {"category_name": "1. Kick-starting the week",
        "id": 1,
        "description": "",
        "items" : [
           {
             "name": "Watch the energizer for this week",
             "id": "task_dprep_3_1_1",
             "description": "To get acquainted with this week's course material, watch the energizer!",
             "links": ["TBA"],
             "optional" : False
           }]},
       {"category_name": "2. DataCamp course: “Intermediate R”",
        "id": 2,
        "description": "",
        "items" : [
           {
             "name": "Able to use the common operators in R (&, |, > etc.)",
             "id": "task_dprep_3_2_1",
             "description": "R has a set of common operators built in, which you will use a lot when cleaning a dataset for example!",
             "links": ["https://www.datacamp.com/courses/intermediate-r"],
             "optional" : False
           },
           {
             "name": "Know how to implement ifelse statements and when to use these",
             "id": "task_dprep_3_2_2",
             "description": "Ifelse statements are commonly used when you have certain conditions a specific code should adhere to. You can use these when creating dummy variables, for example!",
             "links": ["https://www.datacamp.com/courses/intermediate-r"],
             "optional" : False
           },
           {
             "name": "Understand the concepts of using loops",
             "id": "task_dprep_3_2_3",
             "description": "Looping is used to go through a statement a certain amount of times until a condition is met. Loops are an amazing way to simplify your code!",
             "links": ["https://www.datacamp.com/courses/intermediate-r"],
             "optional" : False
           },
           {
             "name": "Write a basic for-loop",
             "id": "task_dprep_3_2_4",
             "description": "For loops are a type of loop in R to repeat a chunk of code multiple times",
             "links": ["https://www.datacamp.com/courses/intermediate-r"],
             "optional" : False
           },
           {
             "name": "Write a basic while loop",
             "id": "task_dprep_3_2_5",
             "description": "We use while loops when we want a chunk of code to keep on running, until a certain condition is met",
             "links": ["https://www.datacamp.com/courses/intermediate-r"],
             "optional" : False
           },
           {
             "name": "Understand the benefits of using functions in R",
             "id": "task_dprep_3_2_6",
             "description": "Functions are used to perform a specific task. R has lots of built-in functions, but you can also create functions yourself to make your code more efficient",
             "links": ["https://www.datacamp.com/courses/intermediate-r"],
             "optional" : False
           },
           {
             "name": "Know how to create a simple function in R",
             "id": "task_dprep_3_2_7",
             "description": "Try creating a basic function yourself! An example could be a function that requires two input parameters that are multiplied by each other",
             "links": ["https://www.datacamp.com/courses/intermediate-r"],
             "optional" : False
           }]},
         {"category_name": "3. R Markdown",
          "id": 3,
          "description": "",
          "items" : [
             {
               "name": "Understand the benefits of using an Rmarkdown file when writing documents with code",
               "id": "task_dprep_2_3_1",
               "description": "The main benefit of using an RMarkdown file is reproducability. Moreover, it supports various output formats (e.g., pdf and html)",
               "links": ["https://datacarpentry.org/r-socialsci/05-rmarkdown/index.html"],
               "optional" : False
             },
             {
               "name": "Know how to use chunks within an R-markdown file",
               "id": "task_dprep_2_3_2",
               "description": "Chunks are used to show code (output) within the document, so users can either see what is going on in the code, what the output looks like or both!",
               "links": ["https://datacarpentry.org/r-socialsci/05-rmarkdown/index.html"],
               "optional" : False
             },
             {
               "name": "Able to knit an RMD file to pdf and html",
               "id": "task_dprep_2_3_2",
               "description": "To export your report and share it with others, you will need to knit the file. In order to knit to pdf, you need to install tinytex, so make sure you are able to do this!",
               "links": ["https://datacarpentry.org/r-socialsci/05-rmarkdown/index.html"],
               "optional" : False
             }]},
         {"category_name": "4. Data exploration in R",
          "id": 4,
          "description": "",
          "items" : [
             {
               "name": "Inspect the dataset by filtering the regional and city level out",
               "id": "task_dprep_2_4_1",
               "description": "To inspect the data on a national level, the other levels are filtered out. Were you able to perform exercise 2 and, if not, do you understand the solution?",
               "links": ["https://dprep.hannesdatta.com/docs/tutorials/data-exploration-in-r/intro-to-r.html"],
               "optional" : False
             },
             {
               "name": "Drop unnecessary columns from the datase",
               "id": "task_dprep_2_4_2",
               "description": "When analyzing data, you will often have columns in your data that you do not need or use (this could be an identifier in survey data for example)",
               "links": ["https://dprep.hannesdatta.com/docs/tutorials/data-exploration-in-r/intro-to-r.html"],
               "optional" : False
             },
             {
               "name": "Write a function that inspects the data",
               "id": "task_dprep_2_4_3",
               "description": "Writing a function here allows you to make your code more efficient. Refresh your knowledge on functions and try making one yourself (exercise 9)!",
               "links": ["https://dprep.hannesdatta.com/docs/tutorials/data-exploration-in-r/intro-to-r.html"],
               "optional" : False
             },
             {
               "name": "Visualize the dataset by making plots",
               "id": "task_dprep_2_4_4",
               "description": "Use the plot() function that is built into R to (re)create the plots shown. Try out some other variations and see how this affects your plot! For you project, you could use ggplot2 to acquire more functionalities when plotting!",
               "links": ["https://dprep.hannesdatta.com/docs/tutorials/data-exploration-in-r/intro-to-r.html"],
               "optional" : False
             }]}],

         "modules": []
   },
   {
     "name": "Week 4",
     "description": "Cleaning and analyzing datasets using dplyr and tidyr packages!",
     "id": 4,
     "order": 1,
     "deadline": "2022-01-31",
     "items": [
       {"category_name": "1. Kick-starting the week",
        "id": 1,
        "description": "",
        "items" : [
           {
             "name": "Watch the energizer for this week",
             "id": "task_dprep_4_1_1",
             "description": "To get acquainted with this week's course material, watch the energizer!",
             "links": ["TBA"],
             "optional" : False
           }]},
       {"category_name": "2. Datacamp course: “Introduction to Tidyverse”",
        "id": 2,
        "description": "",
        "items" : [
           {
             "name": "Know the definitions of verbs in dplyr such as filter, mutate and arrange",
             "id": "task_dprep_4_2_1",
             "description": "The verbs included in the dplyr package are often used to manipulate and clean datasets!",
             "links": ["https://campus.datacamp.com/courses/introduction-to-the-tidyverse"],
             "optional" : False
           },
           {
             "name": "Able to implement these verbs in code to clean a dataset, for example",
             "id": "task_dprep_4_2_2",
             "description": "Make sure you know how to apply these verbs, as you will often use them in your team project and future courses!",
             "links": ["https://campus.datacamp.com/courses/introduction-to-the-tidyverse"],
             "optional" : False
           },
           {
             "name": "Know how to use the group_by and summarize verbs in R",
             "id": "task_dprep_4_2_3",
             "description": "These verbs allow you to group dataframes and extract statistics such as the mean or maximum!",
             "links": ["https://campus.datacamp.com/courses/introduction-to-the-tidyverse"],
             "optional" : False
           },
           {
             "name": "Understand some of the basics of ggplot2",
             "id": "task_dprep_4_2_4",
             "description": "A thorough application of ggplot2 is not required, though it is important to know that this is an extension of the built-in plot function and is recommended when more functionalities are required!",
             "links": ["https://campus.datacamp.com/courses/introduction-to-the-tidyverse"],
             "optional" : False
           }]},
         {"category_name": "3. Datacamp course “Cleaning Data in R”",
          "id": 3,
          "description": "",
          "items" : [
             {
               "name": "Able to convert data types",
               "id": "task_dprep_4_3_1",
               "description": "Sometimes, it may be necessary to convert data types (such as converting to a factor) to extract your required statistics from a dataset",
               "links": ["https://learn.datacamp.com/courses/cleaning-data-in-r"],
               "optional" : False
             },
             {
               "name": "Know how to find duplicates in a dataset",
               "id": "task_dprep_4_3_2",
               "description": "When working with lots of data, it is not uncommon to come across duplicates. Such duplicates need to be further examined and possibly corrected for. Therefore, it is important to be able to detect thesse duplicates in your data!",
               "links": ["https://learn.datacamp.com/courses/cleaning-data-in-r"],
               "optional" : False
             },
             {
               "name": "Able to find inconsistencies within a dataset",
               "id": "task_dprep_4_3_3",
               "description": "Inconsistencies may lead to you making incorrect assumptions. Be aware of these inconsistencies and make sure you are able to correct for these!",
               "links": ["https://learn.datacamp.com/courses/cleaning-data-in-r"],
               "optional" : False
             },
             {
               "name": "Know how to correct for these inconsistencies (e.g., str_to_lower)",
               "id": "task_dprep_4_3_4",
               "description": "There are multiple types of inconsitencies. In this Datacamp course, make sure to understand the tools used to correct for whitespace inconsistencies, for example!",
               "links": ["https://learn.datacamp.com/courses/cleaning-data-in-r"],
               "optional" : False
             }]},
     {"category_name": "4. DataCamp course “Joining Data with dplyr”",
      "id": 4,
      "description": "",
      "items" : [
         {
           "name": "Know how to merge two tables using inner_join",
           "id": "task_dprep_4_4_1",
           "description": "Sometimes, you may want to merge tables based on a common identifier. For this, we can use the inner_join() function in R!",
           "links": ["https://campus.datacamp.com/courses/joining-data-with-dplyr"],
           "optional" : False
         },
         {
           "name": "Able to use extensions to inner_join such as right_join",
           "id": "task_dprep_4_4_2",
           "description": "Additionally, you may want to exclude certain columns from one table, while including these from the other table when merging. For this, you could use a right_join(), for example!",
           "links": ["https://campus.datacamp.com/courses/joining-data-with-dplyr"],
           "optional" : False
             }]}],

         "modules": []
   },
   {
   "name": "Week 5",
   "description": "Using 'make' to automate our workflows and make projects reproducable",
   "id": 5,
   "order": 1,
   "deadline": "",
   "items": [
     {"category_name": "1. Kick-starting the week",
      "id": 1,
      "description": "",
      "items" : [
         {
           "name": "Watch the energizer for this week",
           "id": "task_dprep_5_1_1",
           "description": "To get acquainted with this week's course material, watch the energizer!",
           "links": ["TBA"],
           "optional" : False
         }]},
     {"category_name": "2. Automating and reproducing your research project",
      "id": 2,
      "description": "",
      "items" : [
         {
           "name": "Watch the video on why you should automate the pipelines of your research project",
           "id": "task_dprep_5_2_1",
           "description": "To add structure to your directory and allow you to easily (re)execute it, you should automate your pipeline. Watch the video to see how this can be done!",
           "links": ["https://youtu.be/9aivqe-phL0"],
           "optional" : False
         },
         {
           "name": "Watch the video showing four steps on automating your research project and making it reproducable",
           "id": "task_dprep_5_2_2",
           "description": "Watch the video to see the four steps and how these allow you to automate your work and how they provide reproducability",
           "links": ["https://youtu.be/rJGGCX6bcPo"],
           "optional" : False
         }]},
       {"category_name": "3. Reading on make",
        "id": 3,
        "description": "",
        "items" : [
           {
             "name": "Read the article on Tilburg Science Hub on makefiles",
             "id": "task_dprep_5_3_1",
             "description": "For automating your research project, we use makefiles that provide instructions on how to build the project. Read the TSH article to learn all about it!",
             "links": ["https://tilburgsciencehub.com/learn/makefiles"],
             "optional" : False
           }]},
       {"category_name": "4. Make tutorial",
        "id": 4,
        "description": "",
        "items" : [
           {
             "name": "Understand the purpose of using makefiles for automating research projects",
             "id": "task_dprep_5_4_1",
             "description": "As explained in the TSH article as well, make sure you fully understand what a makefile is and why we use this to automate our research projects",
             "links": ["https://dprep.hannesdatta.com/docs/tutorials/make-tutorial/make-tutorial.html"],
             "optional" : False
           },
           {
             "name": "Be able to run a simple makefile in the terminal",
             "id": "task_dprep_5_4_2",
             "description": "To ensure you correctly installed make, try running a simple makefile to see if all works fine!",
             "links": ["https://dprep.hannesdatta.com/docs/tutorials/make-tutorial/make-tutorial.html"],
             "optional" : False
           },
           {
             "name": "Succesfully run the makefile with all of the 5 scripts from the tutorial (download.R, clean.R etc.)",
             "id": "task_dprep_5_4_3",
             "description": "With large research projects in particular, your source code will consist of lots of sub-scripts that depend on each other. If you cannot run this makefile, try to see if you spot any errors in your makefile",
             "links": ["https://dprep.hannesdatta.com/docs/tutorials/make-tutorial/make-tutorial.html"],
             "optional" : False
           },
           {
             "name": "Understand the directory structure as explained in the tutorial (e.g., data in data/ and source code in src/)",
             "id": "task_dprep_5_4_4",
             "description": "Not only is this directory structure convenient for you when working on the project, it also makes it reproducable (for others and/or your future self!)",
             "links": ["https://dprep.hannesdatta.com/docs/tutorials/make-tutorial/make-tutorial.html"],
             "optional" : False
           },
           {
             "name": "Run the makefile that triggers the two makefiles in the sub-directories",
             "id": "task_dprep_5_4_5",
             "description": "To prevent the hassle of running makefiles in each subdirectory, we create one makefile in the root directory that triggers the other makefiles, such that you only need to run this makefile to build the project",
             "links": ["https://dprep.hannesdatta.com/docs/tutorials/make-tutorial/make-tutorial.html"],
             "optional" : False
           }]}],

          "modules": []
    },
    {
    "name": "Week 6-7",
    "description": "Course and project wrap-up",
    "id": 6,
    "order": 1,
    "deadline": "",
    "items": [
      {"category_name": "1. Course evaluation",
       "id": 1,
       "description": "",
       "items" : [
          {
            "name": "My programming skills have improved significantly since the start of this course",
            "id": "task_dprep_6_1_1",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "I enjoyed the format of this course (i.e., external website instead of Canvas to stimulate open education)",
            "id": "task_dprep_6_1_2",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "I liked the concept of Pulse and it has helped me with keeping track of what must be done each week",
            "id": "task_dprep_6_1_3",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "The things i have learned in this class w.r.t. automation, reproducability and programming are skills that I will apply in the future",
            "id": "task_dprep_6_1_4",
            "description": "",
            "links": [""],
            "optional" : False
          }]},
      {"category_name": "2. Project evaluation",
       "id": 2,
       "description": "",
       "items" : [
          {
            "name": "The project helped me to further improve my (programming) skills",
            "id": "task_dprep_6_2_1",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "The project aligned well with the other course material",
            "id": "task_dprep_6_2_2",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "The coaching sessions provided enough feedback to continue working on the project",
            "id": "task_dprep_6_2_3",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "I enjoyed working on the project",
            "id": "task_dprep_6_2_4",
            "description": "",
            "links": [""],
            "optional" : False
          }]}],

           "modules": []
   }
 ]
}


print(course_dprep)



course_odcm ={
  "name": "Online Data Collection and Management",
  "description": "Learn how to scrape the web!",
  "id": 2,
  "users": [], # leeg laten
  "modules": [
    {
      "name": "Week 1",
      "description": "Getting started Python!",
      "id": 100,
      "order": 1,
      "deadline": "", #"2022-01-31",
      "items": [
        {"category_name": "1. Get started installing your computer!",
         "id": 1,
         "description": "To follow this course and work on your team project later on, it is necessary to have installed the software, so make sure to complete this part right away!",
         "items" : [
            {
              "name": "Install Anaconda",
              "id": "task_odcm_1_1_1",
              "description": "Anaconda is a Python distribution and set you up with everything that you need to work with Python!",
              "links": ["https://odcm.hannesdatta.com/docs/tutorials/software/anaconda"],
              "optional": False
            },
            {
              "name": "Familiarize yourself with Jupyter Notebook",
              "id": "task_odcm_1_1_2",
              "description": "In this course, we use Jupyter Notebook as it is a great environment to start your coding journey and it can easily combine code with text!",
              "links": ["https://odcm.hannesdatta.com/docs/tutorials/software/jupyter/"],
              "optional":  False
            },
            {
              "name": "Verify that you have a premium account at Datacamp (i.e., mailed the library)",
              "id": "task_odcm_1_1_3",
              "description": "We use Datacamp in this class, but you need to go through a quite cumbersome onboarding procedure with the University library. Do this soon so you can enjoy premium content without having to pay for it!",
              "links": ["https://odcm.hannesdatta.com/docs/course/support/datacamp/"],
              "optional":  False
            }]
            },
        {"category_name": "2. Weblecture on web scraping and APIs",
        "id": 2,
        "description": "",
        "items" : [
            {
            "name": "Watch the weblecture explaining what web scraping and APIs are!",
            "id": "task_odcm_1_2_1",
            "description": "In this course, you learn both how to scrape data from websites aswell as how to extract data using an API. Make sure to understand the concepts and the differences between these!",
            "links": ["https://videocollege.uvt.nl/Mediasite/Play/41afff385bd74db2af5fb8507350ea521d"],
            "optional" : False
            }]
            },
        {"category_name": "3. Python Bootcamp tutorial",
         "id": 3,
          "description": "",
          "items": [
              {
              "name": "Follow the Python introduction class on Datacamp",
              "id": "task_odcm_1_3_1",
              "description": "This Datacamp course is especially useful if you are completely new to programming and Python and will go over the basics of it!",
              "links": ["https://learn.datacamp.com/courses/intro-to-python-for-data-science"],
              "optional" : True
             },
             {
              "name": "Know how to use and work with if-statements",
              "id": "task_odcm_1_3_2",
              "description": "Ifelse statements are commonly used when you have certain conditions a specific code should adhere to. You will use if-statements quite often, so make sure you are able to work with these!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
              "optional" : False
             },
             {
              "name": "Understand the use of dictionaries in Python",
              "id": "task_odcm_1_3_3",
              "description": "We use dictionaries to access values or items by their unique keys. Each new key:value pair is seperated by commas within the curly brackets",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
              "optional" : False
             },
             {
              "name": "Able to extract a value or item within a dictionary by using the key identifier",
              "id": "task_odcm_1_3_4",
              "description": "You can access items within a dictionary by searching for their respective key",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
              "optional" : False
             },
             {
              "name": "Know how to add data to an empty list by using a for-loop",
              "id": "task_odcm_1_3_5",
              "description": "For-loops are used to repeat an iteration more than once. In this tutorial, you use a for-loop to modify the prices of items and store them in an empty list",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
              "optional" : False
             },
             {
              "name": "Know what indices are in Python and how to use these in your code to refer to a specific item",
              "id": "task_odcm_1_3_6",
              "description": "Indices refer to the place at which a certain item is at within a list, for example. The first item has an index value of 0, the second item has an index value of 1 and so forth",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
              "optional" : False
             },
             {
             "name": "Iterating over dictionaries",
             "id": "task_odcm_1_3_7",
             "description": "Know how to iterate over dictionaries in order to extract all the keys, values or both!",
             "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
             "optional" : False
             },
             {
             "name": "Working with functions in Python",
             "id": "task_odcm_1_3_8",
             "description": "Understand how to construct a basic function in Python and use parameters test more functionalities",
             "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
             "optional" : False
             },
             {
             "name": "Get familiar with common errors when working with code",
             "id": "task_odcm_1_3_9",
             "description": "While programming, you will often come across errors in your script. Being able to understand your errors makes it a lot easier to solve it. Try and Except is a good way to test pieces of code for errors!",
             "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
             "optional" : False
             },
             {
             "name": "Be able to both read and write to csv files",
             "id": "task_odcm_1_3_10",
             "description": "The csv package in Python allows you to both read and create csv files. You will most likely use this in your team project, so make sure you know how to do this!",
             "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/pythonbootcamp/python-bootcamp.ipynb"],
             "optional" : False
             }
             ]
            }
            ]
  },
  {
    "name": "Week 2",
    "description": "Learn how to scrape data!",
    "id": 102,
    "order": 1,
    "deadline": "",
    "items": [
      {"category_name": "1. Kick-starting the week",
       "id": 1,
       "description": "",
       "items" : [
          {
            "name": "Watch the energizer for this week",
            "id": "task_odcm_2_1_1",
            "description": "To get acquainted with this week's course material, watch the energizer!",
            "links": ["TBA"],
            "optional" : False
          }]},
      {"category_name": "2. Reading",
       "id": 2,
       "description": "",
       "items" : [
          {
            "name": "Thoroughly read the Fields of Gold paper",
            "id": "task_odcm_2_2_1",
            "description": "This paper discusses opportunities and challenges of using web data in research projects. You will use the framework presented in this paper for this course, so make sure to fully read and understand the contents!",
            "links": ["https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3820666"],
            "optional" : False
          }]},
        {"category_name": "3. Tutorial: Web data for dummies - Web scraping",
         "id": 3,
         "description": "",
         "items" : [
            {
              "name": "Understand the definition of web scraping and how this differs from using APIs",
              "id": "task_odcm_2_3_1",
              "description": "We can use web scraping to extract information from a given website, which we can then save or analyze, for example. This way, we do not lose valuable information when a site is updated!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            },
            {
              "name": "Understand the html structure of the book presented in the tutorial (A Light in the Attic)!",
              "id": "task_odcm_2_3_2",
              "description": "Inspect the web page and look at the structure at which the page is setup. You will see that information such as the title and price is surrounded by corresponding tags, which we later on use to extract this data!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            },
            {
              "name": "Use the requests library to extract the book title or product description!",
              "id": "task_odcm_2_3_3",
              "description": "By using the requests library, we load the source code of the website into Python, allowing us to extract our preferred data from the web page!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            },
            {
              "name": "Simplify your search by using the BeautifulSoup library to get your desired piece of data!",
              "id": "task_odcm_2_3_4",
              "description": "As you most likely noticed, the BeautifulSoup library is a much more convenient way to scrape the data. Use the .find() or .get_text() methods and combine these with indices to capture the website's content!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            }]},
        {"category_name": "4. Tutorial: Web data for dummies - API",
         "id": 4,
         "description": "",
         "items" : [
            {
              "name": "Understand the definition of APIs and how this differs from using web scraping",
              "id": "task_odcm_2_4_1",
              "description": "Contrary to web scraping (which you use software for extract data), APIs are designed to extract data from a website and give you access to it. They are, therefore, a more legit way to retrieve data - but are also limited in providing the data",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            },
            {
              "name": "Understand the structure of a JSON tree and how data is stored within these trees",
              "id": "task_odcm_2_4_2",
              "description": "The JSON tree is basically the backend of what the output shows. Lists and dictionaries are used to store the data. Navigate through the tree to get a grasp of how the data is structured and to what parent each piece belongs to!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            },
            {
              "name": "Print out a random joke from the presented website by following the steps for using an API!",
              "id": "task_odcm_2_4_3",
              "description": "By providing Python with a URL and the proper headers, we can extract the data from the website (which is a random joke each time). Tip: Make sure you imported the requests library!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            },
            {
              "name": "Rather then simply printing out a random joke, try saving multiple ones within an empty list by using a for-loop",
              "id": "task_odcm_2_4_4",
              "description": "When collecting data, you most likely want to store it (temporarily). Therefore, try collecting a few jokes within an empty list!",
              "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webdata-for-dummies/webdata-for-dummies.ipynb"],
              "optional" : False
            }]}],

         "modules": []
   },
   {
     "name": "Week 3",
     "description": "Improving your web scraping skills!",
     "id": 103,
     "order": 1,
     "deadline": "",
     "items": [
       {"category_name": "1. Kick-starting the week",
        "id": 1,
        "description": "",
        "items" : [
           {
             "name": "Watch the energizer for this week",
             "id": "task_odcm_3_1_1",
             "description": "To get acquainted with this week's course material, watch the energizer!",
             "links": ["TBA"],
             "optional" : False
           }]},
       {"category_name": "2. Finalize your team",
        "id": 2,
        "description": "",
        "items" : [
           {
             "name": "Make sure your found a team to work on the project with and sign up on Canvas",
             "id": "task_odcm_3_2_1",
             "description": "Once your team is complete, you can already start working on the project by brainstorming for ideas!",
             "links": ["On Canvas, go to people --> Groups to sign up!"],
             "optional" : False
           }]},
         {"category_name": "3. Tutorial: Web scraping 101",
          "id": 3,
          "description": "",
          "items" : [
             {
               "name": "Recall your understanding of how a HTML structure is setup",
               "id": "task_odcm_3_3_1",
               "description": "To receive only our desired information from a website, we refer to tags that belond to a specific class. By doing so, all other tags that are not within this class are excluded from the search result",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Extract the correct link for the second book of the list by combining the base url with the book url",
               "id": "task_odcm_3_3_2",
               "description": "Combining these parts allows us to create the full link to refer to the correct book page!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Store the titles and urls of all the books in an empty list by using a for-loop",
               "id": "task_odcm_3_3_3",
               "description": "You can easily add new information (such as price of rating) to this empty list by adding it to the source code. The output shows each book title and URL within a dictionary, where all books are seperated by commas",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Collect all the URLs for the first 10 pages of the quotes to scrape website",
               "id": "task_odcm_3_3_4",
               "description": "Most likely, you want to extract all the data from a website, rather than just the first page. Here, we iterate over the first 10 pages and collect the respective URLs!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Run and understand the function that extracts all the book titles and URLs",
               "id": "task_odcm_3_3_5",
               "description": "Often times, websites get updated with new information (e.g., new books are added). Therefore, we automate our scraper, such that it still works and collects all the data when the website is updated!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Follow the step-by-step guide on how to extract the numbers of stars a book has received",
               "id": "task_odcm_3_3_6",
               "description": "Each step narrows down the amount of output is given. Make sure you understand the changes in the output for each change in the source code!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Write the book descriptions to a csv file",
               "id": "task_odcm_3_3_7",
               "description": "Once you gathered the data and saved it in a list, you often want to save it to a csv file as well (for example, to conduct further analyses). Therefore, try to write the code to a csv file succesfully and check if you can open it!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Understand the differences between Jupyter Notebook and Spyder or PyCharm",
               "id": "task_odcm_3_3_8",
               "description": "Jupyter Notebook is a great for people who are new to programming. As your skills improve, you may prefer an IDE such as Spyder or PyCharm over Notebook! You can run the code in Spyder to see how this differs from Notebook yourself.",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscraping101/webscraping-101.ipynb"],
               "optional" : False
             }]}],

         "modules": []
   },
   {
     "name": "Week 4",
     "description": "Extracting data using APIs",
     "id": 104,
     "order": 1,
     "deadline": "",
     "items": [
       {"category_name": "1. Kick-starting the week",
        "id": 1,
        "description": "",
        "items" : [
           {
             "name": "Watch the energizer for this week",
             "id": "task_odcm_4_1_1",
             "description": "To get acquainted with this week's course material, watch the energizer!",
             "links": ["TBA"],
             "optional" : False
           }]},
       {"category_name": "2. Limitations to using web data",
        "id": 2,
        "description": "",
        "items" : [
           {
             "name": "Make a list of issues you may face when scraping data from site or using an API",
             "id": "task_odcm_4_2_1",
             "description": "When extracting data, you may be confronted with all sorts of ethical or legal boundaries. For example, it may not be allowed to store sensitive information of users. Be aware of this when working with web data in your team projects or future research!",
             "links": [""],
             "optional" : False
           }]},
         {"category_name": "3. Tutorial: API 101",
          "id": 3,
          "description": "",
          "items" : [
             {
               "name": "Create a function that shows the number of jokes that include a specific search term",
               "id": "task_odcm_4_3_1",
               "description": "This function is the equivalent of searching for that term in the search bar on a website and shows how many jokes include it!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apis101/api-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Extend this function by making it loop over all pages!",
               "id": "task_odcm_4_3_2",
               "description": "This extension allows you to collect all the jokes on the website without being restricted the current page!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apis101/api-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Create a function that extracts the numbers of total and active users of a given subreddit",
               "id": "task_odcm_4_3_3",
               "description": "For this task, look how the .json url corresponds to the source code to extract the number of (active) users!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apis101/api-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Analyze the reddit activity by using the 'after' attribute to apply pagination",
               "id": "task_odcm_4_3_4",
               "description": "Contrary to the sites we have seen thus far, Reddit does not have a 'next' page. Therefore, we use the next key each time to get the next batch of 25 comments and posts!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apis101/api-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Write and run a function that extracts all the data (e.g., username, time a post was created etc.) of the first few pages of a subreddit",
               "id": "task_odcm_4_3_5",
               "description": "Rather than collecting snippets of the web page, we may want to extract as much information as possible and analyze it at a later instance. This function allows us to do so!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apis101/api-101.ipynb"],
               "optional" : False
             },
             {
               "name": "Write the results of this function to a csv file and try opening it to see the results!",
               "id": "task_odcm_4_3_6",
               "description": "To save our data, we export the data to a csv file so we can access it later or open it in another software program, for example!",
               "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apis101/api-101.ipynb"],
               "optional" : False
             }]}],

         "modules": []
   },
   {
   "name": "Week 5",
   "description": "Developing a prototype for your team project!",
   "id": 105,
   "order": 1,
   "deadline": "",
   "items": [
     {"category_name": "1. Kick-starting the week",
      "id": 1,
      "description": "",
      "items" : [
         {
           "name": "Watch the energizer for this week",
           "id": "task_odcm_5_1_1",
           "description": "To get acquainted with this week's course material, watch the energizer!",
           "links": ["TBA"],
           "optional" : False
         }]},
     {"category_name": "2. Tutorial: APIs advanced",
      "id": 2,
      "description": "",
      "items" : [
         {
           "name": "Work on part 1 of the tutorial",
           "id": "task_odcm_5_2_1",
           "description": "The first part teaches you how to use an API that requires user authentication, which is useful if you use an API in your team project!",
           "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apisadvanced/api-advanced.ipynb"],
           "optional" : True
         },
         {
           "name": "Work on part 2 of the tutorial",
           "id": "task_odcm_5_2_2",
           "description": "The second part focuses on parsing JSON into CSV format, which is also convenient for your team project!",
           "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/apisadvanced/api-advanced.ipynb"],
           "optional" : True
         }]},
       {"category_name": "3. Tutorial: Web scraping advanced",
        "id": 3,
        "description": "",
        "items" : [
           {
             "name": "Work on part 1 of the tutorial",
             "id": "task_odcm_5_3_1",
             "description": "This part introduces you to Selenium, which is capable of handling dynamic websites (i.e., websites of which the content changes when refreshing a page)",
             "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscrapingadvanced/webscraping-advanced.ipynb"],
             "optional" : True
           },
           {
             "name": "Work on part 2 of the tutorial",
             "id": "task_odcm_5_3_1",
             "description": "The second part puts your fresh Selenium skills into practice for Instagram and teaches you how to scrape images from here, for example!",
             "links": ["https://colab.research.google.com/github/hannesdatta/course-odcm/blob/master/content/docs/tutorials/webscrapingadvanced/webscraping-advanced.ipynb"],
             "optional" : True
           }]}],

          "modules": []
    },
    {
    "name": "Week 6-7",
    "description": "Course and project wrap-up",
    "id": 106,
    "order": 1,
    "deadline": "",
    "items": [
      {"category_name": "1. Course evaluation",
       "id": 1,
       "description": "",
       "items" : [
          {
            "name": "My programming skills have improved significantly since the start of this course",
            "id": "task_odcm_6_1_1",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "I enjoyed the format of this course (i.e., external website instead of Canvas to stimulate open education)",
            "id": "task_odcm_6_1_2",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "I liked the concept of Pulse and it has helped me with keeping track of what must be done each week",
            "id": "task_odcm_6_1_3",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "",
            "id": "task_odcm_6_1_4",
            "description": "",
            "links": [""],
            "optional" : False
          }]},
      {"category_name": "2. Project evaluation",
       "id": 2,
       "description": "",
       "items" : [
          {
            "name": "The project helped me to further improve my (programming) skills",
            "id": "task_odcm_6_2_1",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "The project aligned well with the other course material",
            "id": "task_odcm_6_2_2",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "The coaching sessions provided enough feedback to continue working on the project",
            "id": "task_odcm_6_2_3",
            "description": "",
            "links": [""],
            "optional" : False
          },
          {
            "name": "I enjoyed working on the project",
            "id": "task_odcm_6_2_4",
            "description": "",
            "links": [""],
            "optional" : False
          }]}],

           "modules": []
   }
 ]
}


db = TinyDB('db.json')

#db.drop_tables()
db.drop_table('courses')
table = db.table('courses')
#users = db.table('users')

table.insert(course_dprep)
table.insert(course_odcm)

#users.insert({'email': 'h.datta@tilburguniversity.edu',
#              'name': 'Hannes Datta',
#              'nickname': 'Haynce',
#              'id': 1})


class AppUser(UserMixin, object):

    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def get_id(self):
        return(self.id)
