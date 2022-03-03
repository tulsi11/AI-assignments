def job_scheduling(job,deadline):
    n = len(job)
    
    # sorting
    for i in range(n):
        for j in range(n-1-i):
            if job[j][2] < job[j+1][2]:
                job[j],job[j+1] =  job[j+1],job[j]
    
    result = [False] * deadline # Track of free slot
    
    schedule_job = ['-1'] * deadline
    
    profit = 0
    
    for i in range(n):
        for j in range(min(deadline-1,job[i][1]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                schedule_job[j]=job[i][0]
                profit = profit + job[i][2]
                break
    print("Schedule job: ",schedule_job)
    print("Profit: ",profit)
            
job = [['A',2,100],['B',1,19],['C',2,27],['D',1,3],['E',3,15]]

print(job_scheduling(job,3)) #deadline = 3