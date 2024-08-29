from django.db import models

"""
Models are essentially database layouts    
"""

class header(models.Model):
    header_text = models.CharField(max_length = 200)
    
"""
Each model can have a bunch of different classes in it, this class name represents a database field in the model
"""

class username(models.Model):
    username_text = model

