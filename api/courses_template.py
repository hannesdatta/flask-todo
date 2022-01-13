
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
        {"category_name": "Get started installing your computer!",
         "id": 1,
         "description": "To follow this course and work on your team project later on, it is necessary to have installed the software, so make sure to complete this part right away!",
         "items" : [
            {
              "name": "Install R & RStudio",
              "id": "task_odcm_1_1_1",
              "description": "R & R Studio are the workhorse in this course - make sure to install it right away!"
            },
            {
              "name": "Install Git and make an account on GitHub",
              "id": "task_odcm_1_1_2",
              "description": "Git allows you to have an unlimited 'version history' - so you can always go back to any version of the file ever made. Get started now!"
            },
            {
              "name": "Install make",
              "id": "task_odcm_1_1_3",
              "description": "Make is like a robot, that runs your entire project from beginning to end! Sit back & relax, while you see your project come together!"
            },
            {
              "name": "Install Hugo",
              "id": "task_odcm_1_1_4",
              "description": "Hugo is a framework which we use to run our course website locally!"
            },
            {
              "name": "Verify that you have a premium account at Datacamp (i.e., mailed the library).",
              "id": "task_odcm_1_1_5",
              "description": "We use Datacamp in this class, but you need to go through a quite cumbersome onboarding procedure with the University library. Do this soon so you can enjoy premium content without having to pay for it!"
            }]
            },
            {"category_name": "2. Familiarize with Scrum",
            "id": 2,
            "description": "Scrum is avery flexible way to work in teams, so get acquainted with it and use it with your project group later on!",
            "items" : [
            {
            "name": "Read the page on using Scrum on TSH.",
            "id": "task_odcm_1_2_1",
            "description": "Scrum is an effective way to collaborate with team members – Read through this article on TSH!"
            },
            {
            "name": "Understand what the benefits are of using the scrum framework.",
            "id": "task_odcm_1_2_1",
            "description": "Scrum is an effective way to collaborate with team members – Read through this article on TSH!"
            }]
            },
            {"category_name": "3. Readings",
             "id": 3,
              "description": "This week introduces one reading on gathering and selecting data.",
              "items": [
              {
              "name": "Read the paper on data selection and procurement (Mela, 2011).",
              "id": "task_odcm_1_3_1",
              "description": "This paper shows the process of gathering and selecting data and what should be taken into account."
             }
            ]},
            {"category_name": "4. R Bootcamp Tutorial",
             "id": 4,
              "description": "This tutorial will introduce you to R and teach you the basic skills that you will use a lot when working with data.",
              "items": [
              {
              "name": "Know about data types in R (characteric, numeric, vector etc.)",
              "id": "task_odcm_1_4_1",
              "description": "Data types are used to constrain the values that an expression might take. You will use these a lot while programming!"
             },
             {
              "name": "Ability to load datasets in R and perform some data inspection tasks.",
              "id": "task_odcm_1_4_2",
              "description": "These are generally the first things you do; loading the data and getting a glimpse of it."
             },
             {
              "name": "Know what a factor is and how to convert and rename these.",
              "id": "task_odcm_1_4_3",
              "description": "Factors are variables which take on a certain number of different values."
             },
             {
              "name": "Understand what a pipeline (%>%) is in R and be able to work with these",
              "id": "task_odcm_1_4_4",
              "description": "Pipelines are a great way to combine multiple operations and simplify your code!"
             },
             {
              "name": "Know how to use data manipulation codes such as filter, group_by and mutate",
              "id": "task_odcm_1_4_5",
              "description": "These are common manipulation tasks that you will use very often when analyzing data."
             },
             {
             "name": "Know how to export data and write a cleaned dataset to a csv file",
             "id": "task_odcm_1_4_6",
             "description": "Once you have cleaned a dataset, you can store the cleaned datafile in a csv by using the write_csv function in R!"
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
      {"category_name": "Category",
       "id": 1,
       "description": "This is a category",
       "items" : [
          {
            "name": "task 1",
            "id": "1",
            "description": "bla"
          },
          {
            "name": "task 2",
            "id": "2",
            "description": "blu"
          },
          {
            "name": "task 3",
            "id": "3",
            "description": "tra"
          }
          ],
         "modules": []
   }
 ]
}
]
 }


print(course)
