library(httr)
library(rlist)
library(data.table)
library(jsonlite)
library(dplyr)

# TASK DATA

## Retrieve dump of database
req=GET('http://ec2-3-70-177-108.eu-central-1.compute.amazonaws.com:8000/test')

## Filter for oDCM tasks
tasks <- fromJSON(content(req, as='text')) #%>% filter(grepl('odcm', task_id))
tasks <- data.table(tasks)

## Keep most recent "task" update
setorderv(tasks, c('task_id', 'user_id', 'timestamp'), order=c(1,1,-1))
tasks[, keep:=1:.N==1, by =c('task_id','user_id')]
tasks <- tasks[keep==T]
tasks[, completed:=F]
tasks[type=='completed', completed:=T]

## Reshape
tmp = dcast(tasks, task_id~user_id, value.var='completed', fill = F)


# User names
users <- rbindlist(lapply(unique(tasks$user_id), function(u) {
  req=GET(paste0('http://ec2-3-70-177-108.eu-central-1.compute.amazonaws.com:8000/user.info/', u))
  ex=fromJSON(content(req, as='text'))
  data.frame(ex$id, ex$nickname, ex$email)
  }))

setnames(users, c('id','nickname','email'))


# Task descriptions
req=GET(paste0('http://ec2-3-70-177-108.eu-central-1.compute.amazonaws.com:8000/user.get_courses/1'))
taskcontent=fromJSON(content(req, as='text'))

descriptions <- rbindlist(lapply(seq(along=taskcontent$name), function(tc) {
  # Course
  rbindlist(lapply(seq(along=taskcontent$modules[[tc]]$items), function(tcc) {
    # Module
    rbindlist(lapply(seq(along=taskcontent$modules[[tc]]$items[[tcc]]$items), function(tccc) {
      ret = taskcontent$modules[[tc]]$items[[tcc]]$items[[tccc]]
      ret$category_name = taskcontent$modules[[tc]]$items[[tcc]]$category_name[tccc]
      ret
    }))[, module:=taskcontent$modules[[tc]]$name[tcc]]
   
 }))[, course:=taskcontent$name[tc]]
}))

descriptions[, order:=1:.N]

setcolorder(descriptions, c('course', 'module', 'category_name', 'order','id', 'name'))
descriptions[, ':=' (links=NULL, description=NULL)]

# Overall merge
tasks2 <- merge(tasks, users, by.x = c('user_id'), by.y=c('id'),all.x=T)
setkey(tasks2, task_id)
setkey(descriptions, id)
tasks2[descriptions, ':=' (descr=i.name, order=i.order, course=i.course, module=i.module, category=i.category)]

#tmp = dcast(tasks2 %>% filter(grepl('collection', course, ignore.case=T)), nickname+user_id+email~order+task_id, value.var='completed', fill = F)

tmp = dcast(tasks2 %>% filter(grepl('preparation', course, ignore.case=T)), course+module+order+task_id+descr~email, value.var='completed', fill = F)
tmp[tmp==T]<-1
tmp[tmp==F]<-0

tmp_split = split(tmp, paste0(tmp$course,'_', tmp$module))

tmp_split <- lapply(tmp_split, function(tmp2) {
  compl_rates <- tmp2[, lapply(.SD, mean, na.rm=T),.SDcol=grepl('[@]', colnames(tmp2))][, task_id:='completion_rate']
  melted_compl <- melt(compl_rates)
  melted_compl[, rank:=rank(-value,na.last = T, ties.method='average')]
  setorder(melted_compl, rank, variable)
  
  res <- rbindlist(list(tmp2, compl_rates), fill=T)

  cols = c('course','module','order','task_id','descr', as.character(melted_compl$variable))
  setcolorder(res, cols)
  
  res})

for (j in seq(along=tmp_split)) {
  append=T
  if (j==1) append=F
  Sys.sleep(1)
  xlsx:::write.xlsx(tmp_split[[j]], 'report.xlsx', row.names=F, append=append, sheetName = paste0('Sheet_', j))
  
}


write.table(tmp, 'output.csv', row.names=F, sep = ';')

# users
