# jobsArray contains jobs objects that have the form:
# sampleJob = { id: str, deadline: int, penalty: int }

def schedule_jobs(jobsArray):
  # Sorting the jobsArray so penalties are in descending order
  sortedJobs = sorted(jobsArray, key=lambda k: k['penalty'], reverse=True)
  
  # Creating the jobsSchedule array with which to assign jobs within
  jobsSchedule = [0] * len(sortedJobs)
  result = [0] * len(sortedJobs)

  for i in sortedJobs:
    for j in range(0, min(len(sortedJobs), i['deadline'])):
      if jobsSchedule[j] == 0:
        result[j] = i['id']
        jobsSchedule[j] = 1
        break
        
  #Print the result
  for i in range(0, len(jobsSchedule)):
    if jobsSchedule[i] != 0:
      print(result[i])
  

schedule_jobs([{'id': 'c', 'deadline': 2, 'penalty': 27 }, {'id': 'a', 'deadline': 2, 'penalty': 100}, {'id': 'b', 'deadline': 1, 'penalty': 19}, {'id': 'd', 'deadline': 1, 'penalty': 25}, {'id': 'e', 'deadline': 3, 'penalty': 15}])
  
