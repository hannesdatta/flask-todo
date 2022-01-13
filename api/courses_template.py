
course ={
  "name": "Online Data Collection and Management",
  "description": "Learn how to scrape the web!",
  "id": 1,
  "users": [], # leeg laten
  "modules": [
    {
      "name": "Week 1",
      "description": "Get started installing your computer!",
      "id": 1,
      "order": 1,
      "deadline": "", #"2022-01-31",
      "items": [
        {"category_name": "Category",
         "id": 1,
         "description": "This is a category",
         "items" : [
            {
              "name": "task 1",
              "id": "task_odcm_1x1",
              "description": "bla"
            },
            {
              "name": "task 2",
              "id": "x2",
              "description": "blu"
            },
            {
              "name": "task 3",
              "id": "x3",
              "description": "tra"
            }
            ]
     },
     {"category_name": "Category 2",
      "id": 2,
      "description": "This is a category 2",
      "items" : [
         {
           "name": "task 1b",
           "id": "x4",
           "description": "bla"
         },
         {
           "name": "task 2b",
           "id": "x5",
           "description": "blu"
         },
         {
           "name": "task 3b",
           "id": "x6",
           "description": "tra"
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
