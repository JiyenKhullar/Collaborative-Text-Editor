from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Raw text content for the document (can be HTML)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User, through='CollaboratorRole', related_name='collaborated_documents', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def is_collaborator(self, user):
        return self.collaborators.filter(id=user.id).exists()

    def is_owner(self, user):
        return self.owner == user

class CollaboratorRole(models.Model):
    EDITOR = 'Editor'
    COMMENTER = 'Commenter'
    VIEWER = 'Viewer'

    ROLE_CHOICES = [
        (EDITOR, 'Editor'),
        (COMMENTER, 'Commenter'),
        (VIEWER, 'Viewer'),
    ]

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=VIEWER)

    def __str__(self):
        return f"{self.user.username} - {self.role} on {self.document.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    text = models.TextField()
    highlighted_text = models.TextField()  # Store the selected text
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.document.title}'
