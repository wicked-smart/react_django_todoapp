from django.db import models
# Create your models here.

#work status
TODO = "TD"
INPROGRESS = "IP"
DONE = "DO"

TODO_STATUS = [
    (TODO, 'Todo'),
    (INPROGRESS, 'In-Progress'),
    (DONE, 'Done')
]


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description  = models.TextField()
    status = models.CharField(max_length=2, choices=TODO_STATUS, default=TODO)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
